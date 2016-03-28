import csv
from re import split
from math import log
from random import shuffle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

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


def classify(text, label):

    #~ Testing purpose: 10-fold cross validation
    cv = KFold(n = len(label), n_folds = 10)

    clf = Pipeline([
            ('vect',
                    CountVectorizer(
                            analyzer='word',
                            ngram_range=(1),
                            stop_words = 'english',
                            lowercase=True,
                            token_pattern=r'\b\w+\b',
                            min_df = 1)),
            ('feature_selection',
                    SelectKBest(
                            chi2,
                            k=35)),
            ('classification',
                    SVC())
    ])

    print "len(label) ", len(label), " | text ", len(text)

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
            print "class ", row[5]
            print "text ", row[10]
            tmp.append(row[5])
            tmp.append(row[10])
            training_data.append(tmp)

    #~ for i in training_data:
        #~ print "i ", i
    print "len of training data ", len(training_data)
    print ""

    classify(
        [lst[1] for lst in training_data],
        [lst[0] for lst in training_data])
