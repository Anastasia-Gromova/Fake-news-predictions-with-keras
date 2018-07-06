import pandas as pd
import numpy as np

import datetime as dt
import spacy
import os

# helping function to clean the output in terminal
def clear():
    os.system('clear')

# loading English multi-task CNN provided by spacy
nlp = spacy.load('en_core_web_md')

# cleaning dataset from NaN values and converting it to numpy array
df = pd.read_csv('./fake_news.csv')
df = df.dropna()
for j in range(900):
    name = str(j)
    df[name] = None
columns = df.columns.tolist()
data = np.array(df)

n = k = 0
N = to_do = 3 * len(data)

# capturing the starting time for the finish time estimation
start_time = dt.datetime.now()

for x in range(3):
    for i in range(len(data)):
        # obtaining the list of 300 vectors
        temp = nlp(data[i][x + 2]).vector
        for j in range(300):
            num = 6 + j + 300 * k
            data[i][num] = temp[j]
        
        # printing the percent of work done and estimated finish time
        n += 1
        done = round(n * 100 / N, 3)
        clear()
        print (str(done) + '% is done')
        
        if n == 1:
            time_now = dt.datetime.now()
            time_per_one = (int(time_now.strftime('%s')) - int(start_time.strftime('%s'))) / n
            finish_time = dt.datetime.fromtimestamp((time_per_one * to_do) + 
                                                    int(start_time.strftime('%s')))
            finish_time = finish_time.strftime('%H:%M %d %B')
        print('Estimated finish: ' + finish_time)
        
        to_do -= 1

    k += 1

# saving to csv file
pd.DataFrame(data, columns=columns).to_csv('./vectorized_fake_news.csv')
