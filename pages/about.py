import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('SenSonic')

sonic_image = Image.open('data\sonic.png')
st.image(sonic_image)