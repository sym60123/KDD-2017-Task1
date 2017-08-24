
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from Tools import handleTime


# In[122]:

train_20min = pd.read_csv('F:/KDDCUP/dataSets/training/training_20min_avg_travel_time.csv')
test_20min = pd.read_csv('F:/KDDCUP/dataSets/training/test1_20min_avg_travel_time.csv')


# In[123]:

def split_time_window(time_window):
    time_start = [time[1:-1].split(',')[0] for time in time_window]
    time_end = [time[1:-1].split(',')[1] for time in time_window]

    return pd.to_datetime(pd.Series(time_start)), pd.to_datetime(pd.Series(time_end))
train_20min['time_start'], train_20min['time_end'] = split_time_window(train_20min.time_window)


# In[125]:

train_20min['date'] = train_20min.time_start.apply(lambda x:x.date())
train_20min['hour'] = train_20min.time_start.apply(lambda x:x.hour)
train_20min['minute'] = train_20min.time_start.apply(lambda x:x.minute)


# In[127]:

days ={'day':[]}
hours = [6,7]
for day,df in train_20min.groupby(['date']):
    days['day'] += [day]
    for hour in hours:
        for minute in train_20min['minute'].unique():
            for key,t in train_20min.groupby(['intersection_id','tollgate_id']):
                ind = ((t['minute'] == minute)
                      &(t['hour'] == hour)
                      &(t['date'] == day))
                
                t = t[ind]
                iid,tid = key
                name = '_'.join(['time',str(iid),str(tid),str(hour),str(minute)])
                
                if(name not in days):
                    days[name] = []
                
                if(len(t) == 0):
                    days[name] +=[None]
                elif(len(t) == 1):
                    days[name] += [t.avg_travel_time.values[0]]
                else:
                    print("error",len(t))


# In[128]:

pd.DataFrame(days)


# In[49]:

train_20min = pd.read_csv('F:/KDDCUP/dataSets/training/feature/train_temptrave0429.csv')
train_20min = train_20min.drop(['time_window'],axis=1)
train_20min.to_csv('F:/KDDCUP/dataSets/training/feature/train_temptrave0429.csv')


# In[68]:

train_20min = pd.read_csv('F:/KDDCUP/dataSets/training/feature/train_temptrave0429.csv')
train_20min.dtypes


# In[50]:

train_20min = pd.read_csv('F:/KDDCUP/dataSets/training/feature/train_temptrave0429.csv')
train_20min


# In[72]:

train_20min['time_start'][1].split(' ')[0][5:]


# In[73]:

day = []
for i in range(0,len(train_20min)):
    day.append(train_20min['time_start'][i].split(' ')[0][5:])
day


# In[80]:

#train_20min['time_start'] = day
train_20min=train_20min.groupby(['time_start','intersection_id','tollgate_id','avg_travel_time','time_end']).count()
train_20min.to_csv('F:/KDDCUP/dataSets/training/feature/train_travel_day0429.csv')


# In[84]:

train_20min = pd.read_csv('F:/KDDCUP/dataSets/training/feature/train_travel_day0429.csv')
train_20min


# In[116]:

date = []
count = []
sum = 0
x = '07-19'
for i in range(0,len(train_20min)):
    if train_20min['time_start'][i]!=x:
        date.append(train_20min['time_start'][i])
        x = train_20min['time_start'][i]
date


# In[121]:

A_2=0
for i in range(0,len(train_20min)):
    if train_20min['intersection_id'][i]=='A' and train_20min['tollgate_id'][i]==2 and train_20min['time_start'][i]==date[j]:
        A_2 += train_20min['avg_travel_time'][i]
A_2


# In[57]:

sum_day = []
A_1=0
A_2=0
A_3=0
B_1=0
B_2=0
B_3=0
C_1=0
C_2=0
C_3=0
for i in range(0,len(train_20min)):
    if train_20min['intersection_id'][i]=='A' and train_20min['tollgate_id'][i]==1 and train_20min['time_start'][i]<='2016-07-19 01:20:00':
        A_1 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='A' and train_20min['tollgate_id'][i]==2 and train_20min['time_end'][i]<=24:
        A_2 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='A' and train_20min['tollgate_id'][i]==3 and train_20min['time_end'][i]<=24:
        A_3 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='B' and train_20min['tollgate_id'][i]==1 and train_20min['time_end'][i]<=24:
        B_1 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='B' and train_20min['tollgate_id'][i]==2 and train_20min['time_end'][i]<=24:
        B_2 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='B' and train_20min['tollgate_id'][i]==3 and train_20min['time_end'][i]<=24:
        B_3 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='C' and train_20min['tollgate_id'][i]==1 and train_20min['time_end'][i]<=24:
        C_1 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='C' and train_20min['tollgate_id'][i]==2 and train_20min['time_end'][i]<=24:
        C_2 += train_20min['avg_travel_time'][i]
    if train_20min['intersection_id'][i]=='C' and train_20min['tollgate_id'][i]==3 and train_20min['time_end'][i]<=24:
        C_3 += train_20min['avg_travel_time'][i]


# In[58]:

C_1


# In[4]:

data_train = data_train.groupby(['starting_time','intersection_id','tollgate_id','travel_time']).count()
data_train.to_csv('F:/KDDCUP/dataSets/training/feature/traveltime_temp.csv')
data_train = pd.read_csv('F:/KDDCUP/dataSets/training/feature/traveltime_temp.csv')
data_train.drop(['vehicle_id','travel_seq','travel_seq'])


# In[ ]:



