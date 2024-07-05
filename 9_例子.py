import pandas as pd
import numpy as np
#讀取csv 


data = pd.read_csv('2_groupby/output_1.csv',encoding='ANSI')

#找year=2020
data_2020 = data[data['Year'] == 2020]
# 根據Date列對數據進行分組
grouped_2020 = data_2020.groupby('Date')
max_kwh_2020 = grouped_2020.apply(lambda x: x.loc[x['KWH_A'].idxmax(), [ 'Month','Hour', 'KWH_A']])
names_2020 = np.asarray(max_kwh_2020['KWH_A']).astype('str')



import plotly.express as px
import plotly.io as pio
import os
# pio.renderers.default = 'notebook'


fig = px.box(max_kwh_2020, x="Month", y="Hour",title='2020年_每月每天最高用電量在幾點的盒鬚圖',points="all")
fig.update_yaxes(range=[-1,24], dtick=1)

os.makedirs("9_例子/id_1", exist_ok=True)
# fig.write_image("9_例子/box_plot_2020.png")
fig.write_html("9_例子/id_1/2020年_每月每天最高用電量在幾點的盒鬚圖.html")
fig.show()


os.makedirs("9_例子/id_1", exist_ok=True)
max_kwh_2020.to_csv('9_例子/id_1/2020年_每月每天最高用電量在幾點的盒鬚圖.csv')

import pandas as pd
import numpy as np
#讀取畫圖的數據csv 
data = pd.read_csv('9_例子/id_1/2020年_每月每天最高用電量在幾點的盒鬚圖.csv',encoding='ANSI')

import plotly.express as px
import plotly.io as pio
import os
pio.renderers.default = 'notebook'

fig = px.box(data, x="Month", y="Hour",title='2020年_每月每天最高用電量在幾點的盒鬚圖',points="all")
fig.update_yaxes(range=[-1,24], dtick=1)

fig.show()