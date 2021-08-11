'''
This is the child window that is used for the second window showing 
segmented imagery, which derives from the segment_gui module.

Created on Jul 29, 2021

@author: maltaweel
'''
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

import os, sys
 
pn=os.path.abspath(__file__)
pn=pn.split("gui")[0]

'''
The ChildWindow class that takes a QWidget superclass.
@param QWidget-- Superclass used to create a widget class 
that enables a window to be created.
'''
class ChildWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    '''
    Method to initialise the UI, creating relevant layouts and scroll windows.
    '''
    def initUI(self):
        
        #first create relevant layout
        listBox = QVBoxLayout(self)
        self.setLayout(listBox)
        self.listBox=listBox

        #create a scroll area for the window and scroll widget
        scroll = QScrollArea(self)
        listBox.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        self.scroll=scroll
        
        #For the scoll area, create the relevant layout
        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        self.scrollContent=scrollContent
        self.scrollLayout=scrollLayout

        #set the window's title
        self.setWindowTitle('Segmented View')
    
    '''
    Method to dispaly the window showing the segmented image/video.
    @param image-- the file to be segmented if it is a video image.
    @param video-- if the item to segment is a video (true or false).
    '''        
    def showWindow(self,image,video):
    #   self.btn = QPushButton('Open a new window', self)
    #   self.move(self.x() + self.btn.geometry().x() + 1,
    #       self.y() + self.btn.geometry().y() + self.btn.height() + 35)
    #   window = QWidget()
       
        #determine if a video is to be segmented or not
        #if not, then grab the image from segment.jopg in the output_segmentation folder
        if video is False:
            path=os.path.join(pn,'output_segmentation','segmented.jpg')
            
            #create the gui labels and pixmap
            labelImage = QLabel(self)
            pixmap = QPixmap(path)
            
            labelImage.setPixmap(pixmap)
        
            #add the widget to the scroll layout
            self.scrollLayout.addWidget(labelImage)
           
#           self.exec_()
        
        #this sets the video image
        else:
            path=image
            self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
            videoWidget = QVideoWidget()
            self.mediaPlayer.setVideoOutput(videoWidget)
            QMediaContent(QUrl.fromLocalFile(path))
            self.mediaPlayer.play()
            self.scrollLayout.addWidget(videoWidget)
            self.scroll.setWidget(self.scrollContent)
        
        #now set the scroll widget
        self.scroll.setWidget(self.scrollContent)
#           self.addWidget(window)
        
        #give options to close, maximize, and minimize window
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        
        #show the window
        self.showNormal()
        self.show()    
        
'''
Local main to launch, which can be used for testing or if the user wants to use this directly.
'''
def main():
    #create the window and show it
    app = QApplication([])
    sg=ChildWindow()
    sg.showWindow()
'''
if __name__ == 'controller':
    main()
'''