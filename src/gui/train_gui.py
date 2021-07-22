'''
Created on Jul 20, 2021

@author: maltaweel
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit

from gui import Gui
from training import train_set as train



class TrainGUI (Gui):
    
    def makeTrainingButtons(self, app):
        window = QWidget()
        self.layout=QVBoxLayout()
        widgets=['Training Library','Weight File']
        self.makeWidgetPushButton(widgets,app)
        
        btn = QPushButton('Input Classes and Batch Dialog')
        btn.toggle()
        btn.clicked.connect(self.showDialog)
        self.layout.addWidget(btn)
        
        self.startButton(self.layout)
        window.setLayout(self.layout)
        window.show()
        app.exec()

        
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
        train.startTraining(self.training, self.weight,self.batch,self.classN)
        
        
def main():

    app = QApplication([])
    tg=TrainGUI()
    tg.makeTrainingButtons(app)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

        