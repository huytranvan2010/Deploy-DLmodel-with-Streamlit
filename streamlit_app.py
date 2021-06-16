import streamlit as st
import cv2
from PIL import Image
import numpy as np

def opencv2pil(opencv_image):
    color_converted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(color_converted)
    return pil_image

def pil2opencv(pil_image):
    opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return opencv_image

st.title("Face Detection with HaarCascade in OpenCV")
st.write("Learn more at [github-huytranvan2010](https://github.com/huytranvan2010/Deploy-DLmodel-with-Streamlit)")

def detection(pil_image, scalefactor=None):
    opencvImage = pil2opencv(pil_image)
    gray_image = cv2.cvtColor(opencvImage, cv2.COLOR_BGR2GRAY)
    haarcascade = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(haarcascade)
    faceRects = detector.detectMultiScale(gray_image, scaleFactor=scalefactor, minNeighbors=5,
									  minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # loop over the faces and draw a rectangle around each
    for (x, y, w, h) in faceRects:  
	    cv2.rectangle(opencvImage, (x, y), (x + w, y + h), (0, 255, 0), 2)

    count = len(faceRects)
    return count, opencv2pil(opencvImage)

uploaded_file = st.file_uploader("Choose a file", type=['jpg', 'jpeg', 'jfif', 'png'])

if uploaded_file is not None:
    pil_image = Image.open(uploaded_file)
    placeholders = st.beta_columns(2)
    placeholders[0].image(pil_image)

    # lamf slider thay đổi scale factor xem ảnh hưởng đến detection như nào
    scale_factor = st.slider("SET Scale Factor", min_value = 1.1, max_value = 1.4, value=1.25, step=0.05)
    count, out_image = detection(pil_image, scalefactor=scale_factor)
    placeholders[1].image(out_image)

    st.write("Number of detected people: ", count)