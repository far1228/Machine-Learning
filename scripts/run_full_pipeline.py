import pandas as pd
import os

from src.anonymization.demo_anonymizer import anonymize_text
from src.preprocessing.preprocessing_demo import preprocess_serialized_text
from src.qi_labeling.qi_demo import add_qi_scores

def run():
    df=pd.read_csv("data/raw/demographics_serialized.csv")
    df["text_anonymized"]=df["text_serialized"].apply(anonymize_text)
    df["clean_text"]=df["text_anonymized"].apply(preprocess_serialized_text)
    df=add_qi_scores(df)
    df.to_csv("data/processed/demographics_qi.csv",index=False)
    print("[DONE] full pipeline demographic")

if __name__=="__main__":
    run()
