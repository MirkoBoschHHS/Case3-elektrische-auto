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
st.title('Analyse Elektrische auto s')


# Get data from API / CSV
response_dataframe = Get_data.OpenChargeMap(max_results)
laadpaal_data = Get_data.load_csv_laadpaal_data('laadpaaldata.csv')



col1, col2 = st.columns(2)

# ---------- Histogram van laadtijd ----------
col1.plotly_chart(Figuren.histogram_laadtijd_elek_auto(laadpaal_data))


# ---------- Voeg de map van locaties toe ----------
m = Figuren.map(response_dataframe)
with col2:
    folium_static(m)





