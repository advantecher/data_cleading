import os
import pandas as pd
import time

"""
dir:excel所在文件夹路径
"""
def to_one_excel(dir):
    start = time.clock()
    file_list = [] # excel文件名集合
    dfs = [] # DataFrame集合

    # 遍历文件夹下所有的excel文件，获得文件名
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_name = os.path.join(root, file)
            # 读excel文件，获得DataFrame集合
            # 取excel表的S,T,AN列数据，跳过0,1,2,3....行，设置列标签为'水中余臭氧浓度(南)', '水中余臭氧浓度(北)',
            # '臭氧破坏前浓度'
            df = pd.read_excel(file_name, sheet_name='臭氧发生', usecols='S, T, AN',
                                  skiprows=[0, 1, 2, 3, 4, 33, 34, 35, 36],
                                  names=['水中余臭氧浓度(南)', '水中余臭氧浓度(北)', '臭氧破坏前浓度'], header=None)
            # 提取每个excel文件的名称，去掉.xlsx后缀
            excel_name = file.replace(".xls", "")
            df['时间'] = excel_name
            dfs.append(df)
    #合并表(DataFrame对象)
    df_concated = pd.concat(dfs)
    #导出表，设定缺失值为0
    df_concated.to_excel(r'D:\testdata\2017-2019三年数据汇总表.xls', index=False, na_rep=0)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))

if __name__ == '__main__':
    to_one_excel(r'D:\testdata' )