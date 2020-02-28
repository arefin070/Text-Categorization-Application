from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from bs4 import BeautifulSoup
import requests
import unicodedata
import io
from http import cookies
from .forms import customform

import numpy as np
import pandas as pd
from numpy import random

from warnings import simplefilter

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.svm import LinearSVC

def custom(request):
    return render(request, 'custom.html')

def suggetion(request):
    strn = request.GET['strn']
    data = pd.read_csv('C:\\Users\\Asus\\Downloads\\Newscraper-master\\Newscraper-master\\search\\preProcessedData.csv')
    count_vect = CountVectorizer()
    text_counts = count_vect.fit_transform(data['Text'])
    tfidf_transformer = TfidfTransformer()
    text_tfidf = tfidf_transformer.fit_transform(text_counts)
    clf = LinearSVC().fit(text_tfidf, data['Label'])

    result = clf.predict(count_vect.transform([strn]))

    return render(request, 'suggetion.html', {'result': result, 'string': strn})
