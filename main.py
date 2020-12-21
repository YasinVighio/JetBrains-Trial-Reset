import sys, platform, subprocess, time
import logging as log
from os import path
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QEventLoop

class resetterUI(QMainWindow):
    def __init__(self):
        super(resetterUI, self).__init__()
        self.loadInterface()
        log.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        resetButton=self.findChild(QPushButton, "resetBt")
        resetButton.clicked.connect(self.resetTrial)

    def loadInterface(self):
        try:
            if(path.exists("Resetter.ui") == False or path.exists("resetfiles\jtr_win.bat") == False or path.exists("resetfiles\jtr_linux.sh")==False):
                raise Exception
            else:
                uic.loadUi('Resetter.ui', self)
                self.show()
        except Exception as ex:
            log.exception(ex)
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Critical Error")
            error.setInformativeText('Some files are missing try reinstalling program')
            error.setWindowTitle("Error")
            error.exec_()
            exit(0)

    def pause(self):
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec_()

    def resetTrial(self):
        try:
            text = ">_ Checking Your OS ...."
            screen = self.findChild(QLabel, "consoleScreen")
            screen.setText(text)
            self.pause()

            text+="\n\n>_ OS: " + str(platform.system())
            screen.setText(text)
            self.pause()

            text+="\n\n>_ Deleting old files..."
            screen.setText(text)
            self.pause()

            text+="\n\n>_ Done..."
            screen.setText(text)
            self.pause()

            text+="\n\n>>> Enjoy your free trial for another month :)"
            screen.setText(text)


            if(str.lower(platform.system()) == "windows"):
                subprocess.call([r'resetfiles\jtr_win.bat'])
            else:
                subprocess.call([r'resetfiles\jtr_linux.bat'])

        except Exception as ex:
            log.exception(ex)

app = QApplication(sys.argv)
mainWindow = resetterUI()
mainWindow.setWindowTitle("JetBrains Trial Reset Program")
app.exec_()