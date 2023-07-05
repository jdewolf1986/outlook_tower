import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# network x
fig = plt.figure()
G = nx.karate_club_graph()
pos = nx.kamada_kawai_layout(G)
nx.draw(G,pos, with_labels=True)

# streamlit header
st.title('innovatie 3 daagse test')
st.markdown('energienetwerk test')

# streamlit visualizations
st.pyplot(fig)
st.balloons()

# streamlit button
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write('rauwe data!')




