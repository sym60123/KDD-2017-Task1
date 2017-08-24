import pandas as pd

def handleTime(time):
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

from IPython.core.display import display, HTML

def displayParam(clf, html = []):
    try:
        for process in clf.steps:
            html += ['<h2>{}</h2>'.format(process[0])]
            html += ['<ul>']
            for key in process[1].get_params().keys():
                html += ['<li>{}__{}</li>'.format(process[0], key)]
            html += ['</ul>']
    except:
        for process in clf.named_regressors:
            html += ['<h2>{}</h2>'.format(process)]
            html += ['<ul>']
            for key in clf.named_regressors[process].get_params().keys():
                html += ['<li>{}__{}</li>'.format(process, key)]
            html += ['</ul>']
            
    display(HTML('\n'.join(html)))

from sklearn.base import BaseEstimator, TransformerMixin

class Saver(BaseEstimator, TransformerMixin):
    def __init__(self,  path):
        self.path = path;
        
    def fit(self, x, y=None):
        return self

    def transform(self, posts):
        pd.to_pickle(posts, self.path)
        return posts