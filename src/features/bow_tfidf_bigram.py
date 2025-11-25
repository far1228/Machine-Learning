from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

def extract_bow(df, out):
    vec = CountVectorizer(min_df=2, max_df=0.95)
    X = vec.fit_transform(df["clean_text"])
    pd.DataFrame(X.toarray(),columns=vec.get_feature_names_out()).to_csv(out,index=False)

def extract_tfidf(df, out):
    vec = TfidfVectorizer(min_df=2, max_df=0.95)
    X = vec.fit_transform(df["clean_text"])
    pd.DataFrame(X.toarray(),columns=vec.get_feature_names_out()).to_csv(out,index=False)

def extract_bigram(df, out):
    vec = CountVectorizer(ngram_range=(2,2),min_df=2,max_df=0.95)
    X = vec.fit_transform(df["clean_text"])
    pd.DataFrame(X.toarray(),columns=vec.get_feature_names_out()).to_csv(out,index=False)
