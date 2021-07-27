'''
Created on Jul 26, 2021

@author: maltaweel
'''
import easygui
import train_gui as train
import segment_gui as segment

def main():
    result=easygui.buttonbox('Click on your choice.', 'Options', ('Training', 'Segmentation'))
    
    if result=='Training':
        train.main()
    elif result=='Segmentation':
        segment.main()
    
if __name__ == '__main__':
    main()
        