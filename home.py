import sys
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.sip import *
import gallery, about

class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        display = QDesktopWidget().screenGeometry()
        screenHeight = display.height()
        screenWidth = display.width()

        btnHeight = int(screenHeight/14)
        btnWidth = int(screenWidth/5)

        home = QPushButton('Главная',self)
        home.resize(btnWidth, btnHeight)
        home.move( 0, int(screenHeight-btnHeight) )
        home.setStyleSheet('background: #BD00FF; color: white; text-transform: uppercase;')
        home.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))

        about = QPushButton('Об отеле',self)
        about.resize(btnWidth, btnHeight)
        about.move( btnWidth, int(screenHeight-btnHeight) )
        about.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase;')
        about.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))

        gallery = QPushButton('Галерея',self)
        gallery.resize(btnWidth, btnHeight)
        gallery.move( btnWidth*2, int(screenHeight-btnHeight) )
        gallery.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase;')
        gallery.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))

        history = QPushButton('История',self)
        history.resize(btnWidth, btnHeight)
        history.move( btnWidth*3, int(screenHeight-btnHeight) )
        history.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase;')
        history.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))

        contact = QPushButton('Контакты',self)
        contact.resize(btnWidth, btnHeight)
        contact.move( btnWidth*4, int(screenHeight-btnHeight) )
        contact.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase;')
        contact.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))