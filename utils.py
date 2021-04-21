import pandas as pd
import numpy as np
import tensorflow_datasets as tfds
from tensorflow.keras import layers
import tensorflow as tf
import pickle
from keras.models import load_model            
            


def loadmodel():
    
    
    modelDCNN = load_model('model/mymodel')

    return modelDCNN




def preprocess(data):

    with open('model/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    data = tokenizer.encode(data)

    return data
    




def predict(model, data):

    result = model(np.array([data]), training=False).numpy()

    if result > 0.5:
        result = 'Positive'
    else:
        result = 'Negative'

    return result