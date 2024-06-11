#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[4]:


x = [5,2,9,7]
y = [1.1, 6.5, 8.9, 7.2]


# ## 1.畫線圖

# In[22]:


plt.plot(x,y,'r--o')


# ## 2.畫bar圖

# In[10]:


plt.bar(x,y)


# ## 3.畫點圖

# In[11]:


plt.scatter(x,y)


# In[25]:


import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'notebook'
x = [5,2,9,7]
y = [1.1, 6.5, 8.9, 7.2]
# 創建示例數據
data = {'X': x, 'Y': y }
df = pd.DataFrame(data)

# 繪製折線圖
fig = px.line(df, x="X", y="Y", markers=True,title="Line Plot of Month vs Hour")

# 顯示圖表
fig.show()


# In[26]:


import matplotlib.pyplot as plt

# 示例數據
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
y3 = [3, 5, 2, 8, 9]

# 繪製圖表
plt.plot(x, y1, label='y1')       # 實線
plt.plot(x, y2, '--', label='y2') # 虛線
plt.plot(x, y3, ':', label='y3')  # 點線

# 添加圖例
plt.legend()

# 顯示圖表
plt.show()


# In[28]:


import plotly.graph_objects as go

# 示例數據
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
y3 = [3, 5, 2, 8, 9]

# 創建圖表
fig = go.Figure()

# 添加曲線
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='y1'))   # 實線
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', line=dict(dash='dash'), name='y2'))  # 虛線
fig.add_trace(go.Scatter(x=x, y=y3, mode='lines', line=dict(dash='dot'), name='y3'))   # 點線

# 設置圖表標題和軸標籤
fig.update_layout(
    title='Plotly Line Chart Example',
    xaxis_title='X Axis',
    yaxis_title='Y Axis'
)

# 顯示圖表
fig.show()


# In[ ]:




