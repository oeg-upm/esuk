from transformers import (AdamW, MT5ForConditionalGeneration, T5TokenizerFast as T5Tokenizer)
from tqdm.auto import tqdm

import pandas as pd
train_df=pd.read_json("./spanish/spanish/train.json", lines=True)

MODEL_NAME="../espt5-small"
tokenizer=T5Tokenizer.from_pretrained(MODEL_NAME)

res=[]
for i in range(0,len(train_df["article"])):
  if (len(tokenizer.encode(train_df["article"][i]))<600)&(len(tokenizer.encode(train_df["article"][i]))>1300):
    res.append([train_df["article"][i],train_df["summary"][i]])

with open(f'./datos.txt', 'w', encoding='utf-8') as fp:
  fp.write('\n'.join(pd1[0]).join(pd1[1]))