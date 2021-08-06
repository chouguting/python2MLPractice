#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( "TOTAL", 0 )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
largest=0
email=""
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

print(email)
a = [(i['salary']> 1000000 and i['bonus']> 5000000 and i['salary']!='NaN' and i['bonus']!='NaN') for i in data_dict.values()]
print(a)

for i in range(len(a)):
    if a[i]:
        print(data_dict.keys()[i])

#print(i['bonus']> for i in data.values())