# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camOptions.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_camOptions(object):
    def setupUi(self, camOptions):
        camOptions.setObjectName("camOptions")
        camOptions.resize(398, 378)
        camOptions.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(camOptions)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.addIPCam_label = QtWidgets.QLabel(self.frame)
        self.addIPCam_label.setObjectName("addIPCam_label")
        self.verticalLayout_9.addWidget(self.addIPCam_label)
        self.addIPCam_field = QtWidgets.QLineEdit(self.frame)
        self.addIPCam_field.setObjectName("addIPCam_field")
        self.verticalLayout_9.addWidget(self.addIPCam_field)
        self.addIPCam_pushButton = QtWidgets.QPushButton(self.frame)
        self.addIPCam_pushButton.setObjectName("addIPCam_pushButton")
        self.verticalLayout_9.addWidget(self.addIPCam_pushButton)
        self.openDir_label = QtWidgets.QLabel(self.frame)
        self.openDir_label.setObjectName("openDir_label")
        self.verticalLayout_9.addWidget(self.openDir_label)
        self.openDir_pushButton = QtWidgets.QPushButton(self.frame)
        self.openDir_pushButton.setObjectName("openDir_pushButton")
        self.verticalLayout_9.addWidget(self.openDir_pushButton)
        self.openWebcam_label = QtWidgets.QLabel(self.frame)
        self.openWebcam_label.setObjectName("openWebcam_label")
        self.verticalLayout_9.addWidget(self.openWebcam_label)
        self.openWebcam_pushButton = QtWidgets.QPushButton(self.frame)
        self.openWebcam_pushButton.setObjectName("openWebcam_pushButton")
        self.verticalLayout_9.addWidget(self.openWebcam_pushButton)
        self.cancel_PushButton = QtWidgets.QPushButton(self.frame)
        self.cancel_PushButton.setObjectName("cancel_PushButton")
        self.verticalLayout_9.addWidget(self.cancel_PushButton)
        self.horizontalLayout.addWidget(self.frame)
        camOptions.setCentralWidget(self.centralwidget)

        self.retranslateUi(camOptions)
        QtCore.QMetaObject.connectSlotsByName(camOptions)

    def retranslateUi(self, camOptions):
        _translate = QtCore.QCoreApplication.translate
        camOptions.setWindowTitle(_translate("camOptions", "MainWindow"))
        self.addIPCam_label.setText(_translate("camOptions", "Add camera using IP Address"))
        self.addIPCam_field.setText(_translate("camOptions", "ENTER IP ADDRESS HERE"))
        self.addIPCam_pushButton.setText(_translate("camOptions", "ADD"))
        self.openDir_label.setText(_translate("camOptions", "Add video by file from Directory"))
        self.openDir_pushButton.setText(_translate("camOptions", "OPEN"))
        self.openWebcam_label.setText(_translate("camOptions", "Add using Webcam"))
        self.openWebcam_pushButton.setText(_translate("camOptions", "OPEN WEBCAM"))
        self.cancel_PushButton.setText(_translate("camOptions", "CANCEL"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    camOptions = QtWidgets.QMainWindow()
    ui = Ui_camOptions()
    ui.setupUi(camOptions)
    camOptions.show()
    sys.exit(app.exec_())
