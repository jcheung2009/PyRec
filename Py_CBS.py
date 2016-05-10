
import sys
from PyQt4.QtGui import QApplication,QDialog
from PyQt4 import QtCore, QtGui
from PyRecordMenu import Ui_MainWindow
from AudioRecorderFunctions import *
import GlobalVars



def RescanInputsButtonPushed():
    import GlobalVars    
    RescanInputs()    
    ui.InputSelectionSpinBox.setMinimum(0)
    ui.InputSelectionSpinBox.setMaximum(GlobalVars.numdevices)
    
  
def StopPushButton():   
    import GlobalVars
    GlobalVars.isRunning=0
    
    ui.StartPushButton.setEnabled(True)
    ui.RescanInputsPushButton.setEnabled(True)
    ui.ThresholdLineEdit.setEnabled(True)
    ui.BirdNameLineEdit.setEnabled(True)   
    ui.InputSelectionSpinBox.setEnabled(True)
    ui.WorkingDirpushButton.setEnabled(True)
    ui.BufferTimeSpinBox.setEnabled(True)    
    ui.ListeningTextBox.setText('')

def StartPushButton():
    import threading
    import GlobalVars
    
    ui.StartPushButton.setEnabled(False)
    ui.RescanInputsPushButton.setEnabled(False)
    ui.ThresholdLineEdit.setEnabled(False)
    ui.BirdNameLineEdit.setEnabled(False)
    ui.InputSelectionSpinBox.setEnabled(False)
    ui.WorkingDirpushButton.setEnabled(False)
    ui.BufferTimeSpinBox.setEnabled(False)    
    
    GlobalVars.isRunning=1
   # threading.Thread(target=TriggeredRecordAudio, args=arg1).start()
    TriggeredRecordAudio(ui)

def ThresholdLineEditChanged(newvalue):
    import GlobalVars
    GlobalVars.threshold=int(newvalue)

def BufferTimeSpinBoxChanged(newvalue):
    import GlobalVars
    GlobalVars.buffertime=int(newvalue)
    
def InputSelectionSpinBoxChanged(newvalue):
    import GlobalVars
    GlobalVars.inputdeviceindex=int(newvalue)
  
def BirdNameLineEditChanged(newvalue):
    import GlobalVars
    GlobalVars.filename=str(newvalue)

def WorkingDirpushButtonClicked():
    import os
    import GlobalVars
    
    dialog = QtGui.QFileDialog()
    dialog.setFileMode(QtGui.QFileDialog.Directory)
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, True)
    directory = QtGui.QFileDialog.getExistingDirectory(dialog, 'Select Drive')
    directory = str(directory)
    print directory
    GlobalVars.path=directory+'/'


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)
GlobalVars.buffertime=1
GlobalVars.threshold=10500
GlobalVars.filename='output'
GlobalVars.inputdeviceindex=0




ui.RescanInputsPushButton.connect(ui.RescanInputsPushButton,
                                        QtCore.SIGNAL(("clicked()")),
                                        RescanInputsButtonPushed)

ui.StopPushButton.connect(ui.StopPushButton,
                                        QtCore.SIGNAL(("clicked()")),
                                        StopPushButton)

ui.StartPushButton.connect(ui.StartPushButton,
                                        QtCore.SIGNAL(("clicked()")),
                                        StartPushButton)

ui.ThresholdLineEdit.connect(ui.ThresholdLineEdit,
                                        QtCore.SIGNAL(("textChanged(QString)")),
                                        ThresholdLineEditChanged)

ui.BirdNameLineEdit.connect(ui.BirdNameLineEdit,
                                        QtCore.SIGNAL(("textChanged(QString)")),
                                        BirdNameLineEditChanged)
                                       
ui.BufferTimeSpinBox.connect(ui.BufferTimeSpinBox,
                                        QtCore.SIGNAL(("valueChanged(int)")),
                                        BufferTimeSpinBoxChanged) 

ui.InputSelectionSpinBox.connect(ui.InputSelectionSpinBox,
                                        QtCore.SIGNAL(("valueChanged(int)")),
                                        InputSelectionSpinBoxChanged)        

ui.WorkingDirpushButton.connect(ui.WorkingDirpushButton,
                                        QtCore.SIGNAL(("clicked()")),
                                        WorkingDirpushButtonClicked)
window.show()
sys.exit(app.exec_())


    


