'''
* Create a robost supervised machine learning tool

* Practice incremental development

* Learn to combine tools from the standard library
  to build interesting functions out of existing
  capabilities.

'''

from pprint import pprint
from distance import dist
from functools import partial
from heapq import nsmallest
from collections import Counter
from itertools import izip
import csv

# Acquire observations and train the model ################

def load_happy(filename='notes/happy.csv', has_header=True, label_loc=0):
    labels = []                 # hard to measure feature
    points = []                 # easy to measure features
    with open(filename) as f:
        it = iter(csv.reader(f))
        if has_header:
            headers = next(it)
        for row in it: 
            labels.append(row[label_loc])
            points.append(tuple(map(int, row[1:])))
    return points, labels

# Predictions #############################################

def predict(score, points, labels, k=3):
    ''' Predict a person's label from their *score*, by finding
        the *k* closest scores in the *points* which have a given
        list of known *labels*.

        This is called a supervised machined learning categorization
        problem where the underlying assumption is that people who
        are like you are like you.
    '''
    knn = set(nsmallest(k, points, key=partial(dist, score)))
    label_counter = Counter(label for label, point in izip(labels, points) if point in knn)
    # Return the MLE (maximum likelihood estimator) or MAP (maximum a posteriori modal value)
    return label_counter.most_common(1)[0][0]

if __name__ == '__main__':
    points, labels = load_happy()
    print predict((30, 50, 25), points, labels, k=3)
