from PIL import Image

import pandas as pd
import streamlit as st
def developer():
    st.title("Developers")
    image = Image.open('1.jpeg')
    image=image.resize((300,300))
    st.image(image, caption='Rudransh Srivastava')
    st.write(""" Linkedin : https://www.linkedin.com/in/rudransh-srivastava-2a8b1019b/""")

    image2=Image.open('2.jpeg')
    image2=image2.resize((300,350))
    st.image(image2,caption='Chet Mani Singh')
    st.write("""Linkedin : https://www.linkedin.com/in/chet-mani-singh-b27314205/""")