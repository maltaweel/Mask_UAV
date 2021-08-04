#!/usr/bin/env python
'''
Created on Jul 20, 2021

@author: maltaweel
'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton


class Gui (QMainWindow):
    def __init__(self):
        super().__init__()
    
    def makeWidgetPushButton(self,widgets):
    
        layout = self.layout
        
        n=0
        for i in widgets:
            b1=QPushButton(i)
            b1.setCheckable(True)
            b1.toggle()
          
            if n==0:
                b1.clicked.connect(self.doActionOne)
            else:
                b1.clicked.connect(self.doActionTwo)
            n+=1
            layout.addWidget(b1)
        
    
    def startButton(self,layout):
        b1=QPushButton('Start')
        b1.setCheckable(True)
        b1.toggle()
        b1.clicked.connect(self.start)
        layout.addWidget(b1)
            
    def doActionOne(self):
        print('action')
        
    def doActionTwo(self):
        print('action')
    
    def boundSelection(self):
        if self.b1.isChecked():
            return True
    
    def start(self):
        print('start')
