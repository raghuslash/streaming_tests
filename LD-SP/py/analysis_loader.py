import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


plt.rcParams["figure.figsize"]=[15,5]


# In[4]:


raw_ld=pd.read_csv('loader.csv', usecols=['timestamp', 'data.ax', 'data.ay', 'data.az', 'data.A1'])


# In[5]:


raw_ld["acc"] = ( raw_ld["data.ax"]**2 + raw_ld["data.az"]**2 ) ** 0.5


# In[6]:


mins = 50
window = 50 * 60 * 75


# In[7]:


acc=raw_ld[["timestamp", "acc"]]
acc.set_index('timestamp')
acc.head()


# In[8]:


acc.head(window).to_csv('loader_head.csv', index=False)


# In[9]:


test_ld=pd.read_csv('loader_head.csv')
test_ld.plot()
# test_ld['timestamp']=acc.head(window)['timestamp']


# In[10]:


acc=pd.read_csv('loader_head.csv')
test_ld1=acc
test_ld1['acc']=pd.Series.to_frame(test_ld.acc.rolling(75, center=True).std())
test_ld1.to_csv('rollingstd.csv', index=False)


# In[11]:


test_ld=pd.read_csv('rollingstd.csv')
test_ld.plot()


# In[12]:


import scipy.signal
import numpy as np


# In[13]:


refill=scipy.signal.find_peaks(test_ld.acc, height=(0.0050, 0.020), width=100)


# In[14]:


brd=scipy.signal.find_peaks(test_ld.acc,height=(0.015), width=75)

board=scipy.signal.find_peaks(test_ld.acc,height=(0.015), width=75)


# In[15]:


refill


# In[16]:


plt.stem(board[0], board[1]['peak_heights'])
# plt.stem(refill[0],0.04*refill[1]['prominences']/refill[1]['peak_heights'])
plt.title('Board Detection')
# plt.ylim(ymax = 0.04, ymin = 0)
plt.margins(0)
# plt.xlim(xmax = 500000, xmin = 0)


# In[17]:


test_ld.plot()
plt.margins(0)


# In[18]:


plt.stem(refill[0], refill[1]['peak_heights'])
# plt.ylim(ymax = 0.04, ymin = 0)
plt.title("Refill Detection")
# plt.xlim(xmax = 500000, xmin = 0)
# plt.stem(np.fft.fft(refill[1]['peak_heights']))


# In[19]:


test_ld.plot()
plt.margins(0)
# plt.ylim(ymax = 0.04, ymin = 0)
# plt.xlim(xmax = 500000, xmin = 0)


# In[20]:


plt.stem(board[0], board[1]['peak_heights'])
plt.margins(0)


# In[21]:


start=board[0][0]
end=board[0][-1]
block_size=75*60*1
board[1]['refill_status']=[0]*len(refill[0])


# In[22]:


boards=[]
differ=np.diff(board[0])
differ=differ.tolist()
# differ


# In[23]:


binwidth=200
plt.hist(differ, bins=np.arange(min(differ), max(differ) + binwidth, binwidth))
print(np.percentile(differ, 30))


# In[24]:


test_ld.insert(2,'state',0)
boards=[]
boards.append(board[0][0])
for i, x in enumerate(board[0]):
    try:
        if differ[i]>5000:
             #print(x)
            boards.append(board[0][i+1])
            test_ld.at[x, 'state']=1
        else:
            test_ld.at[x, 'state']=2
    except:
        continue


# In[25]:


plt.stem(board[0], board[1]['peak_heights'])
plt.margins(0)


# In[26]:


test_ld.plot()
plt.margins(0)


# In[27]:


test_ld.plot()
plt.margins(0)
plt.stem(boards, np.ones(len(boards))*0.04, 'orange', '--',)
plt.margins(0)


# In[28]:


# plt.stem(boards, np.ones(len(boards)))
# plt.margins(0)


# In[29]:


len(boards)


# In[30]:


test_ld['state'].plot()


# In[31]:


test_ld.drop('acc', axis=1, inplace=True)
# In[32]:

test_ld

