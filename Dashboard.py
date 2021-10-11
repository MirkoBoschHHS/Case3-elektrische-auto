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

import Get_data
import Figuren

# Enkele standaard opties
st.set_page_config(layout="wide") # Zorgt voor default wide op streamlit
pd.set_option('display.max_columns', None) # Print alles van de DataFrame pandas



# Maak een titel
st.title('Analyse Elektrische auto s')



response_dataframe = Get_data.OpenChargeMap()





laadpaal_data = Get_data.load_csv_laadpaal_data('laadpaaldata.csv')

col1, col2 = st.columns(2)

col1.header("Original")
col1.plotly_chart(Figuren.histogram(laadpaal_data))

col2.header("Grayscale")
col2.plotly_chart(Figuren.histogram(laadpaal_data))

