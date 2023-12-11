import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_pages import Page, Section, show_pages, add_page_title
from st_aggrid import AgGrid
from streamlit_lottie import st_lottie 


import matplotlib.font_manager as fm 

add_page_title()

show_pages(
    [
        Page("app.py", "메인화면", "🏠"),
        Page("./page/page1.py", "데이터 확인", "🏠"),
        Page("./page/page_custom.py", "사용자 그래프 (1)", ":books:"),
        Page("./page/page_custom2.py", "사용자 그래프 (2)", ":books:"),
        Page("./page/page2.py", "그래프 확인", ":books:"),
        Page("./page/page3.py",'데이터분석 설명' ,icon="💪"),
    ]
)
data = pd.read_csv('경상남도 김해시_통계지수_노령화지수_20211231.csv',encoding = 'CP949')

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(data)
def download():
    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='data.csv',
    mime='data/csv',)


def main():
    download()
    st.write('노령화지수 통계 데이터 분석')
    st.data_editor(data) # 👈 An editable dataframe
    pass


if __name__ == '__main__':
    main()
    