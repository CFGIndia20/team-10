import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
import time

import pandas as pd 
# import io 
# from google.colab import files 
# uploaded = files.upload()

# df = pd.read_csv(io.BytesIO(uploaded['cd_mumbai_complaints.csv']))
df = pd.read_csv('cd_mumbai_complaints.csv')
df = df.dropna() 
print(df.created_at)

# GroupBy the category and removing the categories which are less than 10

df1= df.groupby('category_id')['category_id'].count()

df1

s = []
for i in df1.keys():
  if(df1[i]<10):
    s.append(i)

# Dropping those IDS

new_df = df[~df.category_id.isin(s)]

# Cleaning the data and removing contractions 

def clean(text):
    text=re.sub(r"what's","what is ",text)
    text=re.sub(r"it's","it is ",text)
    text=re.sub(r"\'ve"," have ",text)
    text=re.sub(r"i'm","i am ",text)
    text=re.sub(r"\'re"," are ",text)
    text=re.sub(r"n't"," not ",text)
    text=re.sub(r"\'d"," would ",text)
    text=re.sub(r"\'s","s",text)
    text=re.sub(r"\'ll"," will ",text)
    text=re.sub(r"can't"," cannot ",text)
    text = re.sub('[!@#$]',"",text)
    text=re.sub(r"e-mail","email",text)
    text=re.sub(r"< br >+"," ",text)
    text=re.sub(r"\n"," ",text)
    text=re.sub(r":"," ",text)
    text=re.sub(r"-"," ",text)
    text=re.sub(r"\_"," ",text)
    text=re.sub(r"ain't", "am not",text)
    text=re.sub(r"aren't", "are not",text)
    text=re.sub(r"can't","cannot",text)
    text=re.sub(r"can't've", "cannot have",text)
    text=re.sub(r"'cause", "because",text)
    text=re.sub(r"could've", "could have",text)
    text=re.sub(r"couldn't", "could not",text)
    text=re.sub(r"couldn't've", "could not have",text)
    text=re.sub(r"didn't", "did not",text)
    text=re.sub(r"doesn't", "does not",text)
    text=re.sub(r"don't", "do not",text)
    text=re.sub(r"hadn't", "had not",text)
    text=re.sub(r"hasn't", "has not",text)
    text=re.sub(r"haven't", "have not",text)
    text=re.sub(r"how'd", "how did",text)
    text=re.sub(r"how'll", "how will",text)
    text=re.sub(r"how's", "how is",text)
    text=re.sub(r"i'd", "i would",text)
    text=re.sub(r"i'll", "i will",text)
    text=re.sub(r"i'm", "i am",text)
    text=re.sub(r"i've", "i have",text)
    text=re.sub(r"isn't", "is not",text)
    text=re.sub(r"it'd", "it would",text)
    text=re.sub(r"it'll", "it will",text)
    text=re.sub(r"it's", "it is",text)
    text=re.sub(r"let's", "let us",text)
    text=re.sub(r"might've", "might have",text)
    text=re.sub(r"mightn't", "might not",text)
    text=re.sub(r"must've", "must have",text)
    text=re.sub(r"mustn't", "must not",text)
    text=re.sub(r"should've", "should have",text)
    text=re.sub(r"shouldn't", "should not",text)
    text=re.sub(r"that'd", "that would",text)
    text=re.sub(r"that's", "that is",text)
    text=re.sub(r"there'd", "there had",text)
    text=re.sub(r"there's", "there is",text)
    text=re.sub(r"they'd", "they would",text)
    text=re.sub(r"they'll", "they will",text)
    text=re.sub(r"they're", "they are",text)
    text=re.sub(r"they've", "they have",text)
    text=re.sub(r"wasn't", "was not",text)
    text=re.sub(r"wouldn't","would not",text)
    text=re.sub(r"what's","what is ",text)
    text=re.sub(r"what's","what is ",text)
    text=re.sub(r"what're","what are",text)
    text=re.sub(r"where's","where is",text)
    text=re.sub(r"\,"," ",text)
    text=re.sub(r"\;"," ",text)
    text=re.sub(r"\d+"," ",text)
    text=re.sub(r"[$#@%&*!~?%{}()]"," ",text)
    text=re.sub(r"\.+",". ",text)
    text=re.sub(r"\ +"," ",text)
    text=re.sub(r"\\+"," ",text)
    text=re.sub(r"\/+"," ",text)
    text=re.sub(r"<br >","",text)
    text=re.sub(r"<br  >","",text)
    text=re.sub(r"<br />","",text)
    return text

# Remove unwanted characters, stopwords, and format the text to create fewer nulls word embeddings'''

def clean_text(text):
    
    # Convert words to lower case
    text = text.lower()
    # Optionally, remove stop words
    text = clean(text)
    text = text.split()
    stops = set(stopwords.words("english"))
    stops.remove('no')
    stops.remove('not')
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Clean the summaries and texts
complain = []
for c in new_df.created_at:
    complain.append(clean_text(c))
print("Complain Appended")

new_df['complain'] = complain

fini = pd.DataFrame(list(zip(new_df['complain'], new_df['category_id'])), 
               columns =['Complain', 'Category_id'])

t = fini['Complain'].apply(lambda x: x.split())
t.head()

from nltk.stem.porter import *
stemmer = PorterStemmer()
t = t.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
t.head()

s = []
for i in range(len(t)):
  temp = ""
  for j in t[i]:
    temp+=j+" "
  temp.strip(" ")
  s.append(temp)

from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer

fini['Com'] =s

train_x, valid_x, train_y, valid_y = model_selection.train_test_split(fini['Com'],fini['Category_id'])

tfidf_vect_ngram = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000)
tfidf_vect_ngram.fit(fini['Com'])

xtrain_tfidf_ngram =  tfidf_vect_ngram.transform(train_x)
xvalid_tfidf_ngram =  tfidf_vect_ngram.transform(valid_x)

import pickle

filename1 = 'tfidf_pre.pkl'
pkl_file1 = open(filename1, 'wb')
pickle.dump(tfidf_vect_ngram, pkl_file1)

pkl_file1.close()

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn import metrics

models = [
    RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]

# 5 Cross-validation
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))

entries = []
for model in models:
  model_name = model.__class__.__name__
  accuracies = cross_val_score(model, xtrain_tfidf_ngram, train_y, scoring='accuracy', cv=CV)
  for fold_idx, accuracy in enumerate(accuracies):
    entries.append((model_name, fold_idx, accuracy))
    
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

mean_accuracy = cv_df.groupby('model_name').accuracy.mean()
std_accuracy = cv_df.groupby('model_name').accuracy.std()

acc = pd.concat([mean_accuracy, std_accuracy], axis= 1, 
          ignore_index=True)
acc.columns = ['Mean Accuracy', 'Standard deviation']
acc

model = LinearSVC()
model.fit(xtrain_tfidf_ngram, train_y)
y_pred = model.predict(xvalid_tfidf_ngram)

# Statistics of the ML model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, cohen_kappa_score

print(confusion_matrix(valid_y, y_pred))
print('Accuracy', accuracy_score(valid_y, y_pred) * 100)
print(classification_report(valid_y, y_pred))
print('Cohen Kappa score:', cohen_kappa_score(valid_y, y_pred))

filename = 'classify.pkl'
pkl_file = open(filename, 'wb')
pickle.dump(model, pkl_file)
pkl_file.close()

import pickle
import numpy as np
from sklearn.svm import LinearSVC

modelling = LinearSVC()

filename = 'classify.pkl'
with open(filename, 'rb') as f:
    modelling.clf = pickle.load(f)

filename1 = 'tfidf_pre.pkl'
with open(filename1, 'rb') as f:
    modelling.vectorizer = pickle.load(f)
print(modelling)

print(modelling.clf.predict(modelling.vectorizer.transform(["garbage"])))