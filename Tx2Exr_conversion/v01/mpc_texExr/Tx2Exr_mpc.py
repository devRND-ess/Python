import sys, math
import os
import subprocess
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import QApplication, QDialog, QListWidgetItem, QListWidget, QIcon

#---------------------------------------------------------------------------------------------------
COMPLETED_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: red;
    width: 10px;
    margin: 1px;
}
"""

class localConversionThread(QtCore.QThread):
    valueChanged = QtCore.pyqtSignal([int])
    taskCompleteSignal = QtCore.pyqtSignal([int])
    taskFinishedSingnal = QtCore.pyqtSignal([int])

    def __init__(self, taskList):
        super(localConversionThread, self).__init__()
        self.taskToRunOnLocal = taskList
        self.progressComplete = 0
        self.taskComplete = False
        self.success = 0
        self.scroll = 0
        self.convert = 1

    def run(self):
        for index ,tasks in enumerate(self.taskToRunOnLocal, start=0):
            print("converting : image"+str(self.taskToRunOnLocal.index(tasks)))
            #----Run Command-------
            subprocess.call(tasks)
            self.success = 1
            self.taskCompleteSignal.emit(self.success)
            self.scroll = index
            self.progressComplete += 100.0/len(self.taskToRunOnLocal)
            if self.taskToRunOnLocal.index(tasks)==(len(self.taskToRunOnLocal)-1):
                self.progressComplete += 100.0-self.progressComplete
            self.valueChanged.emit(self.progressComplete)

            #print("Successfully converted")
            print("-----------------------------------------------------------------")
        self.taskToRunOnLocal = []
        self.taskComplete = True
        self.taskFinishedSingnal.emit(self.taskComplete)

        print("Task Finished")

        # pixmap = QtGui.QPixmap(60, 60)
        # pixmap.fill()
        # painter = QtGui.QPainter(pixmap)
        # painter.setBrush(QtCore.Qt.red)
        # painter.drawRect(5, 10, 50, 30)

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('txUtility.ui', self)
        self.cancel_task.hide()

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setAcceptDrops(True)

        #self.label.setPixmap(canvas)

        self.add_files.clicked.connect(self.fileOpen)
        self.remove_files.clicked.connect(self.removeEvent)
        self.convert_files.clicked.connect(self.runConversion)
        #self.convert_files.clicked.connect(self.hideShow)
        self.choos_dir.clicked.connect(self.chooseOuputPath)
        #self.convert_sel_files.clicked.connect(self.runConversionOnSelected)
        self.connect(self, QtCore.SIGNAL("dropped"), self.fileDropped)
        self.clear_files.clicked.connect(self.clearItems)
        self.cancel_task.clicked.connect(self.stopConversion)


#------DragAndDropEvent------------------------------------------------------------------------

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()


    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.ignore()

    def fileDropped(self, l):
        for files in l:
            if os.path.exists(files) and files.endswith('.tex'):
                print(files+" : Added")
                y = QListWidgetItem(files)
                y.setIcon(QIcon(r"icon.png"));
                self.list_widget.addItem(y)

#------DragAndDropEventEnd----------------------------------------------------------------------


#------------------TX2Exr Convert----------------------------------------------------------------
    def getTxMakeCmd(self, inFile, outFile):
        cmd = r'python G:\Python\qt\mpc_texExr\ice_convert_cmd.py' + " " + '"'+(inFile)+'"' + " " + '"'+outFile+'"'
        return cmd


    def taskList(self):
        taskToRun = []
        outPath = self.getOutputPath()
        outputImages = []
        #------get task list for all------------------
        for i in range(self.list_widget.count()):
            fileToConvert = self.list_widget.item(i).text()
            file = os.path.split(str(fileToConvert))[1]
            convertedFile = str((outPath+r'\''+file[:-3]+"exr").replace("'", ""))
            outputImages.append(convertedFile)
            taskToRun.append(self.getTxMakeCmd(str(fileToConvert), convertedFile))
        return taskToRun, outputImages


    def runConversion(self):
        taskToRunList = self.taskList()[0]
        outputImageList = self.taskList()[1]
        if self.checkOutputExist(outputImageList):
            reply = QtGui.QMessageBox.question(self, 'Message',
                         'some images already exists, do you want to overwrite?',
                          QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply != QtGui.QMessageBox.Yes:
                return

        if (self.list_widget.count())==0:
            QtGui.QMessageBox.warning(self, 'Message', 'No Images!')
            return


        self.localConversionThread = localConversionThread(taskToRunList)
        self.localConversionThread.valueChanged.connect(self.convert_progress.setValue)
        self.localConversionThread.start()
        self.localConversionThread.taskCompleteSignal.connect(self.conversionResult)
        self.localConversionThread.taskFinishedSingnal.connect(self.bringBackUI)
        self.add_files.hide()
        self.clear_files.hide()
        self.remove_files.hide()
        self.cancel_task.show()


    def conversionResult(self):
        initScroll = self.localConversionThread.scroll
        print("----ICON----SET-----:: "+str(self.localConversionThread.success))
        if self.localConversionThread.success==1:
            Itm = self.list_widget.item(initScroll)
            Itm.setIcon(QIcon('icon_ok.png'))
        else:
            print("returning here")
            #Itm = self.list_widget.item(self.localConversionThread.scroll-1)
            #Itm.setIcon(QIcon('icon_Notok.png'))



    def stopConversion(self):
        self.localConversionThread.terminate()
        print("task canceled")
        self.convert_progress.setStyleSheet(COMPLETED_STYLE)
        self.convert_progress.setValue(100)
        self.localConversionThread.disconnect
        self.localConversionThread.taskComplete = False
        self.add_files.show()
        self.clear_files.show()
        self.remove_files.show()
        self.cancel_task.hide()

    def bringBackUI(self):
        if self.localConversionThread.taskComplete==True:
            self.cancel_task.hide()
            self.add_files.show()
            self.clear_files.show()
            self.remove_files.show()

#------------------TX2Exr Convert END---------------------------------------------------------------------
    def chooseOuputPath(self):
        choosenPath = QtGui.QFileDialog.getExistingDirectory(self, 'select output directory')
        self.output_path_le.setText(choosenPath)

    def getOutputPath(self):
        if self.list_widget.count()==0:
            return
        outputPath = ""
        if (self.output_path_le.text())=="":
            outputPath = self.list_widget.item(0).text()
            outputPath = os.path.split(str(outputPath))[0]
        else:
            outputPath = self.output_path_le.text()

        return outputPath

    #check if output image already exists
    def checkOutputExist(self, outputImageList):
        outputExists = False
        for i in outputImageList:
            if os.path.lexists(i):
                outputExists = True
        return outputExists

    def fileOpen(self):
        caption = 'Open file'
        directory = './'
        filter_mask = "(*.tex)"
        file = QtGui.QFileDialog.getOpenFileNames(None,caption, directory, filter_mask)
        for x in file:
            y = QListWidgetItem(x)
            y.setIcon(QIcon(r"icon.png"));
            self.list_widget.addItem(y)

    # def rename(self):
    #     all_items = self.list_widget.selectedItems()
    #     for item in all_items:
    #         x = os.path.split(item.text())
    #         dirName = x[0]
    #         fileName = os.path.splitext(x[1])[0]
    #         ext = os.path.splitext(x[1])[1]
    #         finalFileName = (dirName + r"\"" + fileName.replace(fileName, fileName+self.textToRename_files.text())+ext)
    #         print(finalFileName.replace('"', ""))
    #     #print(dlg.list_widget.selectedItems()[0].text())


    def removeItem(self):
        for SelectedItem in self.list_widget.selectedItems():
            self.list_widget.takeItem(self.list_widget.row(SelectedItem))
        self.convert_progress.setValue(0)


    def removeEvent(self):
        quit_msg = "Are you sure?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.removeItem()
            self.update()
        else:
            return

    def clearItems(self):
        self.list_widget.clear()
        self.convert_progress.setValue(0)
        self.update()

    # def hideShow(self):
    #     self.add_files.hide()
    #     self.clear_files.hide()
    #     self.remove_files.hide()
    #     self.cancel_task.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    object = MyWindow()
    object.show()
    sys.exit(app.exec_())
