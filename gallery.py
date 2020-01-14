import sys
import os

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.sip import *
import about

        
imglink = []

class GalleryWindow(QWidget):
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
        home.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase;')
        home.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))

        about = QPushButton('Об отеле',self)
        about.resize(btnWidth, btnHeight)
        about.move( btnWidth, int(screenHeight-btnHeight) )
        about.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase;')
        about.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))
        about.clicked.connect(self.welcome)

        gallery = QPushButton('Галерея',self)
        gallery.resize(btnWidth, btnHeight)
        gallery.move( btnWidth*2, int(screenHeight-btnHeight) )
        gallery.setStyleSheet('background: #BD00FF; color: white; text-transform: uppercase;')
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

        imagelist = QListWidget(self)

        path = "images/"
        img_list = os.listdir(path)
        for imagin in img_list:
        	img = QListWidgetItem()
        	img.setIcon( QtGui.QIcon(QtGui.QPixmap(path+imagin)) )
        	imagelist.addItem(img)
        	imglink.extend([str(path+imagin)])

        imagelist.setGeometry(QtCore.QRect(0,0,300,int(screenHeight-btnHeight)))
        imagelist.setIconSize( QtCore.QSize(int(imagelist.width()),200))
        imagelist.setStyleSheet('color: white;')
        imagelist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        imagelist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        imagelist.setViewMode(QListWidget.IconMode)
        imagelist.setMovement(QListWidget.Static)
        imagelist.setFlow(QListWidget.TopToBottom)
        imagelist.setWrapping(False)
        imagelist.itemClicked.connect(self.item_click)

        self.image = QLabel(self)
        self.image.setGeometry(300,0,int(screenWidth),int(screenHeight-btnHeight))
        self.image.setPixmap(QtGui.QPixmap('images/image_01.jpg'))
        self.image.setScaledContents(True)

        self.setStyleSheet('background: #210020')
        self.showFullScreen()

    def item_click(self, item):
        clckimg = item.listWidget()
        curimg = clckimg.currentRow()
        self.image.setPixmap(QtGui.QPixmap(str(imglink[curimg])))
    
    def welcome(self):
        self.w = about.AboutWindow()
        self.w.showFullScreen()
        self.close()