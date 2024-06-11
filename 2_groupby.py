# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:55:07 2023

@author: 621882
"""

import pandas as pd
import os

# 讀取原始CSV文件
data = pd.read_csv('用戶1~3.csv',encoding='ANSI')

# 根據fcustomerid列對數據進行分組
grouped = data.groupby('fcustomerid')

os.makedirs('2_groupby',exist_ok=True)
# 對每個分組應用函數,將數據寫入新的CSV文件
for name, group in grouped:
    group.to_csv(f'2_groupby/output_{name}.csv', index=False,encoding='ANSI')






