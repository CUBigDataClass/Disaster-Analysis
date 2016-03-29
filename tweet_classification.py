import csv
import re
from math import log
from random import shuffle
from nltk.corpus import stopwords

from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet

import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression, chi2
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import argparse

def get_tag(tag):
    if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
        return wordnet.NOUN
    elif tag in ['RB', 'RBR', 'RBS']:
        return wordnet.ADV
    elif tag in ['JJ', 'JJR', 'JJS']:
        return wordnet.ADJ
    else:
        return wordnet.VERB


def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stems = [stemmer.stem(t) for t in tokens]
    return stems

def tokenize_doc(doc):
    text = word_tokenize("And now for something completely different")

    wnl = WordNetLemmatizer()
    tok = word_tokenize(doc)
    pos_list = pos_tag(tok)
    tokens = [wnl.lemmatize(pt[0], get_tag(pt[1])) for pt in pos_list]
    #~ stems = stem_tokens(tokens)
    #~ return stems
    return tokens

def classify(text, label):
    #~ Testing purpose: 10-fold cross validation
    cv = KFold(n = len(label), n_folds = 10)

    clf = Pipeline([
            ('vect',
                    CountVectorizer(
                            analyzer='word',
                            ngram_range=(1, 1),
                            stop_words = 'english',
                            lowercase=True,
                            token_pattern=r'\b\w+\b',
                            tokenizer=tokenize_doc,
                            min_df = 1)),
            ('feature_selection',
                    SelectKBest(
                            chi2,
                            k=35)),
            ('classification',
                    SVC())
    ])

    print "len(label) ", len(label), " | text ", len(text)
    print ""

    clf.fit(np.asarray(text), np.asarray(label))

    cv_score = cross_val_score(clf, text, label, cv = cv, verbose = 1)
    print "Accuracy List ", cv_score, " | Avg Accuracy ", np.mean(cv_score)


    #~ return pred_y


#~ '''
if __name__ == "__main__":

    training_data = []
    i = 0

    with open('disaster-tweets-DFE.csv', 'rb') as data:
        has_header = csv.Sniffer().has_header(data.read(1024))
        data.seek(0)
        csvreader = csv.reader(data)
        if has_header:
            next(csvreader)

        for row in csvreader:
            #~ if i < 10:
                #~ i+=1
            tmp = []
            tmp.append(row[5])
            tmp.append(row[10])
            training_data.append(tmp)

    #~ for i in training_data:
        #~ print "i ", i
    print "len of training data ", len(training_data)

    classify(
        [lst[1] for lst in training_data],
        [lst[0] for lst in training_data])
