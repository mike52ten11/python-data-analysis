#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


a = np.array([
    [1,2,3],
    [4,5,6]
], dtype=np.float32)


# In[8]:


print(a.ndim)#數據維度


# In[9]:


print(a.shape)#數據形狀(列x行)


# In[ ]:


print(a.dtype)#數據型態


# In[10]:


print(np.average(a))#平均


# In[12]:


a.reshape(-1)#變成1維


# In[13]:


a.reshape((3,2))#變成3x2


# In[15]:


a.T#a轉置


# In[20]:


a.transpose((1,0))#a 列轉置


# In[21]:


a.transpose((0,1))#a 行轉置


# ## 內積

# In[34]:


inner_product  = np.dot(np.array([1,2,3]) ,np.array([4,5,6]))
print('用np.dot = ',inner_product)

inner_product  = np.array([1,2,3]) @ np.array([4,5,6])
print('用@ = ',inner_product)



# ## 逐元素乘法

# In[40]:


a = np.array([1,2,3])
b = np.array([4,5,6])
elementwise_product = np.zeros((3),dtype=int)
for i in range(3):
    elementwise_product[i] = a[i]*b[i]

print('用for 迴圈:',elementwise_product)

#想要每個元素相乘可以使用*就好了
elementwise_product = np.array([1,2,3]) * np.array([4,5,6])
print('用np函式',elementwise_product)


# ## cos 相似性

# In[23]:


import numpy as np

# 定義兩個 numpy array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 計算內積
dot_product = np.dot(a, b)

# 計算 L2 範數
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

# 計算余弦相似性
cosine_similarity = dot_product / (norm_a * norm_b)

print("余弦相似性:", cosine_similarity)


# In[ ]:




