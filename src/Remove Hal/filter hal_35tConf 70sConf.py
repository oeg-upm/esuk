def encontrar(df1,df2,j,suport):
  si=0;
  if int(df1['Resources'][j]['@support'])>suport:
    if df1['Resources'][j]['@URI']==df2['Resources'][j]['@URI']:
      si=1
  return si

import pandas as pd
df = pd.read_csv("../../data/700tokensVal.csv", sep=";")
df["summary"]=df["1"]
df["article"]=df["0"]

resultado=[]
for l in range(0,42597):
  try:
    df2 = pd.read_json("../../data/valS/valS/text"+str(l)+".json")
    df1 = pd.read_json("../../data/val/val/text"+str(l)+".json")
    for j in range(0,len(df2['Resources'])):
      a=encontrar(df1,j,300)
      if a==1:
        resultado.append(j)

df3=df.iloc[resultado].copy()
df3.to_csv("../../data/700tokensValNoHal.csv", sep=';')




df = pd.read_csv("../../data/700tokens.csv", sep=";")
df["summary"]=df["1"]
df["article"]=df["0"]
resultado=[]
for l in range(0,42597):
  try:
    df2 = pd.read_json("../../data/trainS/trainS/text"+str(l)+".json")
    df1 = pd.read_json("../../data/train/train/text"+str(l)+".json")
    for j in range(0,len(df2['Resources'])):
      a=encontrar(df1,j,300)
      if a==1:
        resultado.append(j)

df3=df.iloc[resultado].copy()
df3.to_csv("../../data/700tokensNoHal.csv", sep=';')