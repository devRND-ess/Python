import sys, math
import os
import subprocess
import time
import threading
import concurrent.futures
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import QApplication, QDialog, QListWidgetItem, QListWidget, QIcon
from PyQt4.QtCore import Qt


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
Group_box_style = """
QGroupBox {
    font: bold;
    border: 2px solid grey;
    border-radius: 6px;
    margin-top: 6px;
}

QGroupBox::title {
    color: rgb(199, 199, 199);
    subcontrol-origin: margin;
    left: 7px;
    padding: 0px 5px 0px 5px;
}
"""
Btn_style = """
QPushButton 
{
    color: rgb(188, 188, 188);
    background-color: rgb(68,68,68);
}

QPushButton:hover:!pressed
{
    border: 2px solid green;
}
"""
tab_style = """
 QTabWidget::pane { /* The tab widget frame */
     border-top: 2px solid #C2C7CB;
     position: absolute;
     top: -0.5em;
 }

 QTabWidget::tab-bar {
     alignment: left;
 }
 QTabBar::tear {
     image: url(tear_indicator.png);
 }

 QTabBar::scroller { /* the width of the scroll buttons */
     width: 20px;
 }
"""
#-----------------##Txmake Command for exr2tex##------------------------------------------
def getExr2TexCmd(bitDepth, inputImg, outputImg):
    cmd = 'txmake'
    if bitDepth=='16-bit':
        cmd += ' -short'
    elif bitDepth=='32-bit':
        cmd += ' -float'
    elif bitDepth=='8-bit':
        cmd += ' -byte'

    cmd += ' -smode periodic -tmode periodic'
    cmd += ' -format pixar -filter box -resize up- -ch 0,1,2 -extraargs displaywindow'
    cmd += ' %s %s' %(inputImg,outputImg)
    return cmd
#-------------------------------------------------------------------------------------------

class localConversionThread(QtCore.QThread):
    valueChanged = QtCore.pyqtSignal([int])
    taskCompleteSignal = QtCore.pyqtSignal([int])
    taskFinishedSingnal = QtCore.pyqtSignal([int])

    def __init__(self, taskList):
        super(localConversionThread, self).__init__()
        self.taskToRunOnLocal = taskList
        self.progressComplete = 0
        self.interrupt = False
        self.result = 0
        self.retcode = 0

    def runCmd(self, task):
        self.retcode = 0
        self.retcode = subprocess.call(task)
        print("converted"+"-"*35)
        print(self.retcode)
        return self.retcode


    def run(self):
        print("\n Process PID : ", os.getpid())
        print("\n Thread Count: ", threading.active_count())
        for thread in threading.enumerate():
            print(thread)

        start_time = time.time()
        if self.interrupt:
            return;
        with concurrent.futures.ThreadPoolExecutor() as executor:
            run = [executor.submit(self.runCmd, x) for x in self.taskToRunOnLocal]

            for f in concurrent.futures.as_completed(run):
                success = (f.result())
                self.taskCompleteSignal.emit(success)

        self.result = 1
        self.taskFinishedSingnal.emit(self.result)
        end_time = time.time()

        print("\n Process PID : ", os.getpid())
        print("\n Thread Count: ", threading.active_count())
        for thread in threading.enumerate():
            print(thread)        
        print('Conversion finished in {} second(s)'.format(round(end_time-start_time)))
        return


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('txUtility.ui', self)
        self.thisDir = os.path.dirname(os.path.abspath(__file__))
        self.groupBox.setStyleSheet(Group_box_style)
        self.groupBox_out.setStyleSheet(Group_box_style)
        self.add_file.setStyleSheet(Btn_style)
        self.convert_files.setStyleSheet(Btn_style)
        self.remove_files.setStyleSheet(Btn_style)
        self.clear_files.setStyleSheet(Btn_style)
        # self.tabWidget.setStyleSheet(tab_style)
        # self.view_in_it.setStyleSheet(Btn_style)
        self.choos_dir.setStyleSheet(Btn_style)
        self.cancel_task.hide()

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setAcceptDrops(True)
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.worker1 = None
        self.worker2 = None
        self.worker3 = None
        self.worker4 = None
        self.conversionTask1 = []
        self.conversionTask2 = []
        self.conversionTask3 = []
        self.conversionTask4 = []

        #self.label.setPixmap(canvas)

        self.add_file.clicked.connect(self.fileOpen)
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
            if self.cmBox_mode.currentText()=='Tex 2 Exr':
                if os.path.exists(files) and files.endswith('.tex'):
                    print(files+" : Added")
                    y = QListWidgetItem(files)
                    y.setIcon(QIcon(r"icon.png"));
                    self.list_widget.addItem(y)
            else:
                if os.path.exists(files) and files.endswith('.exr'):
                    print(files+" : Added")
                    y = QListWidgetItem(files)
                    y.setIcon(QIcon(r"icon.png"));
                    self.list_widget.addItem(y)                
#------DragAndDropEventEnd----------------------------------------------------------------------


#------------------TX2Exr Convert----------------------------------------------------------------
    def devideTasks(self,taskList):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for x in taskList:
            if taskList.index(x)<len(taskList)/4:
                l1.append(x)
            elif taskList.index(x)>(len(taskList)/4)-1 and taskList.index(x)<2*((len(taskList)/4)):
                l2.append(x)
            elif taskList.index(x)>(2*len(taskList)/4)-2 and taskList.index(x)<3*(len(taskList)/4):
                l3.append(x)
            else:
                l4.append(x)
        return l1, l2, l3, l4


    def getTxMakeCmd(self, inFile, outFile):
        cmd = r'python {}\ice_convert_cmd.py "{}" "{}"'.format(self.thisDir,inFile,outFile)
        return cmd

    def searchReplaceOutImg(self, search_txt, replace_txt, outImg):
        return outImg.replace(search_txt, replace_txt)


    def taskList(self):
        taskToRun = []
        outPath = self.getOutputPath()
        outputImages = []
        #------get task list for all------------------
        for i in range(self.list_widget.count()):
            fileToConvert = self.list_widget.item(i).text()
            file = os.path.split(str(fileToConvert))[1]
            if self.cmBox_mode.currentText()=='Tex 2 Exr':
                convertedFile = str((outPath+r'\''+file[:-3]+"exr").replace("'", ""))
                if self.ln_edt_search.text() and self.ln_edt_replace.text() != "":
                    convertFile = self.searchReplaceOutImg(self.ln_edt_search.text(), self.ln_edt_replace.text(), convertedFile)
                outputImages.append(convertedFile)
                taskToRun.append(self.getTxMakeCmd(str(fileToConvert), convertedFile))
            else:
                convertedFile = str((outPath+r'\''+file[:-3]+"tex").replace("'", ""))
                if self.ln_edt_search.text() and self.ln_edt_replace.text() != "":
                    convertFile = self.searchReplaceOutImg(self.ln_edt_search.text(), self.ln_edt_replace.text(), convertedFile)
                outputImages.append(convertedFile)
                taskToRun.append(getExr2TexCmd(self.cmBox_bitDepth.currentText(), fileToConvert, convertedFile))

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
        if self.check_multithreaded.isChecked():
            self.conversionTask1,self.conversionTask2,self.conversionTask3,self.conversionTask4 = self.devideTasks(taskToRunList)
        else:
            self.conversionTask1 = taskToRunList

        self.worker1 = localConversionThread(self.conversionTask1)

        # self.worker1.valueChanged.connect(self.convert_progress.setValue)
        self.worker1.taskCompleteSignal.connect(self.conversionResult1)
        self.worker1.taskFinishedSingnal.connect(lambda : self.lockControl(0))
        self.lockControl(1)
        self.counter1 = 0
        self.worker1.start()


        self.add_file.hide()
        self.clear_files.hide()
        self.remove_files.hide()
        self.cancel_task.show()


    def conversionResult1(self, taskCompleteSignal):
        Itm = self.list_widget.item(self.counter1)
        if taskCompleteSignal==0:
            Itm.setIcon(QIcon('icon_ok.png'))
        else:
            print("returning here")
        self.list_widget.scrollToItem(Itm)
        self.counter1+=1



    def stopConversion(self):
        if not self.check_multithreaded.isChecked() and self.worker1:
            self.worker1.interrupt = True
            self.worker1.disconnect
            self.worker1.quit()
            print("task canceled")
            # self.convert_progress.setStyleSheet(COMPLETED_STYLE)

        if self.worker1 and self.worker2 and self.worker3 and self.worker4:
            self.worker1.interrupt = True
            self.worker2.interrupt = True
            self.worker3.interrupt = True
            self.worker4.interrupt = True
            self.worker1.disconnect
            self.worker1.quit()
            self.worker2.disconnect
            self.worker2.quit()
            self.worker3.disconnect
            self.worker3.quit()
            self.worker4.disconnect
            self.worker4.quit()
            print("task canceled")
            self.convert_progress.setStyleSheet(COMPLETED_STYLE)

    def lockControl(self, lock):
        if lock:
            QApplication.setOverrideCursor(Qt.WaitCursor)
        else:
            QApplication.restoreOverrideCursor()
            self.cancel_task.hide()
            self.add_file.show()
            self.clear_files.show()
            self.remove_files.show()


#------------------TX2Exr Convert END---------------------------------------------------------------------
    def chooseOuputPath(self):
        choosenPath = QtGui.QFileDialog.getExistingDirectory(self, 'select output directory')
        self.output_path_le.setText(choosenPath)

    def getOutputPath(self):
        if self.list_widget.count()==0:
            returntaskCompleteSignal
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
        if self.cmBox_mode.currentText()=='Tex 2 Exr':
            filter_mask = "(*.tex)"
        else:
            filter_mask = "(*.exr)"
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
        # self.convert_progress.setValue(0)
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
