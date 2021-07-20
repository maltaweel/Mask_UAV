'''
Created on Jul 20, 2021

@author: maltaweel
'''
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

from gui.gui import Gui




class TrainGUI (Gui):
    
    def makeTrainingButtons(self):
        
        widgets=['Training Library','Weight File']
        self.makeWidgetPushButton(widgets)
        
    def doAction(self):
        qid = QFileDialog()
        filename=QFileDialog.getOpenFileName()
        
        print('stop')
    
def main():

    app = QApplication(sys.argv)
    tg=TrainGUI
    tg.makeTrainingButtons()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

        