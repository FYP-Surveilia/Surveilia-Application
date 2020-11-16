# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveiliaFrontEnd.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_surveiliaFrontEnd(object):
    def setupUi(self, surveiliaFrontEnd):
        surveiliaFrontEnd.setObjectName("surveiliaFrontEnd")
        surveiliaFrontEnd.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(surveiliaFrontEnd.sizePolicy().hasHeightForWidth())
        surveiliaFrontEnd.setSizePolicy(sizePolicy)
        surveiliaFrontEnd.setMinimumSize(QtCore.QSize(1000, 800))
        surveiliaFrontEnd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        surveiliaFrontEnd.setSizeIncrement(QtCore.QSize(0, 0))
        surveiliaFrontEnd.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 30px;\n"
"background-color:#1C1D25;\n"
"}\n"
"QFrame{\n"
"background: #2A2F3C ;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"background:white;\n"
"border-radius:60px;\n"
"}\n"
"QLineEdit{\n"
"background: transparent;\n"
"border:none;\n"
"color:BLACK;\n"
"border-bottom:1px solid black;\n"
"font-size:20px;\n"
"}\n"
"QPushButton{\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"color:white ;\n"
"background:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"#logoLabel{\n"
"background:transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(surveiliaFrontEnd)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background-color:#1C1D25;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background: #1C1D25;\n"
"border:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 30px;\n"
"background-color:#1C1D25;\n"
"}\n"
"QFrame{\n"
"background: #2A2F3C ;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"background:white;\n"
"border-radius:60px;\n"
"}\n"
"QLineEdit{\n"
"background: transparent;\n"
"border:none;\n"
"color:WHITE;\n"
"border-bottom:1px solid WHITE;\n"
"font-size:20px;\n"
"\n"
"}\n"
"QPushButton{\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"#logoLabel{\n"
"background:transparent;\n"
"}")
        self.login_page.setObjectName("login_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.login_page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login_widget = QtWidgets.QWidget(self.login_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_widget.sizePolicy().hasHeightForWidth())
        self.login_widget.setSizePolicy(sizePolicy)
        self.login_widget.setMinimumSize(QtCore.QSize(560, 600))
        self.login_widget.setObjectName("login_widget")
        self.logo1_label = QtWidgets.QLabel(self.login_widget)
        self.logo1_label.setGeometry(QtCore.QRect(200, 80, 150, 100))
        self.logo1_label.setStyleSheet("background: transparent;")
        self.logo1_label.setText("")
        self.logo1_label.setPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"))
        self.logo1_label.setScaledContents(True)
        self.logo1_label.setObjectName("logo1_label")
        self.loginForm_frame = QtWidgets.QFrame(self.login_widget)
        self.loginForm_frame.setGeometry(QtCore.QRect(70, 130, 411, 571))
        self.loginForm_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginForm_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginForm_frame.setObjectName("loginForm_frame")
        self.title1_label = QtWidgets.QLabel(self.loginForm_frame)
        self.title1_label.setGeometry(QtCore.QRect(110, 100, 221, 71))
        self.title1_label.setStyleSheet("font-size:35px;")
        self.title1_label.setObjectName("title1_label")
        self.username1_field = QtWidgets.QLineEdit(self.loginForm_frame)
        self.username1_field.setGeometry(QtCore.QRect(50, 190, 301, 30))
        self.username1_field.setObjectName("username1_field")
        self.password1_field = QtWidgets.QLineEdit(self.loginForm_frame)
        self.password1_field.setGeometry(QtCore.QRect(50, 250, 301, 30))
        self.password1_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password1_field.setObjectName("password1_field")
        self.login_pushButton = QtWidgets.QPushButton(self.loginForm_frame)
        self.login_pushButton.setGeometry(QtCore.QRect(100, 440, 211, 40))
        self.login_pushButton.setObjectName("login_pushButton")
        self.security_radioButton = QtWidgets.QRadioButton(self.loginForm_frame)
        self.security_radioButton.setGeometry(QtCore.QRect(170, 380, 151, 21))
        self.security_radioButton.setStyleSheet("QRadioButton{\n"
"color:WHITE;\n"
"font-size:16px;\n"
"background:transparent;\n"
"\n"
"\n"
"}")
        self.security_radioButton.setObjectName("security_radioButton")
        self.admin_radioButton = QtWidgets.QRadioButton(self.loginForm_frame)
        self.admin_radioButton.setGeometry(QtCore.QRect(170, 340, 141, 20))
        self.admin_radioButton.setStyleSheet("QRadioButton{\n"
"color:WHITE;\n"
"font-size:16px;\n"
"background:transparent;\n"
"\n"
"}")
        self.admin_radioButton.setObjectName("admin_radioButton")
        self.loginas1_label = QtWidgets.QLabel(self.loginForm_frame)
        self.loginas1_label.setGeometry(QtCore.QRect(50, 330, 91, 41))
        self.loginas1_label.setStyleSheet("*{\n"
"background: transparent;\n"
"border:none;\n"
"color:WHITE;\n"
"font-size:18px;\n"
"font-weight:500;\n"
"\n"
"}")
        self.loginas1_label.setObjectName("loginas1_label")
        self.loginFlag_label = QtWidgets.QLabel(self.loginForm_frame)
        self.loginFlag_label.setGeometry(QtCore.QRect(50, 290, 301, 16))
        self.loginFlag_label.setStyleSheet("font-size:16px;\n"
"COLOR:red;")
        self.loginFlag_label.setText("")
        self.loginFlag_label.setObjectName("loginFlag_label")
        self.eye_toolButton = QtWidgets.QToolButton(self.loginForm_frame)
        self.eye_toolButton.setGeometry(QtCore.QRect(320, 250, 27, 22))
        self.eye_toolButton.setStyleSheet("background: #2A2F3C ;\n"
"")
        self.eye_toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/invisible-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eye_toolButton.setIcon(icon)
        self.eye_toolButton.setObjectName("eye_toolButton")
        self.logo1_toolButton = QtWidgets.QToolButton(self.login_widget)
        self.logo1_toolButton.setGeometry(QtCore.QRect(210, 70, 120, 120))
        self.logo1_toolButton.setText("")
        self.logo1_toolButton.setObjectName("logo1_toolButton")
        self.loginForm_frame.raise_()
        self.logo1_toolButton.raise_()
        self.logo1_label.raise_()
        self.horizontalLayout.addWidget(self.login_widget)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.mainStackedWidget.addWidget(self.login_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.menuBar = QtWidgets.QWidget(self.main_page)
        self.menuBar.setMinimumSize(QtCore.QSize(90, 0))
        self.menuBar.setMaximumSize(QtCore.QSize(80, 16777215))
        self.menuBar.setStyleSheet("*{background: #1C1D25;\n"
"font-size: 16px;\n"
"}\n"
"QToolButton:hover{\n"
"     background-color:#2A2F3C;\n"
"}\n"
"QToolButton:pressed{\n"
"     background-color: #2A2F3C ;     \n"
"}")
        self.menuBar.setObjectName("menuBar")
        self.camera_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.camera_toolButton.setGeometry(QtCore.QRect(0, 100, 90, 71))
        self.camera_toolButton.setMinimumSize(QtCore.QSize(90, 0))
        self.camera_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.camera_toolButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("camera-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camera_toolButton.setIcon(icon1)
        self.camera_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.camera_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.camera_toolButton.setObjectName("camera_toolButton")
        self.logout_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.logout_toolButton.setGeometry(QtCore.QRect(0, 550, 90, 71))
        self.logout_toolButton.setMinimumSize(QtCore.QSize(90, 0))
        self.logout_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.logout_toolButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("logout-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_toolButton.setIcon(icon2)
        self.logout_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.logout_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.logout_toolButton.setObjectName("logout_toolButton")
        self.users_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.users_toolButton.setGeometry(QtCore.QRect(0, 460, 90, 71))
        self.users_toolButton.setMinimumSize(QtCore.QSize(90, 0))
        self.users_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.users_toolButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("group-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.users_toolButton.setIcon(icon3)
        self.users_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.users_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.users_toolButton.setObjectName("users_toolButton")
        self.language_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.language_toolButton.setGeometry(QtCore.QRect(0, 280, 90, 71))
        self.language_toolButton.setMinimumSize(QtCore.QSize(90, 0))
        self.language_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.language_toolButton.setFont(font)
        self.language_toolButton.setStyleSheet("font-size:16px;\n"
"background-repeat:no-repeat;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/logo/geography-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.language_toolButton.setIcon(icon4)
        self.language_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.language_toolButton.setCheckable(False)
        self.language_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.language_toolButton.setObjectName("language_toolButton")
        self.logo_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.logo_toolButton.setGeometry(QtCore.QRect(0, 10, 90, 71))
        self.logo_toolButton.setMinimumSize(QtCore.QSize(90, 0))
        self.logo_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.logo_toolButton.setFont(font)
        self.logo_toolButton.setStyleSheet("background-color:white;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_toolButton.setIcon(icon5)
        self.logo_toolButton.setIconSize(QtCore.QSize(90, 90))
        self.logo_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.logo_toolButton.setObjectName("logo_toolButton")
        self.alarm_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.alarm_toolButton.setGeometry(QtCore.QRect(0, 190, 90, 71))
        self.alarm_toolButton.setMinimumSize(QtCore.QSize(90, 0))
        self.alarm_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.alarm_toolButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("alarm-clock-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alarm_toolButton.setIcon(icon6)
        self.alarm_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.alarm_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.alarm_toolButton.setObjectName("alarm_toolButton")
        self.account_toolButton = QtWidgets.QToolButton(self.menuBar)
        self.account_toolButton.setGeometry(QtCore.QRect(0, 370, 90, 71))
        self.account_toolButton.setMinimumSize(QtCore.QSize(90, 0))
        self.account_toolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.account_toolButton.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("contacts-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_toolButton.setIcon(icon7)
        self.account_toolButton.setIconSize(QtCore.QSize(30, 30))
        self.account_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.account_toolButton.setObjectName("account_toolButton")
        self.camera_toolButton.raise_()
        self.users_toolButton.raise_()
        self.logout_toolButton.raise_()
        self.language_toolButton.raise_()
        self.logo_toolButton.raise_()
        self.alarm_toolButton.raise_()
        self.account_toolButton.raise_()
        self.horizontalLayout_5.addWidget(self.menuBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleBar2 = QtWidgets.QWidget(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBar2.sizePolicy().hasHeightForWidth())
        self.titleBar2.setSizePolicy(sizePolicy)
        self.titleBar2.setMinimumSize(QtCore.QSize(0, 80))
        self.titleBar2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.titleBar2.setStyleSheet("background: #1C1D25;\n"
"font-size: 24px;")
        self.titleBar2.setObjectName("titleBar2")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.titleBar2)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.title_label = QtWidgets.QLabel(self.titleBar2)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_17.addWidget(self.title_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_21.addItem(spacerItem4)
        self.userName_label = QtWidgets.QLabel(self.titleBar2)
        self.userName_label.setStyleSheet("font-size:15px;\n"
"text-align: right;\n"
"")
        self.userName_label.setText("")
        self.userName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.userName_label.setObjectName("userName_label")
        self.verticalLayout_21.addWidget(self.userName_label)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem5)
        self.dateTime_label = QtWidgets.QLabel(self.titleBar2)
        self.dateTime_label.setStyleSheet("text-align: right;\n"
"font-size:15px;")
        self.dateTime_label.setText("")
        self.dateTime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTime_label.setObjectName("dateTime_label")
        self.verticalLayout_21.addWidget(self.dateTime_label)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_21.addItem(spacerItem6)
        self.horizontalLayout_17.addLayout(self.verticalLayout_21)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem7)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_17)
        self.verticalLayout_2.addWidget(self.titleBar2)
        self.menuStackedWidget = QtWidgets.QStackedWidget(self.main_page)
        self.menuStackedWidget.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"border:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 20px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.menuStackedWidget.setObjectName("menuStackedWidget")
        self.welcome_page = QtWidgets.QWidget()
        self.welcome_page.setStyleSheet("BACKGROUND-COLOR:#2C313F;")
        self.welcome_page.setObjectName("welcome_page")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.welcome_page)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem8)
        self.frame_3 = QtWidgets.QFrame(self.welcome_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(470, 500))
        self.frame_3.setStyleSheet("QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.logo2_toolButton_2 = QtWidgets.QToolButton(self.frame_3)
        self.logo2_toolButton_2.setGeometry(QtCore.QRect(120, 50, 120, 120))
        self.logo2_toolButton_2.setStyleSheet("BACKGROUND-COLOR:WHITE;")
        self.logo2_toolButton_2.setText("")
        self.logo2_toolButton_2.setObjectName("logo2_toolButton_2")
        self.logo2_label_2 = QtWidgets.QLabel(self.frame_3)
        self.logo2_label_2.setGeometry(QtCore.QRect(110, 60, 150, 100))
        self.logo2_label_2.setStyleSheet("background: transparent;")
        self.logo2_label_2.setText("")
        self.logo2_label_2.setPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"))
        self.logo2_label_2.setScaledContents(True)
        self.logo2_label_2.setObjectName("logo2_label_2")
        self.welcome_label = QtWidgets.QLabel(self.frame_3)
        self.welcome_label.setGeometry(QtCore.QRect(30, 210, 321, 31))
        self.welcome_label.setStyleSheet("font-size:28px;")
        self.welcome_label.setObjectName("welcome_label")
        self.getStarted_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.getStarted_pushButton.setGeometry(QtCore.QRect(60, 357, 251, 41))
        self.getStarted_pushButton.setStyleSheet("background-color:#1C1D25;\n"
"")
        self.getStarted_pushButton.setObjectName("getStarted_pushButton")
        self.welcomeName_label = QtWidgets.QLabel(self.frame_3)
        self.welcomeName_label.setGeometry(QtCore.QRect(10, 260, 341, 21))
        self.welcomeName_label.setStyleSheet("text-align:center;")
        self.welcomeName_label.setText("")
        self.welcomeName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeName_label.setObjectName("welcomeName_label")
        self.horizontalLayout_18.addWidget(self.frame_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.menuStackedWidget.addWidget(self.welcome_page)
        self.camera_page = QtWidgets.QWidget()
        self.camera_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"background-color:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.camera_page.setObjectName("camera_page")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.camera_page)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.display_1 = QtWidgets.QLabel(self.camera_page)
        self.display_1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.display_1.setText("")
        self.display_1.setObjectName("display_1")
        self.verticalLayout_15.addWidget(self.display_1)
        self.gridLayout.addLayout(self.verticalLayout_15, 0, 0, 1, 1)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.display_5 = QtWidgets.QLabel(self.camera_page)
        self.display_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.display_5.setText("")
        self.display_5.setObjectName("display_5")
        self.verticalLayout_17.addWidget(self.display_5)
        self.gridLayout.addLayout(self.verticalLayout_17, 0, 2, 1, 1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.display_2 = QtWidgets.QLabel(self.camera_page)
        self.display_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.display_2.setText("")
        self.display_2.setObjectName("display_2")
        self.verticalLayout_16.addWidget(self.display_2)
        self.gridLayout.addLayout(self.verticalLayout_16, 0, 1, 1, 1)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.display_3 = QtWidgets.QLabel(self.camera_page)
        self.display_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.display_3.setText("")
        self.display_3.setObjectName("display_3")
        self.verticalLayout_18.addWidget(self.display_3)
        self.gridLayout.addLayout(self.verticalLayout_18, 1, 0, 1, 1)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.display_4 = QtWidgets.QLabel(self.camera_page)
        self.display_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.display_4.setText("")
        self.display_4.setObjectName("display_4")
        self.verticalLayout_19.addWidget(self.display_4)
        self.gridLayout.addLayout(self.verticalLayout_19, 1, 1, 1, 1)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.display_6 = QtWidgets.QLabel(self.camera_page)
        self.display_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.display_6.setText("")
        self.display_6.setObjectName("display_6")
        self.verticalLayout_20.addWidget(self.display_6)
        self.gridLayout.addLayout(self.verticalLayout_20, 1, 2, 1, 1)
        self.horizontalLayout_36.addLayout(self.gridLayout)
        self.widget = QtWidgets.QWidget(self.camera_page)
        self.widget.setMinimumSize(QtCore.QSize(200, 500))
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setStyleSheet("*{\n"
"background: #1C1D25;\n"
"}\n"
"QToolButton{\n"
"background: #2A2F3C ;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background:#2A2F3C ;\n"
"}\n"
"QToolButton:pressed{\n"
"background:#1C1D25;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        spacerItem10 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem10)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem11)
        self.addNew_pushButton = QtWidgets.QToolButton(self.widget)
        self.addNew_pushButton.setMinimumSize(QtCore.QSize(0, 100))
        self.addNew_pushButton.setMaximumSize(QtCore.QSize(16777215, 100))
        self.addNew_pushButton.setStyleSheet("*{\n"
"FONT-SIZE: 18px;\n"
"background: #2A2F3C ;\n"
"}\n"
"QToolButton:hover{\n"
"background:#2A2F3C ;\n"
"}\n"
"QToolButton:pressed{\n"
"background:#1C1D25;\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/logo/plus-8-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNew_pushButton.setIcon(icon8)
        self.addNew_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.addNew_pushButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.addNew_pushButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.addNew_pushButton.setObjectName("addNew_pushButton")
        self.horizontalLayout_35.addWidget(self.addNew_pushButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem12)
        self.verticalLayout_22.addLayout(self.horizontalLayout_35)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem13)
        self.cameras_label = QtWidgets.QLabel(self.widget)
        self.cameras_label.setStyleSheet("font-size:20px;")
        self.cameras_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cameras_label.setObjectName("cameras_label")
        self.verticalLayout_22.addWidget(self.cameras_label)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.camLabel1 = QtWidgets.QLabel(self.widget)
        self.camLabel1.setStyleSheet("font-size:16px;")
        self.camLabel1.setObjectName("camLabel1")
        self.horizontalLayout_12.addWidget(self.camLabel1)
        self.cam01_pushButton = QtWidgets.QToolButton(self.widget)
        self.cam01_pushButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/logo/edit-2-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cam01_pushButton.setIcon(icon9)
        self.cam01_pushButton.setObjectName("cam01_pushButton")
        self.horizontalLayout_12.addWidget(self.cam01_pushButton)
        self.displaycross_1 = QtWidgets.QToolButton(self.widget)
        self.displaycross_1.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/logo/x-mark-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.displaycross_1.setIcon(icon10)
        self.displaycross_1.setObjectName("displaycross_1")
        self.horizontalLayout_12.addWidget(self.displaycross_1)
        self.verticalLayout_22.addLayout(self.horizontalLayout_12)
        spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem15)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.camLabel2 = QtWidgets.QLabel(self.widget)
        self.camLabel2.setStyleSheet("font-size:16px;")
        self.camLabel2.setObjectName("camLabel2")
        self.horizontalLayout_21.addWidget(self.camLabel2)
        self.cam02_pushButton = QtWidgets.QToolButton(self.widget)
        self.cam02_pushButton.setText("")
        self.cam02_pushButton.setIcon(icon9)
        self.cam02_pushButton.setObjectName("cam02_pushButton")
        self.horizontalLayout_21.addWidget(self.cam02_pushButton)
        self.displaycross_2 = QtWidgets.QToolButton(self.widget)
        self.displaycross_2.setText("")
        self.displaycross_2.setIcon(icon10)
        self.displaycross_2.setObjectName("displaycross_2")
        self.horizontalLayout_21.addWidget(self.displaycross_2)
        self.verticalLayout_22.addLayout(self.horizontalLayout_21)
        spacerItem16 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem16)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.camLabel3 = QtWidgets.QLabel(self.widget)
        self.camLabel3.setStyleSheet("font-size:16px;")
        self.camLabel3.setObjectName("camLabel3")
        self.horizontalLayout_31.addWidget(self.camLabel3)
        self.cam03_pushButton = QtWidgets.QToolButton(self.widget)
        self.cam03_pushButton.setText("")
        self.cam03_pushButton.setIcon(icon9)
        self.cam03_pushButton.setObjectName("cam03_pushButton")
        self.horizontalLayout_31.addWidget(self.cam03_pushButton)
        self.displaycross_3 = QtWidgets.QToolButton(self.widget)
        self.displaycross_3.setText("")
        self.displaycross_3.setIcon(icon10)
        self.displaycross_3.setObjectName("displaycross_3")
        self.horizontalLayout_31.addWidget(self.displaycross_3)
        self.verticalLayout_22.addLayout(self.horizontalLayout_31)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem17)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.camLabel4 = QtWidgets.QLabel(self.widget)
        self.camLabel4.setStyleSheet("font-size:16px;")
        self.camLabel4.setObjectName("camLabel4")
        self.horizontalLayout_34.addWidget(self.camLabel4)
        self.cam04_pushButton = QtWidgets.QToolButton(self.widget)
        self.cam04_pushButton.setText("")
        self.cam04_pushButton.setIcon(icon9)
        self.cam04_pushButton.setObjectName("cam04_pushButton")
        self.horizontalLayout_34.addWidget(self.cam04_pushButton)
        self.displaycross_4 = QtWidgets.QToolButton(self.widget)
        self.displaycross_4.setText("")
        self.displaycross_4.setIcon(icon10)
        self.displaycross_4.setObjectName("displaycross_4")
        self.horizontalLayout_34.addWidget(self.displaycross_4)
        self.verticalLayout_22.addLayout(self.horizontalLayout_34)
        spacerItem18 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem18)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.camLabel5 = QtWidgets.QLabel(self.widget)
        self.camLabel5.setStyleSheet("font-size:16px;")
        self.camLabel5.setObjectName("camLabel5")
        self.horizontalLayout_32.addWidget(self.camLabel5)
        self.cam05_pushButton = QtWidgets.QToolButton(self.widget)
        self.cam05_pushButton.setText("")
        self.cam05_pushButton.setIcon(icon9)
        self.cam05_pushButton.setObjectName("cam05_pushButton")
        self.horizontalLayout_32.addWidget(self.cam05_pushButton)
        self.displaycross_5 = QtWidgets.QToolButton(self.widget)
        self.displaycross_5.setText("")
        self.displaycross_5.setIcon(icon10)
        self.displaycross_5.setObjectName("displaycross_5")
        self.horizontalLayout_32.addWidget(self.displaycross_5)
        self.verticalLayout_22.addLayout(self.horizontalLayout_32)
        spacerItem19 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem19)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.camLabel6 = QtWidgets.QLabel(self.widget)
        self.camLabel6.setStyleSheet("font-size:16px;")
        self.camLabel6.setObjectName("camLabel6")
        self.horizontalLayout_33.addWidget(self.camLabel6)
        self.cam06_pushButton = QtWidgets.QToolButton(self.widget)
        self.cam06_pushButton.setText("")
        self.cam06_pushButton.setIcon(icon9)
        self.cam06_pushButton.setObjectName("cam06_pushButton")
        self.horizontalLayout_33.addWidget(self.cam06_pushButton)
        self.displaycross_6 = QtWidgets.QToolButton(self.widget)
        self.displaycross_6.setText("")
        self.displaycross_6.setIcon(icon10)
        self.displaycross_6.setObjectName("displaycross_6")
        self.horizontalLayout_33.addWidget(self.displaycross_6)
        self.verticalLayout_22.addLayout(self.horizontalLayout_33)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem20)
        self.horizontalLayout_36.addWidget(self.widget)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem21)
        self.menuStackedWidget.addWidget(self.camera_page)
        self.alarm_page = QtWidgets.QWidget()
        self.alarm_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"}\n"
"QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
" gridline-color: black;\n"
"    font-size: 14px;\n"
"}\n"
"QHeaderView::section {\n"
"background: #2A2F3C ;\n"
"color:white;\n"
"    \n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 12px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.alarm_page.setObjectName("alarm_page")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.alarm_page)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem22 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_12.addItem(spacerItem22)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem23)
        self.alarmHistory_label = QtWidgets.QLabel(self.alarm_page)
        self.alarmHistory_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px")
        self.alarmHistory_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alarmHistory_label.setObjectName("alarmHistory_label")
        self.horizontalLayout_24.addWidget(self.alarmHistory_label)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem24)
        self.verticalLayout_12.addLayout(self.horizontalLayout_24)
        spacerItem25 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem25)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem26)
        self.alarmHistoryDetail_label = QtWidgets.QLabel(self.alarm_page)
        self.alarmHistoryDetail_label.setObjectName("alarmHistoryDetail_label")
        self.horizontalLayout_22.addWidget(self.alarmHistoryDetail_label)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem27)
        self.verticalLayout_12.addLayout(self.horizontalLayout_22)
        spacerItem28 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem28)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem29 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem29)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem30 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem30)
        self.anomalySearch_lineEdit = QtWidgets.QLineEdit(self.alarm_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.anomalySearch_lineEdit.sizePolicy().hasHeightForWidth())
        self.anomalySearch_lineEdit.setSizePolicy(sizePolicy)
        self.anomalySearch_lineEdit.setMinimumSize(QtCore.QSize(300, 31))
        self.anomalySearch_lineEdit.setStyleSheet("QLineEdit{\n"
"background-color:#1C1D25;\n"
"border:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}")
        self.anomalySearch_lineEdit.setObjectName("anomalySearch_lineEdit")
        self.horizontalLayout_29.addWidget(self.anomalySearch_lineEdit)
        self.anomalySearch_pushButton = QtWidgets.QPushButton(self.alarm_page)
        self.anomalySearch_pushButton.setObjectName("anomalySearch_pushButton")
        self.horizontalLayout_29.addWidget(self.anomalySearch_pushButton)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem31)
        self.verticalLayout_11.addLayout(self.horizontalLayout_29)
        self.alarm_tableWidget = QtWidgets.QTableWidget(self.alarm_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarm_tableWidget.sizePolicy().hasHeightForWidth())
        self.alarm_tableWidget.setSizePolicy(sizePolicy)
        self.alarm_tableWidget.setMinimumSize(QtCore.QSize(650, 0))
        self.alarm_tableWidget.setStyleSheet("QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"color:white;\n"
"    background-color:#1C1D25;\n"
"\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 15px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #2A2F3C\n"
"    border: 1px solid black;\n"
"}")
        self.alarm_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alarm_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.alarm_tableWidget.setObjectName("alarm_tableWidget")
        self.alarm_tableWidget.setColumnCount(5)
        self.alarm_tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.alarm_tableWidget.setHorizontalHeaderItem(4, item)
        self.alarm_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.alarm_tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.alarm_tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.alarm_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.alarm_tableWidget.verticalHeader().setVisible(False)
        self.alarm_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_11.addWidget(self.alarm_tableWidget)
        spacerItem32 = QtWidgets.QSpacerItem(1, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem32)
        self.horizontalLayout_28.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_28)
        self.menuStackedWidget.addWidget(self.alarm_page)
        self.storage_page = QtWidgets.QWidget()
        self.storage_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background: #201f1f;\n"
"border:#201f1f;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background: #2A2F3C ;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.storage_page.setObjectName("storage_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.storage_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem33 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem33)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem34)
        self.storage_label = QtWidgets.QLabel(self.storage_page)
        self.storage_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px")
        self.storage_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.storage_label.setObjectName("storage_label")
        self.horizontalLayout_9.addWidget(self.storage_label)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem35)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem36 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem36)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.show_label = QtWidgets.QLabel(self.storage_page)
        self.show_label.setObjectName("show_label")
        self.horizontalLayout_8.addWidget(self.show_label)
        spacerItem37 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem37)
        self.anomalyClip_checkBox = QtWidgets.QCheckBox(self.storage_page)
        self.anomalyClip_checkBox.setStyleSheet("\n"
"font-size:16px;\n"
"color:white;")
        self.anomalyClip_checkBox.setObjectName("anomalyClip_checkBox")
        self.horizontalLayout_8.addWidget(self.anomalyClip_checkBox)
        self.cameraFeed_checkBox = QtWidgets.QCheckBox(self.storage_page)
        self.cameraFeed_checkBox.setStyleSheet("\n"
"font-size:16px;\n"
"color:white;")
        self.cameraFeed_checkBox.setIconSize(QtCore.QSize(30, 30))
        self.cameraFeed_checkBox.setChecked(False)
        self.cameraFeed_checkBox.setAutoRepeat(False)
        self.cameraFeed_checkBox.setAutoExclusive(False)
        self.cameraFeed_checkBox.setTristate(False)
        self.cameraFeed_checkBox.setObjectName("cameraFeed_checkBox")
        self.horizontalLayout_8.addWidget(self.cameraFeed_checkBox)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem38)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem39)
        self.storage_tableWidget = QtWidgets.QTableWidget(self.storage_page)
        self.storage_tableWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.storage_tableWidget.setStyleSheet("QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"color:white;\n"
"    background-color:#1C1D25;\n"
"\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 12px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: black;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #2A2F3C\n"
"    border: 1px solid black;\n"
"}")
        self.storage_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.storage_tableWidget.setObjectName("storage_tableWidget")
        self.storage_tableWidget.setColumnCount(3)
        self.storage_tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(2, item)
        self.storage_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.storage_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.storage_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.storage_tableWidget.verticalHeader().setVisible(False)
        self.storage_tableWidget.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_7.addWidget(self.storage_tableWidget)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem40)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.menuStackedWidget.addWidget(self.storage_page)
        self.accountInfo_page = QtWidgets.QWidget()
        self.accountInfo_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"background-color:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.accountInfo_page.setObjectName("accountInfo_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.accountInfo_page)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem41 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem41)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem42)
        self.account_form = QtWidgets.QFormLayout()
        self.account_form.setObjectName("account_form")
        self.accountInfo_label = QtWidgets.QLabel(self.accountInfo_page)
        self.accountInfo_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px;")
        self.accountInfo_label.setObjectName("accountInfo_label")
        self.account_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.accountInfo_label)
        spacerItem43 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem43)
        self.fname_label = QtWidgets.QLabel(self.accountInfo_page)
        self.fname_label.setObjectName("fname_label")
        self.account_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fname_label)
        self.fname_field = QtWidgets.QLineEdit(self.accountInfo_page)
        self.fname_field.setText("")
        self.fname_field.setObjectName("fname_field")
        self.account_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fname_field)
        self.lname_label = QtWidgets.QLabel(self.accountInfo_page)
        self.lname_label.setObjectName("lname_label")
        self.account_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lname_label)
        self.lname_field = QtWidgets.QLineEdit(self.accountInfo_page)
        self.lname_field.setText("")
        self.lname_field.setObjectName("lname_field")
        self.account_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lname_field)
        self.username_label = QtWidgets.QLabel(self.accountInfo_page)
        self.username_label.setObjectName("username_label")
        self.account_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_field = QtWidgets.QLineEdit(self.accountInfo_page)
        self.username_field.setText("")
        self.username_field.setObjectName("username_field")
        self.account_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.username_field)
        self.password_label = QtWidgets.QLabel(self.accountInfo_page)
        self.password_label.setObjectName("password_label")
        self.account_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_field = QtWidgets.QLineEdit(self.accountInfo_page)
        self.password_field.setText("")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.account_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.password_field)
        self.contactInfo_label = QtWidgets.QLabel(self.accountInfo_page)
        self.contactInfo_label.setObjectName("contactInfo_label")
        self.account_form.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.contactInfo_label)
        self.contactInfo_field = QtWidgets.QLineEdit(self.accountInfo_page)
        self.contactInfo_field.setText("")
        self.contactInfo_field.setObjectName("contactInfo_field")
        self.account_form.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.contactInfo_field)
        self.address_label = QtWidgets.QLabel(self.accountInfo_page)
        self.address_label.setObjectName("address_label")
        self.account_form.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.address_field = QtWidgets.QTextEdit(self.accountInfo_page)
        self.address_field.setStyleSheet("border-radius: 0px;")
        self.address_field.setObjectName("address_field")
        self.account_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.address_field)
        spacerItem44 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem44)
        self.edit_pushButton = QtWidgets.QPushButton(self.accountInfo_page)
        self.edit_pushButton.setStyleSheet("FONT-SIZE: 18PX;")
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.account_form.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.edit_pushButton)
        self.horizontalLayout_10.addLayout(self.account_form)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem45)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.menuStackedWidget.addWidget(self.accountInfo_page)
        self.usersInfo_page = QtWidgets.QWidget()
        self.usersInfo_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"background-color:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.usersInfo_page.setObjectName("usersInfo_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.usersInfo_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem46 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem46)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem47)
        self.userInfo_label = QtWidgets.QLabel(self.usersInfo_page)
        self.userInfo_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px;FONT-WEIGHT:BOLD;")
        self.userInfo_label.setObjectName("userInfo_label")
        self.horizontalLayout_16.addWidget(self.userInfo_label)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem48)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        spacerItem49 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem49)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem50 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem50)
        self.viewLabel = QtWidgets.QLabel(self.usersInfo_page)
        self.viewLabel.setObjectName("viewLabel")
        self.horizontalLayout_14.addWidget(self.viewLabel)
        self.adminstable_radioButton = QtWidgets.QRadioButton(self.usersInfo_page)
        self.adminstable_radioButton.setStyleSheet("font-size:18px;\n"
"color: white;")
        self.adminstable_radioButton.setObjectName("adminstable_radioButton")
        self.horizontalLayout_14.addWidget(self.adminstable_radioButton)
        self.securitytable_radioButton = QtWidgets.QRadioButton(self.usersInfo_page)
        self.securitytable_radioButton.setStyleSheet("font-size:18px;\n"
"color: white;")
        self.securitytable_radioButton.setObjectName("securitytable_radioButton")
        self.horizontalLayout_14.addWidget(self.securitytable_radioButton)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem51)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.stackedWidget = QtWidgets.QStackedWidget(self.usersInfo_page)
        self.stackedWidget.setObjectName("stackedWidget")
        self.usertable_stackedWidget = QtWidgets.QWidget()
        self.usertable_stackedWidget.setObjectName("usertable_stackedWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.usertable_stackedWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem52 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem52)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem53 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem53)
        self.userAdd_pushButton = QtWidgets.QPushButton(self.usertable_stackedWidget)
        self.userAdd_pushButton.setObjectName("userAdd_pushButton")
        self.horizontalLayout_23.addWidget(self.userAdd_pushButton)
        self.userDelete_pushButton = QtWidgets.QPushButton(self.usertable_stackedWidget)
        self.userDelete_pushButton.setObjectName("userDelete_pushButton")
        self.horizontalLayout_23.addWidget(self.userDelete_pushButton)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem54)
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem55 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem55)
        self.user_tableWidget = QtWidgets.QTableWidget(self.usertable_stackedWidget)
        self.user_tableWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.user_tableWidget.setMouseTracking(False)
        self.user_tableWidget.setStyleSheet("QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"color:white;\n"
"    background-color:#1C1D25;\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 15px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color:#1C1D25;\n"
"    border: 1px solid black;\n"
"}")
        self.user_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user_tableWidget.setShowGrid(True)
        self.user_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.user_tableWidget.setObjectName("user_tableWidget")
        self.user_tableWidget.setColumnCount(7)
        self.user_tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_tableWidget.setHorizontalHeaderItem(6, item)
        self.user_tableWidget.horizontalHeader().setVisible(False)
        self.user_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.user_tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.user_tableWidget.horizontalHeader().setHighlightSections(True)
        self.user_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.user_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.user_tableWidget.verticalHeader().setVisible(False)
        self.user_tableWidget.verticalHeader().setHighlightSections(True)
        self.horizontalLayout_15.addWidget(self.user_tableWidget)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.stackedWidget.addWidget(self.usertable_stackedWidget)
        self.admintable_stackedWidget = QtWidgets.QWidget()
        self.admintable_stackedWidget.setObjectName("admintable_stackedWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.admintable_stackedWidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem56 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem56)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem57 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem57)
        self.adminAdd_pushButton = QtWidgets.QPushButton(self.admintable_stackedWidget)
        self.adminAdd_pushButton.setObjectName("adminAdd_pushButton")
        self.horizontalLayout_25.addWidget(self.adminAdd_pushButton)
        self.adminDelete_pushButton = QtWidgets.QPushButton(self.admintable_stackedWidget)
        self.adminDelete_pushButton.setObjectName("adminDelete_pushButton")
        self.horizontalLayout_25.addWidget(self.adminDelete_pushButton)
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem58)
        self.verticalLayout_10.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem59 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem59)
        self.admin_tableWidget = QtWidgets.QTableWidget(self.admintable_stackedWidget)
        self.admin_tableWidget.setStyleSheet("QTableWidget{ \n"
"  width: 100%;\n"
"   padding: 10px;\n"
"  text-align: left;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"color:white;\n"
"    background-color:#1C1D25;\n"
"    padding: 2px;\n"
"    border: 1px solid black;\n"
"    font-size: 15px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color:#1C1D25;\n"
"    border: 1px solid black;\n"
"}")
        self.admin_tableWidget.setObjectName("admin_tableWidget")
        self.admin_tableWidget.setColumnCount(7)
        self.admin_tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_tableWidget.setHorizontalHeaderItem(6, item)
        self.admin_tableWidget.horizontalHeader().setVisible(False)
        self.admin_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.admin_tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.admin_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.admin_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_26.addWidget(self.admin_tableWidget)
        self.verticalLayout_10.addLayout(self.horizontalLayout_26)
        self.stackedWidget.addWidget(self.admintable_stackedWidget)
        self.horizontalLayout_13.addWidget(self.stackedWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.menuStackedWidget.addWidget(self.usersInfo_page)
        self.addNewUser_page = QtWidgets.QWidget()
        self.addNewUser_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background: #2A2F3C ;\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color:#1C1D25;\n"
"border:#1C1D25;\n"
"\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font-size: 18px;\n"
"\n"
"}\n"
"QPushButton, QToolButton{\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"")
        self.addNewUser_page.setObjectName("addNewUser_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.addNewUser_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem60 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem60)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem61)
        self.addUser_form = QtWidgets.QFormLayout()
        self.addUser_form.setObjectName("addUser_form")
        self.addUser_label = QtWidgets.QLabel(self.addNewUser_page)
        self.addUser_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px;")
        self.addUser_label.setObjectName("addUser_label")
        self.addUser_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.addUser_label)
        spacerItem62 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.addUser_form.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem62)
        self.afname_label = QtWidgets.QLabel(self.addNewUser_page)
        self.afname_label.setObjectName("afname_label")
        self.addUser_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.afname_label)
        self.alname_label = QtWidgets.QLabel(self.addNewUser_page)
        self.alname_label.setObjectName("alname_label")
        self.addUser_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alname_label)
        self.aPassword_label = QtWidgets.QLabel(self.addNewUser_page)
        self.aPassword_label.setObjectName("aPassword_label")
        self.addUser_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.aPassword_label)
        self.aContactNo_label = QtWidgets.QLabel(self.addNewUser_page)
        self.aContactNo_label.setObjectName("aContactNo_label")
        self.addUser_form.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.aContactNo_label)
        self.aAddress_label = QtWidgets.QLabel(self.addNewUser_page)
        self.aAddress_label.setObjectName("aAddress_label")
        self.addUser_form.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.aAddress_label)
        self.addNewUser_pushButton = QtWidgets.QPushButton(self.addNewUser_page)
        self.addNewUser_pushButton.setStyleSheet("FONT-SIZE: 18PX;")
        self.addNewUser_pushButton.setObjectName("addNewUser_pushButton")
        self.addUser_form.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.addNewUser_pushButton)
        self.ausername_label = QtWidgets.QLabel(self.addNewUser_page)
        self.ausername_label.setObjectName("ausername_label")
        self.addUser_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ausername_label)
        self.afname_field = QtWidgets.QLineEdit(self.addNewUser_page)
        self.afname_field.setObjectName("afname_field")
        self.addUser_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.afname_field)
        self.alname_field = QtWidgets.QLineEdit(self.addNewUser_page)
        self.alname_field.setObjectName("alname_field")
        self.addUser_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alname_field)
        self.ausername_field = QtWidgets.QLineEdit(self.addNewUser_page)
        self.ausername_field.setObjectName("ausername_field")
        self.addUser_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ausername_field)
        self.aPassword_field = QtWidgets.QLineEdit(self.addNewUser_page)
        self.aPassword_field.setObjectName("aPassword_field")
        self.addUser_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.aPassword_field)
        self.aContactNo_field = QtWidgets.QLineEdit(self.addNewUser_page)
        self.aContactNo_field.setObjectName("aContactNo_field")
        self.addUser_form.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.aContactNo_field)
        self.aAddress_field = QtWidgets.QTextEdit(self.addNewUser_page)
        self.aAddress_field.setStyleSheet("border-radius:0px;")
        self.aAddress_field.setObjectName("aAddress_field")
        self.addUser_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.aAddress_field)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.aAdmin_radioButton = QtWidgets.QRadioButton(self.addNewUser_page)
        self.aAdmin_radioButton.setStyleSheet("color:white;\n"
"font-size: 16px;")
        self.aAdmin_radioButton.setObjectName("aAdmin_radioButton")
        self.horizontalLayout_20.addWidget(self.aAdmin_radioButton)
        self.aSecurity_radioButton = QtWidgets.QRadioButton(self.addNewUser_page)
        self.aSecurity_radioButton.setStyleSheet("color:white;\n"
"font-size: 16px;")
        self.aSecurity_radioButton.setObjectName("aSecurity_radioButton")
        self.horizontalLayout_20.addWidget(self.aSecurity_radioButton)
        self.addUser_form.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_20)
        self.accountType_label = QtWidgets.QLabel(self.addNewUser_page)
        self.accountType_label.setObjectName("accountType_label")
        self.addUser_form.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.accountType_label)
        spacerItem63 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.addUser_form.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem63)
        self.horizontalLayout_11.addLayout(self.addUser_form)
        spacerItem64 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem64)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.menuStackedWidget.addWidget(self.addNewUser_page)
        self.dialog_page = QtWidgets.QWidget()
        self.dialog_page.setObjectName("dialog_page")
        self.menuStackedWidget.addWidget(self.dialog_page)
        self.language_page = QtWidgets.QWidget()
        self.language_page.setObjectName("language_page")
        self.english_radioButton = QtWidgets.QRadioButton(self.language_page)
        self.english_radioButton.setGeometry(QtCore.QRect(230, 170, 141, 31))
        self.english_radioButton.setStyleSheet("font-size:21px;\n"
"COLOR:WHITE;")
        self.english_radioButton.setObjectName("english_radioButton")
        self.chooseLanguage_label = QtWidgets.QLabel(self.language_page)
        self.chooseLanguage_label.setGeometry(QtCore.QRect(100, 100, 191, 31))
        self.chooseLanguage_label.setObjectName("chooseLanguage_label")
        self.urdu_radioButton = QtWidgets.QRadioButton(self.language_page)
        self.urdu_radioButton.setGeometry(QtCore.QRect(230, 220, 111, 31))
        self.urdu_radioButton.setStyleSheet("font-size:21px;\n"
"COLOR:WHITE;")
        self.urdu_radioButton.setObjectName("urdu_radioButton")
        self.menuStackedWidget.addWidget(self.language_page)
        self.accessdenied_page = QtWidgets.QWidget()
        self.accessdenied_page.setObjectName("accessdenied_page")
        self.accessdenied_label = QtWidgets.QLabel(self.accessdenied_page)
        self.accessdenied_label.setGeometry(QtCore.QRect(330, 300, 371, 91))
        self.accessdenied_label.setObjectName("accessdenied_label")
        self.menuStackedWidget.addWidget(self.accessdenied_page)
        self.edit_page = QtWidgets.QWidget()
        self.edit_page.setObjectName("edit_page")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.edit_page)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem65 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_14.addItem(spacerItem65)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem66 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem66)
        self.account_form_2 = QtWidgets.QFormLayout()
        self.account_form_2.setObjectName("account_form_2")
        self.editInfo_label = QtWidgets.QLabel(self.edit_page)
        self.editInfo_label.setStyleSheet("FONT-WEIGHT:BOLD;\n"
"font-size:24px;")
        self.editInfo_label.setObjectName("editInfo_label")
        self.account_form_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.editInfo_label)
        spacerItem67 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form_2.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem67)
        self.fname_label_2 = QtWidgets.QLabel(self.edit_page)
        self.fname_label_2.setObjectName("fname_label_2")
        self.account_form_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fname_label_2)
        self.fname_field_2 = QtWidgets.QLineEdit(self.edit_page)
        self.fname_field_2.setText("")
        self.fname_field_2.setObjectName("fname_field_2")
        self.account_form_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fname_field_2)
        self.lname_label_2 = QtWidgets.QLabel(self.edit_page)
        self.lname_label_2.setObjectName("lname_label_2")
        self.account_form_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lname_label_2)
        self.lname_field_2 = QtWidgets.QLineEdit(self.edit_page)
        self.lname_field_2.setText("")
        self.lname_field_2.setObjectName("lname_field_2")
        self.account_form_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lname_field_2)
        self.username_label_2 = QtWidgets.QLabel(self.edit_page)
        self.username_label_2.setObjectName("username_label_2")
        self.account_form_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.username_label_2)
        self.username_field_2 = QtWidgets.QLineEdit(self.edit_page)
        self.username_field_2.setText("")
        self.username_field_2.setObjectName("username_field_2")
        self.account_form_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.username_field_2)
        self.password_label_2 = QtWidgets.QLabel(self.edit_page)
        self.password_label_2.setObjectName("password_label_2")
        self.account_form_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.password_label_2)
        self.password_field_2 = QtWidgets.QLineEdit(self.edit_page)
        self.password_field_2.setText("")
        self.password_field_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field_2.setObjectName("password_field_2")
        self.account_form_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.password_field_2)
        self.contactInfo_label_2 = QtWidgets.QLabel(self.edit_page)
        self.contactInfo_label_2.setObjectName("contactInfo_label_2")
        self.account_form_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.contactInfo_label_2)
        self.contactInfo_field_2 = QtWidgets.QLineEdit(self.edit_page)
        self.contactInfo_field_2.setText("")
        self.contactInfo_field_2.setObjectName("contactInfo_field_2")
        self.account_form_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.contactInfo_field_2)
        self.address_label_2 = QtWidgets.QLabel(self.edit_page)
        self.address_label_2.setObjectName("address_label_2")
        self.account_form_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.address_label_2)
        self.address_field_2 = QtWidgets.QTextEdit(self.edit_page)
        self.address_field_2.setStyleSheet("border-radius: 0px;")
        self.address_field_2.setObjectName("address_field_2")
        self.account_form_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.address_field_2)
        spacerItem68 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.account_form_2.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem68)
        self.edit_pushButton_2 = QtWidgets.QPushButton(self.edit_page)
        self.edit_pushButton_2.setStyleSheet("FONT-SIZE: 18PX;")
        self.edit_pushButton_2.setObjectName("edit_pushButton_2")
        self.account_form_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.edit_pushButton_2)
        self.horizontalLayout_30.addLayout(self.account_form_2)
        spacerItem69 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem69)
        self.verticalLayout_14.addLayout(self.horizontalLayout_30)
        self.menuStackedWidget.addWidget(self.edit_page)
        self.verticalLayout_2.addWidget(self.menuStackedWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.mainStackedWidget.addWidget(self.main_page)
        self.loggedOut_page = QtWidgets.QWidget()
        self.loggedOut_page.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 30px;\n"
"background-color:#1C1D25;\n"
"}\n"
"QFrame{\n"
"\n"
"background: #2A2F3C ;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"background:white;\n"
"border-radius:60px;\n"
"}\n"
"QLineEdit{\n"
"background: transparent;\n"
"border:none;\n"
"color:BLACK;\n"
"border-bottom:1px solid black;\n"
"font-size:20px;\n"
"}\n"
"QPushButton{\n"
"font-size:18px;\n"
"font-weight:bold;\n"
"color:white ;\n"
"background-color:#1C1D25;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"#logoLabel{\n"
"background:transparent;\n"
"}")
        self.loggedOut_page.setObjectName("loggedOut_page")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.loggedOut_page)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem70 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem70)
        self.loggedOut_widget = QtWidgets.QWidget(self.loggedOut_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loggedOut_widget.sizePolicy().hasHeightForWidth())
        self.loggedOut_widget.setSizePolicy(sizePolicy)
        self.loggedOut_widget.setMinimumSize(QtCore.QSize(560, 600))
        self.loggedOut_widget.setObjectName("loggedOut_widget")
        self.logo3_label = QtWidgets.QLabel(self.loggedOut_widget)
        self.logo3_label.setGeometry(QtCore.QRect(200, 80, 150, 100))
        self.logo3_label.setStyleSheet("background: transparent;")
        self.logo3_label.setText("")
        self.logo3_label.setPixmap(QtGui.QPixmap(":/logo/surveilialogo.PNG"))
        self.logo3_label.setScaledContents(True)
        self.logo3_label.setObjectName("logo3_label")
        self.loggedOut_frame = QtWidgets.QFrame(self.loggedOut_widget)
        self.loggedOut_frame.setGeometry(QtCore.QRect(70, 130, 411, 571))
        self.loggedOut_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loggedOut_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loggedOut_frame.setObjectName("loggedOut_frame")
        self.title3_label = QtWidgets.QLabel(self.loggedOut_frame)
        self.title3_label.setGeometry(QtCore.QRect(110, 110, 231, 61))
        self.title3_label.setStyleSheet("font-size:35px;")
        self.title3_label.setObjectName("title3_label")
        self.cancel_pushButton = QtWidgets.QPushButton(self.loggedOut_frame)
        self.cancel_pushButton.setGeometry(QtCore.QRect(100, 420, 211, 40))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.loginAgain_pushButton = QtWidgets.QPushButton(self.loggedOut_frame)
        self.loginAgain_pushButton.setGeometry(QtCore.QRect(100, 350, 211, 40))
        self.loginAgain_pushButton.setObjectName("loginAgain_pushButton")
        self.loggedOut_label = QtWidgets.QLabel(self.loggedOut_frame)
        self.loggedOut_label.setGeometry(QtCore.QRect(80, 230, 281, 51))
        self.loggedOut_label.setStyleSheet("font-size:18px;")
        self.loggedOut_label.setObjectName("loggedOut_label")
        self.logo3_toolButton = QtWidgets.QToolButton(self.loggedOut_widget)
        self.logo3_toolButton.setGeometry(QtCore.QRect(210, 70, 120, 120))
        self.logo3_toolButton.setText("")
        self.logo3_toolButton.setObjectName("logo3_toolButton")
        self.loggedOut_frame.raise_()
        self.logo3_toolButton.raise_()
        self.logo3_label.raise_()
        self.horizontalLayout_27.addWidget(self.loggedOut_widget)
        spacerItem71 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem71)
        self.mainStackedWidget.addWidget(self.loggedOut_page)
        self.verticalLayout_3.addWidget(self.mainStackedWidget)
        surveiliaFrontEnd.setCentralWidget(self.centralwidget)

        self.retranslateUi(surveiliaFrontEnd)
        self.mainStackedWidget.setCurrentIndex(1)
        self.menuStackedWidget.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(surveiliaFrontEnd)

    def retranslateUi(self, surveiliaFrontEnd):
        _translate = QtCore.QCoreApplication.translate
        surveiliaFrontEnd.setWindowTitle(_translate("surveiliaFrontEnd", "MainWindow"))
        self.title1_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.username1_field.setPlaceholderText(_translate("surveiliaFrontEnd", "Username"))
        self.password1_field.setPlaceholderText(_translate("surveiliaFrontEnd", "Password"))
        self.login_pushButton.setText(_translate("surveiliaFrontEnd", "LOGIN"))
        self.security_radioButton.setText(_translate("surveiliaFrontEnd", "Security Guard"))
        self.admin_radioButton.setText(_translate("surveiliaFrontEnd", "Admin"))
        self.loginas1_label.setText(_translate("surveiliaFrontEnd", "Login as:"))
        self.camera_toolButton.setText(_translate("surveiliaFrontEnd", "Camera"))
        self.logout_toolButton.setText(_translate("surveiliaFrontEnd", "Logout"))
        self.users_toolButton.setText(_translate("surveiliaFrontEnd", "Users"))
        self.language_toolButton.setText(_translate("surveiliaFrontEnd", "Language"))
        self.logo_toolButton.setText(_translate("surveiliaFrontEnd", "Logout"))
        self.alarm_toolButton.setText(_translate("surveiliaFrontEnd", "Alarm Log"))
        self.account_toolButton.setText(_translate("surveiliaFrontEnd", "Account"))
        self.title_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.welcome_label.setText(_translate("surveiliaFrontEnd", "Welcome to SURVEILIA"))
        self.getStarted_pushButton.setText(_translate("surveiliaFrontEnd", "GET STARTED"))
        self.addNew_pushButton.setText(_translate("surveiliaFrontEnd", "Add Camera"))
        self.cameras_label.setText(_translate("surveiliaFrontEnd", "CAMERAS LIST"))
        self.camLabel1.setText(_translate("surveiliaFrontEnd", "CAMERA_01"))
        self.camLabel2.setText(_translate("surveiliaFrontEnd", "CAMERA_02"))
        self.camLabel3.setText(_translate("surveiliaFrontEnd", "CAMERA_03"))
        self.camLabel4.setText(_translate("surveiliaFrontEnd", "CAMERA_04"))
        self.camLabel5.setText(_translate("surveiliaFrontEnd", "CAMERA_05"))
        self.camLabel6.setText(_translate("surveiliaFrontEnd", "CAMERA_06"))
        self.alarmHistory_label.setText(_translate("surveiliaFrontEnd", "ALARM HISTORY"))
        self.alarmHistoryDetail_label.setText(_translate("surveiliaFrontEnd", "The history of alarms is displayed here."))
        self.anomalySearch_lineEdit.setText(_translate("surveiliaFrontEnd", "Enter data to search"))
        self.anomalySearch_pushButton.setText(_translate("surveiliaFrontEnd", "Search"))
        self.alarm_tableWidget.setSortingEnabled(True)
        item = self.alarm_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "1"))
        item = self.alarm_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "2"))
        item = self.alarm_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "3"))
        item = self.alarm_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "4"))
        item = self.alarm_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "5"))
        item = self.alarm_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "Camera ID"))
        item = self.alarm_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Event"))
        item = self.alarm_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Date"))
        item = self.alarm_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Time"))
        item = self.alarm_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "Video URL"))
        self.storage_label.setText(_translate("surveiliaFrontEnd", "STORAGE"))
        self.show_label.setText(_translate("surveiliaFrontEnd", "           Show:"))
        self.anomalyClip_checkBox.setText(_translate("surveiliaFrontEnd", "Anomaly Clip"))
        self.cameraFeed_checkBox.setText(_translate("surveiliaFrontEnd", "Camera Feed"))
        item = self.storage_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "1"))
        item = self.storage_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "2"))
        item = self.storage_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "3"))
        item = self.storage_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "4"))
        item = self.storage_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "5"))
        item = self.storage_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("surveiliaFrontEnd", "6"))
        item = self.storage_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "Filename"))
        item = self.storage_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "Date"))
        item = self.storage_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Size"))
        self.accountInfo_label.setText(_translate("surveiliaFrontEnd", "ACCOUNT INFORMATION"))
        self.fname_label.setText(_translate("surveiliaFrontEnd", "First Name:"))
        self.lname_label.setText(_translate("surveiliaFrontEnd", "Last Name:"))
        self.username_label.setText(_translate("surveiliaFrontEnd", "Username:"))
        self.password_label.setText(_translate("surveiliaFrontEnd", "Password:"))
        self.contactInfo_label.setText(_translate("surveiliaFrontEnd", "Contact Info:"))
        self.address_label.setText(_translate("surveiliaFrontEnd", "Address:"))
        self.address_field.setHtml(_translate("surveiliaFrontEnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.edit_pushButton.setText(_translate("surveiliaFrontEnd", "EDIT"))
        self.userInfo_label.setText(_translate("surveiliaFrontEnd", "  USERS INFORMATION"))
        self.viewLabel.setText(_translate("surveiliaFrontEnd", "View:"))
        self.adminstable_radioButton.setText(_translate("surveiliaFrontEnd", "Admins"))
        self.securitytable_radioButton.setText(_translate("surveiliaFrontEnd", "Security Guards"))
        self.userAdd_pushButton.setText(_translate("surveiliaFrontEnd", "ADD"))
        self.userDelete_pushButton.setText(_translate("surveiliaFrontEnd", "DELETE"))
        self.user_tableWidget.setSortingEnabled(True)
        item = self.user_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "1"))
        item = self.user_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "2"))
        item = self.user_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "User ID"))
        item = self.user_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "First Name"))
        item = self.user_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Last Name"))
        item = self.user_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Username"))
        item = self.user_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "Password"))
        item = self.user_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("surveiliaFrontEnd", "Contact No."))
        item = self.user_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("surveiliaFrontEnd", "Address"))
        self.adminAdd_pushButton.setText(_translate("surveiliaFrontEnd", "ADD"))
        self.adminDelete_pushButton.setText(_translate("surveiliaFrontEnd", "DELETE"))
        item = self.admin_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "1"))
        item = self.admin_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "2"))
        item = self.admin_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("surveiliaFrontEnd", "Admin ID"))
        item = self.admin_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("surveiliaFrontEnd", "First Name"))
        item = self.admin_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("surveiliaFrontEnd", "Last Name"))
        item = self.admin_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("surveiliaFrontEnd", "Username"))
        item = self.admin_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("surveiliaFrontEnd", "Password"))
        item = self.admin_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("surveiliaFrontEnd", "Contact No."))
        item = self.admin_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("surveiliaFrontEnd", "Address"))
        self.addUser_label.setText(_translate("surveiliaFrontEnd", "ADD NEW USER"))
        self.afname_label.setText(_translate("surveiliaFrontEnd", "First Name:"))
        self.alname_label.setText(_translate("surveiliaFrontEnd", "Last Name:"))
        self.aPassword_label.setText(_translate("surveiliaFrontEnd", "Password:"))
        self.aContactNo_label.setText(_translate("surveiliaFrontEnd", "Contact No."))
        self.aAddress_label.setText(_translate("surveiliaFrontEnd", "Address:"))
        self.addNewUser_pushButton.setText(_translate("surveiliaFrontEnd", "ADD USER"))
        self.ausername_label.setText(_translate("surveiliaFrontEnd", "Username:"))
        self.aAdmin_radioButton.setText(_translate("surveiliaFrontEnd", "Admin"))
        self.aSecurity_radioButton.setText(_translate("surveiliaFrontEnd", "Security Guard"))
        self.accountType_label.setText(_translate("surveiliaFrontEnd", "Account Type:"))
        self.english_radioButton.setText(_translate("surveiliaFrontEnd", "English"))
        self.chooseLanguage_label.setText(_translate("surveiliaFrontEnd", "Choose Language:"))
        self.urdu_radioButton.setText(_translate("surveiliaFrontEnd", "Urdu"))
        self.accessdenied_label.setText(_translate("surveiliaFrontEnd", "ACCESS DENIED"))
        self.editInfo_label.setText(_translate("surveiliaFrontEnd", "EDIT INFORMATION"))
        self.fname_label_2.setText(_translate("surveiliaFrontEnd", "First Name:"))
        self.lname_label_2.setText(_translate("surveiliaFrontEnd", "Last Name:"))
        self.username_label_2.setText(_translate("surveiliaFrontEnd", "Username:"))
        self.password_label_2.setText(_translate("surveiliaFrontEnd", "Password:"))
        self.contactInfo_label_2.setText(_translate("surveiliaFrontEnd", "Contact Info:"))
        self.address_label_2.setText(_translate("surveiliaFrontEnd", "Address:"))
        self.address_field_2.setHtml(_translate("surveiliaFrontEnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.edit_pushButton_2.setText(_translate("surveiliaFrontEnd", "EDIT"))
        self.title3_label.setText(_translate("surveiliaFrontEnd", "SURVEILIA"))
        self.cancel_pushButton.setText(_translate("surveiliaFrontEnd", "CANCEL"))
        self.loginAgain_pushButton.setText(_translate("surveiliaFrontEnd", "LOGIN AGAIN"))
        self.loggedOut_label.setText(_translate("surveiliaFrontEnd", "You have been logged out!"))


import resource01_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    surveiliaFrontEnd = QtWidgets.QMainWindow()
    ui = Ui_surveiliaFrontEnd()
    ui.setupUi(surveiliaFrontEnd)
    surveiliaFrontEnd.show()
    sys.exit(app.exec_())
