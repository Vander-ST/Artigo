import nltk.corpus
import pandas as pd
import numpy as np
import re
import unidecode
import matplotlib.pyplot as plt
import ipywidgets as widgets
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


stopwords_br = nltk.corpus.stopwords.words('portuguese')
stopwords_br