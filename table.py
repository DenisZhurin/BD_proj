import pandas as pd
import streamlit as st
from bokeh.models.widgets import Div
st.set_page_config(layout = "wide")
data = pd.read_csv('https://github.com/DenisZhurin/BD_proj/blob/0112ca88c66d310183c0edbe214771923f6ff1ba/data.csv?raw=true')
st.write(data)
