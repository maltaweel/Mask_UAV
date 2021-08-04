'''
Created on Jul 26, 2021

@author: maltaweel
'''
import easygui
import gui.train_gui as train
import gui.segment_gui as segment
import labelme.__main__ as labelMe

def main():
    result=easygui.buttonbox('Click on your choice.', 'Options', ('Training', 'Segmentation','Annotation'))
    
    if result=='Training':
        train.main()
    elif result=='Segmentation':
        segment.main()
    else:
        labelMe.main()
    
if __name__ == '__main__':
    main()
        