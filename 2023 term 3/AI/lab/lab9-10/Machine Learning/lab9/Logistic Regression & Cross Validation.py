#!/usr/bin/env python
# coding: utf-8

# # <center> Scikit Learn Introuduction </center>
# 

# ### Installation
# https://scikit-learn.org/stable/install.html
# 
# ### User Guide
# https://scikit-learn.org/stable/user_guide.html

# # <center> Logistic Regression & Cross Validation </center>

# # pyDataset
# Library documentation: https://pydataset.readthedocs.io/en/latest/

# In[1]:


from pydataset import data
data()


# In[ ]:


import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)



# In[ ]:


admit= data('admit')
admit


# In[ ]:


data('admit', show_doc=True)



# In[ ]:


admit.plot()


# # Logistic Regression & Cross Validation
# 
# We will use logistic regression to classify breast cancer as either malignant or benign. First run the code below to print and read the description of the dataset. 

# In[ ]:


from sklearn.datasets import load_breast_cancer
import numpy as np

DataCancer=load_breast_cancer()
print(DataCancer.keys())
print(DataCancer.DESCR)

X_features=DataCancer.data
Y_targetClass=DataCancer.target


# In[ ]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
import numpy as np

DataCancer=load_breast_cancer()

X_features=DataCancer.data
Y_targetClass=np.ravel(DataCancer.target)

X_train, X_test, Y_train, Y_test = train_test_split(
    X_features, Y_targetClass, random_state=42)
c=1

FittedLogRegModel= LogisticRegression(C=c,max_iter=10000).fit(X_train,Y_train)
    
test_score = FittedLogRegModel.score(X_test, Y_test)
print("Test set score", test_score)


# In[ ]:


from IPython.display import Image
Image("overfitting.png")


# ### A) Using logistic regression, with ridge regularization and tuning parameter set to 1. Then, we will find the accuracy of the model. Scale the features  to have zero mean and unit variance. 
# - Use random_state = 0 in the train_test_split.

# In[ ]:


from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st_scaler_x = preprocessing.StandardScaler()
x_scaled = st_scaler_x.fit_transform(X_features)
X_train, X_test, Y_train, Y_test = train_test_split( x_scaled , Y_targetClass, random_state= 0)
LogRegModel = LogisticRegression(C=1).fit(X_train, Y_train) #max_iter= 500
R2 = LogRegModel.score(X_test, Y_test)


print("R^2 = ", R2)




# ### B) For the same problem, we will use logistic regression but want to select the best tuning parameter of Ridge regularization in logistic regression. We try the following set of values for the tuning parameter: [0.01, 0.1, 1, 10, 100], and use the five fold cross validation. We will find the best tuning parameter in this set, and test accuracy of the model when the best tuning parameter is selected. 
# 

# ## <center> Cross validation process </center>
# 
# ![Cross validation](https://scikit-learn.org/stable/_images/grid_search_workflow.png)
# 
# [Useful Resource](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)

# In[ ]:


from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
st_scaler_x = preprocessing.StandardScaler()
x_scaled = st_scaler_x.fit_transform(X_features)
X_trainval, X_test, Y_trainval, Y_test = train_test_split(x_scaled , Y_targetClass, random_state= 0)


best_score = 0 
kfolds=5
# C:float, default=1.0
# Inverse of regularization strength; must be a positive float.
# Like in support vector machines, smaller values specify stronger regularization.
# -----------------------------------------------------------------
for c in [0.01, 0.1, 1, 10, 100]: 
    print('======================= c=', c, "=======================")
    model = LogisticRegression(C=c, max_iter=500) # 
    scores =cross_val_score(model, X_trainval, Y_trainval, cv=kfolds)
    print('Scores= ') # Show the score for each fold
    print(scores)
    score =np.mean(scores)
    print("Mean score=", score) # Show the mean score for the c parameter
    if score > best_score:
        best_score =score
        best_parameters = c

SelectedModel =LogisticRegression(C=best_parameters).fit(X_trainval, Y_trainval)
test_score =SelectedModel.score(X_test, Y_test)
print("Best score on validation set is:", best_score)
print("Best parameter for regularization (alpha) is:", best_parameters)
print ("Test set score with best C parameter is", test_score)


# ## Now your turn. Use the dataset, "admit" from pyDataset , to build a Logistic regression model with Cross Validation.

# In[ ]:


admit= data('admit')
admit


# In[ ]:


admit


# In[ ]:


type(admit)


# In[ ]:




