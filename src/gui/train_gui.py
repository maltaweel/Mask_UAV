'''
Created on Jul 20, 2021

@author: maltaweel
'''
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

from gui import Gui
from training import train_set as train



class TrainGUI (Gui):
    
    def makeTrainingButtons(self, app):
        
        widgets=['Training Library','Weight File']
        self.makeWidgetPushButton(widgets,app)
        
    def doActionOne(self):
        qid = QFileDialog()
        location=str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.training=location
    
    def doActionTwo(self):
        qid = QFileDialog()
        location=str(QFileDialog.getOpenFileName()[0])
        self.weight=location
    
    def start(self):
        train.startTraining(self.training, self.weight)
        
        
def main():

    app = QApplication([])
    tg=TrainGUI()
    tg.makeTrainingButtons(app)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

        