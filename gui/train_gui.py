#!/usr/bin/env python
'''
This is the training window GUI. Users select what folder of images to train
and then can either save the choices or launch training to commence. 

Created on Jul 20, 2021

@author: maltaweel
'''
import sys
import os
import csv


from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit, QLabel

from gui.gui import Gui
from training import train_set as train


'''
The TraingGUI class builds from the Gui superclass.
@param Gui- the Gui superclass to build the GUI window.
'''
class TrainGUI (Gui):
    
    '''
    Initialise the class with defaults set.
    '''
    def __init__(self):
        super().__init__()
        self.network='resnet101'
        self.epoch=300
    
    '''
    The training buttons created for the application, including the 
    training library to select and the weight file to use in training.
    
    @param app- the main application
    '''
    def makeTrainingButtons(self, app):
        #create the window widget for options
        window = QWidget()
        self.window=window
        self.layout=QVBoxLayout()
        #user choices are the training library and weight file to select
        widgets=['Training Library','Weight File']
        self.makeWidgetPushButton(widgets)
        
        #users then can select the number of classes and batch number during training
        btn = QPushButton('Input Class Number and Batch Number')
        btn.toggle()
        btn.clicked.connect(self.showDialog)
        self.layout.addWidget(btn)
        
        #add more user input options
        self.defaultInput()
        
        #now create the start and save button
        self.startButton(self.layout)
        self.saveButton()
        
        #set the layout and show the window
        window.setLayout(self.layout)
        window.show()
#       app.exec()
    
    '''
    The save button to save the run options.
    '''
    def saveButton(self):
        #simply create a push button to save the run and create the action.
        b3=QPushButton('Save')
        b3.setCheckable(True)
        b3.toggle()
        b3.clicked.connect(self.save)
        self.layout.addWidget(b3)
    
    '''
    The method to set the network model choice and epoch runs to select for the user.
    '''   
    def defaultInput(self):
        
        #the layouts used for the additional options
        horizontalLayout1 = QHBoxLayout()
        horizontalLayout2 = QHBoxLayout()
        
        #the options are network model and epoch runs
        label1 = QLabel("Network Model:")
        label2 = QLabel("Epoch Runs:")
        
        #this sets the default network (resnet101) but it is editable
        self.e = QLineEdit("resnet101")
        self.e.setReadOnly(False)
        self.e.editingFinished.connect(self.enterPress)
        horizontalLayout1.addWidget(label1)
        horizontalLayout1.addWidget(self.e)
        
        #the network choice layout added to the main layout
        self.layout.addLayout(horizontalLayout1)
        
        #epoch runs set to 300 for default
        self.e2 = QLineEdit("300")
        self.e2.setReadOnly(False)
        self.e2.editingFinished.connect(self.enterPress)
        
        #the selection is added to the widget's second layout    
        horizontalLayout2.addWidget(label2)
        horizontalLayout2.addWidget(self.e2)
        self.layout.addLayout(horizontalLayout2)
        
    '''
    This is the action that saves the network and epoch choices to the class.
    '''   
    def enterPress(self):
        self.network=self.e.text
        self.epoch=int(self.e2.text)
    
    '''
    The options for the batch size and class number are taken and set to the class.
    '''   
    def showDialog(self):
        #get options for batch size and class number
        text1, ok1=QInputDialog.getText(self, "Get text","Batch Size", QLineEdit.Normal, "")
        text2, ok2=QInputDialog.getText(self, "Get text","Class Number", QLineEdit.Normal, "")
        
        #add batch number
        if ok1:
            self.batch=int(text1)
        #add number of classes
        if ok2:
            self.classN=int(text2)
    
    '''
    Directory choice made for training with the training location set to the class.
    '''       
    def doActionOne(self):
        #dialog sets the training folder to the class.
        qid = QFileDialog()
        location=str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.training=location
    
    '''
    This sets the location of the training file to the class.
    '''
    def doActionTwo(self):
        #dialog sets the training file to class.
        qid = QFileDialog()
        location=str(QFileDialog.getOpenFileName()[0])
        self.weight=location
    
    '''
    This starts the training if the choice to start is selected.
    '''
    def start(self):
        train.startTraining(self.training, self.weight,self.batch,self.classN,
                            self.network,self.epoch)
    '''
    This is the option to save the training data to a file. 
    '''
    def save(self):
        #get the local path lto save file to
        pn=os.path.abspath(__file__)
        pn=pn.split("gui")[0]
        
        #fieldnames to save to training file
        fieldnames=['Training Location','Weight Location','Batch Number','Class Number',
                    'Network Model','Epochs']
        
        #set the file output path
        fileOutput=os.path.join(pn,"training_data",'training_data.csv')
        with open(fileOutput, 'w') as csvf:
            
            #make the writer
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)
            
            #write the header
            writer.writeheader()
            
            #write the output that has user choices
            writer.writerow({'Training Location': str(self.training),
            'Weight Location':str(self.weight),'Batch Number':str(self.batch),
            'Class Number':str(self.classN),'Network Model':str(self.network),
            'Epochs':str(self.epoch)})
            
            #close the file
            csvf.close()
'''
The main to launch the application; not used but users can modify but may need to 
update library locations for modules referenced. 
'''     
def main():

    app = QApplication([])
    tg=TrainGUI()
    tg.makeTrainingButtons(app)
    sys.exit(app.exec_())
'''    
if __name__ == 'controller':
    main()
'''
        