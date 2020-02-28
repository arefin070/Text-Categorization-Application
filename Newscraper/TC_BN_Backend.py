import inline as inline
import matplotlib as matplotlib
import numpy as np
import pandas as pd

from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
from numpy import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC

data = pd.read_csv("preProcessedData.csv")

count_vect = CountVectorizer()
text_counts = count_vect.fit_transform(data['Text'])
tfidf_transformer = TfidfTransformer()
text_tfidf = tfidf_transformer.fit_transform(text_counts)

clf = LinearSVC().fit(text_tfidf,  data['Label'])

# content = input("Unidentified content: ")

def getValue(content):
    return clf.predict(count_vect.transform([content]))