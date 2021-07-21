'''
Created on Jul 20, 2021

@author: maltaweel
'''
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class Gui:
    
    def makeWidgetPushButton(self,widgets, app):
        window = QWidget()
        layout = QVBoxLayout()
        
        n=0
        for i in widgets:
            b1=QPushButton(i)
            b1.setCheckable(True)
            b1.toggle()
         #  b1.clicked.connect(lambda:self.whichbtn(self.b1))
            if n==0:
                b1.clicked.connect(self.doActionOne)
            else:
                b1.clicked.connect(self.doActionTwo)
            n+=1
            layout.addWidget(b1)
        
        self.startButton(layout)
        window.setLayout(layout)
        window.show()
        app.exec()
        self.layout=layout
    
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
    
    def start(self):
        print('start')
