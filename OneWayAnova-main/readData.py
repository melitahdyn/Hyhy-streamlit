import pandas as pd
import streamlit as st


def readExcelData(datapath, transdim=True):
    """
    用pandas获取excel的数据
    返回一个全体数据的一维数组
    """
    # 读取excel文件，默认第一个sheet
    df = pd.read_excel(datapath)
    # df.values 获取全部数据，返回二维ndarray
    data = df.values[:,1:]
    # 展示数据
    st.dataframe(data, width=680, height=220)

    # 选择是否转换成一维
    if transdim:
        # stats.levene() 只能使用一维数组，所以转换为一维数组
        data_onedim = data.reshape([-1])

        return data_onedim
    else:
        return data


def readCsvData(datapath, transdim=True):
    """
    用pandas获取Csv的数据
    返回一个全体数据的一维数组
    """
    # 读取excel文件，默认第一个sheet
    df = pd.read_csv(datapath)
    # df.values 获取全部数据，返回二维ndarray
    data = df.values[:,1:]
    # 展示数据
    st.dataframe(data)

    # 选择是否转换成一维
    if transdim:
        # stats.levene() 只能使用一维数组，所以转换为一维数组
        data_onedim = data.reshape([-1])

        return data_onedim
    else:
        return data