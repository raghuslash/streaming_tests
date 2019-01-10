import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


plt.rcParams["figure.figsize"]=[15,5]


# In[4]:


raw_sp = pd.read_csv('screenprinter.csv', usecols =['timestamp', 'data.A1'])
#only one phase for sp


# In[5]:


mins=50
test_sp=raw_sp.head(60*mins)
# test_sp.index=test_sp['timestamp']
test_sp.to_csv('sp_head.csv', index=False)
# test_sp


# In[6]:


test_sp=pd.read_csv('sp_head.csv')
test_sp.plot()
plt.margins(0)


# In[7]:


import scipy.signal
import numpy as np


# In[8]:


test_sp=test_sp[['data.A1','timestamp']]
events=scipy.signal.find_peaks(test_sp['data.A1'], height=(2.75), width=1)
# test_sp['data.A1']


# In[9]:


plt.scatter(events[0], events[1]['peak_heights'], color='r', marker='o')
plt.stem(events[0], events[1]['peak_heights'])
plt.xlim(xmin = 0)


# In[10]:


test_sp.insert(2,'state',0)
sampleno=0
for x in events[0]:
    if test_sp.at[x, 'data.A1'] < 5:
        test_sp.at[x, 'state'] = 1
    elif test_sp.at[x, 'data.A1'] > 9:
        test_sp.at[x, 'state'] = 2


# In[11]:


test_sp.plot()
plt.xlim(xmin = 0)


# In[12]:


test_sp['state'].value_counts()
len(test_sp.query('state == 1'))


# In[13]:


test_sp.drop('data.A1', axis=1, inplace=True)


# In[14]:


test_sp


# In[15]:


test_sp[test_sp.columns[0]]

