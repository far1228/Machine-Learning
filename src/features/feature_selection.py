from sklearn.feature_selection import SelectKBest, chi2
import pandas as pd

def select_features(input_file, out_file, k=1000):
    df = pd.read_csv(input_file)
    y = pd.read_csv("data/processed/demographics_qi.csv")["label"]
    selector = SelectKBest(chi2,k=min(k,df.shape[1]))
    X = selector.fit_transform(df, y)
    sel_cols = df.columns[selector.get_support()]
    pd.DataFrame(X,columns=sel_cols).to_csv(out_file,index=False)
