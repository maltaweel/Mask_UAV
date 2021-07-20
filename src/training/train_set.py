'''
Created on Mar 27, 2021

@author: maltaweel
'''
import os
import pixellib
from pixellib.custom_train import instance_custom_training

#path 
pn=os.path.abspath(__file__)
pn=pn.split("src")[0]
path=os.path.join(pn,'structures')
model_path=os.path.join(pn,'model_dir','mask_rcnn_models')
weights_path=os.path.join(pn,'weights','mask_rcnn_coco.h5')

#training sequence
train_maskrcnn = instance_custom_training()
train_maskrcnn.modelConfig(network_backbone = "resnet101", num_classes= 1, batch_size = 2)
train_maskrcnn.load_pretrained_model(weights_path)
train_maskrcnn.load_dataset(path)
#train_maskrcnn.visualize_sample()
train_maskrcnn.train_model(num_epochs = 300, augmentation=True,  path_trained_models = model_path)
