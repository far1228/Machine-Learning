import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import json

def prepare_sequences(df, max_words=20000, max_len=100):
    texts = df["clean_text"].astype(str).tolist()
    labels = (df["label"] == "HIGH_RISK").astype(int).values

    tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
    tokenizer.fit_on_texts(texts)

    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=max_len, padding="post")

    X_train, X_test, y_train, y_test = train_test_split(
        padded, labels, test_size=0.2, random_state=42, stratify=labels
    )

    return tokenizer, X_train, X_test, y_train, y_test


def build_rnn(vocab_size, max_len=100):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, 64, input_length=max_len),
        tf.keras.layers.SimpleRNN(64),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model


def build_lstm(vocab_size, max_len=100):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, 128, input_length=max_len),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model


def train_rnn(df, out="results/rnn.json"):
    tokenizer, X_train, X_test, y_train, y_test = prepare_sequences(df)
    model = build_rnn(20000)

    model.fit(X_train, y_train, epochs=3, batch_size=32, validation_split=0.2)
    _, acc = model.evaluate(X_test, y_test, verbose=0)

    with open(out, "w") as f:
        json.dump({"accuracy": float(acc)}, f)

    print("[DONE] RNN accuracy:", acc)


def train_lstm(df, out="results/lstm.json"):
    tokenizer, X_train, X_test, y_train, y_test = prepare_sequences(df)
    model = build_lstm(20000)

    model.fit(X_train, y_train, epochs=3, batch_size=32, validation_split=0.2)
    _, acc = model.evaluate(X_test, y_test, verbose=0)

    with open(out, "w") as f:
        json.dump({"accuracy": float(acc)}, f)

    print("[DONE] LSTM accuracy:", acc)
