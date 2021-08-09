MASK_RCNN_Drone

This project is for developing drone image analysis using a Mask R-CNN algorithm to segment and auto-detect archaeological features. 
This functions enabled include annotation handling, model creation for deep learning classification based on training data, and segmentation options for analysed images.

The workflow of the software is given below
![workflow](https://user-images.githubusercontent.com/6896620/128731973-c67bc528-f4fc-4e43-b0f2-8f6c4f57b156.jpg)



The controller.py module enables options to conduct annotation, training, and segmentation. Launching this module will provide choices for the user

![Screenshot from 2021-08-09 11-40-56](https://user-images.githubusercontent.com/6896620/128730858-dec2c198-0c88-4119-9411-3f0064028fe3.png)


<B>Annotation</B> 

The software is broken into three components. The first is annotation, which simply launched the LabelMe tool (https://github.com/wkentaro/labelme). Usrs should look at the software for instruction on how to annotate images on Labelme (or labelme).

![Screenshot from 2021-08-09 11-42-00](https://user-images.githubusercontent.com/6896620/128730951-e69d4315-73fd-46c2-9588-c8fe29acf536.png)


<B>Training</B>

Training is done by first launching the training gui via the controller. There, the training library can be selected, that is the images to use for training which should all be annotated (i.e, with .json files having the annotations). The weight file, which is the initial training weight (.h5) file, can be selected. The number of classes and batch number, that is the training examples used in forward and backward propagation used in deep neural networks. Users can then choose the neural network model, with the default set to resnet101. This is neural network model that is a convolutional neural network with101 layers; users can also select resnet50, which has 50 layers and runs faster due to fewer layers. The final choice is epochs, which is the number of passes for the training dataset during runs. Users then can press start, which will launch the training using Pixellib, or save the run, which will save to a training_data.csv file in the training_data folder within Mask_RCNN_UAV. If a user saves the run, then to launch the training, it is recommended to use the train_set.py module in the training folder. This can be launched using a high performance computing (HPC) system with GPU enabled options.

![Screenshot from 2021-08-09 11-42-20](https://user-images.githubusercontent.com/6896620/128733062-e5065f28-2f5c-43df-b766-1bc115caebf5.png)







