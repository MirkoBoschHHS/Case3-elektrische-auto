import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.figure_factory as ff
import plotly.express as px
import io
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from streamlit_folium import folium_static
import folium

import Get_data
import Figuren

# Enkele standaard opties
st.set_page_config(layout="wide") # Zorgt voor default wide op streamlit
pd.set_option('display.max_columns', None) # Print alles van de DataFrame pandas

# Get secrets
try:
    max_results = st.secrets["max_results"]
except:
    max_results = 50

# Maak een titel
st.title('Dashboard elektrische auto\'s')


# Get data from API / CSV

laadpaal_data = Get_data.load_csv_laadpaal_data('laadpaaldata.csv')








# ---------- Histogram van laadtijd ----------
st.header("Wat is de laadtijd van elektrische auto\'s")
col1, col2 = st.columns([1,2])
col1.write("Hier nog een tekst of interactie")
col2.plotly_chart(Figuren.histogram_laadtijd_elek_auto(laadpaal_data))




st.markdown("""---""")
# ---------- Voeg de map van locaties toe ----------
st.header("Waar bevinden openbare laadstations van Open Chargemap")
col1, col2 = st.columns([1,2])
response_dataframe = Get_data.OpenChargeMap(col1, max_results)
m, bar = Figuren.map_folium(response_dataframe, max_results)
bar.progress(99)
with col2:
    folium_static(m)
bar.progress(100)
bar.empty()




st.markdown("""---""")
# ---------- Voeg de map van locaties toe ----------
col1, col2 = st.columns([1,2])
col1.write("Hier nog een tekst of interactie")
autos_per_maand_cum = Get_data.rdw_data()
#fig = Figuren.lijn(autos_per_maand_cum)
#col2.plotly_chart(fig)

st.write("Succes")



