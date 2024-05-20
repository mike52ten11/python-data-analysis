# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:55:07 2023

@author: 621882
"""

import pandas as pd
import numpy as np
import datetime
import json

from sklearn.model_selection import train_test_split

# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename,'r+',encoding='utf8') as file:
          
        file_data = json.load(file)
        
        file_data["emp_details"].append(new_data)
        
        file.seek(0)
       
        json.dump(file_data, file, indent = 4,ensure_ascii=False)

def text_example(context,name = 'pw_test.json'):
    Data = {}
    for i in range(1,len(context[:,0])):#
        fcustomerid = context[i-1,0]
        country = context[i-1,1]
        Date = context[i-1,2]
        Week =  context[i-1,5]
        Time =  context[i-1,6]
        Holiday =  context[i-1,7]
        KWH_A =  context[i-1,8]

        pred_Date = context[i,2]
        pred_Week =  context[i,5]
        pred_Time =  context[i,6]
        pred_Holiday =  context[i,7]
        pred_KWH_A =  context[i,8]
        if Holiday=='N':
            Holiday = "不是假日"
        elif Holiday=='Y':
            Holiday = "是假日" 
        else:
            raise 'Holiday 有錯誤' 
        if pred_Holiday=='N':
            pred_Holiday = "不是假日"
        elif pred_Holiday=='Y':
            pred_Holiday = "是假日" 
        else:
            raise 'pred_Holiday 有錯誤'  


        if i%500==0:
            print('===================================================')
            print('  i=',i)
            print(f'Date = {Date} {pred_Time}')
            print(f'pred_Date = {pred_Date} {pred_Time}')
        Data["instruction"] = "你現在是預測大師，會根據我給的資訊來預測該用戶的用電量，一般來說假日用電量會比較高" 
        Data["input"] = f"我想預測{fcustomerid}的用電量，根據我給的資訊來預測用戶{fcustomerid}的用電量;"\
                        f"我給的資訊:用戶{fcustomerid}，縣市是{country}，日期是{Date}，星期{Week}，時間{Time}點，{Holiday}，且用電量(KWH_A)是{KWH_A}"\
                        f"，要預測的日期是{pred_Date}，星期{pred_Week}，時間{pred_Time}點，{pred_Holiday}。"
        Data["output"] = f"用戶{fcustomerid}，縣市是{country}，預測日期{pred_Date}，星期{pred_Week}，時間{pred_Time}點，{pred_Holiday}，且用電量(KWH_A)是{pred_KWH_A}"
        
        write_json(Data,filename = name)
        
if __name__ == '__main__':
     

    data = pd.read_csv('all.csv')
    ytrain,ytest = train_test_split(data,
                                    train_size=0.9,
                                    shuffle=True)
    
    ytrain = ytrain.to_numpy()
    ytest = ytest.to_numpy()
    print(ytrain[0,:])
    print(ytest[0,:])    
    Train_data = {} 
    Test_data = {}

    text_example(ytest,'test.json')

    text_example(ytrain,'train.json') 
        

    # fcustomerid = data[:,0]
    # Open = data[:,1]   
    # High = data[:,2]
    # Low = data[:,3]
    # Close = data[:,4]
    # Adj_Close = data[:,5] 
    # Volume = data[:,6]
    # OuptData = {}
    # for i in range(len(data[:,0])):
        
    #     if Date[i].strftime("%Y")=='2023':
    #        OuptData["train"] = [0,i]
    #        OuptData["test"] = [i,len(data[:,0])-1]
    #        break
    
    # Data = {}
    # forword = 5
    # for i in range(OuptData[datasetname][0]+forword,OuptData[datasetname][1]-1):#
        
    #     Data["instruction"] = "你現在是股市預測大師，會根據我給的資訊來預測台股加權指數的收盤價" 
    #     inpu_text = "請預測台股加權指數的收盤價，根據前5個交易日的資訊來預測"+Date[i+1].strftime("%Y年%m月%d日")+"的台股加權指數的收盤價；前5個交易日資訊:"
            
    #     for forword_day in range(forword-1,-1,-1):            
             
    #         inpu_text= inpu_text+\
    #         '前'+str(forword_day+1)+'個交易日'+\
    #         "日期:"+Date[i-forword_day+1].strftime("%Y年%m月%d日")+\
    #         "、"+"開盤價:"+str(math.floor(Open[i]*100)/100.0)+\
    #         "、"+"最高價:"+str(math.floor(High[i]*100)/100.0)+\
    #         "、"+"最低價:"+str(math.floor(Low[i]*100)/100.0)+\
    #         "、"+"收盤價:"+str(math.floor(Close[i]*100)/100.0)+\
    #         "、"+"成交量:"   +str( Volume[i])+"萬。"
    
       
    #     Data["input"] = inpu_text        
    #     Data["output"] = Date[i+1].strftime("%Y年%m月%d日")+"台股加權指數的的收盤價為" + str(math.floor(Close[i+1]*100)/100.0)

        
    #     write_json(Data,filename = 'stock_market_'+datasetname+'.json')
    
    









