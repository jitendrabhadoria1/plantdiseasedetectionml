import numpy
import numpy as np
import cv2
from keras.models import load_model


def predict_disease(plant_image):
    model = load_model(
        r'E:\M.Tech\Machine Learning with Python\ML Project\model1.h5')

    CLASS_NAMES = ['Apple-Scab', 'Apple-Black Rot', 'Apple-No Disease', 'Potato-Early Blight', 'Potato-No Disease',
                   'Potato-Late Blight', 'Tomato-No Disease', 'Tomato-Spider Mites', 'Tomato-Yellow Leaf Curl Virus']

    if plant_image is not None:

        opencv_image = numpy.array(plant_image)
        opencv_image = opencv_image[:, :, ::-1].copy()

        opencv_image = cv2.resize(opencv_image, (256, 256))
        
        opencv_image.shape = (1, 256, 256, 3)
       
        Y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(Y_pred)]
        return str("This is a " + result.split('-')[0] + " plant's leaf with " + result.split('-')[1]+".")
