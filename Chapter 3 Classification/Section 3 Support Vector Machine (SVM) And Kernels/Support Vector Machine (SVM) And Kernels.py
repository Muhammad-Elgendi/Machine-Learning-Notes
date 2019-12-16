#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Support Vector Machine (SVM) And Kernels
"""
# import dataset
# import pandas library and give it "pd" as alias
import pandas as pd
# read dataset from csv file
dataset = pd.read_csv("Social_Network_Ads.csv")

# show first five observation of the dataset
# print(dataset.head())
# To see the statistical details of the dataset, we can use describe():
# print(dataset.describe())

# we are intersted in Age ,EstimatedSalary ,and Purchased features
# split the dataset to dependant and independant variables
# dependant variable is Purchased
# y = dataset.iloc[:,-1].astype(float).values
# here we used astype() which Cast a pandas object to
# a specified dtype. and we want to cast it float so
# that we can apply feature scaling with StandardScaler class
# without any warning
y = dataset.iloc[:,-1]
# independant variables are Age ,EstimatedSalary
x = dataset.iloc[:,2:-1]

# split dataset to training set and test set
# import train_test_split class
from sklearn.cross_validation import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,
                                                 random_state = 42)

# apply feature scaling to independant variables x
# import StandardScaler class
from sklearn.preprocessing import StandardScaler
# create instance of StandardScaler
xScaler = StandardScaler()
# scale x_train
x_train = xScaler.fit_transform(x_train)
# scale x_test to the same scale that fitted to x_train
x_test = xScaler.transform(x_test)

"""
What's the support vector machine ?
"""

"""
What is the kernel ?
"""

"""
What is the kernel trick ?
"""

"""
What are the different types of kernels ?
"""

# split observations to purchased and not purchased
# filter out the purchased observations
purchased = dataset.loc[y == 1]
# filter out the not purchased observations
not_purchased = dataset.loc[y == 0]

# visualize true observations from the dataset
# import matplotlib.pyplot and give it "plt" as an alias
import matplotlib.pyplot as plt
# create new figure
plt.figure()
# plot purchased observations in green color
plt.scatter(purchased.iloc[:,3], purchased.iloc[:,2], label='Purchased' ,color="blue")
# plot not_purchased observations in red color
plt.scatter(not_purchased.iloc[:,3], not_purchased.iloc[:,2], label='Not Purchased' ,color="brown")
plt.title('Age vs Estimated Salary')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
# adjust the padding of the figure
plt.tight_layout()
# export the figure to an image
plt.savefig("Age vs Estimated Salary.png")

"""
What is linear SVM ?
"""

# Now let's create a linear SVM classifier
# import SVC class from svm module
from sklearn.svm import SVC
# create an instance of SVC with these parameters
linearClassifier = SVC(kernel = 'linear', random_state =0)
# fit (train) the linearClassifier into training set
linearClassifier.fit(x_train,y_train)
# test the linearClassifier on the test set
y_linear_predicted = linearClassifier.predict(x_test)

# calculate the confusion matrix
"""
What is confusion matrix ?

"""
# import confusion_matrix class
from sklearn.metrics import confusion_matrix
confusionMatrixForLinear = confusion_matrix(y_test,y_linear_predicted)
# print confusionMatrixForLinear
print("Confusion matrix for linear kernel : \n"+ str(confusionMatrixForLinear))


# visualize the linear SVM with the test set
# import numpy and give it an alias "np"
import numpy as np
from matplotlib.colors import ListedColormap

# create new figure
plt.figure()

# assign x and y sets to your sets
# (Note! these sets must be a numpy array)
X_set, y_set = x_test, y_test.values

# create coordinate matrices from coordinate vectors.(mesh grid)
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))

# plot the model decision boundary
plt.contourf(X1, X2, linearClassifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))

# plot scaled observations
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
    
# set limits of axes
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

# show the legend of the figure
plt.legend()

# set title and axes labels
plt.title('Age vs Estimated Salary (linear SVM Test set classification)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')

# adjust the padding of the figure
plt.tight_layout()

# export the figure to an image
plt.savefig("linear SVM (Test set classification).png")

# show the figure
plt.show()

"""
What is radial basis function kernel ?
"""
# Now let's create a SVM classifier with radial basis function kernel
# import SVC class from svm module
from sklearn.svm import SVC
# create an instance of SVC with these parameters
radialClassifier = SVC(kernel = 'rbf', random_state =0)
# fit (train) the radialClassifier into training set
radialClassifier.fit(x_train,y_train)
# test the radialClassifier on the test set
y_radial_predicted = radialClassifier.predict(x_test)

# calculate the confusion matrix
"""
What is confusion matrix ?

"""
# import confusion_matrix class
from sklearn.metrics import confusion_matrix
confusionMatrixForRadial = confusion_matrix(y_test,y_radial_predicted)
# print confusionMatrixForRadial
print("Confusion matrix for RBF kernel : \n"+ str(confusionMatrixForRadial))


# visualize the RBF kernel classifier with the test set
# import numpy and give it an alias "np"
import numpy as np
from matplotlib.colors import ListedColormap

# create new figure
plt.figure()

# assign x and y sets to your sets
# (Note! these sets must be a numpy array)
X_set, y_set = x_test, y_test.values

# create coordinate matrices from coordinate vectors.(mesh grid)
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))

# plot the model decision boundary
plt.contourf(X1, X2, radialClassifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))

# plot scaled observations
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
    
# set limits of axes
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

# show the legend of the figure
plt.legend()

# set title and axes labels
plt.title('RBF kernel classifier (Test set classification)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')

# adjust the padding of the figure
plt.tight_layout()

# export the figure to an image
plt.savefig("RBF kernel classifier (Test set classification).png")

# show the figure
plt.show()
