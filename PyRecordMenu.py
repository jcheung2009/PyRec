# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PYRecordMenu.ui'
#
# Created: Mon May 25 19:54:04 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.RescanInputsPushButton = QtGui.QPushButton(self.centralwidget)
        self.RescanInputsPushButton.setGeometry(QtCore.QRect(70, 50, 91, 23))
        self.RescanInputsPushButton.setObjectName(_fromUtf8("RescanInputsPushButton"))
        self.InputSelectionSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.InputSelectionSpinBox.setGeometry(QtCore.QRect(70, 110, 61, 22))
        self.InputSelectionSpinBox.setObjectName(_fromUtf8("InputSelectionSpinBox"))
        self.BirdNameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.BirdNameLineEdit.setGeometry(QtCore.QRect(60, 200, 111, 20))
        self.BirdNameLineEdit.setObjectName(_fromUtf8("BirdNameLineEdit"))
        self.ThresholdLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.ThresholdLineEdit.setGeometry(QtCore.QRect(60, 250, 111, 20))
        self.ThresholdLineEdit.setObjectName(_fromUtf8("ThresholdLineEdit"))
        self.GraphOne = QtGui.QGraphicsView(self.centralwidget)
        self.GraphOne.setGeometry(QtCore.QRect(60, 350, 471, 192))
        self.GraphOne.setObjectName(_fromUtf8("GraphOne"))
        self.BirdNameFixedTest = QtGui.QLabel(self.centralwidget)
        self.BirdNameFixedTest.setGeometry(QtCore.QRect(40, 180, 71, 16))
        self.BirdNameFixedTest.setObjectName(_fromUtf8("BirdNameFixedTest"))
        self.InputSelectionFixedText = QtGui.QLabel(self.centralwidget)
        self.InputSelectionFixedText.setGeometry(QtCore.QRect(70, 90, 91, 16))
        self.InputSelectionFixedText.setObjectName(_fromUtf8("InputSelectionFixedText"))
        self.ThresholdFixedText = QtGui.QLabel(self.centralwidget)
        self.ThresholdFixedText.setGeometry(QtCore.QRect(40, 230, 71, 16))
        self.ThresholdFixedText.setObjectName(_fromUtf8("ThresholdFixedText"))
        self.StopPushButton = QtGui.QPushButton(self.centralwidget)
        self.StopPushButton.setGeometry(QtCore.QRect(680, 470, 101, 71))
        self.StopPushButton.setObjectName(_fromUtf8("StopPushButton"))
        self.StartPushButton = QtGui.QPushButton(self.centralwidget)
        self.StartPushButton.setGeometry(QtCore.QRect(560, 470, 101, 71))
        self.StartPushButton.setObjectName(_fromUtf8("StartPushButton"))
        self.ListeningTextBox = QtGui.QLabel(self.centralwidget)
        self.ListeningTextBox.setGeometry(QtCore.QRect(590, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ListeningTextBox.setFont(font)
        self.ListeningTextBox.setText(_fromUtf8(""))
        self.ListeningTextBox.setObjectName(_fromUtf8("ListeningTextBox"))
        self.WorkingDirpushButton = QtGui.QPushButton(self.centralwidget)
        self.WorkingDirpushButton.setGeometry(QtCore.QRect(220, 200, 75, 23))
        self.WorkingDirpushButton.setObjectName(_fromUtf8("WorkingDirpushButton"))
        self.BufferTimeSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.BufferTimeSpinBox.setGeometry(QtCore.QRect(60, 300, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.BufferTimeSpinBox.setFont(font)
        self.BufferTimeSpinBox.setMinimum(1)
        self.BufferTimeSpinBox.setObjectName(_fromUtf8("BufferTimeSpinBox"))
     #   self.InputSelectionSpinBox.setMinimum(0)
        self.ThresholdFixedText_2 = QtGui.QLabel(self.centralwidget)
        self.ThresholdFixedText_2.setGeometry(QtCore.QRect(40, 280, 71, 16))
        self.ThresholdFixedText_2.setObjectName(_fromUtf8("ThresholdFixedText_2"))
  #      MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
   #     MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
    #    MainWindow.setStatusBar(self.statusbar)
    #    self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.RescanInputsPushButton.setText(_translate("MainWindow", "Rescan Inputs", None))
        self.BirdNameLineEdit.setText(_translate("MainWindow", "output", None))
        self.ThresholdLineEdit.setText(_translate("MainWindow", "10500", None))
        self.BirdNameFixedTest.setText(_translate("MainWindow", "Bird Name?", None))
        self.InputSelectionFixedText.setText(_translate("MainWindow", "Input Selection", None))
        self.ThresholdFixedText.setText(_translate("MainWindow", "Threshold", None))
        self.StopPushButton.setText(_translate("MainWindow", "Stop", None))
        self.StartPushButton.setText(_translate("MainWindow", "Start", None))
        self.WorkingDirpushButton.setText(_translate("MainWindow", "Working Dir", None))
        self.ThresholdFixedText_2.setText(_translate("MainWindow", "Buffer time (s)", None))
        #self.menuExit.setTitle(_translate("MainWindow", "Exit", None))

