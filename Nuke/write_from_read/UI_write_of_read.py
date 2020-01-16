import nuke
import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
from panel_ui import Ui_MainWindow

class Panel(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Panel,self).__init__()
        self.setupUi(self)
        self.n_read_list = [x for x in nuke.allNodes() if x.Class()=='Read']

        #signals
        self.btn_createWrite.clicked.connect(self.run)

    def getInputs(self):
        _outPath = self.line_edit_outPath.text()
        _prefix = self.line_edit_prefix.text()
        _suffix = self.line_edit_suffix.text()
        _extension = self.cmb_box_extension.currentText()
        if _extension!='same':
            _extension = '.'+self.cmb_box_extension.currentText()
        return _outPath, _prefix, _suffix, _extension



    def getDepend(r):
    dep = r.dependent()
    if dep:
        return getDepend(dep[0])
    else:
        return r



    def writeFromRead(self, lst, outDir, pFix, sFix, ext):
        for x in lst:
            fileName = x.knob('file').getValue()
            _dir = os.path.split(fileName)[0]
            _filename, _ext = os.path.splitext(os.path.split(fileName)[1])
            if outDir == "":
                outDir = _dir
            if ext == 'same':
                ext = _ext
            if pFix!='':
                _filename = pFix+_filename
            if sFix!='':
                _filename = _filename+sFix

            print(os.path.join(outDir,_filename+ext))
            # create write
            n_write = nuke.createNode('Write')
            n_write.knob('file').setValue(os.path.join(outDir, _filename+ext))
            n_write.knob('file_type').setValue(ext)
            n_write.knob('raw').setValue(1)
            n_write.knob('metadata').setValue(3)
            n_write.knob('compression').setValue(2)
            n_write.setInput(0, x)
            # print('dir is {} and file is {} extension is {}'.format(dir,file,'.png'))

    def run(self):
        outDir, pFix, sFix, ext = self.getInputs()
        self.writeFromRead(self.n_read_list, outDir, pFix, sFix, ext)


# app = QApplication(sys.argv)
obj = Panel()
obj.show()
# app.exec_()
