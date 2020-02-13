# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Github\Python\maya\curve_at_click_utility\curve_ui.ui'
#
# Created: Fri Feb 14 00:19:45 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 475)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_top_Curves_Utility = QtWidgets.QLabel(self.centralwidget)
        self.label_top_Curves_Utility.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Stencil Std")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_top_Curves_Utility.setFont(font)
        self.label_top_Curves_Utility.setStyleSheet("background-color: rgb(72, 170, 181);\n"
"color: rgb(0, 0, 0);")
        self.label_top_Curves_Utility.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_top_Curves_Utility.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_top_Curves_Utility.setLineWidth(1)
        self.label_top_Curves_Utility.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top_Curves_Utility.setMargin(0)
        self.label_top_Curves_Utility.setObjectName("label_top_Curves_Utility")
        self.verticalLayout_5.addWidget(self.label_top_Curves_Utility)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 387, 452))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.grp_add_curves = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.grp_add_curves.setFont(font)
        self.grp_add_curves.setStyleSheet("color: rgb(216, 216, 216);")
        self.grp_add_curves.setFlat(True)
        self.grp_add_curves.setObjectName("grp_add_curves")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grp_add_curves)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_add_curve = QtWidgets.QPushButton(self.grp_add_curves)
        self.btn_add_curve.setEnabled(True)
        self.btn_add_curve.setObjectName("btn_add_curve")
        self.horizontalLayout_2.addWidget(self.btn_add_curve)
        self.btn_del_curve = QtWidgets.QPushButton(self.grp_add_curves)
        self.btn_del_curve.setObjectName("btn_del_curve")
        self.horizontalLayout_2.addWidget(self.btn_del_curve)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.grp_add_curves)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spin_cv_count = QtWidgets.QSpinBox(self.grp_add_curves)
        self.spin_cv_count.setMinimum(2)
        self.spin_cv_count.setMaximum(200)
        self.spin_cv_count.setProperty("value", 5)
        self.spin_cv_count.setObjectName("spin_cv_count")
        self.horizontalLayout.addWidget(self.spin_cv_count)
        self.label_3 = QtWidgets.QLabel(self.grp_add_curves)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dspin_crv_len = QtWidgets.QDoubleSpinBox(self.grp_add_curves)
        self.dspin_crv_len.setMinimum(1.0)
        self.dspin_crv_len.setMaximum(999.99)
        self.dspin_crv_len.setProperty("value", 5.0)
        self.dspin_crv_len.setObjectName("dspin_crv_len")
        self.horizontalLayout.addWidget(self.dspin_crv_len)
        self.check_lock_len = QtWidgets.QCheckBox(self.grp_add_curves)
        self.check_lock_len.setChecked(True)
        self.check_lock_len.setObjectName("check_lock_len")
        self.horizontalLayout.addWidget(self.check_lock_len)
        self.checkBox = QtWidgets.QCheckBox(self.grp_add_curves)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.grp_add_curves)
        self.grp_selection = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.grp_selection.setStyleSheet("color: rgb(216, 216, 216);")
        self.grp_selection.setFlat(True)
        self.grp_selection.setObjectName("grp_selection")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grp_selection)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.check_curve_mode = QtWidgets.QCheckBox(self.grp_selection)
        self.check_curve_mode.setChecked(True)
        self.check_curve_mode.setObjectName("check_curve_mode")
        self.verticalLayout_2.addWidget(self.check_curve_mode)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_sel_curve = QtWidgets.QPushButton(self.grp_selection)
        self.btn_sel_curve.setEnabled(True)
        self.btn_sel_curve.setObjectName("btn_sel_curve")
        self.horizontalLayout_3.addWidget(self.btn_sel_curve)
        self.btn_sel_cv = QtWidgets.QPushButton(self.grp_selection)
        self.btn_sel_cv.setObjectName("btn_sel_cv")
        self.horizontalLayout_3.addWidget(self.btn_sel_cv)
        self.btn_sel_root = QtWidgets.QPushButton(self.grp_selection)
        self.btn_sel_root.setObjectName("btn_sel_root")
        self.horizontalLayout_3.addWidget(self.btn_sel_root)
        self.btn_sel_end = QtWidgets.QPushButton(self.grp_selection)
        self.btn_sel_end.setObjectName("btn_sel_end")
        self.horizontalLayout_3.addWidget(self.btn_sel_end)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.grp_selection)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_scale = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_scale.setStyleSheet("color: rgb(216, 216, 216);")
        self.label_scale.setObjectName("label_scale")
        self.horizontalLayout_4.addWidget(self.label_scale)
        self.dspin_scale_curve = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.dspin_scale_curve.setStyleSheet("color: rgb(216, 216, 216);")
        self.dspin_scale_curve.setObjectName("dspin_scale_curve")
        self.horizontalLayout_4.addWidget(self.dspin_scale_curve)
        self.btn_scale_curve = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_scale_curve.setStyleSheet("color: rgb(216, 216, 216);")
        self.btn_scale_curve.setObjectName("btn_scale_curve")
        self.horizontalLayout_4.addWidget(self.btn_scale_curve)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.check_draw_override = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.check_draw_override.setStyleSheet("color: rgb(216, 216, 216);")
        self.check_draw_override.setObjectName("check_draw_override")
        self.verticalLayout_3.addWidget(self.check_draw_override)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_color = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_color.setStyleSheet("color: rgb(216, 216, 216);")
        self.label_color.setObjectName("label_color")
        self.horizontalLayout_5.addWidget(self.label_color)
        self.btn_color_picker = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_color_picker.setMinimumSize(QtCore.QSize(55, 12))
        self.btn_color_picker.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_color_picker.setStyleSheet("background-color: rgb(37, 37, 110);")
        self.btn_color_picker.setText("")
        self.btn_color_picker.setObjectName("btn_color_picker")
        self.horizontalLayout_5.addWidget(self.btn_color_picker)
        self.slider_color = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.slider_color.setMaximum(100)
        self.slider_color.setOrientation(QtCore.Qt.Horizontal)
        self.slider_color.setObjectName("slider_color")
        self.horizontalLayout_5.addWidget(self.slider_color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_line_width = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_line_width.setStyleSheet("color: rgb(216, 216, 216);")
        self.label_line_width.setObjectName("label_line_width")
        self.horizontalLayout_6.addWidget(self.label_line_width)
        self.spin_line_width = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.spin_line_width.setStyleSheet("color: rgb(216, 216, 216);")
        self.spin_line_width.setMaximum(10.0)
        self.spin_line_width.setSingleStep(0.1)
        self.spin_line_width.setProperty("value", 1.0)
        self.spin_line_width.setObjectName("spin_line_width")
        self.horizontalLayout_6.addWidget(self.spin_line_width)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.group_grouping = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_grouping.sizePolicy().hasHeightForWidth())
        self.group_grouping.setSizePolicy(sizePolicy)
        self.group_grouping.setMinimumSize(QtCore.QSize(0, 150))
        self.group_grouping.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.group_grouping.setFont(font)
        self.group_grouping.setStyleSheet("color: rgb(216, 216, 216);")
        self.group_grouping.setObjectName("group_grouping")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.group_grouping)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.list_groups = QtWidgets.QListWidget(self.group_grouping)
        self.list_groups.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.list_groups.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_groups.setObjectName("list_groups")
        self.verticalLayout_4.addWidget(self.list_groups)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_new_item = QtWidgets.QPushButton(self.group_grouping)
        self.btn_new_item.setObjectName("btn_new_item")
        self.horizontalLayout_7.addWidget(self.btn_new_item)
        self.pushButton_2 = QtWidgets.QPushButton(self.group_grouping)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.btn_del_grp = QtWidgets.QPushButton(self.group_grouping)
        self.btn_del_grp.setObjectName("btn_del_grp")
        self.horizontalLayout_7.addWidget(self.btn_del_grp)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addWidget(self.group_grouping)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Curve Tool", None, -1))
        self.label_top_Curves_Utility.setText(QtWidgets.QApplication.translate("MainWindow", "Guide Builder", None, -1))
        self.grp_add_curves.setTitle(QtWidgets.QApplication.translate("MainWindow", "Add Curves", None, -1))
        self.btn_add_curve.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.btn_del_curve.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "CV Count:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "length:", None, -1))
        self.check_lock_len.setText(QtWidgets.QApplication.translate("MainWindow", "Lock Length", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "Mirror", None, -1))
        self.grp_selection.setTitle(QtWidgets.QApplication.translate("MainWindow", "Selection ", None, -1))
        self.check_curve_mode.setText(QtWidgets.QApplication.translate("MainWindow", "Curve Mode", None, -1))
        self.btn_sel_curve.setText(QtWidgets.QApplication.translate("MainWindow", "Select Curve", None, -1))
        self.btn_sel_cv.setText(QtWidgets.QApplication.translate("MainWindow", "Select CV", None, -1))
        self.btn_sel_root.setText(QtWidgets.QApplication.translate("MainWindow", "Select Root", None, -1))
        self.btn_sel_end.setText(QtWidgets.QApplication.translate("MainWindow", "Select End", None, -1))
        self.label_scale.setText(QtWidgets.QApplication.translate("MainWindow", "Scale:", None, -1))
        self.btn_scale_curve.setText(QtWidgets.QApplication.translate("MainWindow", "Scale*x", None, -1))
        self.check_draw_override.setText(QtWidgets.QApplication.translate("MainWindow", "Draw overrides", None, -1))
        self.label_color.setText(QtWidgets.QApplication.translate("MainWindow", "Color:", None, -1))
        self.label_line_width.setText(QtWidgets.QApplication.translate("MainWindow", "Line Width:", None, -1))
        self.group_grouping.setTitle(QtWidgets.QApplication.translate("MainWindow", "Grouping", None, -1))
        self.btn_new_item.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "New From selected", None, -1))
        self.btn_del_grp.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))

