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

st.image(
    "https://i.ibb.co/R79T9ct/Naamloos.png",
    # Manually Adjust the width of the image as per requirement
)
st.title('Analyse Elektrische auto s')



response_dataframe = Get_data_api.OpenChargeMap()

pd.set_option('display.max_columns', None)
response_dataframe#.head()