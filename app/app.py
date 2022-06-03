from flask import Flask, render_template, request, send_file
import re
import sys 
import os
import uuid
import urllib
import numpy as np
import tensorflow as tf
import keras
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50, preprocess_input

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = 'static/images'

dog_names=['Affenpinscher','Afghan hound','Airedale terrier','Akita','Alaskan malamute',
'American eskimo dog','American foxhound','American staffordshire terrier',
 'American water spaniel','Anatolian shepherd dog','Australian cattle dog', 'Australian shepherd','Australian terrier',
 'Basenji','Basset hound', 'Beagle', 'Bearded collie', 'Beauceron', 'Bedlington terrier',
 'Belgian malinois', 'Belgian sheepdog', 'Belgian tervuren', 'Bernese mountain dog',
 'Bichon frise', 'Black and tan coonhound', 'Black russian terrier', 'Bloodhound',
 'Bluetick coonhound', 'Border collie', 'Border terrier', 'Borzoi',
 'Boston terrier', 'Bouvier des flandres', 'Boxer', 'Boykin spaniel',
 'Briard', 'Brittany', 'Brussels griffon', 'Bull terrier',
 'Bulldog', 'Bullmastiff', 'Cairn terrier', 'Canaan dog',
 'Cane corso', 'Cardigan welsh corgi', 'Cavalier king charles spaniel', 'Chesapeake bay retriever',
 'Chihuahua', 'Chinese crested', 'Chinese shar-pei', 'Chow chow',
 'Clumber spaniel', 'Cocker spaniel', 'Collie', 'Curly-coated retriever',
 'Dachshund', 'Dalmatian', 'Dandie dinmont terrier', 'Doberman pinscher',
 'Dogue de bordeaux', 'English cocker spaniel', 'English setter', 'English springer spaniel',
 'English toy spaniel', 'Entlebucher mountain dog', 'Field spaniel', 'Finnish spitz',
 'Flat-coated retriever', 'French bulldog', 'German pinscher', 'German shepherd dog',
 'German shorthaired pointer', 'German wirehaired pointer', 'Giant schnauzer', 'Glen of imaal terrier',
 'Golden retriever', 'Gordon setter', 'Great dane', 'Great pyrenees',
 'Greater swiss mountain dog', 'Greyhound', 'Havanese', 'Ibizan hound',
 'Icelandic sheepdog', 'Irish red and white setter', 'Irish setter', 'Irish terrier',
 'Irish water spaniel', 'Irish wolfhound', 'Italian greyhound', 'Japanese chin',
 'Keeshond', 'Kerry blue terrier', 'Komondor', 'Kuvasz',
 'Labrador retriever', 'Lakeland terrier', 'Leonberger', 'Lhasa apso',
 'Lowchen', 'Maltese', 'Manchester terrier', 'Mastiff',
 'Miniature schnauzer', 'Neapolitan mastiff', 'Newfoundland', 'Norfolk terrier',
 'Norwegian buhund', 'Norwegian elkhound', 'Norwegian lundehund', 'Norwich terrier',
 'Nova scotia duck tolling retriever', 'Old english sheepdog', 'Otterhound', 'Papillon',
 'Parson russell terrier', 'Pekingese', 'Pembroke welsh corgi', 'Petit basset griffon vendeen',
 'Pharaoh hound', 'Plott', 'Pointer', 'Pomeranian',
 'Poodle', 'Portuguese water dog', 'Saint bernard', 'Silky terrier',
 'Smooth fox terrier', 'Tibetan mastiff', 'Welsh springer spaniel', 'Wirehaired pointing griffon',
 'Xoloitzcuintli', 'Yorkshire terrier']

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and (filename.rsplit('.', 1)[1] in ALLOWED_EXT)

'''
**********************************************
***********| ALL HELPER FUNCTIONS |***********
**********************************************
'''

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def predict_dog(input):
    dog_model = load_model("model/weights.best.Resnet50.hdf5")
    graph_dog = tf.get_default_graph()

    with graph_dog.as_default():
        preds = dog_model.predict(input)
    
    return preds


def extract_Resnet50(tensor):
    ResNet50_model = ResNet50(weights='imagenet', include_top=False)
    graph_RN50 = tf.get_default_graph()

    with graph_RN50.as_default():
        preds = ResNet50_model.predict(preprocess_input(tensor))
    
    return preds

def get_dog_names(predicted_vector, top_n = 1):
    if top_n == 1:
        return dog_names[np.argmax(predicted_vector)]
    else:
        indices = np.argpartition(predicted_vector, -3)[-3:]
        ind = indices[np.argsort(predicted_vector[indices])]
        return np.array(dog_names)[ind] 

def Resnet50_predict_breed(img_path):
    tensor = path_to_tensor(img_path)  # 224, 224 ,3
    print("path_to_tensor.shape:", tensor.shape)

    bottleneck_feature = extract_Resnet50(tensor) # (1, 1, 1, 2048)
    print("bottleneck.shape:", bottleneck_feature.shape)
    keras.backend.clear_session()
    
    predicted_vector = predict_dog(bottleneck_feature)
    keras.backend.clear_session()

    # dummy_thicc = np.load('data/DogResnet50Data.npz')['test']
    # predicted_vector = predict_dog(dummy_thicc)
    print("output.shape:", predicted_vector.shape)
    
    return get_dog_names(predicted_vector)

# Function to push to web format
def predict(img_path):
    prob_result = [1,2,3]
    class_result = [Resnet50_predict_breed(img_path), "Default", "Default2"]
    return class_result , prob_result

'''
**********************************************
******************|END TEST|******************
**********************************************
'''

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

                class_result, prob_result = predict(img_path)
                predictions = {
                      "class1":class_result[0],
                        "class2":class_result[1],
                        "class3":class_result[2],
                        "prob1": prob_result[0],
                        "prob2": prob_result[1],
                        "prob3": prob_result[2],
                }
                print('Image Link Saved', file=sys.stdout)
            except Exception as e : 
                print(str(e))
                error = 'This image from this site is not accesible or inappropriate input'
            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error) 
            
        elif (request.files):
            file = request.files['file']
            print(file)
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename
                # Test extract bottleneck_feature
                print("Test filepath:", img_path)

                class_result, prob_result = predict(img_path)
                predictions = {
                      "class1":class_result[0],
                        "class2":class_result[1],
                        "class3":class_result[2],
                        "prob1": prob_result[0],
                        "prob2": prob_result[1],
                        "prob3": prob_result[2],
                }

                print('Uploaded image saved', file=sys.stdout)
            else:
                error = "Please upload images of jpg , jpeg and png extension only"

            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error)
    else:
        return render_template('index.html')

def main():
    app.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == '__main__':
    main()