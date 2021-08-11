MASK_RCNN_Drone

This project is for developing drone image analysis using a Mask R-CNN algorithm to segment and auto-detect archaeological features. This functions enabled include annotation handling, model creation for deep learning classification based on training data, and segmentation options for analysed images.

Users should also look at Labelme (https://github.com/wkentaro/labelme) and PixelLib (https://pixellib.readthedocs.io/en/latest/) for more information about the annotation, training, and segmentation capabilities used.

The workflow of the software is given below:
![workflow](https://user-images.githubusercontent.com/6896620/128731973-c67bc528-f4fc-4e43-b0f2-8f6c4f57b156.jpg)



The controller.py module enables options to conduct annotation, training, and segmentation. Launching this module will provide choices for the user

![Screenshot from 2021-08-09 11-40-56](https://user-images.githubusercontent.com/6896620/128730858-dec2c198-0c88-4119-9411-3f0064028fe3.png)


<B>Annotation</B> 

The software is broken into three components. The first is annotation, which simply launched the LabelMe tool (https://github.com/wkentaro/labelme). Usrs should look at the software for instruction on how to annotate images on Labelme (or labelme).

![Screenshot from 2021-08-09 11-42-00](https://user-images.githubusercontent.com/6896620/128730951-e69d4315-73fd-46c2-9588-c8fe29acf536.png)


<B>Training</B>

Training is done by first launching the training gui via the controller. There, the training library can be selected, that is the images to use for training which should all be annotated (i.e, with .json files having the annotations). The weight file, which is the initial training weight (.h5) file, can be selected. The number of classes and batch number, that is the training examples used in forward and backward propagation used in deep neural networks. Users can then choose the neural network model, with the default set to resnet101. This is neural network model that is a convolutional neural network with101 layers; users can also select resnet50, which has 50 layers and runs faster due to fewer layers. The final choice is epochs, which is the number of passes for the training dataset during runs. Users then can press start, which will launch the training using Pixellib, or save the run, which will save to a training_data.csv file in the training_data folder within Mask_RCNN_UAV. If a user saves the run, then to launch the training, it is recommended to use the train_set.py module in the training folder. This can be launched using a high performance computing (HPC) system with GPU enabled options.

![Screenshot from 2021-08-09 11-42-20](https://user-images.githubusercontent.com/6896620/128733062-e5065f28-2f5c-43df-b766-1bc115caebf5.png)

<B>Segmentation</B>

After training is conducted, a .h5 model will result from training runs. This model can be used to conduct segmentation on either image files or videos. Going back to the controller.py module, and after a user selects segmentation, a small window opens to enable user choices for segmentation. Users can select a single image or video file. A choice for the model can be made, which enables the user to select which deep learning model output to use for segmentation. One option is to select a segmentation folder, which is a group of images to segment rather than a single image. If a directory for segmentation is chosen, then the folder will be segmented rather than a single image. The classes, which are the names of the annotated classes used, are also inputted (e.g., ruined structures, qanats, and mounded sites). An option to have a bounding box on images is given as well. If a single video is chosen to segment, which can be chosen using the ‘Segment Image’ option, then indicating that this is a video option can be done in the radio button option (‘Segment Video?’). After these, a user can then start the operation using the start button, which launches the custom_segmentation.py module in the segmentation folder. If a single image is selected, another window will open that shows the segmented image to users. Outputs from segmentation include a segment_data.csv file. This file is found in the output_segmentation folder. The file contains the name of the segmented class found in the image, the locations of the bounding box coordinates, and the score of the identified class. The segmented image(s) will be located in the output_segmentation folder.

![Screenshot from 2021-08-09 11-48-14](https://user-images.githubusercontent.com/6896620/128745750-256e5a11-d288-4691-aaa4-3a6129e2b878.png)



<B>Installation of Project</B>

The package can be downloaded and installed using the standard git clone command or download. To install required libraries, use the requirements.txt file in the main folder (i.e., pip install -r requirements.txt). The main GUI can be run by simply launching controller.py in the main folder.

The folder also contains a controller.spec file, which can be used to package the code and create a distribution. This can be done by installing PyInstaller (pip intall pyinstaller) and then using a pyinstaller command (python -m PyInstaller --onedir --windowed controller.spec) from the project folder. Before this step, however, you may need to edit the pathex variable in the .spec file to your local path. After running PyInstaller, you may need to manually install some tensorflow files after build, due to some problems installing tensorflow using PyInstaller. This can be done by moving the required libraries to the folder indicated in any error message. The Labelme default_config.yaml file may also need to be manually installer into the distribution, which can be found in the labelme/config folder in this project. Simply follow the pathway indicated to place the required default_config.yaml file. 

<B>Running on HPC</B>

Users may want to run the training provided on an HPC system. In this case, what is required is running train_set.py in the training folder. The training_data folder contains the training_data.csv file, which can be edited to run the required data. The input in the .csv file includes the path location of the training data, the weight file location (that is the initial .h5 file), the batch number used in the run, the network model (e.g., resnet101), and number of epochs for runs. See PixelLib for further details on these parameters.






