'''
Created on Jul 20, 2021

@author: maltaweel
'''
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class Gui:
    
    def makeWidgetPushButton(self,widgets):
        app = QApplication([])
        window = QWidget()
        layout = QVBoxLayout()
        
        for i in widgets:
            b1=QPushButton(i)
            b1.setCheckable(True)
            b1.toggle()
            b1.clicked.connect(lambda:self.whichbtn(self.b1))
            b1.clicked.connect(self.doAction)
            layout.addWidget(b1)
        

        window.setLayout(layout)
        window.show()
        app.exec()
        
    def doAction(self):
        print('action')
