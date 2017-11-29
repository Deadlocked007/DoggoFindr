from flask import Flask, request
from keras.applications.resnet50 import ResNet50
from sklearn.datasets import load_files
from keras.utils import np_utils
import numpy as np
from glob import glob
import cv2
from keras.preprocessing import image
from tqdm import tqdm
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense, Activation
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam, Adamax
from keras.callbacks import ModelCheckpoint
from extract_bottleneck_features import *
from keras.models import model_from_json
import os

app = Flask(__name__)

dog_names = [item[20:-1] for item in sorted(glob("dogImages/train/*/"))]

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
ResNet_model = model_from_json(loaded_model_json)
ResNet_model.load_weights("model.h5")
ResNet_model.compile(loss='categorical_crossentropy', optimizer=Adamax(lr=0.002), metrics=['accuracy'])

ResNet50_model = ResNet50(weights='imagenet')

def path_to_tensor(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)

def ResNet50_predict_labels(img_path):
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))

def ResNet50_predict_breed(img_path):
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    predicted_vector = ResNet_model.predict(bottleneck_feature)
    breed = dog_names[np.argmax(predicted_vector)]
    print(predicted_vector[0][2])
    if dog_detector(img_path) == True:
        return breed
    else:
        return "Ain't no Doggo here"


@app.route('/')
def hello():
    return "Welcome to the DoggoFindr API!"

@app.route('/breed', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        image = request.files['image']
        image.save(os.path.join('./', image.filename))
        return ResNet50_predict_breed(os.path.join('./', image.filename))
    else:
        return "Use POST method to use /breed endpoint"
