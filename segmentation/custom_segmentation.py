#!/usr/bin/env python
'''
Created on Apr 2, 2021

@author: maltaweel
'''
import os
import csv
import pixellib
from pixellib.instance import custom_segmentation
from pixellib.instance import instance_segmentation


pn=os.path.abspath(__file__)
pn=pn.split("segmentation")[0]
addClasses=[]
seg_out=os.path.join(pn,'output_segmentation','segment_data.csv')

def startSegmenting(image,model,classNumber,classes, boundBox, video):
    #path info
    path=image
    #model_path=os.path.join(pn,'model_dir')
    weights_path=model
    output_segmentation=os.path.join(pn,'output_segmentation','segmented.jpg')
    
    #segment video
    if video==True:
        processVideo(image,model,boundBox)
        
    #segment image
    segment_image = custom_segmentation()
    
    addClasses.append("BG")
    for i in classes:
        addClasses.append(i.strip())
        
    segment_image.inferConfig(num_classes= classNumber, class_names=addClasses)
    segment_image.load_model(weights_path)
    segmask, output=segment_image.segmentImage(path, show_bboxes=boundBox, output_image_name=output_segmentation,
            extract_segmented_objects= True, save_extracted_objects=False)

    outputData(segmask,seg_out,output)

def processVideo(image,model,boundBox):
    output_segmentation=os.path.join(pn,'output_segmentation','segmented.mp4')
            
    segment_video = instance_segmentation()
    segment_video.load_model(model)
    segment_video.process_video(image, show_bboxes=boundBox,  extract_segmented_objects=True,
                                save_extracted_objects=True, frames_per_second= 5,  output_video_name=output_segmentation)

def segmentFolder(model,classNumber,classes,boundBox,input_folder):
    
    addClasses.append("BG")
    for i in classes:
        addClasses.append(i.strip())
    
    output_segmentation=os.path.join(pn,'output_segmentation')
                                     
    ins = custom_segmentation()
    ins.inferConfig(num_classes=classNumber, class_names=addClasses)
    ins.load_model(model)
    segmask, output=ins.segmentBatch(input_folder,  show_bboxes=boundBox, output_folder_name = output_segmentation)
    outputFolderData(segmask, seg_out)

def outputFolderData(segmask,seg_out):
    fieldnames=['id','a','b','c','d','score']
    
    with open(seg_out, 'w') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)

        writer.writeheader() 
        for i in segmask:
            scores=i['scores']
            # masks=segmask['masks']
            rois=i['rois']
            ids=i['class_ids']

            #write the output
            for ii in range(0,len(rois)):
                roi=rois[ii]
                st=ids[ii]
                item=addClasses[st]
                writer.writerow({'id':str(item),'a': str(roi[0]),'b':str(roi[1]),'c':str(roi[2]),'d':str(roi[3]),
                         'score':str(scores[ii])})
        
        
def outputData(segmask,seg_out, output):
#   res = segmask["extracted_objects"]
    scores=segmask['scores']
#   masks=segmask['masks']
    rois=segmask['rois']
    ids=segmask['class_ids']

    fieldnames=['id','a','b','c','d','score']
    
    print(output.shape)
    with open(seg_out, 'w') as csvf:
        #write the output
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)

        writer.writeheader() 

        for i in range(0,len(rois)):
            roi=rois[i]
            st=ids[i]
            item=addClasses[st]
            writer.writerow({'id':str(item),'a': str(roi[0]),'b':str(roi[1]),'c':str(roi[2]),'d':str(roi[3]),
                         'score':str(scores[i])})
        
if __name__ == "controller":
    weight_location=os.path.join(pn,'weights','mask_rcnn_model.003-3.374101.h5')
    images_path=os.path.join(pn,'structures','test')
    
    #image=os.path.join(pn,'structures','test','DJI_0335.JPG')
    
    #startSegmenting(image,weight_location,3,['qanat','mounded sites','ruined structure'],True, False)
    
    
    segmentFolder(weight_location,3,['mounded sites','qanat','ruined structure'],True,images_path)
