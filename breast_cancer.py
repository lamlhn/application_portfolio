import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import accuracy_score
import joblib

cols = ["sample_code_number", "clum_thickness", "uniformity_cell_size", "uniformity_cell_shape", "marginal_adhesion", "single_epithelial_cell_size", "bare_cuclei", "bland_chromatin", "normal_nucleoli", "mitoses", "class"]
df = pd.read_csv("breast_cancer.data", names=cols)
df = df.drop(columns=['sample_code_number'])
df.head()

df.dtypes

df.nunique()

df["bare_cuclei"].unique()

df = df.replace('?', np.nan)
df = df.dropna(how='any')

df.nunique()

df["class"] = (df["class"] == 4).astype(int)
df.head()

def prob_df(df):
  cols = df.columns
  for col in cols[1:-1]:
    plt.hist(df[df["class"] == 1][col], color='blue', label="Malignant", alpha=0.7, density=True)
    plt.hist(df[df["class"] == 0][col], color='red', label="Benign", alpha=0.7, density=True)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel("Probability")
    plt.legend()
    plt.show()

prob_df(df)

"""## Train, validation, test datasets"""

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe, oversample=False):
  x = dataframe[dataframe.columns[:-1]].values
  y = dataframe[dataframe.columns[-1]].values

  scaler = StandardScaler()
  X = scaler.fit_transform(x)

  if oversample:
    ros = RandomOverSampler()
    X, y = ros.fit_resample(X,y)

  data = np.hstack((X, np.reshape(y, (-1, 1))))

  return data, X, y, scaler

train, X_train, y_train, scaler = scale_dataset(train, oversample=True)
valid, X_valid, y_valid, _ = scale_dataset(valid, oversample=False)
test, X_test, y_test, _ = scale_dataset(test, oversample=False)

"""## Logistic Regression"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

lg_model = LogisticRegression()
lg_model = lg_model.fit(X_train, y_train)

# Lưu model và scaler
joblib.dump(lg_model, "breast_cancer_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Formation terminée et modèle, scaler enregistré.")
