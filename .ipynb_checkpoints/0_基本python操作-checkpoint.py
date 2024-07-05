#!/usr/bin/env python
# coding: utf-8

# # 一、賦值

# ## 1.文字

# In[4]:


a='hello world'
print(a)


# ## 2.數字

# In[ ]:


a=5
print(a)


# ## 3.陣列

# ### 3.1 字典

# In[27]:


a={'date':'2024-01-01 04:00',
       'name':'tpri',
      'age':18}
print(a)


# In[28]:


a['date']


# In[32]:


a=[
        {
            'date':'2024-01-01 04:00',
            'name':'tpri',
            'age':18
        },
        {
              'date':'2024-01-01 04:00',
              'name':'TPRI',
              'age':20
        
        }
]
print(a)


# ### 3.2 list

# In[16]:


a=[1,2,3]
print(a)
a.append(4)
print('在後面加入4',a)


# In[ ]:





# # 二、迴圈

# In[ ]:


for i in range(10):
    print(i)


# # 三、條件判斷

# In[25]:


a = 1
b = 1
if a<b:
    print('a<b')
elif a>b:
    print('a<b')
else:
    print('a=b')


# ## 四、字串

# ## 1.字串合併

# In[20]:


a = 'Python'
b = '課程'
c = a + b
print(c)


# ## 2.數值轉換

# In[24]:


s = '3.14159'
fval = float(s)
print(fval)
print(int(fval))
print(bool(fval))#只要不是0就是true


# In[17]:





# In[ ]:




