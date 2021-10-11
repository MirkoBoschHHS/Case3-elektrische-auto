import requests
import json
import pandas as pd

def OpenChargeMap():
  # Max results to load with api
  max_results = 100
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
