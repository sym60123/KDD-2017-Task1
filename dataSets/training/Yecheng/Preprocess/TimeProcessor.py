import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class TimeProcessor(BaseEstimator, TransformerMixin):
    def __init__(self, column = None, title = None):
        self.column = column
        self.title = title
        
    def handleTime(self, time):
        t = pd.to_datetime(time)
        return pd.DataFrame({
                #"date": pd.to_datetime(pd.Series([t.date() for t in time])),
                "year": t.apply(lambda x: x.year),
                "day_in_month": t.apply(lambda x: x.daysinmonth),
                "day_of_year": t.apply(lambda x: x.dayofyear),
                "day_of_week": t.apply(lambda x: x.dayofweek),
                "hour": t.apply(lambda x: x.hour),
                "month": t.apply(lambda x: x.month),
                "minute": t.apply(lambda x: x.minute),
            }) 

    def fit(self, x, y=None):
        return self

    def transform(self, posts):
        timedf = self.handleTime(posts[self.column])
        
        if (self.title != None):
            timedf.rename({col: [self.title, '_', col] for col in timedf.columns})
            
        table = posts.join(timedf)
        return table