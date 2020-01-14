import sys
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.sip import *
import gallery

class AboutWindow(QWidget):
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
        about.setStyleSheet('background: #BD00FF; color: white; text-transform: uppercase;')
        about.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))

        gallery = QPushButton('Галерея',self)
        gallery.resize(btnWidth, btnHeight)
        gallery.move( btnWidth*2, int(screenHeight-btnHeight) )
        gallery.setStyleSheet('background: #6D0094; color: white; text-transform: uppercase;')
        gallery.setFont(QtGui.QFont('font/Open_Sans/OpenSans-regular.ttf', 12))
        gallery.clicked.connect(self.gallery_click)

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

        about_image = QLabel('Image is or was here', self)
        about_image.resize(screenWidth, screenHeight/3)
        about_image.setStyleSheet('background: white')
        about_image.setPixmap(QtGui.QPixmap('images/image_01.jpg'))
        about_image.setScaledContents(False)

        about_text = QLabel(self)
        about_text.resize( screenWidth, int(screenHeight-about_image.height()-btnHeight) )
        about_text.move(0, about_image.height())
        about_text.setStyleSheet('color: white')
        about_text.setWordWrap(True)
        about_text.setFont(QtGui.QFont('font/Open_Sans/OpenSans-Regular.ttf', 13))
        #about_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        about_text.setMargin(btnHeight/10)
        about_text.setText('''
        	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam iure libero maxime omnis, iusto rerum perspiciatis! Est natus eligendi tempora, omnis deleniti, laudantium aperiam distinctio voluptas dolor vitae minima doloremque a iusto perspiciatis temporibus tenetur possimus, vel! Consequatur aut eaque quam velit magnam cumque! Accusamus, molestias voluptatum ullam consectetur earum hic odit beatae magnam iusto eius nam porro error ratione voluptatem velit aperiam tempore, totam magni nostrum repellendus distinctio! In nulla error cumque harum maxime odio quae debitis aliquam asperiores facilis praesentium, iste qui earum voluptatum doloremque maiores eligendi nostrum sed, non distinctio sunt. Harum nisi praesentium eligendi iste reiciendis!
        	
        	1. Lorem ipsum dolor.
        	2. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam, blanditiis.
        	3. Lorem ipsum 854 sq.m at 6 floors  Lorem ipsum dolor sit.
        	4. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iste, quia.
        	
        	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus vel earum deserunt adipisci aperiam quidem, reiciendis tempore illo delectus eveniet. Quis modi dicta minus cum praesentium ut quisquam reiciendis harum eos, incidunt fuga quasi, repudiandae hic aliquid deserunt quibusdam eligendi officia? Maxime nisi cum sequi, laboriosam aliquam modi placeat, eaque laudantium inventore unde obcaecati totam aliquid. Esse explicabo totam inventore doloremque quae ipsa maiores eveniet eaque. Nostrum corrupti perferendis tempore suscipit eum veritatis sapiente inventore illo, perspiciatis quod porro rem illum esse magnam quia recusandae eaque. Facilis voluptates pariatur nam a id consectetur placeat in ratione? Quos ea architecto tempore possimus mollitia omnis est at illum quam eveniet accusamus excepturi, laudantium? Asperiores quo facere illum vero nisi. Excepturi, non totam quos magni! Dicta officia nostrum voluptatem dolorem aspernatur deleniti atque error in ipsum repellendus tenetur voluptate quisquam doloremque modi quo cum inventore illum consequatur, nemo iusto! Vero vel dicta vitae.''')

        self.setStyleSheet('background: #210020')
        self.showFullScreen()

    def gallery_click(self):
        self.w = gallery.GalleryWindow()
        self.w.showFullScreen()
        self.close()