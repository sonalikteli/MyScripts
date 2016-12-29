#!/usr/bin/python
# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
#print(dataset)

# shape
print(dataset.shape)

# head - take a peek at the data
print(dataset.head(20))

# descriptions - statistical summary
print(dataset.describe())

	
# class distribution
print(dataset.groupby('class').size())



# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.savefig('test.png')
