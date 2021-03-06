# -*- coding: utf-8 -*-
"""Simple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N5Nt4nZaFsWCMXyQVbyYrNhiVx6L4EYO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/content/StudentHoursScores.csv')

df.describe()

df.info()

df.columns

df.dtypes

df.shape

df.corr()

x = df['Hours']
y = df['Scores']

plt.title("Study hours VS Score")
plt.xlabel('Hours of study')
plt.ylabel('Score')
plt.scatter(x,y,color='red',marker='*')

plt.show()

x = df.iloc[:,:-1].values
y = df.iloc[:,1].values

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

model = LinearRegression()
model.fit(xtrain,ytrain)

y_predict = model.predict(xtest)
print(y_predict)

print(ytest)

model.coef_

model.intercept_

model.predict([[5]])

"""## Training set """

plt.scatter(xtrain,ytrain, color='red')
plt.plot(xtrain,model.predict(xtrain))
plt.show()

"""## Test set """

plt.scatter(xtest,ytest, color='red')
plt.plot(xtest,model.predict(xtest))
plt.show()

"""## Error"""

print("Mean squared error: %.2f" % np.mean((model.predict(xtest) - ytest) ** 2))

