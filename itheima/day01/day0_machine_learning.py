from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold


def datasets_demo():
    """
    sklearn 数据集使用
    """
    # 获取数据集
    iris = load_iris()
    print("鸢尾花数据集 :\n", iris)
    print("查看数据集描述：\n", iris['DESCR'])
    print("查看特征值的名字：\n", iris.feature_names)
    print("查看特征值：\n", iris.data, iris.data.shape)
    print("查看目标值：\n", iris.target)

    # 数据集划分
    x_train, x_test, y_tran, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print("训练集的特征值：\n:", x_train, x_train.shape)
    return None

def dict_demo():
    """
    字典特征抽取
    """
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]
    # 1.实例化一个转化器类
    tansfer = DictVectorizer(sparse=False)
    # 2.调用fit_transform
    datanew = tansfer.fit_transform(data)
    print("datanew\n", datanew)
    return None

def minmax_demo():
    """
    归一化
    """
    # 1、获取数据
    data = pd.read_csv("dating.txt")
    data = data.iloc[:, :3]
    print("data:\n", data)
    # 2、实例化一个转换器类
    transfer = MinMaxScaler()
    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None


def stan_demo():
    """
    标准化
    """
    # 1、获取数据
    data = pd.read_csv("dating.txt")
    data = data.iloc[:, :3]
    print("data:\n", data)
    # 2、实例化一个转换器类
    transfer = StandardScaler()
    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None


def variance_demo():
    """
    过滤地方差特征
    """
    # 1、获取数据
    data = pd.read_csv("factor_returns.csv")
    data = data.iloc[:, 1:-2]
    print("data:\n", data)
    # 2、实例化一个转换类
    transfer = VarianceThreshold()
    # 3、调用fit_transfer
    data_new = transfer.fit_transform(data)
    print("data_new:\n:", data_new)


if __name__ == '__main__':
    # 代码1：sklearn 数据集使用
    # datasets_demo()
    # 代码2： 字典特征抽取
    # dict_demo()
    # 代码3 ：归一化
    #minmax_demo()
    # 代码4：标准化
    # stan_demo()
    variance_demo()