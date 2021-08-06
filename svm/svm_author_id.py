#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm

clf = svm.SVC(kernel="rbf",C=10000.0)
clf.fit(features_train,labels_train)

pred = clf.predict(features_test)

print(pred[10])
print(pred[26])
print(pred[50])

print(sum([i==1 for i in pred]))

from sklearn.metrics import accuracy_score

print("accuracy:{}".format(accuracy_score(pred,labels_test)))
#########################################################


