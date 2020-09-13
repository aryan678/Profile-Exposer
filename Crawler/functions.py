import keras
import os
import spacy
from pathlib import Path
import time
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
import warnings
import pandas as pd
import pickle


SEQUENCE_LENGTH = 300
tokenizer=Tokenizer()
OUTPUT1='NER Models/Name/content/Model'
OUTPUT2='NER Models/Prefix/content/Model'
OUTPUT3='NER Models/Position Held/Model'


model=keras.models.load_model('Crawler Intelligence/crawler_intelligence.h5')
with open('Crawler Intelligence/tokenizer.pb','rb') as f:
    tokenizer=pickle.load(f)
    
#print("Loading from", OUTPUT_DIR)
nlpN = spacy.load(OUTPUT1)
nlpS = spacy.load(OUTPUT2)
nlpM = spacy.load(OUTPUT3)
def decode_sentiment(score):
    return 0 if score < 0.625 else 1
def predict(text):
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    score = model.predict([x_test])[0]
    return decode_sentiment(score)

