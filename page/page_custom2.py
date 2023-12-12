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

def plot_elderly_population_ratio(df, city_name,font):
    """
    주어진 '시도명'에 따라 해당 시군구의 총 인구수 대비 노인 인구 비율을 막대 그래프로 보여주는 함수입니다.
    """
    # 선택된 시도에 대한 데이터 필터링
    city_data = df[df['시도명'] == city_name]

    # 시군구별 고령인구 비율 계산
    city_data['노령인구비율'] = city_data['고령인구(65세 이상)'] / city_data['총인구수(명)'] * 100

    # 시군구명을 x축으로 하고 노령인구비율을 y축으로 하는 막대 그래프
    plt.rc('font', family=font)
    fig, ax = plt.subplots()
    ax.bar(city_data['시군구명'], city_data['노령인구비율'], color='skyblue')
    plt.xticks(rotation=45)
    ax.set_xlabel('시군구명')
    ax.set_ylabel('노령인구 비율 (%)')
    ax.set_title(f'{city_name} 시군구별 노령인구 비율')

    return fig

def main():
    st.title('고령화 지수 분석')

    # '시도명' 컬럼의 고유값으로 셀렉트박스를 만듭니다.
    selected_city = st.selectbox('시도를 선택하세요.', df['시도명'].unique())
    fontRegistered()
    fontNames = [f.name for f in fm.fontManager.ttflist]
    font = st.selectbox("폰트 선택 (한글의 경우 'SKYBORI'를 선택해주세요) ", unique(fontNames)) 
    # 그래프 그리는 함수를 호출하고 Streamlit에 그래프를 표시합니다.
    if st.button('그래프 그리기'):
        with st.spinner('그래프 불러오는중..'):
            fig = plot_elderly_population_ratio(df, selected_city,font)
            st.pyplot(fig)


if __name__ == '__main__':
    with st.spinner('로딩 중'):
        main()
    