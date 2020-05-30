import pandas as pd
import matplotlib.pyplot as plt

pd = pd.read_excel(r'D:\testdata\first&forcedel.xls', names=['south', 'north', 'before', 'date'])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
pd['south'].plot(label='south', title='南余第一次剔除+暴力删除')
pd['north'].plot(label='north', title='南余北余第一次剔除+暴力删除')
# pd['before'].plot(label='south', title='臭氧破坏前浓度')
# 计算相关系数
print(pd.corr(method='pearson'))
plt.show()