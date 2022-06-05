# Dog Breed Classification

![Dog Breed Classification - Golden Retriever](Success_Scene.png)

## Project Description
This is the Capstone project for the Udacity Data Science Nanodegree course.
You can check out the capstone report in the [Capstone Report](report/report.pdf) for the Project Definition, Motivation, Analysis, and Conclusion.

For the library used, please take a look at [the requirement.txt file](requirements.txt)

## Content:
- [Files](#files)
- [Installation Instruction](#installation-instruction)
- [Use Instruction](#use-instruction)
- [Environment Setup](#environment-setup)

Note: If you want to try out the Notebook, please download data as instructed in the notebook. There is code to download and use the data. 

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
└───report
    │   report.pdf
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
