#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import numpy as np
from datetime import datetime as dt
from matplotlib import pyplot as plt


start_date = '2005-01-01'
end_date = '2017-01-01'


'''将字符串转换成datetime.date形式'''
def s2d(s):
    return dt.strptime(s, '%Y-%m-%d').date()

def s2d2(s):
    return dt.strptime(s, '%Y/%m/%d').date()


'''获取指数收盘价'''
def get_close(index_code, start_date, end_date):
    # 沪深300，上证50，中证500，中证1000
    start_date = s2d(start_date)
    end_date = s2d(end_date)
#     if index_code in ['000300.XSHG', '000016.XSHG', '000905.XSHG', '000852.XSHG']:
    data = get_price(index_code, start_date, end_date).iloc[:, :4]   #开高低收
    return data


'''获取数字货币价格信息'''
def get_close_cry(index_code, start_date, end_date):
    start_date = s2d(start_date)
    end_date = s2d(end_date)
    data = pd.read_csv('%s.csv' % index_code)
    date_list = [s2d2(data.date[i]) for i in range(len(data))]
    data.date = date_list
    data = data.set_index('date')
    data = data.sort_index()
    data = data[(data.index > start_date) & (data.index < end_date)]
    return data



# '''选取每周第一天调仓'''
# def data_filter(data):
#     result = pd.DataFrame(data[0:1])
#     for i in range(1, len(data)):
#         if data.index[i].weekday() - data.index[i-1].weekday() < 0:
#             result = pd.concat([result, data[i:i+1]])
#     return result


'''计算ADX指标'''
def add_MA(data):
    for i in [5, 10, 15, 30]:
        data['ma%s' % (str(i))] = data.close.rolling(window=i).mean()
    return data


def add_signal_MA(data):      
    data['signal'] = 0
    for i in  range(30, len(data)):
        if data.signal.values[i-1] == 0:
            if data.ma5.values[i] > data.ma30.values[i]:
                data.signal.values[i] = 1
        else:
            if data.ma5.values[i] < data.ma10.values[i]:
                data.signal.values[i] = 0
            else:
                data.signal.values[i] = 1
#     data.loc[data.ma5 > data.ma30, 'signal'] = 1  
    return data


def net_value(data):
    data['nv'] = 1.
    data['daily_profit'] = 0.
    for i in range(1, len(data)):
        if data.signal[i-1] == 0:
            data.nv.values[i] = data.nv.values[i-1]
        else:
            data.nv.values[i] = data.nv.values[i-1] * data.close.values[i] / data.close.values[i-1]
            data['daily_profit'].values[i] = data.close.values[i] / data.close.values[i-1] - 1
    return data


def strategy(index_code, start_date, end_date):
    data = get_close_cry(index_code, start_date, end_date)
    data = add_MA(data)
    data = add_signal_MA(data)
    data = net_value(data)
    return data


def plot_nv(data, index_code):
    data_temp = data[20:]
    fig = plt.figure(figsize=(20, 10))
    plt.tick_params(labelsize=17)  
    ax = fig.add_subplot(111)
    ax.plot(data_temp.close / data_temp.close.values[0], 'r', label=index_code)
    ax.plot(data_temp.nv, 'g', label='strategy_net_value')
    ax.legend(loc='upper left', fontsize=17)
    
    


def plot_factor(data):
    data_temp = data[20:]
    date_list = [data_temp.index[0]]
    for i in range(1, len(data_temp)):
        if data_temp.index[i] != data_temp.index[i-1]:
            date_list.append(data_temp.index[i])
    fig = plt.figure(figsize=(20, 10))
    plt.tick_params(labelsize=17)    
    ax = fig.add_subplot(111)
    ax.plot(date_list, data_temp.close, 'r', label='BTC')
    ax2 = ax.twinx()
    plt.tick_params(labelsize=17)  
#     data['line'] = bond_line
#     ax2.plot(data.line, 'b')
    ax2.plot(data_temp.adx, 'g', label='ADX')
    ax.legend(loc='upper left', fontsize=17)
    ax2.legend(loc='upper right', fontsize=17)
    

    
def performance(data):
    # 年化收益率
    days = (data.index[-1] - data.index[0]).days
    annual_return = pow(data['nv'].values[-1], 365. / days) -1
    
    # 最大回撤
    max_drawdown = 0.
    max_nv = 1.
    for i in range(1, len(data)):
        drawdown = 1 - data['nv'].values[i] / max_nv
        max_drawdown = drawdown if (drawdown > max_drawdown) else max_drawdown
        max_nv = data['nv'].values[i] if (data['nv'].values[i] > max_nv) else max_nv
    
    # 夏普比率
    annual_return_benchmark = pow(data['close'].values[-1] / data['close'].values[0], 365. / days) - 1
    std_profit = std(data.loc[:, 'daily_profit'])
    sharpe = (annual_return - annual_return_benchmark) / std_profit
    return annual_return, max_drawdown, sharpe


# In[74]:


ind = 'XRP'
start_date = '2000-01-01'
end_date = '2019-01-01'
data = strategy(ind, start_date, end_date)
plot_nv(data, ind)
print(performance(data))


# In[ ]:




