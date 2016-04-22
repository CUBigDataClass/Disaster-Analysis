from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import csv
import re

from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.feature_selection import SelectKBest, f_regression, chi2

from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.metrics import accuracy_score

import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
    wnl = WordNetLemmatizer()
    tok = word_tokenize(doc)
    #~ pos_list = pos_tag(tok)
    #~ tokens = [wnl.lemmatize(pt[0], get_tag(pt[1])) for pt in pos_list]
    tokens = [wnl.lemmatize(t, wordnet.VERB) for t in tok]
    #~ stems = stem_tokens(tokens)
    #~ return stems
    return tokens


def test_feature(clf, test):
    # return clf.transform(np.asarray(test))
    return clf.fit(np.asarray(test))

def classify_tweet(clf, test_vector):
    return clf.predict(np.asarray(test_vector))

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.train = []
        self.label = []
        self.tweet_count = 0
        self.tweet_list = []

        with open('/home/ec2-user/storm_kafka/wordcount/src/bolts/disaster-tweets-DFE.csv', 'rb') as data:
            has_header = csv.Sniffer().has_header(data.read(1024))
            data.seek(0)
            csvreader = csv.reader(data)
            if has_header:
                next(csvreader)

            for row in csvreader:
                self.train.append(row[10])
                self.label.append(row[5])

        self.clf = Pipeline([
                        ('vect',
                                TfidfVectorizer(
                                        analyzer='word',
                                        ngram_range=(1, 1),
                                        stop_words = 'english',
                                        lowercase=True,
                                        token_pattern=r'\b\w+\b',
                                        tokenizer=tokenize_doc,
                                        min_df = 1)),
                        #('dim_reduction',
                        #        TruncatedSVD(n_components=1000)),
                        ('classification',
                                MultinomialNB())
                                #~ LogisticRegression())
                                #~ SVC(kernel = 'linear'))
                ])

        self.clf.fit(np.asarray(self.train), np.asarray(self.label))


    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1

        self.tweet_count += 1
        #if (len(self.tweet_list) == 0):
        #    self.tweet_list.append("ghost ********* SSS")
        #else:
        self.tweet_list.append(word)

        if (len(self.tweet_list) >= 200):
            msg = "ghost EEEEEEEEEEEEEEEEE"
            self.log('%s: %d %d' % (msg, len(self.tweet_list), self.tweet_count))
            #tv = test_feature(self.clf, self.tweet_list)
            c = classify_tweet(self.clf, self.tweet_list)

            msg = "ghost CCCCCCCCCCCCCCCCC"
            self.log('%s: %s %d' % (msg, len(c), self.tweet_count))
            for i in range(len(c)):
                if c[i] == "Relevant":
                    msg = "ghost CCCCCCCCCCCCCCCCCVVVVVVVVVVVVVV"
                    self.log('%s: %s | %s' % (msg, c[i], self.tweet_list[i]))

            self.tweet_list = []

        self.emit([word, self.counts[word]])
        #if c is 1:
        pred = 9998765
        #else:
        #    pred = 7777777
        self.log('%s: %d' % (word, pred))
