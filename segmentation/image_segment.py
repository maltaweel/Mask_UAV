'''
This is just to test the segmentation capabilities in PixelLib. 
Users can modify this to test or simply ignore this module.

Created on Mar 27, 2021

@author: maltaweel
'''
import os
from pixellib.instance import instance_segmentation


#path  for data files
pn=os.path.abspath(__file__)
pn=pn.split("src")[0]
path=os.path.join(pn,'structures','test','50741238347_32422cb32e_o.jpg')
model_path=os.path.join(pn,'model_dir')
weights_path=os.path.join(pn,'weights','mask_rcnn_model.001-1.412928.h5')
output_segmentation=os.path.join(pn,'output_segmentation','segmented.jpg')

#segmentation setup, configuration, and implementation
instance_seg = instance_segmentation()
instance_seg.load_model(weights_path)
instance_seg.load_model(weights_path, by_name=True, exclude=[ "mrcnn_class_logits", "mrcnn_bbox_fc", "mrcnn_bbox", "mrcnn_mask"])
instance_seg.segmentImage(path, show_bboxes = True, output_image_name = output_segmentation)
