'''
Created on Jul 29, 2021

@author: maltaweel
'''
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os, sys
 
pn=os.path.abspath(__file__)
pn=pn.split("gui")[0]

class ChildWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        listBox = QVBoxLayout(self)
        self.setLayout(listBox)
        self.listBox=listBox

        scroll = QScrollArea(self)
        listBox.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        self.scroll=scroll
        
        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        self.scrollContent=scrollContent
        self.scrollLayout=scrollLayout
     #   self.setGeometry(50, 50, 1800, 950)
      #  self.setFixedSize(self.size())
        self.setWindowTitle('Segmented Image View')

        
    def doScroll(self):
        qsa=QScrollArea(self)
        qsa.setGeometry(self.geometry())
        qsa.setWidget(self)
        qsa.setWidgetResizable(True)
        qsa.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        qsa.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.addWidget(qsa)
        qsa.show()
                
    def showWindow(self):
    #   self.btn = QPushButton('Open a new window', self)
    #   self.move(self.x() + self.btn.geometry().x() + 1,
    #       self.y() + self.btn.geometry().y() + self.btn.height() + 35)
    #   window = QWidget()
       
        labelImage = QLabel(self)
        path=os.path.join(pn,'output_segmentation','segmented.jpg')
        pixmap = QPixmap(path)
    #   pixmap.scaled(1000, 1000, Qt.KeepAspectRatio)
        labelImage.setPixmap(pixmap)
        
        self.scrollLayout.addWidget(labelImage)
        self.scroll.setWidget(self.scrollContent)
     #  self.addWidget(window)
        
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        
        self.showNormal()
        self.show()
 #      self.exec_()

def main():
    app = QApplication([])
    sg=ChildWindow()
    sg.showWindow()
'''
if __name__ == '__main__':
    main()
'''