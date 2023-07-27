import torch

import pandas as pd
import csv
from collections import Counter
from tqdm.auto import tqdm, trange
from transformers import MT5ForConditionalGeneration, T5Tokenizer
tokenizer = T5Tokenizer.from_pretrained("google/mt5-large")
model = MT5ForConditionalGeneration.from_pretrained('google/mt5-large')


df_es = pd.read_csv('../data/spa_news_2020_1M/spa_news_2020_1M-sentences.txt', sep='\t', header=None, quoting=csv.QUOTE_NONE)
df_es.columns = ['idx', 'text']
cnt_es = Counter()
for text in tqdm(df_es.text):
    cnt_es.update(tokenizer.encode(text))
print(len(cnt_es), len(cnt_es)/tokenizer.vocab_size)  
new_tokens = set(range(1000))

for i, (k, v) in enumerate(cnt_es.most_common(25_000)):
    if len(new_tokens) == 29_900:
        print(i, 'Esp tokens are included')
        break
    if k not in new_tokens:
        new_tokens.add(k)
for t in range(tokenizer.vocab_size - 100, tokenizer.vocab_size):
    new_tokens.add(t)
print(len(new_tokens))
kept_ids = sorted(new_tokens)

new_size = len(kept_ids)
new_emb = torch.nn.Embedding(new_size, model.shared.embedding_dim)
new_head = torch.nn.Linear(in_features=model.lm_head.in_features, out_features=new_size, bias=False)
for new_id, old_id in enumerate(kept_ids):
    new_emb.weight.data[new_id] = model.shared.weight.data[old_id]
    new_head.weight.data[new_id] = model.lm_head.weight.data[old_id]
model.shared.weight = new_emb.weight
model.lm_head.weight = new_head.weight
model.config.__dict__['vocab_size'] = new_size
model.config.__dict__['_name_or_path'] = 'cointegrated/es5-large'

! wget https://raw.githubusercontent.com/google/sentencepiece/master/src/sentencepiece_model.proto
! protoc --python_out=. sentencepiece_model.proto
import sentencepiece_model_pb2 as spmp
smp = tokenizer.sp_model.serialized_model_proto()
m = spmp.ModelProto()
m.ParseFromString(smp)
print('the loaded model has pieces:', len(m.pieces))
new_pieces = [m.pieces[idx] for idx in kept_ids]
print('the new pieces:', len(new_pieces))
# replace the content of the first 30K pieces
for i, p in enumerate(new_pieces):
    m.pieces[i].piece = p.piece
    m.pieces[i].score = p.score
    m.pieces[i].type = p.type
# drop the remaining pieces
n = len(new_pieces)
for i in trange(len(m.pieces) - n):
    m.pieces.pop(len(m.pieces) - 1)
print(len(m.pieces))
with open('new_sp.model', 'wb') as f:
    f.write(m.SerializeToString())
new_tokenizer = T5Tokenizer('new_sp.model', extra_ids=100)

new_tokenizer.save_pretrained('espt5-large')
model.save_pretrained('espt5-large')