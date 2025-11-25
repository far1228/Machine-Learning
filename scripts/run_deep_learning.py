import pandas as pd
from src.deep_learning.rnn_lstm import train_rnn, train_lstm
from src.deep_learning.ft_lstm import train_ft_lstm

DATA = "data/processed/demographics_qi.csv"

def run():
    df = pd.read_csv(DATA)

    print("\n=== TRAINING RNN ===")
    train_rnn(df, out="results/rnn.json")

    print("\n=== TRAINING LSTM ===")
    train_lstm(df, out="results/lstm.json")

    print("\n=== TRAINING FINE-TUNED LSTM ===")
    train_ft_lstm(df, out="results/ft_lstm.json")


if __name__ == "__main__":
    run()
