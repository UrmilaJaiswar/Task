# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K02f2w8O85ZFDsfc5HaFxC5XDWEb9J33

Linear Regression with Python scikit Learn

In this section we will see how the Python scikit-Learn library for machine learning can be used to implement Regression functions.We will start 
with simple linear regression involving two variables.

Simple Linear Regression

In this regression task we will predict the percentage of marks that a student is expected to score based upon the number of hours they 
studied. This is a simple linear regression task as it invoves just two variables.
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing all libraries required in this notebook
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

# Reading dara from remote link
url = "https://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")

s_data.head(10)

s_data.shape

s_data.dtypes

s_data.describe()

"""Checking for null values"""

s_data.isna().sum()

"""Exploratory Data Analysis (EDA)


Visualizing with scatter plot
"""

# Plotting the distribution of scores
s_data.plot(x='Hours', y='Scores', style='o')  
plt.legend()
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()

"""From the above graph, we can clearly see that there is a positive linear relation between the number of hours studied and percentage of score


Visualizing using histogram
"""

plt.hist(s_data["Hours"])
plt.title("Hours")
plt.grid()
plt.show()

s_data.Hours.value_counts().plot(kind='bar')

s_data.Scores.value_counts().plot(kind='bar')

sns.barplot(x="Hours",y="Scores",data=s_data)

"""Checking for Outlier Values"""

sns.boxplot(s_data["Hours"])

sns.boxplot(s_data["Scores"])

"""From above boxplot representation, it is clear that there are no outlier values in the data

Correlation
"""

cor_mat= s_data.corr()    #correlation using heatmap representation    
print(cor_mat)           
sns.heatmap(cor_mat,vmax=1, vmin=-1, annot=True, linewidths=1.5, cmap="YlGnBu")

"""From above correlation matrix, It is clear that Hours and Scores are strongly correlated

Visualizing using basic line plot
"""

from matplotlib import style
style.use("ggplot")
df = s_data.sort_values(["Hours","Scores"])
df.plot(x="Hours",y="Scores")
plt.grid(True,color="blue")
plt.show()

from sklearn import preprocessing
a= np.array(s_data['Scores'])
normalized_a = preprocessing.normalize([a])
normalized_a

sns.distplot(normalized_a,color="r")

from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(s_data)
cov_matrix = np.cov(X_std.T)
print('Covariance Matrix \n%s', cov_matrix)

X_std_df = pd.DataFrame(X_std)
axes = pd.plotting.scatter_matrix(X_std_df)
plt.tight_layout()

"""Preparing the data

Dividing the data info attributes (Inpurs) and labels (Outputs)
"""

X = s_data["Hours"]
y = s_data["Scores"]

X=X.values.reshape(-1, 1)
X

y.head()

"""Splitting the data into training and test sets

Now we have our attributes and labels, gence, next step is to splot the data into training and test sets. We will do this by using Scikit-Learn's built-in train_test_split() method
"""

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, random_state=0)

"""Training the Algoritham

We have split our data into training and testing sets, and next step is to train our algoritham.

Using Linear Regression for modelling
"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("Training complete.")

regressor.coef_

regressor.intercept_

"""Making Predictions

Since we have trained our algoritham, now we have to do some predictions.
"""

print(X_test)

y_pred = regressor.predict(X_test)
y_pred

"""Comparing Actual Vs Predicted"""

Results = pd.DataFrame(columns=["Hours","Actual","Predicted"])
Results["Actual"]= y_test
Results["Predicted"] = y_pred
Results["Hours"] = X_test
Results=Results.reset_index()
Results

"""Visualizing Training Dataset Results"""

plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="red")
plt.title("Hours Studied Vs Percentage Score - Training Set")
plt.xlabel("Hours Studied")
plt.ylabel("Percentage Score")
plt.show()

"""Visualising Testing Dataset Results

What will be the predicted score if a student studies for 9.25 hrs/day?
"""

hours = 9.25
prediction = regressor.predict([[hours]])
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(prediction[0]))

"""Evaluating The Model

The metrics here we use to evaluate regression model are:

Mean Absoluate Error,

Mean Square Error,

Root Mean Square Error
"""

from sklearn import metrics
import math
print("Mean Absolute Error : ",metrics.mean_absolute_error(y_pred,y_test))

print("Mean Square Error :",metrics.mean_absolute_error(y_pred,y_test))
print()
print("Root Mean Square Error :",math.sqrt(metrics.mean_absolute_error(y_pred,y_test)))

"""Calculating Training Error"""

y_pred_training = regressor.predict(X_train)
print("Root Mean Square Error :",math.sqrt(metrics.mean_absolute_error(y_pred_training,y_train)))

"""Checking R^2 (Coefficient of determination) regression score function

R squared is a measure of how close the data are to the fitted regression line.

It is also known as coefficient of determination or coefficient of multiple determination for multiple regression.

Best possible score is 1.0
"""

from sklearn.metrics import r2_score
r2_score(y_test,y_pred)