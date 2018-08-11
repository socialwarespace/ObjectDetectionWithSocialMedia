from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import VGG16
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.imagenet_utils import decode_predictions, preprocess_input
from keras.models import load_model
import numpy as np
from PIL import Image

"""
    This class provides find object in image. 
    This class uses VGG16 model for object detection.
"""
class CNNModel:

    def __init__(self):
        """
        Load downloaded VGG16 model from project folder.
        """
        self._model = InceptionResNetV2(weights='imagenet')
        # self._model.save('inception_model.h5')
        # self._model = VGG16(weights='imagenet')
        # self._vgg_model.save('vgg16_model.h5')
        # self._model = load_model('inception_model.h5')

    def preprocess_img(self, img):
        """
        This function provides prepare image before predict image.
        :param img: Downloaded image from url
        :return: Processing image
        """
        r_img = img.resize((224, 224), Image.ANTIALIAS)
        r_img = img_to_array(r_img)
        r_img = np.expand_dims(r_img, axis=0)

        return preprocess_input(r_img)

    def predict(self, img):
        """
        This function predict object in image with VGG16 model.
        :param img: Processing image
        :return: Prediction result (Prediction name and its accuracy)
        """
        predictions = self._model.predict(img)
        labels = decode_predictions(predictions)

        return "{} and it's accuracy {}.".format(labels[0][0][1], round(labels[0][0][2], 3))
