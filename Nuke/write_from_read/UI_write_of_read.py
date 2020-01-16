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
        # self.n_read_list = [x for x in nuke.allNodes() if x.Class()=='Read']

        #signals
        self.btn_createWrite.clicked.connect(self.getInputs)

    def getInputs(self):
        _outPath = self.line_edit_outPath.text()
        _prefix = self.line_edit_prefix.text()
        _suffix = self.line_edit_suffix.text()
        _extension = self.cmb_box_extension.currentText()
        if _extension!='same':
            _extension = '.'+self.cmb_box_extension.currentText()
        return _outPath, _prefix, _suffix, _extension



    def writeFromRead(lst, outDir, pFix, sFix, ext):
        outDir, pFix, sFix, ext = self.getInputs()


        for x in lst:
            fileName = x.knob('file').getValue()
            _filename, _ext = os.path.splitext(os.path.split(fileName)[1])
            if ext == 'same':
                ext = _ext
            if pFix!='':
                _filename = pFix+_filename
            if sFix!='':
                _filename = _filename+sFix

            #create write
            n_write = nuke.createNode('Write')
            n_write.knob('file').setValue(os.path.join(outDir, _filename+ext))
            n_write.knob('file_type').setValue('exr')
            n_write.knob('raw').setValue(1)
            n_write.knob('metadata').setValue(3)
            n_write.knob('compression').setValue(2)
            n_write.setInput(0, x)
            #print('dir is {} and file is {} extension is {}'.format(dir,file,'.png'))


# app = QApplication(sys.argv)
obj = Panel()
obj.show()
# app.exec_()
