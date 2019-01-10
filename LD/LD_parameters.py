#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal
import numpy as np


# In[2]:


plt.rcParams["figure.figsize"]=[15,5]


# In[4]:


raw_ld=pd.read_csv('loader_jan.csv', usecols=['timestamp', 'data.ax', 'data.ay', 'data.az'])
#raw_ld.dropna(axis=1, inplace=True)


# In[5]:


#Load LD data and plot
raw_ld["acc"] = ( raw_ld["data.ax"]**2 + raw_ld["data.az"]**2 ) ** 0.5
acc=raw_ld[["timestamp", "acc"]]
acc.set_index('timestamp')
test_ld=acc
test_ld['acc']=pd.Series.to_frame(test_ld.acc.rolling(100, center=True).std())


# In[6]:


timethresh=12
test_ld.insert(2,'state',0)


# In[7]:


get_ipython().run_line_magic('matplotlib', 'tk')


# In[8]:


plt.plot(test_ld['timestamp'], test_ld['acc'])


# In[ ]:


#Get boards from Loader
board=scipy.signal.find_peaks(test_ld.acc,height=(0.01), distance=timethresh*100, width=1)
differ=np.diff(board[0])
differ=differ.tolist()

# boards=[]
# boards.append(board[0][0])
# sumdiffer=0
# for i, x in enumerate(board[0]):
#     try:
#         sumdiffer+=differ[i]
#         if sumdiffer>timethresh*100:
#             boards.append(board[0][i])
#             test_ld.at[x, 'state']=1
#             sumdiffer=0
#         if differ[i] < timethresh*100:
#             test_ld.at[x, 'state']=2
#     except:
#         continue
for x in board[0]:
    test_ld.at[x, 'state'] = 1

ld_boards=test_ld[test_ld['state']==1]
print('Boards detected in LD:', ld_boards.shape[0])


# In[ ]:


import datetime as dt
import time
import matplotlib.dates as mdates

pattern="%Y-%m-%dT%H:%M:%S.%f"
test_ld['timestamp'] =  pd.to_datetime(test_ld['timestamp'], format=pattern)
ld_boards['timestamp'] =  pd.to_datetime(ld_boards['timestamp'], format=pattern)


# In[ ]:


fig, ax1 = plt.subplots()

ax1.stem(ld_boards['timestamp'], ld_boards['state'], 'orange')

# ax1.xaxis.set_major_locator(mdates.DateFormatter('%H:%M'))

ax1.set_xlabel('Time')

ax2 = ax1.twinx()

ax2.plot(test_ld['timestamp'], test_ld['acc'], 'blue')

plt.title('Board Detections')

