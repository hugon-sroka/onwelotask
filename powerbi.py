import json
import boto3
import requests
import pandas as pd
import os
import csv
import openpyxl

datas = []
x = []

## I am aware that there external project and library to prepare data exist, however I wanted to prepare...
## data on my own
with open('economist_country_codes.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')
    for row in spamreader:
        x.append(row[1])

country_codes = x[1:]

print(country_codes)
res = {}
for i in country_codes:
    api_url = f'https://data.nasdaq.com/api/v3/datasets/ECONOMIST/BIGMAC_{i}.json?start_date=2021-07-01&end_date=2021-07-31&api_key=Bv9SfFKRue5dKpH1bCKk'
    response = requests.get(api_url)
    json_data = response.json()
    try:
        json_dataset = json_data['dataset']['data'][0]
        json_dataset.append(i)
    except IndexError:
        json_dataset = json_data['dataset']['data']
        json_dataset.append(i)
        json_dataset.append('null data')
    datas.append(json_dataset)

df = pd.DataFrame(datas)

column_names = json_data['dataset']['column_names']
column_names = column_names.append('country_code')
df.columns = column_names
df.to_excel('output.xlsx')
