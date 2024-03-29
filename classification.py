import pickle
import numpy as np
from sklearn.svm import LinearSVC

def category(text):
    modelling = LinearSVC()
    filename = 'classify.pkl'
    with open(filename, 'rb') as f:
        modelling.clf = pickle.load(f)
    filename1 = 'tfidf_pre.pkl'
    with open(filename1, 'rb') as f:
        modelling.vectorizer = pickle.load(f)
    print(modelling)
    resp = modelling.clf.predict(modelling.vectorizer.transform([]))
    print(resp)
