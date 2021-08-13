<H1>MASK_RCNN_UAV</H1>

<B>About</B>

This project is for developing drone (UAV) image analysis using a Mask R-CNN algorithm to segment and auto-detect archaeological features. Other algorithms are planned but this is the current working version. The current functionality include annotation handling, model creation for deep learning classification based on training data, and segmentation options for analysed images.

Users should also look at Labelme (https://github.com/wkentaro/labelme) and PixelLib (https://pixellib.readthedocs.io/en/latest/) for more information about the annotation (Labelme), training (PixelLib), and segmentation (PixelLib) capabilities used.  The Mask_UAV project was created and tested using Python 3.8+.



<B>Running and Installation of Project</B>

The package can be downloaded and installed using the standard git clone command or download. To install required libraries, use the requirements.txt file in the main folder that contains the needed external libraries (i.e., pip install -r requirements.txt). The main GUI can be run by simply launching controller.py in the main folder. The code was tested on Python 3.8 but users should be sure to have at least Python 3.6 or higher installed.

The folder also contains a controller.spec file, which can be used to package the code and create a distribution. This can be done by installing PyInstaller (pip intall pyinstaller) and then using a pyinstaller command (python -m PyInstaller --onedir --windowed controller.spec) from the project folder to create the build and distribution folders. Before this step, however, you may need to edit the pathex variable in the .spec file to your own local path. After running PyInstaller, you may need to manually install some tensorflow files after build, due to some problems installing tensorflow using PyInstaller. This can be done by moving the required libraries to the distribution folder indicated in any error message. The Labelme default_config.yaml file may also need to be manually installed into the distribution, which can be found in the labelme/config folder in this project. Simply follow the pathway indicated to place the required default_config.yaml file in the distrbution folder that is created by PyInstaller. Once built and the distribution folder created, simply go to the distribution folder and launch the controller file inside (e.g., in Linux ./controller).


In regards to this software, the workflow of the software is given below with the overview to follow:
![workflow](https://user-images.githubusercontent.com/6896620/128998737-e5e28587-e5ab-4451-aabf-da0f2d7c070a.jpg)




The controller.py module enables options to conduct annotation, training, and segmentation. Launching this module will provide choices for the user

![Screenshot from 2021-08-09 11-40-56](https://user-images.githubusercontent.com/6896620/128730858-dec2c198-0c88-4119-9411-3f0064028fe3.png)


<B>Annotation</B> 

The software is broken into three components. The first is annotation, which simply launched the LabelMe tool (https://github.com/wkentaro/labelme). Usrs should look at the software for instruction on how to annotate images on Labelme (or labelme).

![Screenshot from 2021-08-09 11-42-00](https://user-images.githubusercontent.com/6896620/128730951-e69d4315-73fd-46c2-9588-c8fe29acf536.png)


<B>Training</B>

Training is done by two primary ways. First, launching the training gui via the controller is one possibility. There, the training library can be selected, that is the images to use for training which should all be annotated (i.e, with .json files having the annotations). The training data should have a test folder with the .json files. The weight file, which is the initial training weight (.h5) file, can be selected. The number of classes and batch number, that is the training examples used in forward and backward propagation used in deep neural networks. Users can then choose the neural network model, with the default set to resnet101. This is a neural network model that is a convolutional neural network with101 layers; users can also select resnet50, which has 50 layers and runs faster due to fewer layers. The final choice is epochs, which is the number of passes for the training dataset during runs. Users then can press start, which will launch the training using PixelLib, or save the run, which will save to a training_data.csv file in the training_data folder within Mask_UAV. If a user saves the run, then applies training later or on another system such as HPC, it is recommended to use the train_set.py module in the training folder to launch training. Users can simply modify the training_data.csv file to use for remote data training.

![Screenshot from 2021-08-09 11-42-20](https://user-images.githubusercontent.com/6896620/128733062-e5065f28-2f5c-43df-b766-1bc115caebf5.png)

<B>Segmentation</B>

After training is conducted, a .h5 model will result from training runs. This model can be used to conduct segmentation on either image files or videos. Going back to the controller.py module, and after a user selects segmentation, a small window opens to enable user choices for segmentation. Users can select a single image or video file. A choice for the model can be made, which enables the user to select which deep learning model output to use for segmentation. One option is to select a segmentation folder, which is a group of images to segment rather than a single image. If a directory for segmentation is chosen, then the folder will be segmented rather than a single image. The classes, which are the names of the annotated classes used, are also inputted (e.g., ruined structures, qanats, and mounded sites). An option to have a bounding box on images is given as well. If a single video is chosen to segment, which can be chosen using the ‘Segment Image’ option, then indicating that this is a video option can be done in the radio button option (‘Segment Video?’). After these, a user can then start the operation using the start button, which launches the custom_segmentation.py module in the segmentation folder. If a single image is selected, another window will open that shows the segmented image to users. Outputs from segmentation include a segment_data.csv file, which provides segmentation summary data. This file is found in the output_segmentation folder. The file contains the name of the segmented class found in the image, the locations of the bounding box coordinates, and the score of the identified class. The segmented image(s) or segmented video will be located in the output_segmentation folder. If only one image is segmented, it will be called segmented.jpg and be located in the output_segmentation folder. If more than one file is segmented, then the original file name will be used with the output images located in the output folder.

![Screenshot from 2021-08-09 11-48-14](https://user-images.githubusercontent.com/6896620/128745750-256e5a11-d288-4691-aaa4-3a6129e2b878.png)


<B>Running on HPC</B>

Users may want to run the training provided on an HPC system. In this case, what is required is running train_set.py in the training folder. The training_data folder contains the training_data.csv file, which can be edited to run the required data. The input in the .csv file includes the path location of the training data, the weight file location (that is the initial .h5 file), the batch number used in the run, the network model (e.g., resnet101), and number of epochs for runs. See PixelLib for further details on these parameters.

<B>Subfolders</B>

For more details on how different packages, or subfolders, are used then please see those packages and code inside, which have comments on individual methods.

The first subfolder is the gui folder, which contains the GUI components. The train_gui.py module applies the main training GUI, while segment_gui.py applies the segmentation. 

The segmentation subfolder contains custom_segmentation.py, which applies the segmentation used and outputs segmented images to the output_segmentation folder. There segment_data.csv file is also outputted to the output_segmentation folder, with the file containing information about the item segmented and its location in an image. The module image_segment.py is testing code but it can be modified by users if they wish to create their own segmentation.

The subfolder training contains train_set.py, which can be run independently from the controller and uses the training_data/training_data.csv file for training. 

The icons subfolder could be used to create an icon for the built controller package using the controller.spec file. This can be done by adding --icon=icons/mask.png to the pyinstaller command. The labelme folder contains the file (default_config.yml) used in the distribution of the project. The model_dir folder will contain the .h5 file output from training.






