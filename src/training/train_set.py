'''
Created on Mar 27, 2021

@author: maltaweel
'''
import os
import pixellib
from pixellib.custom_train import instance_custom_training

pn=os.path.abspath(__file__)
pn=pn.split("src")[0]

def startTraining(training_location,weight_location, batch, classN):

    #path 
    path=training_location
    model_path=os.path.join(pn,'model_dir','mask_rcnn_models')
    weights_path=weight_location

    #training sequence
    train_maskrcnn = instance_custom_training()
    train_maskrcnn.modelConfig(network_backbone = "resnet101", num_classes= classN, batch_size = batch)
    train_maskrcnn.load_pretrained_model(weights_path)
    train_maskrcnn.load_dataset(path)
    #train_maskrcnn.visualize_sample()
    train_maskrcnn.train_model(num_epochs = 300, augmentation=True,  path_trained_models = model_path)

if __name__ == "__main__":
    # use this for HPC training
    #first setup paths for training and weight
    training_location=os.path.join(pn,'structures')
    weight_location=os.path.join(pn,'weights','mask_rcnn_coco.h5')
    
    #do the training
    startTraining(training_location,weight_location,4,3)
    
    print("Finished") 