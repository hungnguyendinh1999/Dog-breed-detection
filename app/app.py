from data.extract_bottleneck_features import extract_Resnet50
import flask
from flask import Flask, render_template, request, send_file
import re
import sys 
import os
import base64
import uuid
import urllib
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from data.extract_bottleneck_features import extract_Resnet50
import model.load
from model.load import *

# sys.path.append(os.path.abspath("../model"))
# from load import * 
# sys.path.append(os.path.abspath("../data"))
# from extract_bottleneck_features import *

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = 'static/images'
'''
Pre-processing for input images to match with model input format
INPUT: PNG or JPG image
OUTPUT: Convert to tensor
'''
directories = {
    'data': '../data',
    'model': '../model',
}

Resnet50_model = init()

# # function to extract dog name from dog_names[index] (trim excess strings)
# def get_proper_dog_name(path):
#     return path.split('.')[1]

# def Resnet50_predict_breed(img_path):
#     bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
#     predicted_vector = Resnet50_model.predict(bottleneck_feature)
#     return get_proper_dog_name(dog_names[np.argmax(predicted_vector)])

# def init(): 
# 	#load weights into new model
# 	model = load_model("model/weights.best.Resnet50.hdf5")
# 	print("Loaded Model from disk")

# 	return model


ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and (filename.rsplit('.', 1)[1] in ALLOWED_EXT)

classes = ['airplane' ,'automobile', 'bird' , 'cat' , 'deer' ,'dog' ,'frog', 'horse' ,'ship' ,'truck']

# def predict(filename , model):
#     img = load_img(filename , target_size = (32 , 32))
#     img = img_to_array(img)
#     img = img.reshape(1 , 32 ,32 ,3)
#     img = img.astype('float32')
#     img = img/255.0
#     result = model.predict(img)
#     dict_result = {}
#     for i in range(10):
#         dict_result[result[0][i]] = classes[i]
#     res = result[0]
#     res.sort()
#     res = res[::-1]
#     prob = res[:3]
    
#     prob_result = []
#     class_result = []
#     for i in range(3):
#         prob_result.append((prob[i]*100).round(2))
#         class_result.append(dict_result[prob[i]])
#     return class_result , prob_result

'''
app.Routes
'''
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success' , methods = ['GET' , 'POST'])
def success():
    error = ''
    target_img = os.path.join(os.getcwd() , 'app/'+UPLOAD_FOLDER)
    if request.method == 'POST':
        if(request.form):
            link = request.form.get('link')
            try :
                resource = urllib.request.urlopen(link)
                unique_filename = str(uuid.uuid4())
                filename = unique_filename+".jpg"
                img_path = os.path.join(target_img , filename)
                output = open(img_path , "wb")
                output.write(resource.read())
                output.close()
                img = filename
                # class_result , prob_result = predict(img_path , model)
                # predictions = {
                #       "class1":class_result[0],
                #         "class2":class_result[1],
                #         "class3":class_result[2],
                #         "prob1": prob_result[0],
                #         "prob2": prob_result[1],
                #         "prob3": prob_result[2],
                # }
                print('Image Link Saved', file=sys.stdout)
            except Exception as e : 
                print(str(e))
                error = 'This image from this site is not accesible or inappropriate input'
            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = 'dog')# predictions)
            else:
                return render_template('index.html' , error = error) 
            
        elif (request.files):
            file = request.files['file']
            print(file)
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename
                # class_result , prob_result = predict(img_path , model)
                # predictions = {
                #       "class1":class_result[0],
                #         "class2":class_result[1],
                #         "class3":class_result[2],
                #         "prob1": prob_result[0],
                #         "prob2": prob_result[1],
                #         "prob3": prob_result[2],
                # }

                print('Uploaded image saved', file=sys.stdout)
            else:
                error = "Please upload images of jpg , jpeg and png extension only"

            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = 'dog') #predictions)
            else:
                return render_template('index.html' , error = error)
    else:
        return render_template('index.html')

def main():
    app.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == '__main__':
    main()