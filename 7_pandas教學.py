#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[6]:


s = pd.Series(np.array([1,2,3]))
print(s)


# In[8]:


s = pd.Series(np.array([2024,6,3]),index=['年','月','日'])
print(s)


# In[13]:


data = {
    '年':2024
    ,'月':6
    ,'日':3
}
s = pd.Series(data)
print(s)


# In[14]:


data = {
    '年':0.234
    ,'月':0.666
    ,'日':0.777
}
s = pd.Series(data)
print(s)


# In[18]:


value_to_find=0.777
key = next((k for k, v in data.items() if v == value_to_find), None)
print(key)


# # 缺值

# In[28]:


data = {
    '年':2024
    ,'月':6
    ,'日':3
    ,'時':np.nan
    ,'分':np.nan
}
s = pd.Series(data)
print(s,'\n')

# 找出 NaN 值
s[pd.isna(s)] = 0

print('找出 NaN 值並一次替換\n',s)


# # 合併dataframe

# In[29]:


data1=[['A',1],['BB',2],['CCC',3]]
df2=pd.DataFrame(data1,columns=['Name','Age'])
print(df2)

data2=[['AA',11],['BBB',21],['CCCC',31]]
df3=pd.DataFrame(data2,columns=['Name','Age'])

print(df3)
pd.concat([df2,df3])


# ## index 接著編號

# In[33]:


df = pd.concat([df2,df3],ignore_index=True)
df


# In[38]:


for index , row in df.iterrows():
    print('index = ',index)
    print('row = ', row)
    print('============================')


# In[39]:


df = pd.DataFrame({
    'key1' : ['a','a','b','b','a'],
    'key2' : ['one','two','one','two','one'],
    'data1' : np.random.randn(5),
    'data2' : np.random.randn(5)
})
print(df)



# In[48]:


grouped = df.groupby(df['key1'])
for i, group in grouped:
    print(f'============== 分組 {i}    ===================')
    print(group)
    print('\n')
    


# In[ ]:




