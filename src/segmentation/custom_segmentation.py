'''
Created on Apr 2, 2021

@author: maltaweel
'''
import os
import csv
import pixellib
from pixellib.instance import custom_segmentation

pn=os.path.abspath(__file__)
pn=pn.split("src")[0]

def startSegmenting(image,weight,classNumber,classes, boundBox):
    #path info
    path=image
    #model_path=os.path.join(pn,'model_dir')
    weights_path=weight
    output_segmentation=os.path.join(pn,'output_segmentation','segmented.jpg')
    seg_out=os.path.join(pn,'output_segmentation','segment_data.csv')

    #segment
    segment_image = custom_segmentation()
    
    addClasses=[]
    addClasses.append("BG")
    for i in classes:
        addClasses.append(i)
        
    segment_image.inferConfig(num_classes= classNumber, class_names=addClasses)
    segment_image.load_model(weights_path)
    segmask, output=segment_image.segmentImage(path, show_bboxes=boundBox, output_image_name=output_segmentation,
            extract_segmented_objects= True, save_extracted_objects=False)

    outputData(segmask,seg_out)
    
def outputData(segmask,seg_out):
    res = segmask["extracted_objects"]
    scores=segmask['scores']
    ids=segmask['class_ids']

    fieldnames=['id','a','b','c','score']
    with open(seg_out, 'w') as csvf:
        #write the output
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)

        writer.writeheader() 

        for i in range(0,len(res)):
            writer.writerow({'id':str(ids[i]),'a': str(res[i].shape[0]),'b':str(res[i].shape[1]),'c':str(res[i].shape[2]),
                         'score':str(scores[i])})
        
if __name__ == "__main__":
    image=os.path.join(pn,'structures','test','Burials-APAAME_20100601_SES-0108.jpg')
    weight_location=os.path.join(pn,'weights','mask_rcnn_model.001-1.412928.h5')
    
    startSegmenting(image,weight_location,1,['BG','ruined structure'],True)
    
