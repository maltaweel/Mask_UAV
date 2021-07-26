#!/usr/bin/env python
'''
Created on Jul 20, 2021

@author: maltaweel
'''
import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit, QLabel

from gui import Gui
from training import train_set as train



class TrainGUI (Gui):
    
    def __init__(self):
        super().__init__()
        self.network='resnet101'
        self.epoch=300
        
    def makeTrainingButtons(self, app):
        window = QWidget()
        self.layout=QVBoxLayout()
        widgets=['Training Library','Weight File']
        self.makeWidgetPushButton(widgets,app)
        
        btn = QPushButton('Input Classes and Batch Dialog')
        btn.toggle()
        btn.clicked.connect(self.showDialog)
        self.layout.addWidget(btn)
        
        self.defaultInput()
        
        self.startButton(self.layout)
        window.setLayout(self.layout)
        window.show()
        app.exec()

    def defaultInput(self):
        
        horizontalLayout1 = QHBoxLayout()
        horizontalLayout2 = QHBoxLayout()
        
        label1 = QLabel("Network Model:")
        label2 = QLabel("Epoch Runs:")
        
        self.e = QLineEdit("resnet101")
        self.e.setReadOnly(False)
        self.e.editingFinished.connect(self.enterPress)
        horizontalLayout1.addWidget(label1)
        horizontalLayout1.addWidget(self.e)
        
        self.layout.addLayout(horizontalLayout1)
        
        self.e2 = QLineEdit("300")
        self.e2.setReadOnly(False)
        self.e2.editingFinished.connect(self.enterPress)
                
        horizontalLayout2.addWidget(label2)
        horizontalLayout2.addWidget(self.e2)
        self.layout.addLayout(horizontalLayout2)
        
        
    def enterPress(self):
        self.network=self.e.text
        self.epoch=int(self.e2.text)
        
    def showDialog(self):
        text1, ok1=QInputDialog.getText(self, "Get text","Batch Size", QLineEdit.Normal, "")
        text2, ok2=QInputDialog.getText(self, "Get text","Class Number", QLineEdit.Normal, "")
        
        if ok1:
            self.batch=int(text1)
        if ok2:
            self.classN=int(text2)
            
    def doActionOne(self):
        qid = QFileDialog()
        location=str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.training=location
    
    def doActionTwo(self):
        qid = QFileDialog()
        location=str(QFileDialog.getOpenFileName()[0])
        self.weight=location
    
    def start(self):
        print(self.network)
        print(self.epoch)
        train.startTraining(self.training, self.weight,self.batch,self.classN,
                            self.network,self.epoch)
        
        
def main():

    app = QApplication([])
    tg=TrainGUI()
    tg.makeTrainingButtons(app)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

        