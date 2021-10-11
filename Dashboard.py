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

import Get_data_api
import Figuren

# Enkele standaard opties
st.set_page_config(layout="wide") # Zorgt voor default wide op streamlit
pd.set_option('display.max_columns', None) # Print alles van de DataFrame pandas



# Maak een titel
st.title('Analyse Elektrische auto s')



response_dataframe = Get_data_api.OpenChargeMap()


# response_dataframe#.head()

# response_dataframe.iloc[1]["Connections"]#[0]#["ConnectionTypeID"]





# Sjoerd zijn code

# laadpaal_data = Get_data_api.load_csv_laadpaal_data('D:/Documents/Pycharm/Case_opdrachten/Case3-elektrische-auto/laadpaaldata.csv')
try:
    laadpaal_data = Get_data_api.load_csv_laadpaal_data('laadpaaldata.csv')
    st.write("Using short path")
except:
    laadpaal_data = Get_data_api.load_csv_laadpaal_data(
        'D:/Documents/Pycharm/Case_opdrachten/Case3-elektrische-auto/laadpaaldata.csv')
    st.write("Using full path")

fig = Figuren.histogram(laadpaal_data)

st.plotly_chart(fig)