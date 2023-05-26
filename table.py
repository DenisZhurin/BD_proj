import pandas as pd
import streamlit as st
from bokeh.models.widgets import Div
st.set_page_config(layout = "wide")
data = pd.read_csv('data.csv')
st.write(data)
