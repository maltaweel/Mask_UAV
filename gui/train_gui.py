#!/usr/bin/env python
'''
Created on Jul 20, 2021

@author: maltaweel
'''
import sys
import os
import csv


from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit, QLabel

from gui.gui import Gui
from training import train_set as train



class TrainGUI (Gui):
    
    def __init__(self):
        super().__init__()
        self.network='resnet101'
        self.epoch=300
        
    def makeTrainingButtons(self, app):
        window = QWidget()
        self.window=window
        self.layout=QVBoxLayout()
        widgets=['Training Library','Weight File']
        self.makeWidgetPushButton(widgets)
        
        btn = QPushButton('Input Class Number and Batch Dialog')
        btn.toggle()
        btn.clicked.connect(self.showDialog)
        self.layout.addWidget(btn)
        
        self.defaultInput()
        
        self.startButton(self.layout)
        self.saveButton()
        
        window.setLayout(self.layout)
        window.show()
#       app.exec()

    def saveButton(self):
        b3=QPushButton('Save')
        b3.setCheckable(True)
        b3.toggle()
        b3.clicked.connect(self.save)
        self.layout.addWidget(b3)
        
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
        train.startTraining(self.training, self.weight,self.batch,self.classN,
                            self.network,self.epoch)
        
    def save(self):
        pn=os.path.abspath(__file__)
        pn=pn.split("gui")[0]
        
        fieldnames=['Training Location','Weight Location','Batch Number','Class Number',
                    'Network Model','Epochs']
        
        fileOutput=os.path.join(pn,"training_data",'training_data.csv')
        with open(fileOutput, 'w') as csvf:
            
            #write the output
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            writer.writerow({'Training Location': str(self.training),
            'Weight Location':str(self.weight),'Batch Number':str(self.batch),
            'Class Number':str(self.classN),'Network Model':str(self.network),
            'Epochs':str(self.epoch)})
            
            csvf.close()
        
def main():

    app = QApplication([])
    tg=TrainGUI()
    tg.makeTrainingButtons(app)
    sys.exit(app.exec_())
'''    
if __name__ == '__main__':
    main()
'''
        