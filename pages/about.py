import streamlit as st
import pandas as pd
from PIL import Image

st.title('SenSonic')

sonic_image = Image.open('data\sonic.png')
st.image(sonic_image)