from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
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
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

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
    #~ pos_list = pos_tag(tok)
    #~ tokens = [wnl.lemmatize(pt[0], get_tag(pt[1])) for pt in pos_list]
    tokens = [wnl.lemmatize(t, wordnet.VERB) for t in tok]
    #~ stems = stem_tokens(tokens)
    #~ return stems
    return tokens

class WordCounter(Bolt):

    #def initialize(self, conf, ctx):
    #    self.counts = Counter()
    def initialize(self, conf, ctx):
        train = []
        label = []
        i = 0
    
        with open('/home/ec2-user/storm_kafka/wordcount/src/bolts/disaster-tweets-DFE.csv', 'rb') as data:
            has_header = csv.Sniffer().has_header(data.read(1024))
            data.seek(0)
            csvreader = csv.reader(data)
            if has_header:
                next(csvreader)
    
            for row in csvreader:
                #~ if i < 10:
                    #~ i+=1
                train.append(row[10])
                label.append(row[5])

        #print "ghost len of training data ", len(training_data)

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
                        ('dim_reduction',
                                TruncatedSVD(n_components=1000)),
                        #~ ('feature_selection',
                                #~ SelectKBest(
                                        #~ chi2,
                                        #~ k=35)),
                        ('classification',
                                MultinomialNB())
                                #~ LogisticRegression())
                                #~ SVC(kernel = 'linear'))
                ])

        self.clf.fit(np.asarray(train), np.asarray(label))

    def test_feature(self, test):
        return self.clf.transform(np.asarray(test))

    def classify_tweet(self, test_vector):
        return self.clf.predict(np.asarray(test_vector))

    def process(self, tup):
        sentence = tup.values[0]  # extract the sentence
        sentence = re.sub(r"[,.;!\?]", "", sentence)  # get rid of punctuation
        words = [[word.strip()] for word in sentence.split(" ") if word.strip()]
        if not words:
            # no words to process in the sentence, fail the tuple
            self.fail(tup)
            return

        #self.emit([sentence, 9999])
        tf = test_feature(sentence)
        pred = classify_tweet(tf)
        pred = 9999
        self.emit([sentence, pred])

        #word = tup.values[0]
        #self.counts[word] += 1
        #self.emit([word, self.counts[word]])
        #self.log('%s: %d' % (word, self.counts[word]))
