# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_view = QtWidgets.QVBoxLayout()
        self.main_view.setObjectName("main_view")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.main_view.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addLayout(self.main_view)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_4.addWidget(self.label_23)
        self.prsample_et = QtWidgets.QLineEdit(self.centralwidget)
        self.prsample_et.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setKerning(False)
        self.prsample_et.setFont(font)
        self.prsample_et.setAutoFillBackground(True)
        self.prsample_et.setDragEnabled(False)
        self.prsample_et.setReadOnly(False)
        self.prsample_et.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.prsample_et.setClearButtonEnabled(True)
        self.prsample_et.setObjectName("prsample_et")
        self.horizontalLayout_4.addWidget(self.prsample_et)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setMinimumSize(QtCore.QSize(50, 0))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setWordWrap(False)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_4.addWidget(self.label_24)
        self.prtip_et = QtWidgets.QLineEdit(self.centralwidget)
        self.prtip_et.setMaximumSize(QtCore.QSize(100, 16777215))
        self.prtip_et.setClearButtonEnabled(True)
        self.prtip_et.setObjectName("prtip_et")
        self.horizontalLayout_4.addWidget(self.prtip_et)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(192, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.etip_et = QtWidgets.QLineEdit(self.centralwidget)
        self.etip_et.setMaximumSize(QtCore.QSize(100, 16777215))
        self.etip_et.setClearButtonEnabled(True)
        self.etip_et.setObjectName("etip_et")
        self.horizontalLayout_10.addWidget(self.etip_et)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        self.label_28.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_10.addWidget(self.label_28)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setObjectName("label_41")
        self.gridLayout_8.addWidget(self.label_41, 3, 0, 1, 1)
        self.r2_after = QtWidgets.QLabel(self.centralwidget)
        self.r2_after.setMinimumSize(QtCore.QSize(80, 0))
        self.r2_after.setMaximumSize(QtCore.QSize(80, 16777215))
        self.r2_after.setAlignment(QtCore.Qt.AlignCenter)
        self.r2_after.setObjectName("r2_after")
        self.gridLayout_8.addWidget(self.r2_after, 3, 3, 1, 1)
        self.rt_et = QtWidgets.QLabel(self.centralwidget)
        self.rt_et.setAlignment(QtCore.Qt.AlignCenter)
        self.rt_et.setObjectName("rt_et")
        self.gridLayout_8.addWidget(self.rt_et, 2, 2, 1, 1)
        self.after_time = QtWidgets.QLabel(self.centralwidget)
        self.after_time.setAlignment(QtCore.Qt.AlignCenter)
        self.after_time.setObjectName("after_time")
        self.gridLayout_8.addWidget(self.after_time, 3, 2, 1, 1)
        self.slope_after = QtWidgets.QLabel(self.centralwidget)
        self.slope_after.setMinimumSize(QtCore.QSize(80, 0))
        self.slope_after.setMaximumSize(QtCore.QSize(80, 16777215))
        self.slope_after.setAlignment(QtCore.Qt.AlignCenter)
        self.slope_after.setObjectName("slope_after")
        self.gridLayout_8.addWidget(self.slope_after, 3, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 0, 2, 1, 1)
        self.ac_et = QtWidgets.QLineEdit(self.centralwidget)
        self.ac_et.setMinimumSize(QtCore.QSize(0, 0))
        self.ac_et.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ac_et.setAcceptDrops(False)
        self.ac_et.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ac_et.setClearButtonEnabled(True)
        self.ac_et.setObjectName("ac_et")
        self.gridLayout_8.addWidget(self.ac_et, 3, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 1, 0, 1, 1)
        self.slope_before = QtWidgets.QLabel(self.centralwidget)
        self.slope_before.setMinimumSize(QtCore.QSize(80, 0))
        self.slope_before.setMaximumSize(QtCore.QSize(80, 16777215))
        self.slope_before.setAlignment(QtCore.Qt.AlignCenter)
        self.slope_before.setObjectName("slope_before")
        self.gridLayout_8.addWidget(self.slope_before, 1, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 3, 1, 1)
        self.r2_before = QtWidgets.QLabel(self.centralwidget)
        self.r2_before.setMinimumSize(QtCore.QSize(80, 0))
        self.r2_before.setMaximumSize(QtCore.QSize(80, 16777215))
        self.r2_before.setAlignment(QtCore.Qt.AlignCenter)
        self.r2_before.setObjectName("r2_before")
        self.gridLayout_8.addWidget(self.r2_before, 1, 3, 1, 1)
        self.before_time = QtWidgets.QLabel(self.centralwidget)
        self.before_time.setAlignment(QtCore.Qt.AlignCenter)
        self.before_time.setObjectName("before_time")
        self.gridLayout_8.addWidget(self.before_time, 1, 2, 1, 1)
        self.bc_et = QtWidgets.QLineEdit(self.centralwidget)
        self.bc_et.setMinimumSize(QtCore.QSize(0, 0))
        self.bc_et.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bc_et.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bc_et.setClearButtonEnabled(True)
        self.bc_et.setObjectName("bc_et")
        self.gridLayout_8.addWidget(self.bc_et, 1, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setObjectName("label_40")
        self.gridLayout_8.addWidget(self.label_40, 2, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.tipGeometryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.tipGeometryComboBox.setObjectName("tipGeometryComboBox")
        self.tipGeometryComboBox.addItem("")
        self.tipGeometryComboBox.addItem("")
        self.tipGeometryComboBox.addItem("")
        self.horizontalLayout_9.addWidget(self.tipGeometryComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 155))
        self.stackedWidget.setStatusTip("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Berkovich = QtWidgets.QWidget()
        self.Berkovich.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Berkovich.setObjectName("Berkovich")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Berkovich)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_16 = QtWidgets.QLabel(self.Berkovich)
        self.label_16.setMinimumSize(QtCore.QSize(50, 0))
        self.label_16.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 5, 0, 1, 1)
        self.et_c4 = QtWidgets.QLineEdit(self.Berkovich)
        self.et_c4.setMinimumSize(QtCore.QSize(100, 0))
        self.et_c4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.et_c4.setClearButtonEnabled(True)
        self.et_c4.setObjectName("et_c4")
        self.gridLayout_6.addWidget(self.et_c4, 4, 1, 1, 1)
        self.et_c3 = QtWidgets.QLineEdit(self.Berkovich)
        self.et_c3.setMinimumSize(QtCore.QSize(100, 0))
        self.et_c3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.et_c3.setClearButtonEnabled(True)
        self.et_c3.setObjectName("et_c3")
        self.gridLayout_6.addWidget(self.et_c3, 3, 1, 1, 1)
        self.label_hc = QtWidgets.QLabel(self.Berkovich)
        self.label_hc.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_hc.setObjectName("label_hc")
        self.gridLayout_6.addWidget(self.label_hc, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 1, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.Berkovich)
        self.label_18.setMinimumSize(QtCore.QSize(50, 0))
        self.label_18.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.Berkovich)
        self.label_34.setMinimumSize(QtCore.QSize(50, 0))
        self.label_34.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_6.addWidget(self.label_34, 1, 0, 1, 1)
        self.et_c1 = QtWidgets.QLineEdit(self.Berkovich)
        self.et_c1.setMinimumSize(QtCore.QSize(100, 0))
        self.et_c1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.et_c1.setClearButtonEnabled(True)
        self.et_c1.setObjectName("et_c1")
        self.gridLayout_6.addWidget(self.et_c1, 1, 1, 1, 1)
        self.et_c2 = QtWidgets.QLineEdit(self.Berkovich)
        self.et_c2.setMinimumSize(QtCore.QSize(100, 0))
        self.et_c2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.et_c2.setClearButtonEnabled(True)
        self.et_c2.setObjectName("et_c2")
        self.gridLayout_6.addWidget(self.et_c2, 2, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.Berkovich)
        self.label_30.setMinimumSize(QtCore.QSize(50, 0))
        self.label_30.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 4, 0, 1, 1)
        self.label_ac = QtWidgets.QLabel(self.Berkovich)
        self.label_ac.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_ac.setObjectName("label_ac")
        self.gridLayout_6.addWidget(self.label_ac, 6, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.Berkovich)
        self.label_32.setMinimumSize(QtCore.QSize(50, 0))
        self.label_32.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 6, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.Berkovich)
        self.label_29.setMinimumSize(QtCore.QSize(50, 0))
        self.label_29.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_6)
        self.stackedWidget.addWidget(self.Berkovich)
        self.Spherical = QtWidgets.QWidget()
        self.Spherical.setObjectName("Spherical")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Spherical)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 3, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.Spherical)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.radius_et = QtWidgets.QLineEdit(self.page)
        self.radius_et.setMinimumSize(QtCore.QSize(0, 0))
        self.radius_et.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radius_et.setClearButtonEnabled(True)
        self.radius_et.setObjectName("radius_et")
        self.horizontalLayout_6.addWidget(self.radius_et)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setMinimumSize(QtCore.QSize(20, 0))
        self.label_9.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.previoustoolButton = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/pic/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previoustoolButton.setIcon(icon)
        self.previoustoolButton.setIconSize(QtCore.QSize(16, 16))
        self.previoustoolButton.setAutoRaise(True)
        self.previoustoolButton.setObjectName("previoustoolButton")
        self.horizontalLayout_8.addWidget(self.previoustoolButton)
        self.nexttoolButton = QtWidgets.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/pic/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nexttoolButton.setIcon(icon1)
        self.nexttoolButton.setAutoRaise(True)
        self.nexttoolButton.setObjectName("nexttoolButton")
        self.horizontalLayout_8.addWidget(self.nexttoolButton)
        self.alltoolButton = QtWidgets.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/pic/all.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alltoolButton.setIcon(icon2)
        self.alltoolButton.setAutoRaise(True)
        self.alltoolButton.setObjectName("alltoolButton")
        self.horizontalLayout_8.addWidget(self.alltoolButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.toolButton_open = QtWidgets.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/pic/single.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_open.setIcon(icon3)
        self.toolButton_open.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_open.setAutoRaise(True)
        self.toolButton_open.setObjectName("toolButton_open")
        self.horizontalLayout_8.addWidget(self.toolButton_open)
        self.toolButton_folder = QtWidgets.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/pic/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_folder.setIcon(icon4)
        self.toolButton_folder.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_folder.setAutoRaise(True)
        self.toolButton_folder.setObjectName("toolButton_folder")
        self.horizontalLayout_8.addWidget(self.toolButton_folder)
        self.toolButton_excel = QtWidgets.QToolButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("res/pic/Excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_excel.setIcon(icon5)
        self.toolButton_excel.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_excel.setAutoRaise(True)
        self.toolButton_excel.setObjectName("toolButton_excel")
        self.horizontalLayout_8.addWidget(self.toolButton_excel)
        self.toolButton_txt = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton_txt.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("res/pic/txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_txt.setIcon(icon6)
        self.toolButton_txt.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_txt.setAutoRaise(True)
        self.toolButton_txt.setObjectName("toolButton_txt")
        self.horizontalLayout_8.addWidget(self.toolButton_txt)
        self.toolButton_setting = QtWidgets.QToolButton(self.centralwidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("res/pic/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_setting.setIcon(icon7)
        self.toolButton_setting.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_setting.setAutoRaise(True)
        self.toolButton_setting.setObjectName("toolButton_setting")
        self.horizontalLayout_8.addWidget(self.toolButton_setting)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)
        self.y_combo = QtWidgets.QComboBox(self.centralwidget)
        self.y_combo.setObjectName("y_combo")
        self.gridLayout_3.addWidget(self.y_combo, 0, 1, 1, 1)
        self.x_combo = QtWidgets.QComboBox(self.centralwidget)
        self.x_combo.setObjectName("x_combo")
        self.gridLayout_3.addWidget(self.x_combo, 0, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.smooth_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.smooth_spinBox.setObjectName("smooth_spinBox")
        self.gridLayout_3.addWidget(self.smooth_spinBox, 0, 5, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.label_tips = QtWidgets.QLabel(self.centralwidget)
        self.label_tips.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_tips.setFont(font)
        self.label_tips.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_tips.setObjectName("label_tips")
        self.verticalLayout_4.addWidget(self.label_tips)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Poisson\'s Ratio"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>sampl</p></body></html>"))
        self.prsample_et.setText(_translate("MainWindow", "1"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p>tip</p></body></html>"))
        self.prtip_et.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "Elasic Modulus of tip"))
        self.etip_et.setText(_translate("MainWindow", "1"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p>Pa</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Slope"))
        self.label_41.setText(_translate("MainWindow", "End:"))
        self.r2_after.setText(_translate("MainWindow", "1"))
        self.rt_et.setText(_translate("MainWindow", "0"))
        self.after_time.setText(_translate("MainWindow", "0"))
        self.slope_after.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Time Point(s)"))
        self.ac_et.setText(_translate("MainWindow", "100"))
        self.label_35.setText(_translate("MainWindow", "Start:"))
        self.slope_before.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Goodness of fit"))
        self.r2_before.setText(_translate("MainWindow", "1"))
        self.before_time.setText(_translate("MainWindow", "0"))
        self.bc_et.setText(_translate("MainWindow", "100"))
        self.label_40.setText(_translate("MainWindow", "Retract:"))
        self.label_3.setText(_translate("MainWindow", "Type of Indenter"))
        self.tipGeometryComboBox.setItemText(0, _translate("MainWindow", "Berkovich"))
        self.tipGeometryComboBox.setItemText(1, _translate("MainWindow", "Spherical"))
        self.tipGeometryComboBox.setItemText(2, _translate("MainWindow", "Punch"))
        self.label_16.setText(_translate("MainWindow", "hc:"))
        self.et_c4.setText(_translate("MainWindow", "0"))
        self.et_c3.setText(_translate("MainWindow", "0"))
        self.label_hc.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "C3:"))
        self.label_34.setText(_translate("MainWindow", "C1:"))
        self.et_c1.setText(_translate("MainWindow", "0"))
        self.et_c2.setText(_translate("MainWindow", "0"))
        self.label_30.setText(_translate("MainWindow", "C4:"))
        self.label_ac.setText(_translate("MainWindow", "0"))
        self.label_32.setText(_translate("MainWindow", "Ac:"))
        self.label_29.setText(_translate("MainWindow", "C2:"))
        self.label_5.setText(_translate("MainWindow", "Radius:"))
        self.radius_et.setText(_translate("MainWindow", "3.022"))
        self.label_9.setText(_translate("MainWindow", "um"))
        self.previoustoolButton.setText(_translate("MainWindow", "..."))
        self.nexttoolButton.setText(_translate("MainWindow", "..."))
        self.alltoolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_open.setText(_translate("MainWindow", "open"))
        self.toolButton_folder.setText(_translate("MainWindow", "flod"))
        self.toolButton_excel.setText(_translate("MainWindow", "export"))
        self.toolButton_txt.setText(_translate("MainWindow", "..."))
        self.toolButton_setting.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "Smooth Level:"))
        self.label_10.setText(_translate("MainWindow", "X-axis"))
        self.label_12.setText(_translate("MainWindow", "Y-axis"))
        self.label_tips.setText(_translate("MainWindow", "Tips"))
