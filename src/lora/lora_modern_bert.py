import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import LoraConfig, get_peft_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json

MODEL_NAME="cahya/bert-base-indonesian-1.5G"

class TextDS(Dataset):
    def __init__(self,txt,lbl,tok,max_len=128):
        self.txt=txt; self.lbl=lbl; self.tok=tok; self.max_len=max_len
    def __len__(self): return len(self.txt)
    def __getitem__(self,idx):
        enc=self.tok(self.txt[idx],truncation=True,padding="max_length",max_length=self.max_len,return_tensors="pt")
        item={k:v.squeeze(0) for k,v in enc.items()}
        item["labels"]=torch.tensor(self.lbl[idx])
        return item

def train_lora_modern_bert(df,epochs=2,output="results/lora.json"):
    tok = AutoTokenizer.from_pretrained(MODEL_NAME)
    base = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME,num_labels=2)
    cfg = LoraConfig(r=8,lora_alpha=16,lora_dropout=0.1,target_modules=["query","key","value"])
    model = get_peft_model(base, cfg)

    Xtr,Xte,ytr,yte=train_test_split(df["clean_text"],df["label_id"],test_size=0.2,stratify=df["label_id"])

    train_ds=TextDS(Xtr.tolist(),ytr.tolist(),tok)
    test_ds =TextDS(Xte.tolist(),yte.tolist(),tok)

    dl=DataLoader(train_ds,batch_size=2,shuffle=True)
    opt=torch.optim.AdamW(model.parameters(),lr=2e-5)
    device="cuda" if torch.cuda.is_available() else "cpu"
    model=model.to(device)

    for ep in range(epochs):
        model.train()
        for b in dl:
            b={k:v.to(device) for k,v in b.items()}
            out=model(**b)
            opt.zero_grad()
            out.loss.backward()
            opt.step()

    # EVAL
    model.eval()
    preds=[]; labels=[]
    for b in DataLoader(test_ds,batch_size=4):
        b={k:v.to(device) for k,v in b.items()}
        with torch.no_grad():
            out=model(**b)
        preds.extend(torch.argmax(out.logits,dim=1).cpu().numpy())
        labels.extend(b["labels"].cpu().numpy())

    res={"accuracy":float(accuracy_score(labels,preds))}
    with open(output,"w") as f: json.dump(res,f)
    print("[DONE] LORA saved:", output)
