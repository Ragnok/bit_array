'Apply supervised machine learning to a practical problem using a real dataset'

# https://archive.ics.uci.edu/ml/datasets/iris

from pprint import pprint
from k_nearest import predict
import sqlite3

# Load the data ######################
c = sqlite3.connect('notes/irises.db')
labels = []
points = []
for label, sep_len, sep_wid, pet_len, pet_wid in c.execute('SELECT * FROM Irises;'):
    labels.append(label)
    points.append((sep_len, sep_wid, pet_len, pet_wid))

new_iris = (6.1, 3.5, 4.5, 3.0)
print predict(new_iris, points, labels, k=5)
