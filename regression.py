from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import random
from scipy.spatial import KDTree
from sklearn.metrics import mean_absolute_error
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

class Regression:
  def __init__(self, csv_file = './data/king_county_data_geocoded.csv', data = None, values = None):
    if (data is None and csv_file is not None):
      df = pd.read_csv(csv_file)
      self.values = df['AppraisedValue']
      df = df.drop('AppraisedValue', 1)
      df = (df - df.mean()) / (df.max() - df.min())
      self.df = df
      self.df = self.df[['lat', 'long', 'SqFtLot']]
   
    elif (data is not None and values is not None):
      self.df = data
      self.values = values
    else:
      raise ValueError("Must have either csv_file or data set")

    self.n = len(self.df)

    self.kdtree = KDTree(self.df)
    self.metric = np.mean

    # TODO: set k to a number, try a few numbers out
    # self.k = None

  def regress(self, query_point):
    distances, indexes = self.kdtree.query(query_point, self.k)
    m = self.metric(self.values.iloc[indexes])
    if np.isnan(m):
      raise ValueError("There is a NaN in the data")
    else:
      return m

  def plot_error_rates(self):
    # TODO: Perhaps lower the amount of folds so you can try out more values of K
    folds = range(2, 11)
    errors = pd.DataFrame({'max': 0, 'min': 0}, index=folds)
    for f in folds:
      error_rates = self.error_rate(f)
      errors['max'][f] = max(error_rates)
      errors['min'][f] = min(error_rates)
    # TODO: Are you going to use a mean absolute error or something else?
    errors.plot(title='Mean Absolute Error of KNN over different folds')
    plt.show()

  def error_rate(self, folds):
    holdout = 1 / float(folds)
    errors = []
    for fold in range(folds):
      y_hat, y_true = self.__validation_data(holdout)
      # TODO: Take a look at sklearn.metrics to see if any other metric you might want to look at
      errors.append(mean_absolute_error(y_true, y_hat))

    return errors
    
  def __validation_data(self, holdout):
    test_rows = random.sample(list(self.df.index), int(round(len(self.df) * holdout)))
    train_rows = set(range(len(self.df))) - set(test_rows)
    df_test = self.df.ix[test_rows]
    df_train = self.df.drop(test_rows)
    
    test_values = self.values.ix[test_rows]
    train_values = self.values.ix[train_rows] 
    kd = Regression(data=df_train, values=train_values) 

    y_hat = []
    y_true = []

    for idx, row in df_test.iterrows():
      # TODO:
      # what do you append to y_hat here?
      # What method would give you the value given a row?
      # y_hat.append(??)
      y_true.append(self.values[idx])

    return (y_hat, y_actual)
