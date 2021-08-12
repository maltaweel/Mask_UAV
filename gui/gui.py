#!/usr/bin/env python
'''
The main superclass GUI used to create the training and segment GUIs.


Created on Jul 20, 2021

@author: maltaweel
'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

'''
The main GUI class which uses a QMainWindow from PyQt5.
@param QMainWindow- the super class used to create a main window
'''
class Gui (QMainWindow):
    
    '''
    The initialisation method that simply class the superclass init.
    '''
    def __init__(self):
        super().__init__()
    
    '''
    Method to make widget push buttons to select options.
    @param widgets-- the widget options to make.
    '''
    def makeWidgetPushButton(self,widgets):
    
        layout = self.layout
        
        n=0
        #iterate through widgets
        for i in widgets:
            #create push buttons
            b1=QPushButton(i)
            b1.setCheckable(True)
            b1.toggle()
          
            #setup actions
            if n==0:
                b1.clicked.connect(self.doActionOne)
            else:
                b1.clicked.connect(self.doActionTwo)
            n+=1
            #add widget to layout
            layout.addWidget(b1)
        
    '''
    The default start button.
    @param layout-- layout used to add start button widget.
    '''
    def startButton(self,layout):
        
        #create push button, make it checkable, set action method, and add
        #to layout
        b1=QPushButton('Start')
        b1.setCheckable(True)
        b1.toggle()
        b1.clicked.connect(self.start)
        layout.addWidget(b1)
    
    '''
    The first action method from a push button option.
    '''       
    def doActionOne(self):
        print('action')
      
    '''
    The section action method from a push button option.
    '''   
    def doActionTwo(self):
        print('action')
    
    '''
    The radio selection (true or false).
    
    @return true or false.
    ''' 
    def boundSelection(self):
        if self.b1.isChecked():
            return True
    
    '''
    Method to start the action. Should be locally implemented for training
    or segmentation.
    '''
    def start(self):
        print('start')
