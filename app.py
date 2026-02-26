import streamlit as st
from PIL import Image

st.title("Mi primera app")
st.header("En este espacio cominezo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('image.jpeg')
st.image(image, caption='Interfaces Multimodales')


texto = st.text_input('Buenas tardes', 'Buenas noches')
st.write('El texto escrito es', texto)
