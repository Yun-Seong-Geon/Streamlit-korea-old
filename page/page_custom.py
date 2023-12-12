import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_pages import Page, Section, show_pages, add_page_title
from st_aggrid import AgGrid
from streamlit_lottie import st_lottie 


import matplotlib.font_manager as fm 


import os
def unique(list):
    x = np.array(list)
    return np.unique(x)

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/font']  # 사용자 정의 폰트 디렉토리 경로
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)


add_page_title()

show_pages(
    [
        Page("app.py", "메인화면", "🏠"),
        Page("./page/page1.py", "데이터 확인", "🏠"),
        Page("./page/page_custom.py", "사용자 그래프 (1)", ":books:"),
        Page("./page/page_custom2.py", "사용자 그래프 (2)", ":books:"),
        Page("./page/page2.py", "그래프 확인", ":books:"),
        Page("./page/page_code.py", "그래프 코드 확인", ":books:"),
        Page("./page/page3.py",'데이터분석 설명' ,icon="💪"),
    ]
)

data = pd.read_csv('경상남도 김해시_통계지수_노령화지수_20211231.csv',encoding = 'CP949')
df = data.copy()
colors = ['blue', 'green', 'red', 'purple', 'orange']

def draw_graph(selected_city,font):
    # 선택된 시도에 해당하는 데이터만 필터링합니다.
    filtered_df = df[df['시도명'] == selected_city]
    plt.rc('font', family=font)
    # 그래프를 그립니다. 여기서는 예시로 산점도를 그리겠습니다.
    fig, ax = plt.subplots()
    sns.scatterplot(x='유소년(14세 이하)', y='노령화지수(퍼센트)', data=filtered_df, ax=ax, hue='시군구명')
    ax.set_title(f'{selected_city}의 고령화지수와 유소년 인구수의 관계')
    ax.set_xlabel('유소년(14세 이하)')
    ax.set_ylabel('노령화지수(퍼센트)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # Streamlit에 그래프를 표시합니다.
    st.pyplot(fig)

def main():
    st.write('노령화지수 통계 데이터 분석')
        # '시도명' 컬럼의 고유값으로 셀렉트박스를 만듭니다.
    city_list = df['시도명'].unique()
    selected_city = st.selectbox('시도를 선택하세요.', city_list)

    # 그래프 그리는 함수를 호출합니다.
    fontRegistered()
    fontNames = [f.name for f in fm.fontManager.ttflist]
    font = st.selectbox("폰트 선택 (한글의 경우 'SKYBORI'를 선택해주세요) ", unique(fontNames))
    with st.spinner('그래프 불러오는중..'): 
        draw_graph(selected_city,font)
    pass


if __name__ == '__main__':
    main()
    