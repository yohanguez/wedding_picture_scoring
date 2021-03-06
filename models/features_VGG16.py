from keras.applications.vgg16 import VGG16
from keras.models import Model
import glob
import pickle
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
from keras.applications.imagenet_utils import  preprocess_input

class features_VGG16():
    def __init__(self, p_path):
        self.path = p_path
        self.pic_list = None
        self.features_list = []


    def compute_features(self):
        model_vgg16_conv = VGG16(weights='imagenet', include_top=True)
        inp = model_vgg16_conv.input
        out = model_vgg16_conv.layers[-2].output
        model = Model(inp, out)

        self.pic_list = glob.glob(self.path + '/*.JPG')
        for pic_path in self.pic_list:
            img = load_img(pic_path, target_size=(224, 224))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            self.features_list.append(model.predict(x))

    def dump(self, path):
        with open(path + '/result/pic_list.pkl', 'wb') as f:
            pickle.dump(self.pic_list, f)
        with open(path + '/result/features_list_VGG16.pkl', 'wb') as f:
            pickle.dump(self.features_list, f)