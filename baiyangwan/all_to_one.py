# -*- coding:utf-8 –*-

"""
利用pandas将多张excel表中的指定列数据合并成一张；因为原始的多张数据存在同样列名的数据，
因为原始多张excel是从csv文件转换股
并且我们只需要其中的部分列数据，所以进行指定列提取并汇总至res文件中
"""
import os
import pandas as pd


# 输入参数为excel表格所在目录
def to_one_excel(dir):
    dfs = []
    # 遍历文件目录，将所有表格表示为pandas中的DataFrame对象
    # for root_dir, sub_dir, files in os.walk(r'' + dir):     # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
    for root_dir, sub_dir, files in os.walk(dir):  # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
        for file in files:
            if file.endswith('xlsx'):
                # 构造绝对路径
                file_name = os.path.join(root_dir, file)
                # df = pd.read_excel(file_name)
                df_1 = list(pd.read_excel(file_name, nrows=1))  # 读取excel第一行数据并放进列表
                # excel第一行数据返回列表
                print(file_name)
                print(type(df_1))
                print(df_1)
                # 根据第一行列名获取每个文件中需要列的列索引，返回索引数值
                # suo_yin_1 = df_1.index("Billing Country")
                # suo_yin_2 = df_1.index("Created at")
                # suo_yin_3 = df_1.index("Updated at")
                # suo_yin_4 = df_1.index("Paid Price")
                # suo_yin_5 = df_1.index("Shipment Type Name")
                # suo_yin_6 = df_1.index("Status")
                # 读取文件内容  usecols=[1, 3, 4] 读取第1,3,4列
                df = pd.read_excel(file_name, usecols=[1, 3, 4]
                                   , sheet_name='臭氧发生')

                # pf = pd.read_excel('xxx.xls', usecols=[1, 3, 4], sheet_name='data')
                # print(pf)

                # 追加一列数据，将每个文件的名字追加进该文件的数据中，确定每条数据属于哪个文件
                excel_name = file.replace(".xlsx", "")  # 提取每个excel文件的名称，去掉.xlsx后缀
                df["日期"] = excel_name  # 新建列名为“店铺”，列数据为excel文件名
                dfs.append(df)  # 将新建店铺列追加进汇总excel中
    # 行合并
    df_concated = pd.concat(dfs)

    # 构造输出目录的绝对路径
    out_path = os.path.join(dir, 'res.xlsx')
    # 输出到excel表格中，并删除pandas默认的index列
    df_concated.to_excel(out_path, sheet_name='Sheet1', index=None)


# 调用并执行函数
to_one_excel(r'D:\testdata' )