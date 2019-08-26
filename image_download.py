import os
import requests
import json
import csv
import pandas as pd

cwd = os.getcwd()
path='data/Indian_Number_plates.json'
df1 = pd.read_json('data/Indian_Number_plates.json',lines=True)
i=0
for data in df1['content']:
    page = requests.get(data)
    f_ext = os.path.splitext(data)[-1]
    f_name = str(i)+'img{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    i+=1
    






