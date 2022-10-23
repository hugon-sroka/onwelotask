import json
import boto3
import botocore
from botocore import UNSIGNED
from botocore.config import Config
from botocore.handlers import disable_signing
import requests
import pandas as pd
import os
import csv


bucket_name = 'XXXXXX'
api2_url = 'https://data.nasdaq.com/api/v3/datasets/ECONOMIST/BIGMAC_ROU.json?start_date=2021-07-01&end_date=2021-07-31&api_key=Bv9SfFKRue5dKpH1bCKk'
#There is the method used for upload data without personal data account credential for task purposes.
#bucket ARN will be sent via e-mail
response = requests.get(api2_url)
json_data = response.json()
json_data = json.dumps(json_data).encode('UTF-8')
s3_client = boto3.client('s3',config=Config(signature_version=UNSIGNED))
s3_client.put_object(Body=(bytes(json_data)), Bucket=bucket_name, Key='test.json')
