# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playAnomalyVideo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_playAnomalyVideo(object):
    def setupUi(self, playAnomalyVideo):
        playAnomalyVideo.setObjectName("playAnomalyVideo")
        playAnomalyVideo.resize(594, 543)
        playAnomalyVideo.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(playAnomalyVideo)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.videoPathfield = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.videoPathfield.sizePolicy().hasHeightForWidth())
        self.videoPathfield.setSizePolicy(sizePolicy)
        self.videoPathfield.setMinimumSize(QtCore.QSize(320, 31))
        self.videoPathfield.setStyleSheet("QLineEdit{\n"
"background-color:#1C1D25;\n"
"border:#1C1D25;\n"
"color:white;\n"
"font-size:18px;\n"
"}")
        self.videoPathfield.setObjectName("videoPathfield")
        self.horizontalLayout_6.addWidget(self.videoPathfield)
        self.videoPathEnter_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.videoPathEnter_pushButton.setObjectName("videoPathEnter_pushButton")
        self.horizontalLayout_6.addWidget(self.videoPathEnter_pushButton)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem)
        self.anomalyVideoDisplay = QVideoWidget(self.centralwidget)
        self.anomalyVideoDisplay.setMinimumSize(QtCore.QSize(350, 400))
        self.anomalyVideoDisplay.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.anomalyVideoDisplay.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.anomalyVideoDisplay.setObjectName("anomalyVideoDisplay")
        self.verticalLayout_13.addWidget(self.anomalyVideoDisplay)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.play_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.play_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menubar/play-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pushButton.setIcon(icon)
        self.play_pushButton.setObjectName("play_pushButton")
        self.horizontalLayout_4.addWidget(self.play_pushButton)
        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pause_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/media-pause-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_pushButton.setIcon(icon1)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.horizontalLayout_4.addWidget(self.pause_pushButton)
        self.videoSlider = QtWidgets.QSlider(self.centralwidget)
        self.videoSlider.setOrientation(QtCore.Qt.Horizontal)
        self.videoSlider.setObjectName("videoSlider")
        self.horizontalLayout_4.addWidget(self.videoSlider)
        self.videoDurationChanged = QtWidgets.QLabel(self.centralwidget)
        self.videoDurationChanged.setObjectName("videoDurationChanged")
        self.horizontalLayout_4.addWidget(self.videoDurationChanged)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_13)
        playAnomalyVideo.setCentralWidget(self.centralwidget)

        self.retranslateUi(playAnomalyVideo)
        QtCore.QMetaObject.connectSlotsByName(playAnomalyVideo)

    def retranslateUi(self, playAnomalyVideo):
        _translate = QtCore.QCoreApplication.translate
        playAnomalyVideo.setWindowTitle(_translate("playAnomalyVideo", "MainWindow"))
        self.videoPathfield.setText(_translate("playAnomalyVideo", "Enter video path here"))
        self.videoPathEnter_pushButton.setText(_translate("playAnomalyVideo", "Enter"))
        self.videoDurationChanged.setText(_translate("playAnomalyVideo", "Duration"))


from PyQt5.QtMultimediaWidgets import QVideoWidget
import resource01_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    playAnomalyVideo = QtWidgets.QMainWindow()
    ui = Ui_playAnomalyVideo()
    ui.setupUi(playAnomalyVideo)
    playAnomalyVideo.show()
    sys.exit(app.exec_())
