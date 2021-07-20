'''
Module that parses location for bounding boxes from example image.

Created on Mar 24, 2021

@author: maltaweel
'''
# example of extracting bounding boxes from an annotation file
from xml.etree import ElementTree
import os
 
# function to extract bounding boxes from an annotation file
def extract_boxes(filename):
    # load and parse the file
    tree = ElementTree.parse(filename)
    # get the root of the document
    root = tree.getroot()
    # extract each bounding box
    boxes = list()
    for box in root.findall('.//bndbox'):
        xmin = int(box.find('xmin').text)
        ymin = int(box.find('ymin').text)
        xmax = int(box.find('xmax').text)
        ymax = int(box.find('ymax').text)
        coors = [xmin, ymin, xmax, ymax]
        boxes.append(coors)
    # extract image dimensions
    width = int(root.find('.//size/width').text)
    height = int(root.find('.//size/height').text)
    return boxes, width, height

pn=os.path.abspath(__file__)
pn=pn.split("src")[0]

path=os.path.join(pn,'kangaroo/annots/00001.xml')
# extract details form annotation file
boxes, w, h = extract_boxes(path)
# summarize extracted details
print(boxes, w, h)