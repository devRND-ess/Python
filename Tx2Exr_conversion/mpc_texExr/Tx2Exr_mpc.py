import sys
import os
import subprocess
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import QApplication, QDialog, QListWidgetItem, QListWidget, QIcon

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('AddFiles.ui', self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setAcceptDrops(True)
        self.add_files.clicked.connect(self.fileOpen)
        self.remove_files.clicked.connect(self.removeEvent)
        self.convert_files.clicked.connect(self.runConversion)
        self.convert_sel_files.clicked.connect(self.runConversionOnSelected)
        self.connect(self, QtCore.SIGNAL("dropped"), self.fileDropped)

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
        for url in l:
            if os.path.exists(url):
                print(url)
                self.list_widget.addItem(url)
#------DragAndDropEventEnd----------------------------------------------------------------------


#------------------TX2Exr Convert----------------------------------------------------------------
    def getTxMakeCmd(self, inFile, outFile):
        cmd = r'python G:\Python\qt\mpc_texExr\ice_convert_cmd.py' + " " + '"'+(inFile)+'"' + " " + '"'+outFile+'"'
        return cmd


    def taskList(self):
        taskToRun = []
        outPath = self.getOutputPath()
        #------get task list for all------------------
        for i in range(self.list_widget.count()):
            fileToConvert = self.list_widget.item(i).text()
            file = os.path.split(str(fileToConvert))[1]
            convertedFile = str((outPath+r'\''+file[:-3]+"exr").replace("'", ""))
            if os.path.exists(convertedFile):
                print(convertedFile+" Already exists!")
                pass
            else:
                taskToRun.append(self.getTxMakeCmd(str(fileToConvert), convertedFile))
        return taskToRun
        #------get task list for selected files------------------
    def taskListSelected(self):
        selTaskToRun = []
        selFiles = []
        outPath = self.getOutputPath()
        for sItem in self.list_widget.selectedItems():
            selFileToConvert = sItem.text()
            fileS = os.path.split(str(selFileToConvert))[1]
            selConvertedFile = str((outPath+r'\''+fileS[:-3]+"exr").replace("'", ""))
            if os.path.exists(selConvertedFile):
                pass
            else:
                selFiles.append(sItem.text())
                selTaskToRun.append(self.getTxMakeCmd(str(selFileToConvert), selConvertedFile))
        #return both the task lists
        return selTaskToRun, selFiles

    def runConversion(self):
        progressPercentage = 0
        taskToRunList = self.taskList()
        for tasks in taskToRunList:
            print("converting "+self.list_widget.item(taskToRunList.index(tasks)).text())
            #----Run Command-------
            subprocess.call(tasks)
            #----------------------
            progressPercentage += 100.0/len(taskToRunList)
            self.convert_progress.setValue(progressPercentage)
            z = QListWidgetItem(self.list_widget.item(taskToRunList.index(tasks)).text())
            z.setIcon(QIcon(r"icon_ok.png"))
            self.list_widget.takeItem(taskToRunList.index(tasks))
            self.list_widget.addItem(z)
            self.list_widget.update()

            print("Successfully converted")
            print("-----------------------------------------------------------------")


    def runConversionOnSelected(self):
        progressPercentage = 0
        SelTaskToRunList = self.taskListSelected()[0]
        selFiles = self.taskListSelected()[1]
        for SelTasks in range(len(SelTaskToRunList)):
            print("converting "+self.list_widget.item(SelTaskToRunList.index(SelTaskToRunList[SelTasks])).text())
            #-------Run Command-------------------------
            subprocess.call(SelTaskToRunList[SelTasks])
            #-------------------------------------------
            progressPercentage += 100.0/len(SelTaskToRunList)
            self.convert_progress.setValue(progressPercentage)
            z = QListWidgetItem((self.list_widget.findItems(selFiles[SelTasks],QtCore.Qt.MatchExactly))[0])
            z.setIcon(QIcon(r"icon_ok.png"))
            self.list_widget.takeItem(self.list_widget.row((self.list_widget.findItems(selFiles[SelTasks],QtCore.Qt.MatchExactly))[0]))
            self.list_widget.addItem(z)
            self.list_widget.update()
            print("Successfully converted")
            print("-----------------------------------------------------------------")
#------------------TX2Exr Convert END---------------------------------------------------------------------

    def getOutputPath(self):
        outputPath = ""
        if (self.output_path_le.text())=="":
            outputPath = self.list_widget.item(0).text()
            outputPath = os.path.split(str(outputPath))[0]
        else:
            outputPath = self.output_path_le.text()

        return outputPath


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
        else:
            pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    object = MyWindow()
    object.show()
    sys.exit(app.exec_())
