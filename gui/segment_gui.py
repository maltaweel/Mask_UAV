#!/usr/bin/env python
'''
The segmentation GUI used in the application.

Created on Jul 22, 2021

@author: maltaweel
'''
import sys

from PyQt5.QtWidgets import QApplication, QButtonGroup, QLabel, QHBoxLayout, QRadioButton,QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QLineEdit


from gui.gui import Gui
from gui.child_window import ChildWindow
from segmentation import custom_segmentation as segment

'''
The main class for segmenting.

@param Gui-- the GUI superclass.
'''
class SegmentGUI(Gui):
    
    '''
    The initialisation method for the class.
    '''
    def __init__(self):
        super().__init__()
        self.boundBox=False
        self.video=False
        self.classNumber=1
        self.classes=['ruined structure','mounded site','qanat']
        self.segment_directory=''
    
    '''
    Method to make segmentation buttons
    @param app-- the application window
    '''
    def makeSegmentingButtons(self, app):
        
        #the window widget and layout
        window = QWidget()
        self.layout=QVBoxLayout()
        
        #subwidgets that include the segmented image and model file
        widgets=['Segment Image','Model File']
        self.makeWidgetPushButton(widgets)
        
        #the push button for a folder to segment images
        b3=QPushButton('Segment Folder')
        b3.setCheckable(True)
        b3.toggle()
        b3.clicked.connect(self.doActionFolder)
        self.layout.addWidget(b3)
        
        #the input class names for segmentation
        btn = QPushButton('Input Class Name(s)')
        btn.toggle()
        btn.clicked.connect(self.showDialog)
        self.layout.addWidget(btn)
        
        self.boundingBox()
        
        #the start button is set with the window shown
        self.startButton(self.layout)
        window.setLayout(self.layout)
        window.show()
        
        #show the application
        app.exec()

    '''
    The action to open a folder of images.
    '''
    def doActionFolder(self):
        qid = QFileDialog()
        location=str(QFileDialog.getExistingDirectory(None, "Select Segmentation Directory"))
        self.segment_directory=location
    
    '''
    The bounding box choice for images.
    '''   
    def boundingBox(self):
        
        #the button group to be added for bounding boxes and videos
        box_group=QButtonGroup(self)
        video_group=QButtonGroup(self)
        
        #create and add the first (bounding box) radio button
        self.b1 = QRadioButton("Button1")
        self.b1.setChecked(False)
        self.b1.toggled.connect(self.boundSelection)
        
        #a layout for the first radio button (bounding box) and adding the label
        horizontalLayout1 = QHBoxLayout()
        label1 = QLabel("Add bounding box?")
    
        horizontalLayout1.addWidget(label1)
        horizontalLayout1.addWidget(self.b1)
        
        #add button to the box group
        box_group.addButton(self.b1)
        box_group.setExclusive(False)
        
        #now create the second radio button for videos
        self.b2 = QRadioButton("Button2")
        self.b2.setChecked(False)
        self.b2.toggled.connect(self.boundSelection)
      
        #layout ad label adding the buttons and label to the layout
        horizontalLayout2 = QHBoxLayout()
        label2 = QLabel("Segment Video?")
        
        #add to the first layout to make it all one line for the two radio buttons
        horizontalLayout1.addWidget(label2)
        horizontalLayout1.addWidget(self.b2)
        
        self.layout.addLayout(horizontalLayout1)
     
        #add also to the second layout
        horizontalLayout2.addWidget(label2)
        horizontalLayout2.addWidget(self.b2)
        
        #add to the video group
        video_group.addButton(self.b2)
        video_group.setExclusive(False)
        
        #finally add the radio button2 layout to the main window layout
        self.layout.addLayout(horizontalLayout2)
    
    '''
    Determine if a bounding box or video should be added based on radio button selection.
    '''
    def boundSelection(self):
        
        #add bounding box if checked
        if self.b1.isChecked():
            self.boundBox=True
        
        #add video if checked
        if self.b2.isChecked():
            self.video=True
    
    '''
    This will take the classes inputed for segmentation and prepare them for the segmentation
    ''' 
    def showDialog(self):
        #get the input dialog from the user
        text1, ok1=QInputDialog.getText(self, "Get text","Class Name (comma seperated)", QLineEdit.Normal, "")

        #split the classes and set them, including number of classes
        if ok1:
            splits=text1.split(',')
            self.classNumber=len(splits)
            self.classes=splits

    '''
    The first action is to open the image to be segmented.
    '''      
    def doActionOne(self):
        qid = QFileDialog()
        location=str(QFileDialog.getOpenFileName()[0])
        self.image=location
    
    '''
    The second option is to set a model to use for segmentation based on the learned Mask R-CNN model.
    '''
    def doActionTwo(self):
        qid = QFileDialog()
        location=str(QFileDialog.getOpenFileName()[0])
        self.model=location
    
    '''
    The start button selection that will launch segementation and window to show a segmented image.
    '''
    def start(self):
        
        #if the choice is a segmentation of images in a directory, then no window will be opened and the segmented images outputted to 
        #output_segmentation
        if self.segment_directory!='':
            segment.segmentFolder(self.model,self.classNumber,self.classes,self.boundBox,self.segment_directory)  
        
        #this will start the segmentation and open a child window to show a segmented image
        else:
            segment.startSegmenting(self.image, self.model,self.classNumber,self.classes,self.boundBox,self.video)
            self.child_Win = ChildWindow()
            self.child_Win.showWindow(self.image,self.video)

'''
The main to launch locally; this is not currently used but can be by the user.
Note, the user may need to change the format of the modules imported as the directory structure is different.
'''     
def main():
    #launch the application and segmentation GUI window
    app = QApplication([])
    sg=SegmentGUI()
    sg.makeSegmentingButtons(app)
    sys.exit(app.exec_())
'''    
if __name__ == '__main__':
    main()
'''