import sys,os
path = r'G:\Python\maya\controll_creator'
sys.path.append(path)
os.chdir(path)
from pyside2uic import compileUi
pyfile = open(r"G:\Python\maya\controll_creator\Ui_control_creator.py", 'w')
compileUi(r"G:\Python\maya\controll_creator\Ui_control_creator.ui", pyfile, False, 4,
False)
pyfile.close()

import maya.cmds as cmds
import maya.OpenMaya as om
from maya import OpenMayaUI as omui
import json
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFrame
from PySide2 import __version__
from shiboken2 import wrapInstance
import Ui_control_creator
reload(Ui_control_creator)
from Ui_control_creator import Ui_MainWindow
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#------------CSS--------------------
label_style = """
QLabel{
  border-radius: 5px;
  min-height: 50px;
  min-width: 20px;
  background-color: rgb(76, 76, 163);
  color: rgb(212, 212, 212)
}
"""
#-----------------------------------

def maya_main_window():
    '''
    Return the Maya main window widget as a Python object
    '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class ControlCreator(MayaQWidgetDockableMixin, QtWidgets.QMainWindow, Ui_MainWindow):
    toolName = 'myToolWidget'
    """docstring for ControlCreator"""
    def __init__(self, parent=None):
        super(ControlCreator, self).__init__(parent=parent)
        self.setupUi(self)
        self.resize(320, 100)
        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        self.mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QMainWindow)
        self.setObjectName(self.__class__.toolName)
        workspaceControlName = self.objectName() + 'WorkspaceControl'
        self.deleteControl(workspaceControlName)
        self.setWindowFlags(QtCore.Qt.Window)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
        self.label_master.setStyleSheet(label_style)

        #Signals and slot
        self.btn_star_stick.clicked.connect(self.star_stick)
        self.btn_water_drop.clicked.connect(self.water_drop)
        self.btn_lever.clicked.connect(self.lever)
        self.btn_drop_stick.clicked.connect(self.drop_stick)

        self.btn_master_arrow.clicked.connect(self.master_arrow)
        self.btn_arc_arrow.clicked.connect(self.arc_arrow)
        self.btn_double_arrow.clicked.connect(self.double_arrow)
        self.btn_double_arc_arrow.clicked.connect(self.double_arc_arrow)
        self.btn_tri_arrow.clicked.connect(self.tri_arrow)
        self.btn_quad_arrow.clicked.connect(self.quad_arrow)
        self.btn_quad_arc_arrow.clicked.connect(self.quad_arc_arrow)
        self.btn_up_arrow.clicked.connect(self.up_arrow)

        self.btn_circle.clicked.connect(self.circle)
        self.btn_circle_double_curved.clicked.connect(self.circle_double_curved)
        self.btn_octa_ring.clicked.connect(self.octa_ring)
        self.btn_orbit.clicked.connect(self.orbit)
        self.btn_spinning_circle.clicked.connect(self.spinning_circle)
        self.btn_square.clicked.connect(self.square)
        self.btn_triangle.clicked.connect(self.triangle)

        self.btn_eye_global.clicked.connect(self.eye_global)
        self.btn_eye_look.clicked.connect(self.eye_look)
        self.btn_ik_fk.clicked.connect(self.ik_fk)

        self.btn_color_picker.clicked.connect(self.color_picker)

    def deleteControl(self, control):
        if cmds.workspaceControl(control, q=True, exists=True):
            cmds.workspaceControl(control, e=True, close=True)
            cmds.deleteUI(control, control=True)

    def create_control(self, name):
        with open('curve_create_data.json') as f:
            data = json.load(f)

        cv_list = data[name]['cvs']
        knot_list = data[name]['knots']
        degree_list = data[name]['degree']
        create_crv_list = []

        for ckd in range(len(cv_list)):
            crv = cmds.curve(p=cv_list[ckd], k=knot_list[ckd], d=degree_list[ckd])
            create_crv_list.append(crv)

        new_crve_name = self.combine_curves(create_crv_list, name)
        self.draw_override(new_crve_name)
#--------------Sticks-----------------------------------
    def star_stick(self):
        self.name = 'star_stick'
        self.create_control(self.name)

    def water_drop(self):
        self.name = 'water_drop'
        self.create_control(self.name)

    def lever(self):
        self.name = 'lever'
        self.create_control(self.name)

    def drop_stick(self):
        self.name = 'drop_stick'
        self.create_control(self.name)
#--------------------------------------------------------
#--------------Arrows------------------------------------
    def master_arrow(self):
        self.name = 'master_arrow'
        self.create_control(self.name)

    def arc_arrow(self):
        self.name = 'arc_arrow'
        self.create_control(self.name)

    def double_arrow(self):
        self.name = 'double_arrow'
        self.create_control(self.name)

    def double_arc_arrow(self):
        self.name = 'double_arc_arrow'
        self.create_control(self.name)

    def tri_arrow(self):
        self.name = 'tri_arrow'
        self.create_control(self.name)

    def quad_arrow(self):
        self.name = 'quad_arrow'
        self.create_control(self.name)

    def quad_arc_arrow(self):
        self.name = 'quad_arc_arrow'
        self.create_control(self.name)

    def up_arrow(self):
        self.name = 'up_arrow'
        self.create_control(self.name)
#--------------------------------------------------------------
#--------------Basics Shapes------------------------------------
    def circle(self):
        self.name = 'circle'
        self.create_control(self.name)

    def circle_double_curved(self):
        self.name = 'circle_double_curved'
        self.create_control(self.name)

    def octa_ring(self):
        self.name = 'octa_ring'
        self.create_control(self.name)

    def orbit(self):
        self.name = 'orbit'
        self.create_control(self.name)

    def spinning_circle(self):
        self.name = 'spinning_circle'
        self.create_control(self.name)

    def square(self):
        self.name = 'square'
        self.create_control(self.name)

    def triangle(self):
        self.name = 'triangle'
        self.create_control(self.name)
#-------------------------------------------------------------
#--------------Face/IK-FK------------------------------------
    def eye_global(self):
        self.name = 'eye_global'
        self.create_control(self.name)

    def eye_look(self):
        self.name = 'eye_look'
        self.create_control(self.name)

    def ik_fk(self):
        self.name = 'ik_fk'
        self.create_control(self.name)
#-------------------------------------------------------------
    def color_picker(self):
        # draw_override = self.check_draw_override.isChecked()
        # self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
        color = QtWidgets.QColorDialog.getColor()
        # self.show()
        self.btn_color_picker.setStyleSheet("QWidget { background-color: %s}" % color.name())
        sel = cmds.ls(sl=True, long=True)
        self.get_color = color.getRgb()


        for s in sel:
            shapes = cmds.listRelatives(s, shapes=True)
            for sh in shapes:
                cmds.setAttr(sh+'.overrideEnabled',1)
                cmds.setAttr(sh+'.overrideRGBColors',1)

                cmds.setAttr(sh+'.overrideColorR', self.get_color[0]/255.0)
                cmds.setAttr(sh+'.overrideColorG', self.get_color[1]/255.0)
                cmds.setAttr(sh+'.overrideColorB', self.get_color[2]/255.0)



    def draw_override(self, crv):
        # sel = cmds.ls(sl=True, long=True)
            shape = cmds.listRelatives(crv, shapes=True)
            for sh in shape:
                cmds.setAttr(sh+'.overrideEnabled',1)
                cmds.setAttr(sh+'.overrideRGBColors',1)
                try:
                    cmds.setAttr(sh+'.overrideColorR', self.get_color[0]/255.0)
                    cmds.setAttr(sh+'.overrideColorG', self.get_color[1]/255.0)
                    cmds.setAttr(sh+'.overrideColorB', self.get_color[2]/255.0)
                except Exception:
                    cmds.setAttr(sh+'.overrideColorR', 0/255.0)
                    cmds.setAttr(sh+'.overrideColorG', 0/255.0)
                    cmds.setAttr(sh+'.overrideColorB', 127/255.0)


    def combine_curves(self, crv_list, _name):
        sel = crv_list
        # if len(sel) < 2:
        #     print('You have less than two object selected. Please select first at least 2 curves you want to combine.\n')
        #     return

        shape = cmds.listRelatives(sel,shapes = True)
        for x in range(len(sel)):
            cmds.makeIdentity(sel[x], apply = True, rotate = True, scale = True, translate = True)

        group = cmds.group(empty = True, name = _name)
        cmds.select(shape[0])
        for x in range(1, (len(shape))):
            cmds.select(shape[x], add  = True)

        cmds.select(group, add = True)
        cmds.parent(relative = True, shape = True)
        cmds.delete(sel)
        print('New curve created')

        return group
        # sys.stdout.write('New curve created.\n')


if __name__ == '__main__':
    try:
        ui.deleteLater()
    except:
        pass
    ui = ControlCreator()

    try:
        ui.show(dockable = True)
    except:
        ui.deleteLater()
