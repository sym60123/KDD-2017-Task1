# coding: utf-8

import pandas as pd
import numpy as np

input_file = '../trajectories(table 5)_training.csv'
output_file = 'new_trajectories_train.csv'

data = pd.read_csv(input_file)

result = data[0:0]
link = []
last_enter_time = []
enter_time = []
travel_time = []

travel_seq = data.travel_seq
i = 0

for seq in travel_seq:
    for line in seq.split(';'):
        lk, et, tt = line.split('#')
        link += [lk]
        enter_time += [et]
        travel_time += [tt]
        #result = result.append(data[i:i+1])
    
    i += 1

result['link'] = link
result['enter_time'] = enter_time
result['link_travel_time'] = travel_time

result.to_csv(output_file, index=False)