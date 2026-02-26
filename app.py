import streamlit as st
from PIL import Image

st.title("Mi primera app")
st.header("En este espacio cominezo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
Image = Image.open('image.jpeg')
st.Image(image, caption='Interfaces Multimodales')
