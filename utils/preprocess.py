import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def preprocess_image(image):
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = preprocess_input(image)  # MobileNet Preprocessing
    return image
