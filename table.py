import pandas as pd
import streamlit as st
from bokeh.models.widgets import Div
st.title('Table')
st.set_page_config(layout = "wide")
data = pd.read_csv('https://github.com/DenisZhurin/BD_proj/blob/0112ca88c66d310183c0edbe214771923f6ff1ba/data.csv?raw=true')
st.write(data)

if st.button('See table with calculated data'):
    js = "window.open('https://deniszhurin-bd-proj-table-1-c3xcjv.streamlit.app/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
