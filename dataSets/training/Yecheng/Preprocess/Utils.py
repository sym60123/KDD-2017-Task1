import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing

class DropProcessor(BaseEstimator, TransformerMixin):
    def __init__(self, columns = None):
        self.columns = columns
        
    def fit(self, x, y=None):
        return self

    def transform(self, posts):
        return posts.drop(self.columns, axis=1)

class MultiColumnLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here
    
    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)
    
class MergeProcessor(BaseEstimator, TransformerMixin):
    def __init__(self, table):
        self.table = table
        self.how = 'left'
        self.on = None
        self.na = -1
    
    def fit(self, x, y=None):
        return self

    def transform(self, posts):
        table = posts.merge(self.table,  how=self.how ,on=self.on)
        return table.fillna(self.na)