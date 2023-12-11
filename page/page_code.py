import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_pages import Page, Section, show_pages, add_page_title
import matplotlib.font_manager as fm 
import font as fn
from st_aggrid import AgGrid

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
df = data.copy()

def 노령화지수분포그래프(fontname):
    code = '''
            plt.rc('font', family=fontname)
            fig=plt.figure(figsize=(8, 6))
            sns.histplot(data['노령화지수(퍼센트)'], bins=20, kde=True)
            plt.title('노령화 지수 분포')
            plt.xlabel('노령화 지수(퍼센트)')
            plt.ylabel('빈도')
            plt.show()
        '''
    st.code(code,language='python')
    plt.rc('font', family=fontname)
    fig=plt.figure(figsize=(8, 6))
    sns.histplot(data['노령화지수(퍼센트)'], bins=20, kde=True)
    plt.title('노령화 지수 분포')
    plt.xlabel('노령화 지수(퍼센트)')
    plt.ylabel('빈도')
    plt.show()
    st.pyplot(fig)

def 시도별고령인구그래프(fontname):
    code = '''
        fig=plt.figure(figsize=(8, 6))
        df['고령인구 비율'] = df['고령인구(65세 이상)'] / df['총인구수(명)'] * 100
        sns.barplot(x='시도명', y='고령인구 비율', data=df, hue='시도명')
        plt.title('시도별 고령 인구 비율')
        plt.xticks(rotation=45)
        plt.xlabel('시도명')
        plt.ylabel('고령인구 비율 (%)')
        plt.show()
    '''
    st.code(code,language='python')
    plt.rc('font', family=fontname)   
    fig=plt.figure(figsize=(8, 6))
    df['고령인구 비율'] = df['고령인구(65세 이상)'] / df['총인구수(명)'] * 100
    sns.barplot(x='시도명', y='고령인구 비율', data=df, hue='시도명')
    plt.title('시도별 고령 인구 비율')
    plt.xticks(rotation=45)
    plt.xlabel('시도명')
    plt.ylabel('고령인구 비율 (%)')
    plt.show()
    st.pyplot(fig)

def 시도별노령화지수평균(fontname):
    code = '''
    plt.rc('font', family=fontname)   
    fig=plt.figure(figsize=(8, 6))
    sns.scatterplot(x='총인구수(명)', y='노령화지수(퍼센트)', data=df)
    plt.title('노령화 지수와 총인구수의 관계')
    plt.xlabel('총인구수(명)')
    plt.ylabel('노령화 지수(퍼센트)')
    plt.show()
    '''
    st.code(code,language='python')
    plt.rc('font', family=fontname)   
    fig=plt.figure(figsize=(8, 6))
    sns.scatterplot(x='총인구수(명)', y='노령화지수(퍼센트)', data=df)
    plt.title('노령화 지수와 총인구수의 관계')
    plt.xlabel('총인구수(명)')
    plt.ylabel('노령화 지수(퍼센트)')
    plt.show()
    st.pyplot(fig)

def 노령화지수총인구수관계그래프(fontname):
    code = '''
    plt.rc('font', family=fontname)   
    avg_aging_index_by_city = df.groupby('시도명')['노령화지수(퍼센트)'].mean().reset_index()
    fig=plt.figure(figsize=(8, 6))
    sns.barplot(x='시도명', y='노령화지수(퍼센트)', data=avg_aging_index_by_city,hue='시도명')
    plt.xticks(rotation=45)
    plt.title('시도별 노령화지수 평균')
    plt.xlabel('시도명')
    plt.ylabel('노령화지수(퍼센트) 평균')
    plt.show()
    '''
    st.code(code,language='python')
    plt.rc('font', family=fontname)   
    avg_aging_index_by_city = df.groupby('시도명')['노령화지수(퍼센트)'].mean().reset_index()
    fig=plt.figure(figsize=(8, 6))
    sns.barplot(x='시도명', y='노령화지수(퍼센트)', data=avg_aging_index_by_city,hue='시도명')
    plt.xticks(rotation=45)
    plt.title('시도별 노령화지수 평균')
    plt.xlabel('시도명')
    plt.ylabel('노령화지수(퍼센트) 평균')
    plt.show()
    st.pyplot(fig)
    
def graphs(fontname):
    st.divider()
    노령화지수분포그래프(fontname)
    st.divider()
    시도별고령인구그래프(fontname)
    st.divider()
    시도별노령화지수평균(fontname)
    st.divider()
    노령화지수총인구수관계그래프(fontname)
    st.divider()

font = "./font/SKYBORI.ttf"

def main():
    with st.spinner('그래프 불러오는중..'):
        graphs(font)
    pass


if __name__ == '__main__':
    main()
    