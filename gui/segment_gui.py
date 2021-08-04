#!/usr/bin/env python
'''
Created on Jul 22, 2021

@author: maltaweel
'''
import sys

from PyQt5.QtWidgets import QApplication, QButtonGroup, QLabel, QHBoxLayout, QRadioButton,QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit


from gui.gui import Gui
from gui.child_window import ChildWindow
from segmentation import custom_segmentation as segment


class SegmentGUI(Gui):
    
    def __init__(self):
        super().__init__()
        self.boundBox=False
        self.video=False
        self.classNumber=1
        self.classes=['ruined structure']
        self.segment_directory=''
        
    def makeSegmentingButtons(self, app):
        window = QWidget()
        self.layout=QVBoxLayout()
        widgets=['Segment Image','Model Weight File']
        self.makeWidgetPushButton(widgets)
        
        b3=QPushButton('Segment Folder')
        b3.setCheckable(True)
        b3.toggle()
        b3.clicked.connect(self.doActionFolder)
        self.layout.addWidget(b3)
        
        btn = QPushButton('Input Class Name(s)')
        btn.toggle()
        btn.clicked.connect(self.showDialog)
        self.layout.addWidget(btn)
        
        self.boundingBox()
        
        self.startButton(self.layout)
        window.setLayout(self.layout)
        window.show()
        app.exec()

    def doActionFolder(self):
        qid = QFileDialog()
        location=str(QFileDialog.getExistingDirectory(None, "Select Segmentation Directory"))
        self.segment_directory=location
        
    def boundingBox(self):
        
        box_group=QButtonGroup(self)
        video_group=QButtonGroup(self)
        
        self.b1 = QRadioButton("Button1")
        self.b1.setChecked(False)
        self.b1.toggled.connect(self.boundSelection)
      
        horizontalLayout1 = QHBoxLayout()
      
        label1 = QLabel("Add bounding box?")
     
        horizontalLayout1.addWidget(label1)
        horizontalLayout1.addWidget(self.b1)
        
        box_group.addButton(self.b1)
        box_group.setExclusive(False)
        
        self.b2 = QRadioButton("Button2")
        self.b2.setChecked(False)
        self.b2.toggled.connect(self.boundSelection)
      
        horizontalLayout2 = QHBoxLayout()
      
        label2 = QLabel("Segment Video?")
        
        horizontalLayout1.addWidget(label2)
        horizontalLayout1.addWidget(self.b2)
        
        self.layout.addLayout(horizontalLayout1)
     
        horizontalLayout2.addWidget(label2)
        horizontalLayout2.addWidget(self.b2)
        
        video_group.addButton(self.b2)
        video_group.setExclusive(False)
        
        self.layout.addLayout(horizontalLayout2)
    
    def boundSelection(self):
        if self.b1.isChecked():
            self.boundBox=True
            
        if self.b2.isChecked():
            self.video=True
        
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
        self.model=location
    
    def start(self):
        if self.segment_directory!='':
            segment.segmentFolder(self.model,self.classNumber,self.classes,self.boundBox,self.segment_directory)  
        
        else:
            segment.startSegmenting(self.image, self.model,self.classNumber,self.classes,self.boundBox,self.video)
            self.child_Win = ChildWindow()
            self.child_Win.showWindow()
       
def main():

    app = QApplication([])
    sg=SegmentGUI()
    sg.makeSegmentingButtons(app)
    sys.exit(app.exec_())
'''    
if __name__ == '__main__':
    main()
'''