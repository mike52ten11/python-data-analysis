# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:55:07 2023

@author: 621882
"""

import pandas as pd
import os

# 讀取原始CSV文件
data = pd.read_csv('L436598_FCUSTOMER_HHD.csv',encoding='ANSI')

# 根據fcustomerid列對數據進行分組
grouped = data.groupby('fcustomerid')

os.makedirs('Group',exist_ok=True)
# 對每個分組應用函數,將數據寫入新的CSV文件
for name, group in grouped:
    group.to_csv(f'Group/output_{name}.csv', index=False,encoding='ANSI')






