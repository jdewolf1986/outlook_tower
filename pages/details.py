import streamlit as st
import pandas as pd
import numpy as np

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