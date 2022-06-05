# Dog Breed Classification

![Dog Breed Classification - Golden Retriever](Success_Scene.png)

## Content:
- [Project Description](#project-description)
- [Files](#files)
- [Installation Instruction](#installation-instruction)
- [Use Instruction](#use-instruction)
- [Environment Setup](#environment-setup)

Note: If you want to try out the Notebook, please download data as instructed in the notebook. There is code to download and use the data. 

The Notebook contains the report required for this project.

## Project Description
This is the Capstone project for the Udacity Data Science Nanodegree course.
For the library used, please take a look at [the requirement.txt file](requirements.txt)

### Project Overview
I have a dog at home and wanted to identify what dog breed looks the most like him (since he is a mixed breed).

### Problem Statement
Each major breed has their own sub-breeds and identifying features. I have a hard time identifying dog breeds due to the sheer number of features and experience required to accurately identify these canines’ ancestry, such as fur color, texture, head shape, ear shape, and facial features. It is even more difficult if we can only see images of dogs. 
The problem is that with traditional Machine Learning models, it is difficult to identify certain features of 133 breeds of dogs. Thus, this will require some research into Convolution Neural Network and Transfer Learning.
My main objective is to train and evaluate a CNN model that takes a colored image of a dog as an input and predict the breed with the highest accuracy possible. I will simply evaluate some models (VGG16, ResNet50, my own model) and gain a basic understanding of Computer Vision in Data Science.

### Metrics
Since this is a classification problem, evaluation is based on accuracy. Typically, the model is evaluated on the test set and in percentage (e.g. 80.9%).


## Files
```
Dog-breed-detection
│   README.md
│   checklist.txt
│   requirements.txt
│
└───app
│   │   app.py
│   │
│   └───static
│   │   │   file111.txt
│   │   │   file112.txt
│   │   │
│   │   └───css
│   │   │   │   *.jpg // image files
│   │   │   │   *.css // style files
│   │   │
│   │   └───images
│   │   │   │   *.jpeg // temp storage for uploaded files
│   │   │
│   │   └───javascript
│   │       │   index.js
│   │
│   └───templates
│       │   index.html
│       │   success.html
│   
└───data
│   │   *.jpeg // examples to use to test
│   │   extract_bottleneck_features.py // containing code for extracting Resnet50 bottleneck features
│
└───model
│   │   load.py // containing code for loading model
│   │   weights.best.Resnet50.hdf5 // model file
│
└───notebook
│   │   dog_app.ipynb
│
```

## Installation Instruction
Once you have pull the repo, or download and unzip this repo, please follow the steps below to complete the setup.
0. Setup an environment (Python 3.6) and install packages from (requirements.txt)[requirements.txt]. Read the instructions from [Environment Setup](#environment-setup) for more info.
1. To run the web application (locally), you'll first tell Flask where to find the application (by setting the path for FLASK_APP), and to run in the developement mode.
```
export FLASK_APP=app/app.py
export FLASK_ENV=development
```

Run the application using `flask run` command.

2. Go to http://127.0.0.1:5000/ to start.

## Use Instruction
Using the web-app is straightforward. You just upload a photo of a dog and see if it outputs the right one. For fun, you could also upload a clear photo of a human face and see what it predicts.

After you have uploaded an appropriate image, press "Upload" and wait for the result!

Note: This app does not yet have the ability to scan and detect human faces nor detect dogs due to versioning issues. Though the full code is in the [Jupyter notebook](notebook/dog_app.ipynb) if you want to try.

## Additional Environment Setup
**NOTE: I use Python 3.6. All versions of packages should be in the [requirements.txt](requirements.txt) file. FYI I use macOS**

I exported the `requirements.txt` file. You can just do `pip install -r requirements.txt` to install required packages for your environment. 

For [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) users:
1. Create Environment:
    - Run this line in Terminal to install all ~290 packages from Anaconda
    `conda create -n env_full anaconda python=3.6`
    
    - Otherwise, run this to create an enviroment and install only the necessary on for this project.
    `conda create -n env --file requirements.txt`
2. Activate Environment
    - `conda activate env_full`
3. When not used, deactivate Environment
    - `conda deactivate`
4. To check all packages installed
    - `conda list -n env_full`
