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
# import seaborn as sns
import plotly.express as px
# 讀取CSV文件
data = pd.read_csv('2_groupby/output_1.csv',encoding='ANSI')
#找year=2020
data_2020 = data[data['Year'] == 2020]
# 根據fcustomerid列對數據進行分組
grouped = data_2020.groupby('Date')
max_kwh = grouped.apply(lambda x: x.loc[x['KWH_A'].idxmax(), [ 'Month','Hour', 'KWH_A']])
names = np.asarray(max_kwh['KWH_A']).astype('str')


# 重置索引
max_kwh = max_kwh.reset_index()

# 設置matplotlib中文顯示
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'

fig = px.box(max_kwh, x="Month", y="Hour",points="all")
fig.update_yaxes(range=[-1,24], dtick=1)

os.makedirs("4_每月用電量最高幾點_盒鬚圖", exist_ok=True)
fig.write_image("4_每月用電量最高幾點_盒鬚圖/box_plot.pdf")
fig.write_html("4_每月用電量最高幾點_盒鬚圖/box_plot.html")
fig.show()








