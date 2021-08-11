#!/usr/bin/env python
'''
This is the training module that can load a training file (training_data)
and receive input from the training gui.

Created on Mar 27, 2021

@author: maltaweel
'''
import os
import csv
from pixellib.custom_train import instance_custom_training

#the path to use and apply in the module
pn=os.path.abspath(__file__)
pn=pn.split("training")[0]

'''
Method to do training of images
@param training_location-- the location of the training imagery data; should have a test folder with .json files.
@param weight_location-- the weight file location for training
@param batch-- the batch number to train
@param classN-- the number of classes
@param network-- the network to do training
@param epoch-- the number of epochs in training
'''
def startTraining(training_location,weight_location, batch, classN,network,epoch):

    #training path location, model directory to output to, and model weight path
    path=training_location
    model_path=os.path.join(pn,'model_dir','mask_rcnn_models')
    weights_path=weight_location

    #training sequence
    train_maskrcnn = instance_custom_training()
    train_maskrcnn.modelConfig(network_backbone = network, num_classes= classN, batch_size = batch)
    train_maskrcnn.load_pretrained_model(weights_path)
    train_maskrcnn.load_dataset(path)
    #train_maskrcnn.visualize_sample()
    train_maskrcnn.train_model(num_epochs = epoch, augmentation=True,  path_trained_models = model_path)

'''
Method to load training file and get relevant data to apply to training.
@return tlocation-- the training folder location
@return wlocation-- the weight file location
@return bn-- the batch number
@return cn-- the class number
@return nModel-- the network model to train with
@return epochs-- the number of epochs to run  
'''
def loadTraining():
    #path to training file
    f=os.path.join(pn,'training_data','training_data.csv')
    
    #open file
    with open(f,'r',encoding="ISO-8859-1") as csvfile:
        reader = csv.DictReader(csvfile)
        
        #read the following information for training:
        #Training Location,Weight Location,Batch Number,Class Number,Network Model,Epochs
        for row in reader:
                    
            #get text
            tlocation=row['Training Location']
            wlocation=row['Weight Location']
            bn=int(row['Batch Number'])
            cn=int(row['Class Number'])
            nModel=row['Network Model']
            epochs=int(row['Epochs'])
            
        #close the file
        csvfile.close()
     
    return tlocation,wlocation,bn,cn,nModel,epochs       

# use this for HPC training or local testing
if __name__ == "controller":
    #first setup paths for training and weight 
    #and other details from input file
    
    tlocation,wlocation,bn,cn,nModel,epochs=loadTraining()
    
    #do the training
    startTraining(tlocation,wlocation,bn,cn,nModel,epochs)
    
    print("Finished") 