#!/usr/bin/env python
'''
Created on Mar 27, 2021

@author: maltaweel
'''
import os
import csv
from pixellib.custom_train import instance_custom_training

pn=os.path.abspath(__file__)
pn=pn.split("training")[0]

def startTraining(training_location,weight_location, batch, classN,network,epoch):

    #path 
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

def loadTraining():
        
    f=os.path.join(pn,'training_data','training_data.csv')
    
    #open files
    with open(f,'r',encoding="ISO-8859-1") as csvfile:
        reader = csv.DictReader(csvfile)
        
        #Training Location,Weight Location,Batch Number,Class Number,Network Model,Epochs
        for row in reader:
                    
            #get text
            tlocation=row['Training Location']
            wlocation=row['Weight Location']
            bn=int(row['Batch Number'])
            cn=int(row['Class Number'])
            nModel=row['Network Model']
            epochs=int(row['Epochs'])
        
        csvfile.close()
     
    return tlocation,wlocation,bn,cn,nModel,epochs       

if __name__ == "__main__":
    # use this for HPC training
    #first setup paths for training and weight 
    #and other details from input file
    
    tlocation,wlocation,bn,cn,nModel,epochs=loadTraining()
    
    #do the training
    startTraining(tlocation,wlocation,bn,cn,nModel,epochs)
    
    print("Finished") 