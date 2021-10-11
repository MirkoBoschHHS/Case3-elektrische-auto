import requests
import json
import pandas as pd
import os
import streamlit as st

def OpenChargeMap(max_results=50):
  # Max results to load with api
  key = "7854aa82-723c-48d4-afb4-3c437a9db1c9"
  country_code = "NL"

  #Get data
  # url = r'https://api.openchargemap.io/v3/poi/?key=7854aa82-723c-48d4-afb4-3c437a9db1c9?output=kml&countrycode=NL&maxresults=2'
  url = r'https://api.openchargemap.io/v3/poi/?key=' + str(key) + '?output=json&countrycode=' + str(country_code) + '&maxresults=' + str(max_results)
  # url = 'https://api.openchargemap.io/v3/poi/?output=json&countrycode=' + str(country_code) + '&maxresults=' + str(max_results) + '&compact=true&verbose=false&key=' + str(key) + ')'
  response = requests.get(url)
  response_json = json.loads(response.text)
  response_dataframe = pd.json_normalize(response.json())
  
  return response_dataframe


def load_csv_laadpaal_data(path):
  # Data inladen
  for i in range(0, 2):
    try:
      laadpaal_data = pd.read_csv(path)
      break
    except:
      if (i == 0): # Try changing directory
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        #st.write("Change directory")
      else: # Could not find
        st.error("Could not find file '" + path + "' on location: " + str(os.getcwd()))
        return None

  # Data inspecteren
  laadpaal_data = laadpaal_data[laadpaal_data.ChargeTime >= 0]
  laadpaal_data['Charge/Connected'] = laadpaal_data.ChargeTime / laadpaal_data.ConnectedTime
  laadpaal_data = laadpaal_data[laadpaal_data['Charge/Connected'] <= 1]


  # Terug sturen van de data
  return laadpaal_data

