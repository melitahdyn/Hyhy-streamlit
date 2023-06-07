import streamlit as st
from scipy import stats
from readData import readExcelData, readCsvData

st.write(
    """
    # 🧮 ANOVA Test App
    Upload your experiment results to see the significance of your ANOVA test.
    """
)

file_style = st.radio(
    "Select the type of file to upload or use the example file",
    ('csv', 'xlsx', 'example file')
)

if file_style == 'csv':
    # 上传文件
    uploaded_file1 = st.file_uploader("Choose the 1st file", type=['csv'], key=1)
    uploaded_file2 = st.file_uploader("Choose the 2ed file", type=['csv'], key=2)

    if (uploaded_file1 and uploaded_file2) is None:
        st.write('statistic and pvalue:')
        st.write('statistic:', 0.00, 'pvalue:', 0.00)

    else:  # 获取到文件的话
        st.subheader("Data preview")
        uploaded_file1 = readCsvData(uploaded_file1)
        uploaded_file2 = readCsvData(uploaded_file2)
        stat, p = stats.f_oneway(uploaded_file1, uploaded_file2)

        st.subheader("Results for ANOVA test")
        st.write('statistic:', stat, 'pvalue:', p)

        if p > 0.05:
            st.success('Probably the same distribution')
        else:
            st.warning('Probably different distributions')

elif file_style == 'xlsx':
    # 上传文件
    uploaded_file1 = st.file_uploader("Choose the 1st file", type=['xlsx'], key=1)
    uploaded_file2 = st.file_uploader("Choose the 2ed file", type=['xlsx'], key=2)

    if (uploaded_file1 and uploaded_file2) is None:
        st.write('statistic and pvalue:')
        st.write('statistic:', 0.00, 'pvalue:', 0.00)

    else:  # 获取到文件的话
        st.subheader("Data preview")
        uploaded_file1 = readExcelData(uploaded_file1)
        uploaded_file2 = readExcelData(uploaded_file2)
        stat, p = stats.f_oneway(uploaded_file1, uploaded_file2)

        st.subheader("Results for ANOVA test")
        st.write('statistic:', stat, 'pvalue:', p)

        if p > 0.05:
            st.success('Probably the same distribution')
        else:
            st.warning('Probably different distributions')

else:
    uploaded_file1 = 'normrvs1.xlsx'
    uploaded_file2 = 'normrvs3.xlsx'
    st.subheader("Data preview")
    uploaded_file1 = readExcelData(uploaded_file1)
    uploaded_file2 = readExcelData(uploaded_file2)
    stat, p = stats.f_oneway(uploaded_file1, uploaded_file2)

    st.subheader("Results for ANOVA test")
    st.write('statistic:', stat, 'pvalue:', p)

    if p > 0.05:
        st.success('Probably the same distribution')
    else:
        st.warning('Probably different distributions')
