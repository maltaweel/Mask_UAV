'''
Created on Jul 26, 2021

@author: maltaweel
'''
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QRadioButton,QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit
from train_gui import TrainGUI
from segment_gui import SegmentGUI

from gui import Gui

class ControllerGUI (Gui):
    
    def __init__(self):
        super().__init__()
        self.boundBox=False
        
    def controlButton(self, app):
        window = QWidget()
        self.layout=QVBoxLayout()
        
        
        self.b1 = QRadioButton("Button 1")
        self.b1.setChecked(False)
        self.b1.toggled.connect(self.boundSelection)
        horizontalLayout1 = QHBoxLayout()
        label1 = QLabel("Run Training?")
        horizontalLayout1.addWidget(label1)
        horizontalLayout1.addWidget(self.b1)
        
        self.b2 = QRadioButton("Button 2")
        self.b2.setChecked(False)
        self.b2.toggled.connect(self.boundSelection)
        horizontalLayout2 = QHBoxLayout()
        label2 = QLabel("Run Segmentation?")
        horizontalLayout2.addWidget(label2)
        horizontalLayout2.addWidget(self.b2)
        
        self.layout.addLayout(horizontalLayout1)
        self.layout.addLayout(horizontalLayout2)
        
        self.startButton(self.layout)
       
        window.setLayout(self.layout)
        window.show()
        app.exec()
        
    def boundSelection(self):
        if self.b1.isChecked():
            self.isTraining=True
            
        if self.b2.isChecked():
            self.isSegmenting=True

    def start(self):
        if self.isTraining is True:
            tg=TrainGUI()
            tg.makeTrainingButtons(self.app)
            
        if self.isSegmenting is True:
            sg=SegmentGUI
            sg.makeSegmentingButtons(self.app)
            

def main():

    app = QApplication([])
    cg=ControllerGUI()
    cg.app=app
    cg.controlButton(app)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
        