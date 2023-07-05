import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go

def load_data(inputfile, nrows):
    df = pd.read_csv(inputfile, nrows=nrows)
    return df

data_load_state = st.text('Loading data...')

df = load_data('data/winter_2032_1_sheet.csv', 100)

data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(df.style.highlight_max(axis=0))

st.data_editor(
    df['p_mw_win'],
    column_config={
        "p_mw_win": st.column_config.NumberColumn(
            "p_mw_win",
            help="p_mw_win",
            width="medium"
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

st.subheader('Aantal megawatt winter')
hist_values = np.histogram(df['p_mw_win'])[0]
st.bar_chart(df['p_mw_win'])

selected_stationsnummer = st.selectbox('Select Category', df['stationsnummer'].unique())
filtered_data = df[df['stationsnummer'] == selected_stationsnummer]

plt.bar(filtered_data['stationsnummer'], filtered_data['p_mw_win'])
plt.xlabel('stationsnummer')
plt.ylabel('p_mw_win')
plt.title('Bar Chart')

# Display the chart using Streamlit
st.pyplot(plt)


column_list = ['functie', 'CBS buurtcode 2020']
selected_columns = st.multiselect("select column", column_list, default="functie")
s = df[selected_columns[0]].str.strip().value_counts()

trace = go.Bar(x=s.index,y=s.values,showlegend = True)
layout = go.Layout(title = "test")
data = [trace]
fig = go.Figure(data=data,layout=layout)
st.plotly_chart(fig)