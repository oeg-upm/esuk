import pandas as pd
import requests
import json
df = pd.read_csv("700tokensVal.csv", sep=";")
df["summary"]=df["1"]
df["article"]=df["0"]
df.dropna()

for i in range(0,len(df["article"])):
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    }

  data = {
    'text': df["article"][i],
    'confidence': '0.75',
  }

  response = requests.post('http://localhost:2222/rest/annotate', headers=headers, data=data)
  json_object=json.loads(response.text)
  final = json.dumps(json_object, indent=4)
  with open("./val/text"+str(i)+".json", "w") as outfile:
    outfile.write(final)
  print(i)