import sys, pprint
from pyside2uic import compileUi
pyfile = open("G:\Python\maya\curve_at_click_utility\curve_ui_out.py", 'w')
compileUi("G:\Python\maya\curve_at_click_utility\curve_ui.ui", pyfile, False, 4,
False)
pyfile.close()

path = r'G:\Python\maya\curve_at_click_utility'
sys.path.append(path)
from maya import OpenMayaUI as omui
import maya.api.OpenMaya as om
# import pymel.core as pm
import maya.mel as mm
import maya.cmds as cmds
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFrame
from PySide2 import __version__
from shiboken2 import wrapInstance
import curve_ui_out
reload(curve_ui_out)
from curve_ui_out import Ui_MainWindow
import curve_util
reload(curve_util)
from curve_util import FollicleBindCurve
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
Btn_style = """
QPushButton
{
    color: rgb(188, 188, 188);
    background-color: rgb(98,98,98);
}

QPushButton:hover:!pressed
{
    border: 1.2px solid blue;
    background-color: rgb(111,111,111);
}
"""
label_style = """
QLabel{
  border-radius: 5px;
  min-height: 50px;
  min-width: 20px;
  background-color: rgb(72, 170, 181);
  color: rgb(222, 222, 222)
}
"""



class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class CollapsibleBox(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(
            text=title, checkable=True, checked=True
        )
        self.toggle_button.setStyleSheet("QToolButton { border: none;\nbackground-color: rgb(100,100,100); }")
        self.toggle_button.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.DownArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"minimumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"maximumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self.content_area, b"maximumHeight")
        )
        self.toggle_animation.start()
    # @QtCore.pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if not checked else QtCore.Qt.RightArrow
        )
        self.toggle_animation.setDirection(
            QtCore.QAbstractAnimation.Forward
            if not checked
            else QtCore.QAbstractAnimation.Backward
        )
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
        )
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(50)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(50)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)




def maya_main_window():
    '''
    Return the Maya main window widget as a Python object
    '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class TestTool(MayaQWidgetDockableMixin, QtWidgets.QMainWindow, Ui_MainWindow):
    toolName = 'curve_at_click'
    def __init__(self, parent=None):
        super(TestTool, self).__init__(parent=parent)
        self.setupUi(self)

        self.setupUI_custom()

        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        self.mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QMainWindow)
        self.setObjectName(self.__class__.toolName)
        workspaceControlName = self.objectName() + 'WorkspaceControl'
        self.deleteControl(workspaceControlName)
        self.setWindowFlags(QtCore.Qt.Window)
        # scroll = QtWidgets.QScrollArea()
        # self.setWidget(scroll)

        # self.setWindowFlags(QtCore.Qt.Tool)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)

        self.selected = cmds.ls(sl=True,long=True) or []
        self.cv_count = 0
        self.crv_len = 0.0

        cmds.selectType(nc=True, alo=False)

        # self.btn_add_curve.setStyleSheet(Btn_style)
        # self.btn_del_curve.setStyleSheet(Btn_style)
        # self.btn_sel_root.setStyleSheet(Btn_style)
        # self.btn_sel_end.setStyleSheet(Btn_style)
        # self.btn_sel_curve.setStyleSheet(Btn_style)
        # self.btn_sel_cv.setStyleSheet(Btn_style)
        # self.btn_scale_curve.setStyleSheet(Btn_style)

        self.label_top_Curves_Utility.setStyleSheet(label_style)
        # self.label_top_Curves_Utility.setMargin(0)
        self.label_top_Curves_Utility.setContentsMargins(0,0,0,0)

        #Signals and slot
        self.btn_add_curve.clicked.connect(self.add_curve)
        self.btn_del_curve.clicked.connect(self.delete_curve)
        self.btn_sel_root.clicked.connect(self.select_first_cv)
        self.btn_sel_end.clicked.connect(self.select_last_cv)
        self.btn_sel_curve.clicked.connect(self.select_crv)
        self.btn_sel_cv.clicked.connect(self.select_cv)
        self.check_curve_mode.stateChanged.connect(self.reset_sel_type)
        self.btn_scale_curve.clicked.connect(self.scale_curve)
        self.check_lock_len.stateChanged.connect(self.lock_length)
        self.btn_color_picker.clicked.connect(self.color_picker)
        self.check_draw_override.stateChanged.connect(self.draw_override)
        self.slider_color.valueChanged.connect(self.slider_color_changed)
        # self.slider_line_width.valueChanged.connect(self.line_width_display)
        self.spin_line_width.valueChanged.connect(self.line_width_display)
        self.btn_new_item.clicked.connect(self.add_item_grouping)
        self.btn_del_grp.clicked.connect(self.removeItem)
        #---------------------------------
        self.list_groups.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list_groups.connect(self.list_groups,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)

    # def listItemRightClicked(self):
    #     print('hello')

    def deleteControl(self, control):
        cmds.selectType(alo=True)
        if cmds.workspaceControl(control, q=True, exists=True):
            cmds.workspaceControl(control, e=True, close=True)
            cmds.deleteUI(control, control=True)

    def setupUI_custom(self):
        collap_add = CollapsibleBox('  Add')
        collap_add.setStyleSheet('color:rgb(223, 110, 65);')
        self.verticalLayout_3.addWidget(collap_add)
        lay_add = QtWidgets.QVBoxLayout()

        lay_add.addWidget(self.grp_add_curves)

        collap_add.setContentLayout(lay_add)

        collap_select = CollapsibleBox('  Selection')
        collap_select.setStyleSheet('color:rgb(223, 110, 65);')
        self.verticalLayout_3.addWidget(collap_select)
        lay_select = QtWidgets.QVBoxLayout()
        lay_select.addWidget(self.grp_selection)
        collap_select.setContentLayout(lay_select)

        collap_grouping = CollapsibleBox('  Grouping')
        collap_grouping.setStyleSheet('color:rgb(223, 110, 65);')
        self.verticalLayout_3.addWidget(collap_grouping)
        lay_group = QtWidgets.QVBoxLayout()
        lay_group.addWidget(self.group_grouping)
        collap_grouping.setContentLayout(lay_group)

        collap_util = CollapsibleBox('  Utility')
        collap_util.setStyleSheet('color:rgb(223, 110, 65);')
        self.verticalLayout_3.addWidget(collap_util)
        lay_util = QtWidgets.QVBoxLayout()
        # lay_util.addLayout(self.horizontalLayout_4)
        lay_util_hori = QtWidgets.QHBoxLayout()
        lay_util_hori.addWidget(self.label_scale)
        lay_util_hori.addWidget(self.dspin_scale_curve)

        lay_util_hori.addWidget(self.btn_scale_curve)
        lay_util.addLayout(lay_util_hori)
        lay_util.addWidget(QHLine())

        lay_util.addWidget(self.check_draw_override)

        lay_util_hori_2 = QtWidgets.QHBoxLayout()
        lay_util_hori_2.addWidget(self.label_color)
        lay_util_hori_2.addWidget(self.btn_color_picker)
        lay_util_hori_2.addWidget(self.slider_color)
        lay_util.addLayout(lay_util_hori_2)

        lay_util.addWidget(QHLine())

        # lay_util.addWidget(li)
        lay_util_hori_3 = QtWidgets.QHBoxLayout()
        lay_util_hori_3.addWidget(self.label_line_width)
        lay_util_hori_3.addWidget(self.spin_line_width)
        lay_util.addLayout(lay_util_hori_3)

        # lay_util.addWidget(self.horizontalSpacer)
        collap_util.setContentLayout(lay_util)


        self.verticalLayout_3.addStretch()


    def listItemRightClicked(self, QPos):
        self.listMenu= QtWidgets.QMenu()
        menu_item_1 = self.listMenu.addAction("Add Selected Curves")
        menu_item_2 = self.listMenu.addAction("Select curves")
        self.connect(menu_item_1, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
        parentPosition = self.list_groups.mapToGlobal(QtCore.QPoint(0, 0))
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show()

    def menuItemClicked(self):
        currentItemName=str(self.list_groups.currentItem().text() )
        print(currentItemName)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def add_item_grouping(self):
        name = 'curve_grp01'
        grp = cmds.group(em=True, n=name)
        self.list_groups.addItem(grp)
        for index in range(self.list_groups.count()):
            item = self.list_groups.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    def removeItem(self):
        for SelectedItem in self.list_groups.selectedItems():
            self.list_groups.takeItem(self.list_groups.row(SelectedItem))
            cmds.delete(SelectedItem.text())

    def color_picker(self):
        draw_override = self.check_draw_override.isChecked()
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
        color = QtWidgets.QColorDialog.getColor()
        self.show()
        self.btn_color_picker.setStyleSheet("QWidget { background-color: %s}" % color.name())
        sel = cmds.ls(sl=True, long=True)
        get_color = color.getRgb()
        print(get_color)

        if draw_override:
            for s in sel:
                shape = cmds.listRelatives(s, shapes=True)[0]
                cmds.setAttr(shape+'.overrideEnabled',1)
                cmds.setAttr(shape+'.overrideRGBColors',1)

                cmds.setAttr(shape+'.overrideColorR', get_color[0]/255.0)
                cmds.setAttr(shape+'.overrideColorG', get_color[1]/255.0)
                cmds.setAttr(shape+'.overrideColorB', get_color[2]/255.0)
        else:
            for s in sel:
                shape = cmds.listRelatives(s, shapes=True)[0]
                cmds.setAttr(shape+'.overrideEnabled', 0)

    def draw_override(self):
        sel = cmds.ls(sl=True, long=True)
        if self.check_draw_override.isChecked():
            for s in sel:
                shape = cmds.listRelatives(s, shapes=True)[0]
                cmds.setAttr(shape+'.overrideEnabled',1)
        else:
            for s in sel:
                shape = cmds.listRelatives(s, shapes=True)[0]
                cmds.setAttr(shape+'.overrideEnabled', 0)

    def slider_color_changed(self):
        color = self.slider_color.value()/100.0
        sel = cmds.ls(sl=True, long=True)
        self.btn_color_picker.setStyleSheet("QWidget { background-color: rgb(%s, %s, %s)}" %(color*255,color*255,color*255))

        if self.check_draw_override.isChecked():
            for s in sel:
                shape = cmds.listRelatives(s, shapes=True)[0]
                cmds.setAttr(shape+'.overrideEnabled',1)
                cmds.setAttr(shape+'.overrideRGBColors',1)

                cmds.setAttr(shape+'.overrideColorR', color)
                cmds.setAttr(shape+'.overrideColorG', color)
                cmds.setAttr(shape+'.overrideColorB', color)

    # def line_width_display(self):
    #     value = self.slider_line_width.value()
    #     self.line_edit_line_width.setText(str(value/10.0))
    #     cmds.modelEditor(lw=value/10.0)

    def line_width_display(self):
        val_line_edit = self.spin_line_width.value()
        # self.slider_line_width.setValue(int(val_line_edit*10.0))
        cmds.modelEditor(lw=val_line_edit)

    def lock_length(self):
        sel = cmds.ls(sl=True)
        for x in sel:
            cmds.setAttr(x + ".lockLength", int(self.check_lock_len.isChecked()))


    def add_curve(self):
        self.cv_count = self.spin_cv_count.value()
        self.crv_len = self.dspin_crv_len.value()
        self.crv_obj = FollicleBindCurve(self.cv_count, self.crv_len, self.selected, self.check_lock_len.isChecked())
        self.crv_obj.run()

    def delete_curve(self):
        sel = cmds.ls(sl=True)
        for obj in sel:
            _follicle_node = 'follicle'+obj[5:]
            cmds.delete(obj)
            cmds.delete(_follicle_node)

    def select_first_cv(self):
        mm.eval('SelectCurveCVsFirst')

    def select_last_cv(self):
        mm.eval('SelectCurveCVsLast;')

    def select_cv(self):
        cmds.selectType(cv=True, p=False, v=False)
        cmds.selectMode(component=True)

    def select_crv(self):
        cmds.selectType(nc=True,alc=False)
        cmds.selectMode(object=True)

    def reset_sel_type(self):
        if self.check_curve_mode.isChecked():
            cmds.selectType(nc=True,alo=False)
        else:
            cmds.selectType(alo=True)

    def scale_curve(self):
        sel = cmds.ls(sl=True)
        scale_val = self.dspin_scale_curve.value()
        px,py,pz = self.crv_obj.get_pivot()
        cmds.scale( scale_val, scale_val, scale_val, absolute=True)
        for obj in sel:
            pass
            # cmds.makeIdentity(obj,apply=True, s=1, n=0)
    def closeEvent(self, event):
        print('exit!')
        cmds.selectType(alo=True)
        event.accept()

    def dockCloseEventTriggered(self):
        print('exit')
        cmds.selectType(alo=True)

ui = TestTool()
ui.show(dockable = True)
# if __name__ == '__main__':
#     try:
#         ui.deleteLater()
#     except:
#         pass
#     ui = TestTool()

#     try:
#         ui.show(dockable = True)
#     except:
#         ui.deleteLater()
