import pandas as pd
import streamlit as st
from bokeh.models.widgets import Div
st.set_page_config(layout = "wide")
st.title('Table with calculated values')
data = pd.read_csv('https://github.com/DenisZhurin/BD_proj/blob/0112ca88c66d310183c0edbe214771923f6ff1ba/data.csv?raw=true')
data['Price(Unit_price*Quantity)'] = round(data['Quantity']*data['Unit_price($)'], 2) #Кол-во на цену одной позиции
data['Tax_price'] = round(data['Price(Unit_price*Quantity)']*0.05, 2)
data['Total'] = round(data['Price(Unit_price*Quantity)']*0.05+data['Price(Unit_price*Quantity)'], 2)

sums = pd.DataFrame([[str('Amount:'), "", "", "", "", sum(data['Quantity']),"","","",round(sum(data['Price(Unit_price*Quantity)']), 2), round(sum(data['Tax_price']), 2),""]], columns=data.columns)
finish = pd.DataFrame([[str('Result:'), sum(data['Total']), "", "", "", "", "", "", "","","",""]], columns=data.columns)
data = pd.concat([data, sums])
data = pd.concat([data, finish])
st.write(data)

if st.button('Return to table'):
    js = "window.open('https://deniszhurin-bd-proj-table-8n36ft.streamlit.app/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
