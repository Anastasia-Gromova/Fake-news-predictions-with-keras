from keras.layers import Dense
from keras.models import Sequential

import pandas as pd
import numpy as np

# converting the dataset to a numpy array leaving only columns
#  with vectors and outputs
df = pd.read_csv('./vectorized_fake_news.csv')
cols = df.columns.tolist()[:6]
df = df.drop(cols, axis=1)
data = np.array(df)

# training model with 33% of validation data to test the result
def train(data, val=.33, epochs=20, ver=2, drop=.2):

    dataY = data[:,0]
    dataX = data[:,1:]
    
    model = Sequential()
    model.add(Dense(20, input_dim = dataX.shape[1], activation='elu'))
    model.add(Dense(20, activation='elu'))
    model.add(Dense(20, activation='elu'))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='logcosh', optimizer='adam', metrics=['accuracy'])
    model.fit(dataX, dataY, validation_split=val, epochs=epochs, batch_size=32, verbose=ver)

train(data, epochs=5, val=.4)
