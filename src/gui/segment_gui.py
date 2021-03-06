#!/usr/bin/env python
'''
Created on Jul 22, 2021

@author: maltaweel
'''
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QRadioButton,QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit

from gui import Gui
from segmentation import custom_segmentation as segment


class SegmentGUI(Gui):
    
    def __init__(self):
        super().__init__()
        self.boundBox=False
        
    def makeSegmentingButtons(self, app):
        window = QWidget()
        self.layout=QVBoxLayout()
        widgets=['Segment Image','Weight File']
        self.makeWidgetPushButton(widgets)
        
        btn = QPushButton('Input Class Name(s)')
        btn.toggle()
        btn.clicked.connect(self.showDialog)
        self.layout.addWidget(btn)
        
        self.boundingBox()
        
        self.startButton(self.layout)
        window.setLayout(self.layout)
        window.show()
        app.exec()

    def boundingBox(self):
        self.b1 = QRadioButton("Button1")
        self.b1.setChecked(False)
        self.b1.toggled.connect(self.boundSelection)
      
        horizontalLayout1 = QHBoxLayout()
      
        label1 = QLabel("Add bounding box?")
     
        horizontalLayout1.addWidget(label1)
        horizontalLayout1.addWidget(self.b1)
        
        self.layout.addLayout(horizontalLayout1)
    
    def boundSelection(self):
        if self.b1.isChecked():
            self.boundBox=True
        
    def showDialog(self):
        text1, ok1=QInputDialog.getText(self, "Get text","Class Name (comma seperated)", QLineEdit.Normal, "")

        
        if ok1:
            splits=text1.split(',')
            self.classNumber=len(splits)
            self.classes=splits

            
    def doActionOne(self):
        qid = QFileDialog()
        location=str(QFileDialog.getOpenFileName()[0])
        self.image=location
    
    def doActionTwo(self):
        qid = QFileDialog()
        location=str(QFileDialog.getOpenFileName()[0])
        self.weight=location
    
    def start(self):
        segment.startSegmenting(self.image, self.weight,self.classNumber,self.classes,self.boundBox)
        
        
def main():

    app = QApplication([])
    sg=SegmentGUI()
    sg.makeSegmentingButtons(app)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()