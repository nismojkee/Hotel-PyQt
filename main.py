import sys
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.sip import *
import gallery, about, home


#Welcome Window with just ONE BUTTON to ENTER
class EnterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        display = QDesktopWidget().screenGeometry()
        screenHeight = display.height()
        screenWidth = display.width()

        button = QPushButton('Вход',self)
        button.resize(int(screenWidth/7), int(screenHeight/9))
        button.move( int(screenWidth-button.width())/2, int(screenHeight-button.height())/2 )
        button.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase; border-radius: 10px;')
        button.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 18))
        button.clicked.connect(self.welcome)

        self.setStyleSheet('background: #210020')
        self.showFullScreen()

    def welcome(self):
        self.w = home.HomeWindow()
        self.w.showFullScreen()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainUI = gallery.GalleryWindow()
    sys.exit(app.exec_())