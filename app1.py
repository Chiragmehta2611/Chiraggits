
from google.colab import drive
drive.mount('/content/drive')
%%writefile app.py
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import tensorflow as tf
import numpy as np
from tensorflow import keras
model_new = keras.models.load_model('Digit_Recognition.hdf5')
 
st.title('Digit Recognizer')
st.markdown('''Try to write a digit!''')
 
SIZE = 190
mode = st.markdown("Draw", True)
canvas_result = st_canvas(
    fill_color='#000000',
    stroke_width=20,
    stroke_color='#FFFFFF',
    background_color='#000000',
    width=SIZE,
    height=SIZE,
    drawing_mode="freedraw" if mode else "transform",
    key='canvas')
 
if canvas_result.image_data is not None:
    img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
    rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
    st.write('Model Input')
    st.image(rescaled)
 
if st.button('Predict'):
    test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    val = model_new.predict(test_x.reshape(1, 28, 28))
    st.write(f'result: {np.argmax(val)}')
