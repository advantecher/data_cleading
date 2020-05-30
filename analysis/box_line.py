import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def outliers(data, col_name, scale=1):##scale--尺度 一般取3

    def box_plot_outliers(data_ser, box_scale):
          ##IQR即尺度*（上四分位点-下四分位点）
        IQR = box_scale * (data_ser.quantile(0.75) - data_ser.quantile(0.25))
        val_low = data_ser.quantile(0.25) - 1.5 * IQR #计算上边缘
        val_up = data_ser.quantile(0.75) + 1.5 * IQR  #计算上下边缘
        rule_low = (data_ser < val_low)         #小于下边缘的值
        rule_up = (data_ser > val_up)           	#大于上边缘的值
        return (rule_low, rule_up), (val_low, val_up)

    data_n = data.copy()
    data_series = data_n[col_name]
    rule, value = box_plot_outliers(data_series, box_scale=scale)
    index = np.arange(data_series.shape[0])[rule[0] | rule[1]] ##对满足在rule_low以下或rule_up以上条件计数
    print("删除了: {} 个数据".format(len(index)))
    data_n = data_n.drop(index)
    data_n.reset_index(drop=True, inplace=True)##取删除离群点后的数据
    print("剩余: {} 个数据".format(data_n.shape[0]))
    index_low = np.arange(data_series.shape[0])[rule[0]]
    outliers = data_series.iloc[index_low]#计在下边缘以下的点
    print("小于下边缘线的数据详细:")
    print(pd.Series(outliers).describe())
    index_up = np.arange(data_series.shape[0])[rule[1]]#计在上边缘以上的点
    outliers = data_series.iloc[index_up]
    print("大于上边缘线的数据详细:")
    print(pd.Series(outliers).describe())
	##可视化数据
    fig, ax = plt.subplots(1, 2, figsize=(10, 7))
    sns.boxplot(y=data[col_name], data=data,ax=ax[0])
    sns.boxplot(y=data_n[col_name], data=data_n,ax=ax[1])
    return data_n


# df = pd.read_excel(r'D:\testdata\2017-2019三年数据汇总表(未处理缺失值).xls', usecols=[0, 1, 2],
#                    )
# box_data = np.array(df)
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# # 对数据进行标准化
# box_data = (box_data - np.mean(box_data, axis=0)) / np.std(box_data, axis=0)
# plt.boxplot(box_data)
# plt.show()
if __name__ == '__main__':
    df = pd.read_excel(r'D:\testdata\2017-2019三年数据汇总表(未处理缺失值).xls', usecols=[0, 1, 2, 3])
    data = outliers(outliers(outliers(df, '臭氧破坏前浓度', scale=1), '水中余臭氧浓度(南)', scale=1), '水中余臭氧浓度(北)', scale=1)
    #data['臭氧破坏前浓度'].replace(0, np.nan, inplace=True)
    data['臭氧破坏前浓度'].value_counts()
    data.to_excel(r'D:\testdata\DDD.xls', index=False, na_rep=0)
    data['水中余臭氧浓度(南)'].plot()

