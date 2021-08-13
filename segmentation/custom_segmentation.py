#!/usr/bin/env python
'''
Class used to segment images.

Created on Apr 2, 2021

@author: maltaweel
'''
import os
import csv
import pixellib
from pixellib.instance import custom_segmentation
from pixellib.instance import instance_segmentation

#this is local pathway data set and the output segment_data class set
pn=os.path.abspath(__file__)
pn=pn.split("segmentation")[0]
addClasses=[]  #classes to segment
seg_out=os.path.join(pn,'output_segmentation','segment_data.csv')

'''
Method to segment image data.
@param image-- the image to segment.
@param model-- the Mask R-CNN model used to segment.
@param classNumber-- The number of classes to segment
@param classes--  The classes to segment (e.g., ruined structure)
@param boundBox-- Use a bounding box or no?
@param video--  Is the file a video file?
'''
def startSegmenting(image,model,classNumber,classes, boundBox, video):
    #path info for image
    path=image
    #model_path=os.path.join(pn,'model_dir')
    weights_path=model
    output_segmentation=os.path.join(pn,'output_segmentation','segmented.jpg')
    
    #segment video; check to see if vidoe or not
    if video==True:
        processVideo(image,model,boundBox)
        
    #get segment image using PixelLib custom_segmentation
    segment_image = custom_segmentation()
    
    #add classes to segment, with BG as default
    addClasses.append("BG")
    for i in classes:
        addClasses.append(i.strip())
    
    #setup the segmentation configuration with classes and class number
    segment_image.inferConfig(num_classes= classNumber, class_names=addClasses)
    
    #load the model
    segment_image.load_model(weights_path)
    
    #segment image with input data
    segmask, output=segment_image.segmentImage(path, show_bboxes=boundBox, output_image_name=output_segmentation,
            extract_segmented_objects= True, save_extracted_objects=False)
    
    #now output the segmentation data to a .csv file
    outputData(segmask,seg_out,output)

'''
For video segmentation, process video data.
@param image-- the file (image) to use
@param model-- the Mask R-CNN model to use
@param boundBox-- bounding box to use or not?
'''
def processVideo(image,model,boundBox):
    #output to a default segmented vidoe (segmented.mp4)
    output_segmentation=os.path.join(pn,'output_segmentation','segmented.mp4')
    
    #get instance segmentation from PixelLib        
    segment_video = instance_segmentation()
    
    #load the model used to segment
    segment_video.load_model(model)
    
    #process the video with segmentation input
    segment_video.process_video(image, show_bboxes=boundBox,  extract_segmented_objects=True,
                                save_extracted_objects=True, frames_per_second= 5,  output_video_name=output_segmentation)

'''
Output segmentation data from a folder of images.
@param model-- the Mask R-CNN model to use
@param classNumber-- the number of classes
@param boundBox-- a bounding box to use or not?
@param input_folder-- the input folder location
'''
def segmentFolder(model,classNumber,classes,boundBox,input_folder):
    
    #Add classes to segment, with the default BG class added.
    addClasses.append("BG")
    for i in classes:
        addClasses.append(i.strip())
    
    #output segmentation location
    output_segmentation=os.path.join(pn,'output_segmentation')
    
    #get custom segmentation from PixelLib                               
    ins = custom_segmentation()
    
    #setup configuration
    ins.inferConfig(num_classes=classNumber, class_names=addClasses)
    
    #load the model (Mask R-CNN) to use
    ins.load_model(model)
    
    #do segmentation of the batch images
    segmask, output=ins.segmentBatch(input_folder,  show_bboxes=boundBox, output_folder_name = output_segmentation)
    
    #take the data and output to .csv file in the output_segmentation folder
    outputFolderData(segmask, seg_out)

'''
Method to output segmentation data to a .csv file from a group of images.
@param segmask-- the segmentation data to use including roi and id of class
@param seg_out-- the segmentation data file to output to.
'''
def outputFolderData(segmask,seg_out):
    
    #the outputs to get with the type of class, a-d for location of found object, 
    #and the score (likelihood) of identified object.
    fieldnames=['id','a','b','c','d','score']
    
    #open and write to file
    with open(seg_out, 'w') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)

        #write the header
        writer.writeheader()
        
        #get mask data and output information 
        for i in segmask:
            #get scores
            scores=i['scores']
            # get rois (regions) and class ids
            rois=i['rois']
            ids=i['class_ids']

            #write the output
            for ii in range(0,len(rois)):
                roi=rois[ii]
                st=ids[ii]
                item=addClasses[st]
                
                #write the output
                writer.writerow({'id':str(item),'a': str(roi[0]),'b':str(roi[1]),'c':str(roi[2]),'d':str(roi[3]),
                         'score':str(scores[ii])})
        #close the file
        csvf.close()
'''
Method to output a single image to a .csv file
@param segmask-- the segmentation mask and output data
@param seg_out-- the segmentation data file to output to.
'''   
def outputData(segmask,seg_out, output):
    #get the segmentation scores
    scores=segmask['scores']
    #get the rois and ids of the classes segmented
    rois=segmask['rois']
    ids=segmask['class_ids']

    #the fieldnames include the class id, roi info (a-d), and score
    fieldnames=['id','a','b','c','d','score']
    
    #now output the data to the .csv file in output_segmentation
    print(output.shape)
    
    #open output file
    with open(seg_out, 'w') as csvf:
        #make the writer
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        
        #write the header
        writer.writeheader() 

        #iterate through output and output it
        for i in range(0,len(rois)):
            roi=rois[i]
            st=ids[i]
            item=addClasses[st]
            
            #write the output
            writer.writerow({'id':str(item),'a': str(roi[0]),'b':str(roi[1]),'c':str(roi[2]),'d':str(roi[3]),
                         'score':str(scores[i])})
            
        
        csvf.close()

#this is just for testing and not to be normally used      
if __name__ == "__main__":
    weight_location=os.path.join(pn,'weights','mask_rcnn_model.003-3.374101.h5')
    images_path=os.path.join(pn,'structures','test')
    
    #image=os.path.join(pn,'structures','test','DJI_0335.JPG')
    
    #startSegmenting(image,weight_location,3,['qanat','mounded sites','ruined structure'],True, False)
    
    
    segmentFolder(weight_location,3,['ruined-structures','qanat_line','mounded sites'],True,images_path)
