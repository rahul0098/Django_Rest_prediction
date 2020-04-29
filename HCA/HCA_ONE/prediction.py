import warnings
warnings.filterwarnings('ignore')

import cv2
from tensorflow.keras.models import load_model

import warnings
warnings.filterwarnings('ignore')

def prediction(image):
    model=load_model('model/feature.h5')
    print('*'*150,image)
    img=cv2.imread('.'+image)

    dim=(200,200)
    resized = cv2.resize(img, dim,1)

    im=resized.reshape(-1,resized.shape[0],resized.shape[1],resized.shape[2])

    result={'0.0':'NOT INFECTED','1.0':'INFECTED'}

    return (result[str(model.predict(im)[0][0])])

