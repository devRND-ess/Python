# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Python\maya\controll_creator\Ui_control_creator.ui'
#
# Created: Wed Feb 12 22:00:00 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_master = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_master.sizePolicy().hasHeightForWidth())
        self.label_master.setSizePolicy(sizePolicy)
        self.label_master.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Stencil Std")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_master.setFont(font)
        self.label_master.setStyleSheet("color: rgb(212,212,212);\n"
"background-color: rgb(17, 194, 126);")
        self.label_master.setAlignment(QtCore.Qt.AlignCenter)
        self.label_master.setObjectName("label_master")
        self.verticalLayout.addWidget(self.label_master)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 358, 550))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.btn_color_picker = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_color_picker.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.btn_color_picker.setText("")
        self.btn_color_picker.setObjectName("btn_color_picker")
        self.horizontalLayout.addWidget(self.btn_color_picker)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(216, 144, 0);")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_drop_stick = QtWidgets.QPushButton(self.groupBox)
        self.btn_drop_stick.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_drop_stick.setObjectName("btn_drop_stick")
        self.gridLayout.addWidget(self.btn_drop_stick, 1, 1, 1, 1)
        self.btn_water_drop = QtWidgets.QPushButton(self.groupBox)
        self.btn_water_drop.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_water_drop.setObjectName("btn_water_drop")
        self.gridLayout.addWidget(self.btn_water_drop, 0, 1, 1, 1)
        self.btn_star_stick = QtWidgets.QPushButton(self.groupBox)
        self.btn_star_stick.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_star_stick.setObjectName("btn_star_stick")
        self.gridLayout.addWidget(self.btn_star_stick, 0, 0, 1, 1)
        self.btn_lever = QtWidgets.QPushButton(self.groupBox)
        self.btn_lever.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_lever.setObjectName("btn_lever")
        self.gridLayout.addWidget(self.btn_lever, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(226, 134, 0);")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_master_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_master_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_master_arrow.setObjectName("btn_master_arrow")
        self.gridLayout_2.addWidget(self.btn_master_arrow, 0, 0, 1, 1)
        self.btn_tri_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_tri_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_tri_arrow.setObjectName("btn_tri_arrow")
        self.gridLayout_2.addWidget(self.btn_tri_arrow, 2, 0, 1, 1)
        self.btn_arc_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_arc_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_arc_arrow.setObjectName("btn_arc_arrow")
        self.gridLayout_2.addWidget(self.btn_arc_arrow, 0, 1, 1, 1)
        self.btn_up_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_up_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_up_arrow.setObjectName("btn_up_arrow")
        self.gridLayout_2.addWidget(self.btn_up_arrow, 3, 1, 1, 1)
        self.btn_quad_arc_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_quad_arc_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_quad_arc_arrow.setObjectName("btn_quad_arc_arrow")
        self.gridLayout_2.addWidget(self.btn_quad_arc_arrow, 3, 0, 1, 1)
        self.btn_quad_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_quad_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_quad_arrow.setObjectName("btn_quad_arrow")
        self.gridLayout_2.addWidget(self.btn_quad_arrow, 2, 1, 1, 1)
        self.btn_double_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_double_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_double_arrow.setObjectName("btn_double_arrow")
        self.gridLayout_2.addWidget(self.btn_double_arrow, 1, 0, 1, 1)
        self.btn_double_arc_arrow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_double_arc_arrow.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_double_arc_arrow.setObjectName("btn_double_arc_arrow")
        self.gridLayout_2.addWidget(self.btn_double_arc_arrow, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: rgb(216, 144, 0);")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_circle_double_curved = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_circle_double_curved.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_circle_double_curved.setObjectName("btn_circle_double_curved")
        self.gridLayout_3.addWidget(self.btn_circle_double_curved, 1, 1, 1, 1)
        self.btn_circle = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_circle.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_circle.setObjectName("btn_circle")
        self.gridLayout_3.addWidget(self.btn_circle, 1, 0, 1, 1)
        self.btn_orbit = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_orbit.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_orbit.setObjectName("btn_orbit")
        self.gridLayout_3.addWidget(self.btn_orbit, 2, 1, 1, 1)
        self.btn_octa_ring = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_octa_ring.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_octa_ring.setObjectName("btn_octa_ring")
        self.gridLayout_3.addWidget(self.btn_octa_ring, 2, 0, 1, 1)
        self.btn_spinning_circle = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_spinning_circle.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_spinning_circle.setObjectName("btn_spinning_circle")
        self.gridLayout_3.addWidget(self.btn_spinning_circle, 3, 0, 1, 1)
        self.btn_square = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_square.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_square.setObjectName("btn_square")
        self.gridLayout_3.addWidget(self.btn_square, 3, 1, 1, 1)
        self.btn_triangle = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_triangle.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_triangle.setObjectName("btn_triangle")
        self.gridLayout_3.addWidget(self.btn_triangle, 5, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("color: rgb(226, 134, 0);")
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_eye_global = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_eye_global.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_eye_global.setObjectName("btn_eye_global")
        self.gridLayout_4.addWidget(self.btn_eye_global, 0, 0, 1, 1)
        self.btn_ik_fk = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_ik_fk.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_ik_fk.setObjectName("btn_ik_fk")
        self.gridLayout_4.addWidget(self.btn_ik_fk, 1, 0, 1, 1)
        self.btn_eye_look = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_eye_look.setStyleSheet("color: rgb(200, 200, 200);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.btn_eye_look.setObjectName("btn_eye_look")
        self.gridLayout_4.addWidget(self.btn_eye_look, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_master.setText(QtWidgets.QApplication.translate("MainWindow", "Control Builder", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Color:", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Sticks", None, -1))
        self.btn_drop_stick.setText(QtWidgets.QApplication.translate("MainWindow", "Drop Stick", None, -1))
        self.btn_water_drop.setText(QtWidgets.QApplication.translate("MainWindow", "Water Drop", None, -1))
        self.btn_star_stick.setText(QtWidgets.QApplication.translate("MainWindow", "Star Stick", None, -1))
        self.btn_lever.setText(QtWidgets.QApplication.translate("MainWindow", "Lever", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Arrows", None, -1))
        self.btn_master_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Master Arrow", None, -1))
        self.btn_tri_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Tri Arrow", None, -1))
        self.btn_arc_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Arc Arrow", None, -1))
        self.btn_up_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Up Arrow", None, -1))
        self.btn_quad_arc_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Quad Arc Arrow", None, -1))
        self.btn_quad_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Quad Arrow", None, -1))
        self.btn_double_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Double Arrow", None, -1))
        self.btn_double_arc_arrow.setText(QtWidgets.QApplication.translate("MainWindow", "Double Arc Arrow", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Basic Shapes", None, -1))
        self.btn_circle_double_curved.setText(QtWidgets.QApplication.translate("MainWindow", "Circle Double Curved", None, -1))
        self.btn_circle.setText(QtWidgets.QApplication.translate("MainWindow", "Circle", None, -1))
        self.btn_orbit.setText(QtWidgets.QApplication.translate("MainWindow", "Orbit", None, -1))
        self.btn_octa_ring.setText(QtWidgets.QApplication.translate("MainWindow", "Octa Ring", None, -1))
        self.btn_spinning_circle.setText(QtWidgets.QApplication.translate("MainWindow", "Spinning_Circle", None, -1))
        self.btn_square.setText(QtWidgets.QApplication.translate("MainWindow", "Square", None, -1))
        self.btn_triangle.setText(QtWidgets.QApplication.translate("MainWindow", "Triangle", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Face/IK-FK", None, -1))
        self.btn_eye_global.setText(QtWidgets.QApplication.translate("MainWindow", "Eye Global", None, -1))
        self.btn_ik_fk.setText(QtWidgets.QApplication.translate("MainWindow", "Ik/Fk", None, -1))
        self.btn_eye_look.setText(QtWidgets.QApplication.translate("MainWindow", "Eye Look", None, -1))

