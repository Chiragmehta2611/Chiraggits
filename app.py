import tensorflow as tf
import streamlit as st
from tensorflow import keras
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from pyngrok import ngrok
from google.colab import drive
drive.mount('/content/drive')
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Image Classifier - 4 Categories! : Dogs, Cats, Fishes and Flowers")

@st.cache(allow_output_mutation = True)
def load_model():
  model = keras.models.load_model(r'/content/drive/MyDrive/AI_PROJECT/xception_model.hdf5')
  return model

with st.spinner('Loading Model into memory......'):
  model = load_model()

classes = ['cat', 'dog', 'fish', 'flower']

def scale(image):
  image = tf.cast(image, tf.float32)
  image /= 255.0

  return tf.image.resize(image, [224,224])

def decode_img(image):
  img = tf.image.decode_jpeg(image, channels = 3)
  img = scale(img)
  return np.expand_dims(img, axis=0)

upload = st.text_input("Enter the URL to classify....",'https://thumbs.dreamstime.com/b/tench-fish-fishing-isolated-white-26542643.jpg')
if upload is not None:
  content = requests.get(upload).content

  st.write("Predicted Class: ")
  with st.spinner("Classifying..... "):
    label = np.argmax(model.predict(decode_img(content)), axis = 1)
    st.write(classes[label[0]])
  st.write("")
  image = Image.open(BytesIO(content))
  st.image(image , caption = 'Classfying given Image', use_column_width = True)
