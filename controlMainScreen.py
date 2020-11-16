import datetime
import urllib.request
import xlrd
import time
import csv
import glob
import sys
import cv2
import numpy as np
import argparse
import pandas as pd
import os
import torchvision
import torch.nn.parallel
import torch.optim
import sqlite3
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5.QtCore import QUrl, pyqtSlot, QDate, QDateTime, QTime
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from surveiliaFrontEnd import Ui_surveiliaFrontEnd
from playAnomalyVideo import Ui_playAnomalyVideo
from camOptions import Ui_camOptions
from PIL import Image
from tsm_model.ops.models import TSN
from tsm_model.ops.transforms import *
from torch.nn import functional as F
from threading import Thread

#######################################database task#########################################
count = 1
connection = sqlite3.connect("Surveilia_database.db")
curs = connection.cursor()
curs.execute(
    "CREATE TABLE IF NOT EXISTS surveilia_users(user_id INTEGER PRIMARY KEY UNIQUE NOT NULL, user_fname STRING NOT NULL, user_lname STRING NOT NULL,user_username STRING NOT NULL,user_password STRING NOT NULL, user_contactno NUMERIC,user_address STRING)"
)
curs.execute(
    "CREATE TABLE IF NOT EXISTS surveilia_admin(admin_id INTEGER PRIMARY KEY UNIQUE NOT NULL, admin_fname STRING NOT NULL, admin_lname STRING NOT NULL,admin_username STRING NOT NULL,admin_password STRING NOT NULL, admin_contactno NUMERIC,admin_address STRING)"
)

class camOptionsDialog(qtw.QMainWindow, Ui_camOptions):
    def __init__(self, parent = None):
        super(camOptionsDialog, self).__init__(parent)
        self.setupUi(self)
    
class playAnomalyDialog(qtw.QMainWindow, Ui_playAnomalyVideo):
    def __init__(self, parent = None):
        super(playAnomalyDialog, self).__init__(parent)
        self.setupUi(self)

class ControlMainWindow(qtw.QMainWindow, Ui_surveiliaFrontEnd):
    def __init__(self, parent = None):
        super(ControlMainWindow, self).__init__(parent)
        self.setupUi(self)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.setupUi(self)
        self.logic = 0
        self.flag = 0
        self.camSignal = 0
        self.mainStackedWidget.setCurrentIndex(0)
        self.menuStackedWidget.setCurrentIndex(0)

        self.user_tableWidget.horizontalHeader().setVisible(True)
        self.user_tableWidget.verticalHeader().setVisible(True)
        self.admin_tableWidget.horizontalHeader().setVisible(True)
        self.admin_tableWidget.verticalHeader().setVisible(True)

        self.loginAgain_pushButton.clicked.connect(
            lambda: self.mainStackedWidget.setCurrentIndex(0)
        )
        self.logo_toolButton.clicked.connect(
            lambda: self.menuStackedWidget.setCurrentIndex(0)
        )
        self.getStarted_pushButton.clicked.connect(
            lambda: self.menuStackedWidget.setCurrentIndex(1)
        )
        self.camera_toolButton.clicked.connect(
            lambda: self.menuStackedWidget.setCurrentIndex(1)
        )
        self.language_toolButton.clicked.connect(
            lambda: self.menuStackedWidget.setCurrentIndex(8)
        )

        self.cameras_label.hide()

        self.camLabel1.hide()
        self.camLabel2.hide()
        self.camLabel3.hide()
        self.camLabel4.hide()
        self.camLabel5.hide()
        self.camLabel6.hide()

        self.cam01_pushButton.hide()
        self.cam02_pushButton.hide()
        self.cam03_pushButton.hide()
        self.cam04_pushButton.hide()
        self.cam05_pushButton.hide()
        self.cam06_pushButton.hide()

        self.display_1.hide()
        self.display_2.hide()
        self.display_3.hide()
        self.display_4.hide()
        self.display_5.hide()
        self.display_6.hide()

        self.displaycross_1.hide()
        self.displaycross_2.hide()
        self.displaycross_3.hide()
        self.displaycross_4.hide()
        self.displaycross_5.hide()
        self.displaycross_6.hide()
        """
        ##########Code to display the anomaly video.. i have hidden it for now///////////////
        self.videoPathfield.hide()
        self.videoPathEnter_pushButton.hide()
        self.anomalyVideoDisplay.hide()
        self.play_pushButton.hide()
        self.pause_pushButton.hide()
        self.videoSlider.hide()
        self.videoDurationChanged.hide()
        ##########################################################
        """
        self.login_pushButton.clicked.connect(self.login)
        self.logout_toolButton.clicked.connect(self.logout)
        self.account_toolButton.clicked.connect(self.showAccountinfo)
        self.users_toolButton.clicked.connect(self.userMenubutton)
        self.addNew_pushButton.clicked.connect(self.addNewCamera)
        # self.addNew_pushButton.clicked.connect(self.addNewCamera)
        self.cancel_pushButton.clicked.connect(self.close)

        self.cam01_pushButton.clicked.connect(self.cam1clicked)
        self.cam02_pushButton.clicked.connect(self.cam2clicked)
        self.cam03_pushButton.clicked.connect(self.cam3clicked)
        self.cam04_pushButton.clicked.connect(self.cam4clicked)
        self.cam05_pushButton.clicked.connect(self.cam5clicked)
        self.cam06_pushButton.clicked.connect(self.cam6clicked)

        # self.cancel_PushButton.clicked.connect(lambda: self.menuStackedWidget.setCurrentIndex(1))
        self.userAdd_pushButton.clicked.connect(
            lambda: self.menuStackedWidget.setCurrentIndex(6)
        )
        self.adminAdd_pushButton.clicked.connect(
            lambda: self.menuStackedWidget.setCurrentIndex(6)
        )
        self.adminstable_radioButton.toggled.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )
        self.securitytable_radioButton.toggled.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )

        self.english_radioButton.toggled.connect(self.changeLanguagetoEnglish)
        self.urdu_radioButton.toggled.connect(self.changeLanguagetoUrdu)
        self.logout_toolButton.clicked.connect(self.changeLanguagetoEnglish)
        self.alarm_toolButton.clicked.connect(self.anomaly_tableDetail)
        self.userDelete_pushButton.clicked.connect(self.deleteUser)
        self.adminDelete_pushButton.clicked.connect(self.deleteAdmin)
        self.addNewUser_pushButton.clicked.connect(self.addnewuser)

        ####################################Display video#########################################

        self.eye_toolButton.clicked.connect(self.revealPassword)
        self.password_shown = False
        # self.anomalySearch_pushButton.clicked.connect(self.anomalySearchAction)
        self.anomalySearch_pushButton.clicked.connect(self.openPlayAnomalyVideo)
        self.anomalysearch = False

        self.displaycross_1.clicked.connect(self.displaycross1Action)
        self.displaycross_2.clicked.connect(self.displaycross2Action)
        self.displaycross_3.clicked.connect(self.displaycross3Action)
        self.displaycross_4.clicked.connect(self.displaycross4Action)
        self.displaycross_5.clicked.connect(self.displaycross5Action)
        self.displaycross_6.clicked.connect(self.displaycross6Action)

    def conditionCross(self):
        if self.cam01_pushButton.isHidden() and self.cam02_pushButton.isHidden() and self.cam03_pushButton.isHidden() and self.cam04_pushButton.isHidden() and self.cam05_pushButton.isHidden() and self.cam06_pushButton.isHidden():
            self.cameras_label.hide()
        else:
            print("yay")

    def openCamOptions(self):
        self.camOptions = camOptionsDialog()
        self.camOptions.openDir_pushButton.clicked.connect(self.openFile)
        self.camOptions.addIPCam_pushButton.clicked.connect(self.openIPcam)
        self.camOptions.openWebcam_pushButton.clicked.connect(self.openWebcam)
        self.camOptions.cancel_PushButton.clicked.connect(self.close)
        self.camOptions.show()


    def openPlayAnomalyVideo(self):
        self.playAnomalyVideo = playAnomalyDialog()

        self.playAnomalyVideo.anomalyVideoDisplay.setStyleSheet(
            "\n" "background-color: rgb(0, 0, 0);\n" ""
        )
        self.playAnomalyVideo.videoPathEnter_pushButton.clicked.connect(self.openVideo)
        self.playAnomalyVideo.mediaPlayer = QMediaPlayer(
            None, QMediaPlayer.VideoSurface
        )  # create media player object
        self.playAnomalyVideo.mediaPlayer.setVideoOutput(
            self.playAnomalyVideo.anomalyVideoDisplay
        )  # pass the widget where the video will be displayed
        self.playAnomalyVideo.play_pushButton.setEnabled(False)
        self.playAnomalyVideo.pause_pushButton.setEnabled(False)
        self.playAnomalyVideo.play_pushButton.clicked.connect(self.playVideo)
        self.playAnomalyVideo.pause_pushButton.clicked.connect(self.pauseVideo)
        self.playAnomalyVideo.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.playAnomalyVideo.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.playAnomalyVideo.show()

    def displaycross1Action(self):
        # self.display_1.setText("Nothing to display.")
        self.conditionCross()
        self.display_1.hide()
        self.displaycross_1.hide()
        self.camLabel1.hide()
        self.cam01_pushButton.hide()

    def displaycross2Action(self):
        # self.display_2.setText("Nothing to display.")
        self.conditionCross()
        self.display_2.hide()
        self.displaycross_2.hide()
        self.camLabel2.hide()
        self.cam02_pushButton.hide()

    def displaycross3Action(self):
        # self.display_3.setText("Nothing to display.")
        self.conditionCross()
        self.display_3.hide()
        self.displaycross_3.hide()
        self.camLabel3.hide()
        self.cam03_pushButton.hide()

    def displaycross4Action(self):
        # self.display_4.setText("Nothing to display.")
        self.conditionCross()
        self.display_4.hide()
        self.displaycross_4.hide()
        self.camLabel4.hide()
        self.cam04_pushButton.hide()

    def displaycross5Action(self):
        # self.display_5.setText("Nothing to display.")
        self.conditionCross()
        self.display_5.hide()
        self.displaycross_5.hide()
        self.camLabel5.hide()
        self.cam05_pushButton.hide()

    def displaycross6Action(self):
        # self.display_6.setText("Nothing to display.")
        self.conditionCross()
        self.display_6.hide()
        self.displaycross_6.hide()
        self.camLabel6.hide()
        self.cam06_pushButton.hide()

    def anomalySearchAction(self):
        if not self.anomalysearch:
            # text = self.anomalySearch_lineEdit.text()
            items = self.alarm_tableWidget.findItems(
                self.anomalySearch_lineEdit.text(), QtCore.Qt.MatchContains
            )
            brush = qtg.QBrush(qtg.QColor("orange"))
            brush.setStyle(QtCore.Qt.SolidPattern)
            for item in items:
                item.setForeground(brush)
            self.anomalysearch = True
        else:
            items = self.alarm_tableWidget.findItems(
                self.anomalySearch_lineEdit.text(), QtCore.Qt.MatchContains
            )
            brush = qtg.QBrush(qtg.QColor("white"))
            brush.setStyle(QtCore.Qt.SolidPattern)
            for item in items:
                item.setForeground(brush)
            self.anomalysearch = False
        """
        items = self.alarm_tableWidget.findItems(self.anomalySearch_lineEdit.text(), QtCore.Qt.MatchExactly)
        if items:
            results = '\n'.join(
                'row %d column %d' % (item.row() + 1, item.column() + 1)
                for item in items)
        else:
            results = 'Found Nothing'
        QMessageBox().information(self, 'Search Results', results)
        """

    def revealPassword(self):
        if not self.password_shown:
            icon = qtg.QIcon()
            icon.addPixmap(
                qtg.QPixmap(":/logo/visible-24.png"), qtg.QIcon.Normal, qtg.QIcon.Off
            )
            self.eye_toolButton.setIcon(icon)
            self.password1_field.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.password_shown = True
        else:
            icon = qtg.QIcon()
            icon.addPixmap(
                qtg.QPixmap(":/logo/invisible-24.png"), qtg.QIcon.Normal, qtg.QIcon.Off
            )
            self.eye_toolButton.setIcon(icon)
            self.password1_field.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password_shown = False

    """
    def menuButtonColor(self):
        while True:
            if self.menuStackedWidget.setCurrentIndex(1) == True:
                print("NOOOO")
                self.camera_toolButton.setStyleSheet("background-color:white;")
                break
            elif self.menuStackedWidget.currentIndex() == 2:
                print("in 2")
                self.alarm_toolButton.setStyleSheet("background-color:#2A2F3C;")
                break
            elif self.menuStackedWidget.currentIndex() == 3:
                print("3rd logic worked hehe")
                self.storage_toolButton.setStyleSheet("background-color:#2A2F3C;")
                break
            elif self.menuStackedWidget.currentIndex() == 4:
                self.account_toolButton.setStyleSheet("background-color:#2A2F3C;")
                break
            elif self.menuStackedWidget.currentIndex() == 5:
                self.user_toolButton.setStyleSheet("background-color:#2A2F3C;")
                break
            elif self.menuStackedWidget.currentIndex() == 6:
                self.language_toolButton.setStyleSheet("background-color:#2A2F3C;")
                break
            else:
                self.logout_toolButton.setStyleSheet("background-color:#2A2F3C;")
                print("I AM NOT GONNA ENTER HEHE")
                break
    """

    def openVideo(self):
        # fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",QDir.homePath())
        fileName = str(self.playAnomalyVideo.videoPathfield.text())
        if fileName != "":
            print(fileName)
            self.playAnomalyVideo.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playAnomalyVideo.mediaPlayer.play()
            self.playAnomalyVideo.play_pushButton.setEnabled(True)
            self.playAnomalyVideo.pause_pushButton.setEnabled(True)
        else:
            print("Video not played")

    def playVideo(self):
        self.playAnomalyVideo.mediaPlayer.play()

    def pauseVideo(self):
        self.playAnomalyVideo.mediaPlayer.pause()

    def positionChanged(self, position):
        self.playAnomalyVideo.videoSlider.setValue(position)

    def durationChanged(self, duration):
        self.playAnomalyVideo.videoSlider.setRange(0, duration)
        minutes = int(duration / 60000)
        seconds = int((duration - minutes * 60000) / 1000)
        self.playAnomalyVideo.videoDurationChanged.setText("{}:{}".format(minutes, seconds))

    def setPosition(self, position):
        self.playAnomalyVideo.mediaPlayer.setPosition(position)

    def MessagesProfile(self, title, message):
        mssg = QMessageBox()
        mssg.setWindowTitle(title)
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mssg.setStyleSheet(
            "*{\n"
            "font-family: century gothic;\n"
            "background: white ;\n"
            "}\n"
            "QPushButton, QToolButton{\n"
            "font-weight:bold;\n"
            "background-color:#1C1D25;\n"
            "color:white ;\n"
            "background: #2A2F3C ;\n"
            "}\n"
            "QPushButton:hover{\n"
            "color:white;\n"
            "background-color:black;\n"
            "}\n"
        )
        mssg.setText(message)
        mssg.buttonClicked.connect(self.buttonClickeed)
        mssg.exec_()

    def buttonClickeed(self, me):
        if me.text() == QMessageBox.Ok:
            self.mainStackedWidget.setCurrentIndex(2)
            print("quit")
            quit()

    def logout(self):
        self.MessagesProfile("Quit", "Will you like to Logout?")
        self.mainStackedWidget.setCurrentIndex(2)
        # self.menuButtonColor()
        # quit()
        # connection.close()

    def addnewuser(self):
        if self.aAdmin_radioButton.isChecked():
            self.addAdmin()
        elif self.aSecurity_radioButton.isChecked():
            self.addUser()

    def addAdmin(self):
        fname = self.afname_field.text()
        lname = self.alname_field.text()
        username = self.ausername_field.text()
        password = self.aPassword_field.text()
        contactno = self.aContactNo_field.text()
        address = self.aAddress_field.toPlainText()
        try:
            curs.execute(
                "INSERT INTO surveilia_admin (admin_fname,admin_lname,admin_username,admin_password,admin_contactno,admin_address) VALUES (?,?,?,?,?,?)",
                (fname, lname, username, password, contactno, address),
            )
            connection.commit()
            print("User added")
            self.Load_DatabaseAdmin()
            self.stackedWidget.setCurrentIndex(1)
        except Exception as error:
            print(error)
        self.menuStackedWidget.setCurrentIndex(5)

    def addUser(self):
        fname = self.afname_field.text()
        lname = self.alname_field.text()
        username = self.ausername_field.text()
        password = self.aPassword_field.text()
        contactno = self.aContactNo_field.text()
        address = self.aAddress_field.toPlainText()
        try:
            curs.execute(
                "INSERT INTO surveilia_users (user_fname,user_lname,user_username,user_password,user_contactno,user_address) VALUES (?,?,?,?,?,?)",
                (fname, lname, username, password, contactno, address),
            )
            connection.commit()
            print("User added")
            self.Load_DatabaseUsers()
        except Exception as error:
            print(error)
        self.menuStackedWidget.setCurrentIndex(5)

    def userMenubutton(self):
        if self.admin_radioButton.isChecked():
            self.menuStackedWidget.setCurrentIndex(5)
            self.Load_DatabaseUsers()
            self.Load_DatabaseAdmin()

        elif self.security_radioButton.isChecked():
            self.menuStackedWidget.setCurrentIndex(9)

    def login(self):
        while True:
            username = self.username1_field.text()
            password = self.password1_field.text()
            if username != "" and password != "":
                if (
                        self.admin_radioButton.isChecked() == False
                        and self.security_radioButton.isChecked() == False
                ):
                    self.loginFlag_label.setText("No account type selected.")
                    break
                if self.admin_radioButton.isChecked():
                    find_user = "SELECT * FROM surveilia_admin WHERE admin_username = ? AND admin_password = ?"

                elif self.security_radioButton.isChecked():
                    find_user = "SELECT * FROM surveilia_users WHERE user_username = ? AND user_password = ?"
            elif username == "" or password == "":
                self.loginFlag_label.setText("Enter username or password.")
                break
            else:
                self.loginFlag_label.setText("Unknown Error Occured.")
                break
            # datetime = QDateTime.currentDateTime()

            now = QDate.currentDate()
            now1 = QTime.currentTime()

            curs.execute(find_user, [(username), (password)])
            results = curs.fetchall()
            if results:
                for i in results:
                    print("Welcome " + i[1])
                    self.mainStackedWidget.setCurrentIndex(1)
                    # self.menuButtonColor()
                    self.welcomeName_label.setText(i[1] + " " + i[2])
                    self.userName_label.setText(i[1] + " " + i[2])
                    self.dateTime_label.setText(now.toString(QtCore.Qt.ISODate) + " " + now1.toString(QtCore.Qt.DefaultLocaleLongDate))
                break
            else:
                print("Username & password not recognized")
                self.loginFlag_label.setText("Invalid Username or Password.")
                break

    def showAccountinfo(self):
        self.menuStackedWidget.setCurrentIndex(4)
        # if self.security_radioButton.isChecked():
        self.edit_pushButton.hide()
        self.fname_field.setReadOnly(True)
        self.lname_field.setReadOnly(True)
        self.username_field.setReadOnly(True)
        self.password_field.setReadOnly(True)
        self.contactInfo_field.setReadOnly(True)
        self.address_field.setReadOnly(True)
        while True:
            username = self.username1_field.text()
            password = self.password1_field.text()
            if self.admin_radioButton.isChecked():
                find_user = "SELECT * FROM surveilia_admin WHERE admin_username = ? AND admin_password = ?"
            elif self.security_radioButton.isChecked():
                find_user = "SELECT * FROM surveilia_users WHERE user_username = ? AND user_password = ?"

            curs.execute(find_user, [(username), (password)])
            results = curs.fetchall()
            if results:
                for i in results:
                    self.fname_field.setText(str(i[1]))
                    self.lname_field.setText(str(i[2]))
                    self.username_field.setText(str(i[3]))
                    self.password_field.setText(str(i[4]))
                    self.contactInfo_field.setText(str(i[5]))
                    self.address_field.setText(str(i[6]))
                break
            else:
                print("UNKNOWN ERROR occured while displaying data.")
                break

    def deleteUser(self):
        # print('ifrah')
        content = "SELECT * FROM surveilia_users"
        res = curs.execute(content)
        for row in enumerate(res):
            if row[0] == self.user_tableWidget.currentRow():
                data = row[1]
                id = data[0]
                fname = data[1]
                lname = data[2]
                username = data[3]
                password = data[4]
                contactno = data[5]
                address = data[6]
                curs.execute(
                    "DELETE FROM surveilia_users WHERE user_id=? AND user_fname=? AND user_lname=? AND user_username = ? AND user_password = ? AND user_contactno =? AND user_address =? ",
                    (id, fname, lname, username, password, contactno, address),
                )
                connection.commit()
                self.Load_DatabaseUsers()
        # self.user_tableWidget.removeRow(self.user_tableWidget.currentRow())

    def deleteAdmin(self):
        content = "SELECT * FROM surveilia_admin"
        res = curs.execute(content)
        for row in enumerate(res):
            if row[0] == self.admin_tableWidget.currentRow():
                data = row[1]
                id = data[0]
                fname = data[1]
                lname = data[2]
                username = data[3]
                password = data[4]
                contactno = data[5]
                address = data[6]
                curs.execute(
                    "DELETE FROM surveilia_admin WHERE admin_id=? AND admin_fname=? AND admin_lname=? AND admin_username = ? AND admin_password = ? AND admin_contactno =? AND admin_address =? ",
                    (id, fname, lname, username, password, contactno, address),
                )
                connection.commit()
                self.Load_DatabaseAdmin()
        # self.admin_tableWidget.removeRow(self.user_tableWidget.currentRow())

    def Load_DatabaseUsers(self):

        while self.user_tableWidget.rowCount() > 0:
            self.user_tableWidget.removeRow(0)
        # connection = sqlite3.connect('Surveilia_database.db')
        content = "SELECT * FROM surveilia_users"
        res = connection.execute(content)
        for row_index, row_data in enumerate(res):
            self.user_tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.user_tableWidget.setItem(
                    row_index, colm_index, QtWidgets.QTableWidgetItem(str(colm_data))
                )
        # self.countLabel.setText("Total Users : " + str(self.user_tableWidget.rowCount()))
        return

    def Load_DatabaseAdmin(self):

        while self.admin_tableWidget.rowCount() > 0:
            self.admin_tableWidget.removeRow(0)
        # connection = sqlite3.connect('Surveilia_database.db')
        content = "SELECT * FROM surveilia_admin"
        res = connection.execute(content)
        for row_index, row_data in enumerate(res):
            self.admin_tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.admin_tableWidget.setItem(
                    row_index, colm_index, QtWidgets.QTableWidgetItem(str(colm_data))
                )
        # self.countLabel.setText("Total Users : " + str(self.user_tableWidget.rowCount()))
        return

    #############################################################################################################################

    # Record Anaomlous event to a file
    def getStatsOfAbnormalActivity(self, cameraID, videoPath):
        x = datetime.datetime.now()
        with open("./appData/Details.csv", mode="a") as csv_file:
            fieldnames = ["CameraID", "Event", "Date", "Time", "Video Path"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:
                writer.writeheader()
            date = str(x.strftime("%A") + "/" + str(x.date()))
            time = str(x.strftime("%H:%M:%S"))


            writer.writerow(
                {
                    "CameraID": cameraID,
                    "Event": "Abnormal",
                    "Date": date,
                    "Time": time,
                    "Video Path": videoPath,
                }
            )

    ######################READ CSV FILE TO DISPLAY DATA IN QTABLEWIDGET###################

    def anomaly_tableDetail(self):
        self.menuStackedWidget.setCurrentIndex(2)
        read_file = pd.read_csv(r"./appData/Details.csv")
        read_file.to_excel(r"./appData/Details.xlsx", index=None, header=True)

        self.anomaly_details = xlrd.open_workbook("./appData/Details.xlsx")
        self.sheet = self.anomaly_details.sheet_by_index(0)
        self.data = [
            [self.sheet.cell_value(r, c) for c in range(self.sheet.ncols)]
            for r in range(self.sheet.nrows)
        ]
        # print(self.data)
        self.alarm_tableWidget.setColumnCount(5)
        self.alarm_tableWidget.setRowCount(
            self.sheet.nrows - 1
        )  # same no.of rows as of csv file
        """
        for index in range(self.alarm_tableWidget.rowCount()):
            self.urlbtn = QtWidgets.QPushButton(self.alarm_tableWidget)
            self.urlbtn.setText("Play Video")
            self.alarm_tableWidget.setCellWidget(index, 4, self.urlbtn)
        """
        for row, columnvalues in enumerate(self.data):
            for column, value in enumerate(columnvalues):
                self.item = QtWidgets.QTableWidgetItem(
                    str(value)
                )  # str is to also display the integer values
                self.alarm_tableWidget.setItem(row - 1, column, self.item)
                # to set the elements read only
                ##############################*******************************CHECKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
                # self.item.setFlags(QtCore.Qt.ItemIsEnabled)

    ##########################################MODEL######################################################
    def tsmmodel(self, f, check):

        # os.environ[""] = "0"

        emptyString = ""

        print()
        print("======>>>>> Loading model ... Please wait ...")

        # just adding some comments to check git
        def parse_shift_option_from_log_name(log_name):
            if "shift" in log_name:
                strings = log_name.split("_")
                for i, s in enumerate(strings):
                    if "shift" in s:
                        break
                return True, int(strings[i].replace("shift", "")), strings[i + 1]
            else:
                return False, None, None

        # args = parser.parse_args()

        this_weights = "tsm_model/checkpoint/TSM_ucfcrime_RGB_mobilenetv2_shift8_blockres_avg_segment8_e50/ckpt.best.pth.tar"
        # this_weights = 'checkpoint/TSM_ucfcrime_RGB_resnet50_shift8_blockres_avg_segment8_e25/ckpt.best.pth.tar'
        is_shift, shift_div, shift_place = parse_shift_option_from_log_name(
            this_weights
        )
        modality = "RGB"
        if "RGB" in this_weights:
            modality = "RGB"

        # Get dataset categories.
        categories = ["Normal Activity", "Abnormal Activity"]
        num_class = len(categories)
        # this_arch = 'resnet50'
        this_arch = "mobilenetv2"

        net = TSN(
            num_class,
            1,
            modality,
            base_model=this_arch,
            consensus_type="avg",
            img_feature_dim="225",
            # pretrain=args.pretrain,
            is_shift=is_shift,
            shift_div=shift_div,
            shift_place=shift_place,
            non_local="_nl" in this_weights,
        )

        checkpoint = torch.load(this_weights, map_location=torch.device("cpu"))
        # checkpoint = torch.load(this_weights)

        checkpoint = checkpoint["state_dict"]

        # base_dict = {('base_model.' + k).replace('base_model.fc', 'new_fc'): v for k, v in list(checkpoint.items())}
        base_dict = {".".join(k.split(".")[1:]): v for k, v in list(checkpoint.items())}
        replace_dict = {
            "base_model.classifier.weight": "new_fc.weight",
            "base_model.classifier.bias": "new_fc.bias",
        }
        for k, v in replace_dict.items():
            if k in base_dict:
                base_dict[v] = base_dict.pop(k)

        net.load_state_dict(base_dict)
        # net.cuda().eval()
        net.eval()
        transform = torchvision.transforms.Compose(
            [
                Stack(roll=(this_arch in ["BNInception", "InceptionV3"])),
                ToTorchFormatTensor(
                    div=(this_arch not in ["BNInception", "InceptionV3"])
                ),
                GroupNormalize(net.input_mean, net.input_std),
            ]
        )
        try:
            os.makedirs("./appData/Anoamly_Clips")
            os.makedirs("./appData/Anoamly_Images")
        except OSError as e:
            pass

        print("loading Video...")
        if f == emptyString:

            cap = cv2.VideoCapture(cv2.CAP_DSHOW)
        else:

            cap = cv2.VideoCapture(f)

        i_frame = -1
        count = 0
        print("Ready!")
        writer = None
        c = 0

        while cap.isOpened():
            count += 1
            i_frame += 1
            ret, img = cap.read()  # (480, 640, 3) 0 ~ 255

            # release everything when job is finished

            if ret:
                if (
                        i_frame % 3 == 0
                ):  # skip every other frame to obtain a suitable frame rate
                    t1 = time.time()

                    img_tran = transform([Image.fromarray(img).convert("RGB")])

                    input = img_tran.view(
                        -1, 3, img_tran.size(1), img_tran.size(2)
                    ).unsqueeze(0)

                    with torch.no_grad():
                        logits = net(input)

                        h_x = torch.mean(F.softmax(logits, 1), dim=0).data

                        print(h_x)

                        pr, li = h_x.sort(0, True)

                        probs = pr.tolist()

                        idx = li.tolist()

                        t2 = time.time()
                        print(count, "-", categories[idx[0]], "Prob: ", probs[0])

                        current_time = t2 - t1
                dim = (420, 420)
                img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                height, width, _ = img.shape
                # height, width, _ = img.shape

                # label = np.ones([height // 10, width, 3]).astype("uint8") + 255

                if categories[idx[0]] == "Abnormal Activity":
                    R = 255
                    G = 0
                    print("\007")
                    Abnormality = True
                    c += 1
                else:
                    R = 0
                    G = 255
                    Abnormality = False

                cv2.putText(
                    img,
                    "Stream: " + str(check) + " " + categories[idx[0]],
                    (20, int(height / 16)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, int(G), int(R)),
                    2,
                )

                cv2.putText(
                    img,
                    "Accuracy: {:.2f}%".format(probs[0] * 100, "%"),
                    (20, int(height / 9)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, int(G), int(R)),
                    2,
                )
                cv2.putText(
                    img,
                    "FPS: {:.1f} ".format(1 / current_time),
                    (250, int(height / 9)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2,
                )
                if writer is None:
                    if c % 60 == 0:
                        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                        (H, W) = img.shape[:2]
                        path = "./appData/Anoamly_Clips/"
                        name = len(glob.glob(path + "*.avi"))

                        getVidName = path + "Abnormal_Event_{}_Cam_{}.avi".format(
                            name + 1, check
                        )
                        self.getStatsOfAbnormalActivity(check, getVidName)
                        writer = cv2.VideoWriter(getVidName, fourcc, 30.0, (W, H), True)

                # Saving Anaomlous Event Image and Clip
                if Abnormality:
                    writer.write(img)
                    # record stat every two seconds if exists
                    # if c % 60 == 0:
                    #    self.getStatsOfAbnormalActivity(check)
                    # if tempThres > 0.75:

                    path = "./appData/Anoamly_Images/"
                    index = len(glob.glob(path + "*.jpg"))
                    # imageName = getFileName(path+'.jpg')
                    imageName = path + "Abnormal_Event_{}_Cam_{}.jpg".format(
                        index + 1, check
                    )
                    cv2.imwrite(imageName, img)

                    # image_frame = np.concatenate((img, label), axis=0)

                if ret == True:
                    if check == 1:
                        dim = (self.display_1.width(), self.display_1.height())
                        img1 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                        height, width, _ = img1.shape
                        bytesPerLine = 3 * width
                        img1 = qtg.QImage(
                            img1.data,
                            width,
                            height,
                            bytesPerLine,
                            qtg.QImage.Format_RGB888,
                        ).rgbSwapped()
                        self.display_1.setPixmap(qtg.QPixmap.fromImage(img1))

                    elif check == 2:
                        dim = (self.display_1.width(), self.display_1.height())
                        img2 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                        height, width, _ = img2.shape
                        bytesPerLine = 3 * width
                        img2 = qtg.QImage(
                            img2.data,
                            width,
                            height,
                            bytesPerLine,
                            qtg.QImage.Format_RGB888,
                        ).rgbSwapped()
                        self.display_2.setPixmap(qtg.QPixmap.fromImage(img2))
                        # self.camSignal = 0

                    elif check == 3:
                        dim = (self.display_1.width(), self.display_1.height())
                        img3 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                        height, width, _ = img3.shape
                        bytesPerLine = 3 * width
                        img3 = qtg.QImage(
                            img3.data,
                            width,
                            height,
                            bytesPerLine,
                            qtg.QImage.Format_RGB888,
                        ).rgbSwapped()
                        self.display_3.setPixmap(qtg.QPixmap.fromImage(img3))
                        # self.camSignal = 0

                    elif check == 4:
                        dim = (self.display_1.width(), self.display_1.height())
                        img4 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                        height, width, _ = img4.shape
                        bytesPerLine = 3 * width
                        img4 = qtg.QImage(
                            img4.data,
                            width,
                            height,
                            bytesPerLine,
                            qtg.QImage.Format_RGB888,
                        ).rgbSwapped()
                        self.display_4.setPixmap(qtg.QPixmap.fromImage(img4))
                        # self.camSignal = 0

                    elif check == 5:
                        dim = (self.display_1.width(), self.display_1.height())
                        img5 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                        height, width, _ = img5.shape
                        bytesPerLine = 3 * width
                        img5 = qtg.QImage(
                            img5.data,
                            width,
                            height,
                            bytesPerLine,
                            qtg.QImage.Format_RGB888,
                        ).rgbSwapped()
                        self.display_5.setPixmap(qtg.QPixmap.fromImage(img5))
                        # self.camSignal = 0

                    elif check == 6:
                        dim = (self.display_1.width(), self.display_1.height())
                        img6 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                        height, width, _ = img6.shape
                        bytesPerLine = 3 * width
                        img6 = qtg.QImage(
                            img6.data,
                            width,
                            height,
                            bytesPerLine,
                            qtg.QImage.Format_RGB888,
                        ).rgbSwapped()
                        self.display_6.setPixmap(qtg.QPixmap.fromImage(img6))
                        # self.camSignal = 0
                else:
                    print("Else not found")

            else:
                cap.release()
                cv2.destroyAllWindows()

    def cam1clicked(self):
        self.camSignal = 1
        # self.menuStackedWidget.setCurrentIndex(7)
        self.openCamOptions()

    def cam2clicked(self):
        self.camSignal = 2
        # self.menuStackedWidget.setCurrentIndex(7)
        self.openCamOptions()

    def cam3clicked(self):
        self.camSignal = 3
        # self.menuStackedWidget.setCurrentIndex(7)
        self.openCamOptions()

    def cam4clicked(self):
        self.camSignal = 4
        # self.menuStackedWidget.setCurrentIndex(7)
        self.openCamOptions()

    def cam5clicked(self):
        self.camSignal = 5
        # self.menuStackedWidget.setCurrentIndex(7)
        self.openCamOptions()

    def cam6clicked(self):
        self.camSignal = 6
        # self.menuStackedWidget.setCurrentIndex(7)
        self.openCamOptions()

    # METHOD TO OPEN THE IP CAM THROUGH IP ADDRESS
    def openIPcam(self):
        self.input = 0
        url = str(self.camOptions.addIPCam_field.text())
        # self.menuStackedWidget.setCurrentIndex(1)
        t = Thread(target=self.tsmmodel, daemon=True, args=(url, self.camSignal))
        t.start()
        cv2.waitKey(10)

    # METHOD TO OPEN WEB CAM
    @pyqtSlot()
    def openWebcam(self):
        self.input = 0
        self.logic = 1
        cap = 0
        # self.menuStackedWidget.setCurrentIndex(1)
        t1 = Thread(target=self.tsmmodel, daemon=True, args=(cap, self.camSignal))
        t1.start()
        # release everything when job is finished
        # cap.release()
        cv2.destroyAllWindows()

    # METHOD TO DISPLAY VIDEO(IMAGE BY IMAGE) IN THE BOX
    """def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        pix = qtg.QPixmap.fromImage(img)
        # pix = pix.scaled(self.display_1.width(), self.display_1.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        pix = pix.scaled(
            600, 450, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
        )
        if self.camSignal == 1:
            self.display_1.setPixmap(pix)
            # self.camSignal = 0
        elif self.camSignal == 2:
            self.display_2.setPixmap(pix)
            # self.camSignal = 0
        elif self.camSignal == 3:
            # pix = pix.scaled(self.display_3.width(), self.display_3.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_3.setPixmap(pix)
            # self.camSignal = 0
        elif self.camSignal == 4:
            # pix = pix.scaled(self.display_4.width(), self.display_4.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_4.setPixmap(pix)
            # self.camSignal = 0
        elif self.camSignal == 5:
            # pix = pix.scaled(self.display_5.width(), self.display_5.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_5.setPixmap(pix)
            # self.camSignal = 0
        elif self.camSignal == 6:
            # pix = pix.scaled(self.display_6.width(), self.display_6.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.display_6.setPixmap(pix)
            # self.camSignal = 0"""

    # METHOD TO OPEN FILE DIALOG
    def openFile(self):
        self.input = 0
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open Video", "", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.wmv)"
        )
        t2 = Thread(target=self.tsmmodel, daemon=True, args=(fileName, self.camSignal))

        if fileName != "":
            # self.displayImage(fileName, 1)
            t2.start()
        else:
            print("NO FILE FOUND")
        # display_1.play()
        # self.menuStackedWidget.setCurrentIndex(1)
        # self.menuStackedWidget.setCurrentIndex(1)

    # METHOD TO ADD NEW CAMERAS
    def addNewCamera(self):

        self.cameras_label.show()

        if self.cam01_pushButton.isHidden():
            self.cam01_pushButton.show()
            self.display_1.show()
            self.displaycross_1.show()
            self.camLabel1.show()
            self.camSignal = 1
            self.openCamOptions()
            # self.menuStackedWidget.setCurrentIndex(7)


        elif self.cam02_pushButton.isHidden():
            self.cam02_pushButton.show()
            self.display_2.show()
            self.displaycross_2.show()
            self.camLabel2.show()
            self.camSignal = 2
            self.openCamOptions()
            # self.menuStackedWidget.setCurrentIndex(7)


        elif self.cam03_pushButton.isHidden():
            self.cam03_pushButton.show()
            self.display_3.show()
            self.displaycross_3.show()
            self.camLabel3.show()
            self.camSignal = 3
            self.openCamOptions()
            # self.menuStackedWidget.setCurrentIndex(7)

        elif self.cam04_pushButton.isHidden():
            self.cam04_pushButton.show()
            self.display_4.show()
            self.displaycross_4.show()
            self.camLabel4.show()
            self.camSignal = 4
            self.openCamOptions()
            # self.menuStackedWidget.setCurrentIndex(7)


        elif self.cam05_pushButton.isHidden():
            self.cam05_pushButton.show()
            self.display_5.show()
            self.displaycross_5.show()
            self.camLabel5.show()
            self.camSignal = 5
            self.openCamOptions()
            # self.menuStackedWidget.setCurrentIndex(7)


        elif self.cam06_pushButton.isHidden():
            self.cam06_pushButton.show()
            self.display_6.show()
            self.displaycross_6.show()
            self.camLabel6.show()
            self.camSignal = 6
            self.openCamOptions()
            # self.menuStackedWidget.setCurrentIndex(7)


        else:
            self.addNew_pushButton.setEnabled(False)
            self.addNew_pushButton.setStyleSheet("background-color: light grey ;\n")

    ############################TRANSLATE INTO URDU######################################

    # METHOD TO CHANGE LANGUAGE
    def changeLanguagetoUrdu(self):

        self.title_label.setText("سرویلیا")
        ################# DO NOT DELETE THIS COMMENTED CODE ##############
        """
        self.username1_field.setPlaceholderText(_translate("surveiliaFrontEnd", "Username"))
        self.password1_field.setPlaceholderText(_translate("surveiliaFrontEnd", "Password"))
        self.login_pushButton.setText(_translate("surveiliaFrontEnd", "LOGIN"))
        self.security_radioButton.setText(_translate("surveiliaFrontEnd", "Security Guard"))
        self.admin_radioButton.setText(_translate("surveiliaFrontEnd", "Admin"))
        self.loginas1_label.setText(_translate("surveiliaFrontEnd", "Login as:"))
        """
        ###################################################################
        self.camera_toolButton.setText("کیمرہ")
        # self.storage_toolButton.setText("اسٹوریج")
        self.logout_toolButton.setText("لاگ آوٹ")
        self.users_toolButton.setText("صارفین")
        self.language_toolButton.setText("زبان")
        self.logo_toolButton.setText("لاگ آوٹ")
        self.alarm_toolButton.setText("الارم لاگ")
        self.account_toolButton.setText("اکاؤنٹ")
        self.title_label.setText("سرویلیا")
        self.welcome_label.setText("سرویلیا میں خوش آمدید")
        self.getStarted_pushButton.setText("آو شروع کریں")
        self.cameras_label.setText("کیمرے")
        self.cam01_pushButton.setText("کیمرہ_01")
        self.cam03_pushButton.setText("کیمرہ_03")
        self.cam02_pushButton.setText("کیمرہ_02")
        self.cam04_pushButton.setText("کیمرہ_04")
        self.cam05_pushButton.setText("کیمرہ_05")
        self.cam06_pushButton.setText("کیمرہ_06")
        self.addNew_pushButton.setText("نیا شامل کریں")
        # self.showAll_pushButton.setText("سب دکھائیں")
        self.alarmHistory_label.setText("الارم کی حسٹری")
        self.alarmHistoryDetail_label.setText("الارم کی تاریخ یہاں ظاہر کی گئی ہے۔")
        self.alarm_tableWidget.horizontalHeaderItem(0).setText(" ID کیمرہ ")
        self.alarm_tableWidget.horizontalHeaderItem(1).setText("واقع")
        self.alarm_tableWidget.horizontalHeaderItem(2).setText("تاریخ")
        self.alarm_tableWidget.horizontalHeaderItem(3).setText("وقت")
        self.storage_label.setText("اسٹوریج")
        self.show_label.setText("دکھائیں:        ")
        self.anomalyClip_checkBox.setText("اناملی کلپ")
        self.cameraFeed_checkBox.setText("کیمرا فیڈ")
        self.storage_tableWidget.horizontalHeaderItem(0).setText("فائل کا نام")
        self.storage_tableWidget.horizontalHeaderItem(1).setText("تاریخ")
        self.storage_tableWidget.horizontalHeaderItem(2).setText("سائز")
        self.accountInfo_label.setText("اکاؤنٹ کی معلومات")
        self.fname_label.setText("پہلا نام")
        self.lname_label.setText("آخری نام")
        self.username_label.setText("آصارف نام")
        self.password_label.setText("پاس ورڈ")
        self.contactInfo_label.setText("رابطہ کی معلومات")
        self.address_label.setText("پتہ")
        self.edit_pushButton.setText("ترمیم کریں")
        self.userInfo_label.setText("صارفین کی معلومات")
        self.viewLabel.setText("دیکھیں:")
        self.adminstable_radioButton.setText("ایڈمن")
        self.securitytable_radioButton.setText("سکیورٹی گارڈ")
        self.userAdd_pushButton.setText("شامل کریں")
        self.userDelete_pushButton.setText("حذف کریں")
        self.user_tableWidget.horizontalHeaderItem(0).setText("صارف کی شناخت")
        self.user_tableWidget.horizontalHeaderItem(1).setText("پہلا نام")
        self.user_tableWidget.horizontalHeaderItem(2).setText("آخری نام")
        self.user_tableWidget.horizontalHeaderItem(3).setText("صارف نام")
        self.user_tableWidget.horizontalHeaderItem(4).setText("پاس ورڈ")
        self.user_tableWidget.horizontalHeaderItem(5).setText("رابطہ نمبر")
        self.user_tableWidget.horizontalHeaderItem(6).setText("پتہ")
        self.adminAdd_pushButton.setText("شامل کریں")
        self.adminDelete_pushButton.setText("حذف کریں")
        self.admin_tableWidget.horizontalHeaderItem(0).setText("صارف کی شناخت")
        self.admin_tableWidget.horizontalHeaderItem(1).setText("پہلا نام")
        self.admin_tableWidget.horizontalHeaderItem(2).setText("آخری نام")
        self.admin_tableWidget.horizontalHeaderItem(3).setText("صارف نام")
        self.admin_tableWidget.horizontalHeaderItem(4).setText("پاس ورڈ")
        self.admin_tableWidget.horizontalHeaderItem(5).setText("رابطہ نمبر")
        self.admin_tableWidget.horizontalHeaderItem(6).setText("پتہ")
        self.addUser_label.setText("نیا صارف شامل کریں:")
        self.afname_label.setText("پہلا نام")
        self.alname_label.setText("آخری نام")
        self.aPassword_label.setText("پاس ورڈ")
        self.aContactNo_label.setText("رابطہ کی معلومات")
        self.aAddress_label.setText("پتہ")
        self.addNewUser_pushButton.setText("نیا صارف شامل کریں")
        self.ausername_label.setText("صارف نام")
        self.aAdmin_radioButton.setText("ایڈمن")
        self.aSecurity_radioButton.setText("سکیورٹی گارڈ")
        self.accountType_label.setText("اکاؤنٹ ٹاعپ")
        # self.addIPCam_label.setText(" ایڈریس کا استعمال کرتے ہوئے کیمرا شامل کریں")
        # self.addIPCam_field.setText("IP ایڈریس یہاں داخل کریں")
        # self.addIPCam_pushButton.setText("شامل کریں")
        # self.openDir_label.setText("ڈائریکٹری سے ویڈیو شامل کریں")
        # self.openDir_pushButton.setText("کھولیں")
        # self.openWebcam_label.setText("ویب کیم کا استعمال کرتے ہوئے شامل کریں")
        # self.openWebcam_pushButton.setText("ویب کیم کھولیں")
        # self.cancel_PushButton.setText("منسوخ کریں")
        self.english_radioButton.setText("English")
        self.chooseLanguage_label.setText("زبان کا انتخاب کریں:")
        self.urdu_radioButton.setText("Urdu")
        self.title3_label.setText("سرویلیا")
        self.cancel_pushButton.setText("منسوخ کریں")
        self.loginAgain_pushButton.setText("دوبارہ لاگ ان")
        self.loggedOut_label.setText("آپ لاگ آؤٹ ہوچکے ہیں")

        ##########################TRANSLATE INTO ENGLISH###################################

    def changeLanguagetoEnglish(self):

        self.title1_label.setText("SURVEILIA")
        self.username1_field.setPlaceholderText("Username")
        self.password1_field.setPlaceholderText("Password")
        self.login_pushButton.setText("LOGIN")
        self.security_radioButton.setText("Security Guard")
        self.admin_radioButton.setText("Admin")
        self.loginas1_label.setText("Login as:")
        self.camera_toolButton.setText("Camera")
        # self.storage_toolButton.setText("Storage")
        self.logout_toolButton.setText("Logout")
        self.users_toolButton.setText("Users")
        self.language_toolButton.setText("Language")
        self.logo_toolButton.setText("Logout")
        self.alarm_toolButton.setText("Alarm Log")
        self.account_toolButton.setText("Account")
        self.title_label.setText("SURVEILIA")
        self.welcome_label.setText("Welcome to SURVEILIA")
        self.getStarted_pushButton.setText("GET STARTED")
        self.cameras_label.setText("CAMERAS")
        self.cam01_pushButton.setText("CAMERA_01")
        self.cam03_pushButton.setText("CAMERA_03")
        self.cam02_pushButton.setText("CAMERA_02")
        self.cam04_pushButton.setText("CAMERA_04")
        self.cam05_pushButton.setText("CAMERA_05")
        self.cam06_pushButton.setText("CAMERA_06")
        self.addNew_pushButton.setText("ADD NEW")
        self.alarmHistory_label.setText("ALARM HISTORY")
        self.alarmHistoryDetail_label.setText(
            "The history of alarms is displayed here."
        )
        self.alarm_tableWidget.horizontalHeaderItem(0).setText("Camera ID")
        self.alarm_tableWidget.horizontalHeaderItem(1).setText("Event")
        self.alarm_tableWidget.horizontalHeaderItem(2).setText("Date")
        self.alarm_tableWidget.horizontalHeaderItem(3).setText("Time")
        self.storage_label.setText("STORAGE")
        self.show_label.setText("           Show:")
        self.anomalyClip_checkBox.setText("Anomaly Clip")
        self.cameraFeed_checkBox.setText("Camera Feed")
        self.storage_tableWidget.horizontalHeaderItem(0).setText("Filename")
        self.storage_tableWidget.horizontalHeaderItem(1).setText("Date")
        self.storage_tableWidget.horizontalHeaderItem(2).setText("Size")
        self.accountInfo_label.setText("ACCOUNT INFORMATION")
        self.fname_label.setText("First Name:")
        self.lname_label.setText("Last Name:")
        self.username_label.setText("Username:")
        self.password_label.setText("Password:")
        self.contactInfo_label.setText("Contact Info:")
        self.address_label.setText("Address:")
        self.edit_pushButton.setText("EDIT")
        self.userInfo_label.setText("  USERS INFORMATION")
        self.viewLabel.setText("View:")
        self.adminstable_radioButton.setText("Admins")
        self.securitytable_radioButton.setText("Security Guards")
        self.userAdd_pushButton.setText("ADD")
        self.userDelete_pushButton.setText("DELETE")
        self.user_tableWidget.horizontalHeaderItem(0).setText("ID")
        self.user_tableWidget.horizontalHeaderItem(1).setText("First Name")
        self.user_tableWidget.horizontalHeaderItem(2).setText("Last Name")
        self.user_tableWidget.horizontalHeaderItem(3).setText("Username")
        self.user_tableWidget.horizontalHeaderItem(4).setText("Password")
        self.user_tableWidget.horizontalHeaderItem(5).setText("Contact No.")
        self.user_tableWidget.horizontalHeaderItem(6).setText("Address")
        self.adminAdd_pushButton.setText("ADD")
        self.adminDelete_pushButton.setText("DELETE")
        self.admin_tableWidget.horizontalHeaderItem(0).setText("ID")
        self.admin_tableWidget.horizontalHeaderItem(1).setText("First Name")
        self.admin_tableWidget.horizontalHeaderItem(2).setText("Last Name")
        self.admin_tableWidget.horizontalHeaderItem(3).setText("Username")
        self.admin_tableWidget.horizontalHeaderItem(4).setText("Password")
        self.admin_tableWidget.horizontalHeaderItem(5).setText("Contact No.")
        self.admin_tableWidget.horizontalHeaderItem(6).setText("Address")
        self.addUser_label.setText("ADD NEW USER")
        self.afname_label.setText("First Name:")
        self.alname_label.setText("Last Name:")
        self.aPassword_label.setText("Password:")
        self.aContactNo_label.setText("Contact No.")
        self.aAddress_label.setText("Address:")
        self.addNewUser_pushButton.setText("ADD USER")
        self.ausername_label.setText("Username:")
        self.aAdmin_radioButton.setText("Admin")
        self.aSecurity_radioButton.setText("Security Guard")
        # self.accountType_label.setText("Account Type:")
        # self.addIPCam_label.setText("Add camera using IP Address")
        # self.addIPCam_field.setText("ENTER IP ADDRESS HERE")
        # self.addIPCam_pushButton.setText("ADD")
        # self.openDir_label.setText("Add video by file from Directory")
        # self.openDir_pushButton.setText("OPEN")
        # self.openWebcam_label.setText("Add using Webcam")
        # self.openWebcam_pushButton.setText("OPEN WEBCAM")
        # self.cancel_PushButton.setText("CANCEL")
        self.english_radioButton.setText("English")
        self.chooseLanguage_label.setText("Choose Language:")
        self.urdu_radioButton.setText("Urdu")
        self.title3_label.setText("SURVEILIA")
        self.cancel_pushButton.setText("CANCEL")
        self.loginAgain_pushButton.setText("LOGIN AGAIN")
        self.loggedOut_label.setText("You have been logged out!")


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = ControlMainWindow()
    widget.show()
    try:
        app.exec_()
    except:
        print("EXITING")
