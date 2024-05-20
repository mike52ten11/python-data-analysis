# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:55:07 2023

@author: 621882
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import seaborn as sns
import plotly.express as px
# 讀取CSV文件
data = pd.read_csv('Group_by_fcustomerid/output_1.csv',encoding='ANSI')
#找year=2020
data_2020 = data[data['Year'] == 2020]
# 根據fcustomerid列對數據進行分組
grouped = data_2020.groupby('Date')
max_kwh = grouped.apply(lambda x: x.loc[x['KWH_A'].idxmax(), [ 'Month','Hour', 'KWH_A']])
names = np.asarray(max_kwh['KWH_A']).astype('str')

# grouped_month = max_kwh.groupby('Month')

# 對每個分組應用函數,將數據寫入新的CSV文件
# len(grouped_month.Month)
# for name, group in grouped_month:
#     print(name)
# 取前30筆資料
# max_kwh = max_kwh.head(30)
# 重置索引
max_kwh = max_kwh.reset_index()

# 設置matplotlib中文顯示
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'

fig = px.box(max_kwh, x="Month", y="Hour",points="all")
fig.update_yaxes(range=[-1,24], dtick=1)
fig.show()








