'''
Created on Apr 2, 2021

@author: maltaweel
'''
import os
import csv
import pixellib
from pixellib.instance import custom_segmentation

#path 
pn=os.path.abspath(__file__)
pn=pn.split("src")[0]
path=os.path.join(pn,'structures','test','The Iron Age Fort at Jebel Buhais, imaged by an ex-drone.JPG')
model_path=os.path.join(pn,'model_dir')
weights_path=os.path.join(pn,'weights','mask_rcnn_model.001-1.412928.h5')
output_segmentation=os.path.join(pn,'output_segmentation','segmented.jpg')
seg_out=os.path.join(pn,'output_segmentation','segment_data.csv')

#segment
segment_image = custom_segmentation()
segment_image.inferConfig(num_classes= 1, class_names= ["BG", 'ruined structure'])
segment_image.load_model(weights_path)
segmask, output=segment_image.segmentImage(path, show_bboxes=True, output_image_name=output_segmentation,
extract_segmented_objects= True, save_extracted_objects=False)

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
