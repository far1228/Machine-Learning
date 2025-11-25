import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

def bench(X,y):
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    models={
        "LR":LogisticRegression(max_iter=500),
        "NB":MultinomialNB()
    }
    res=[]
    for name,model in models.items():
        model.fit(X_train,y_train)
        pred=model.predict(X_test)
        res.append((name,accuracy_score(y_test,pred),f1_score(y_test,pred,average="weighted")))
    return res

def benchmark_models(label_path,bow_path,tfidf_path,bigram_path,output):
    df=pd.read_csv(label_path)
    y=df["label"]

    rows=[]
    for name,file in [("BoW",bow_path),("TFIDF",tfidf_path),("BIGRAM",bigram_path)]:
        X=pd.read_csv(file)
        r=bench(X,y)
        for m,acc,f1 in r:
            rows.append([name,m,acc,f1])

    pd.DataFrame(rows,columns=["Feature","Model","Acc","F1"]).to_csv(output,index=False)
