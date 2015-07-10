import os
import timeit
import numpy as np
from collections import defaultdict

from sklearn.metrics import precision_recall_curve, roc_curve
from sklearn.metrics import auc
from sklearn.cross_validation import ShuffleSplit
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib

from utils import plot_roc, plot_confusion_matrix, GENRE_DIR, GENRE_LIST, TEST_DIR

from ceps import read_ceps, create_ceps, read_ceps_test

from pydub import AudioSegment

genre_list = GENRE_LIST

clf = None

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#          Please run the classifier script first
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def test_model_on_single_file(file_path):
    clf = joblib.load('data/model_ceps.pkl')
    create_ceps(test_file)
    fnpy = file_path[:-3]+"ceps.npy"
    print fnpy
    X, y = read_ceps_test(fnpy)
    probs = clf.predict_proba(X)
    print str(probs)
    #print "\t".join(str(x) for x in traverse)
    #print "\t".join(str("%.3f" % x) for x in probs[0])
    probs=probs[0]
    max_prob = max(probs)
    for i,j in enumerate(probs):
        if probs[i] == max_prob:
            max_prob_index=i
    
    print max_prob_index
    predicted_genre = genre_list[max_prob_index]
    print "\n\npredicted genre = ",predicted_genre
    return predicted_genre

if __name__ == "__main__":


    test_file = "/home/eduardo/Downloads/genres/test/reggae.wav"
    # should predict genre as "ROCK"
    predicted_genre = test_model_on_single_file(test_file)
    