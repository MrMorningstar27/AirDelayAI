# import numpy package for arrays and stuff 
import numpy as np 
import joblib
# import matplotlib.pyplot for plotting our result 
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
# import pandas for importing csv files 
import pandas as pd 
import sklearn as sk

from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import roc_auc_score
# import dataset 


dataset = pd.read_csv("out.csv")

dataset = pd.get_dummies(dataset, columns=['Airport'])

dataset["Holiday time"] = dataset["Holiday time"].astype('category')
dataset["Holiday time cat"] = dataset["Holiday time"].cat.codes
dataset["Hour"] = dataset["Hour"].astype('category')
dataset["Hour cat"] = dataset["Hour"].cat.codes
dataset["Month"] = dataset["Month"].astype('category')
dataset["Month cat"] = dataset["Month"].cat.codes
dataset["Day of week"] = dataset["Day of week"].astype('category')
dataset["Day of week cat"] = dataset["Day of week"].cat.codes
dataset["Day of month"] = dataset["Day of month"].astype('category')
dataset["Day of month cat"] = dataset["Day of month"].cat.codes

print(dataset)
print(dataset.dtypes)

train_x, test_x, train_y, test_y = train_test_split(dataset.drop('Avarage wait', axis=1), dataset['Avarage wait'], test_size=0.4, random_state=42)





model = RandomForestClassifier(random_state=13,n_estimators=70) 
model.fit(train_x, train_y)

print(model.score(test_x,test_y))
# save the model to disk
filename = 'finalized_model_Air.joblib'
joblib.dump(model, filename, compress=3)  