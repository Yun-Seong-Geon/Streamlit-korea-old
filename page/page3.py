import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_pages import Page, Section, show_pages, add_page_title
from st_aggrid import AgGrid
from streamlit_lottie import st_lottie 
import time
from page import page2 as two
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
        Page("./page/page3.py",'데이터분석 설명' ,icon="💪"),
    ]
)

data = pd.read_csv('경상남도 김해시_통계지수_노령화지수_20211231.csv',encoding = 'CP949')

문구1 = '''
히스토그램과 적합 곡선

첫 번째 그래프는 특정 인구 통계 변수의 분포를 나타내는 히스토그램입니다.\n
x축은 고량화 지수를 퍼센트로 나타냈으며 y축은 빈도를 나타냅니다. \n
이 그래프는 고령화 지수에 대한 분포를 나타내는 히스토그램입니다.\n
현재 고량화 지수가 
'''
문구2 = '''
오차 막대가 있는 막대 그래프

두 번째 그래프는 오차 막대가 포함된 다채로운 막대 그래프를 보여줍니다. 오차 막대는 데이터의 변동성 또는 표준 편차를 나타냅니다. 
각 막대는 다른 범주를 대표하며, 이는 다른 연도나 노인 인구 내 다양한 연령 그룹일 수 있습니다. 
오차 막대는 각 범주 내 변동성을 고려하면서 다른 범주의 평균 값을 비교하는 데 유용합니다.
'''
문구3 = '''
산점도

세 번째 그래프는 두 변수 사이의 관계를 보여주는 산점도입니다. 
x축은 총 인구수와 같은 지수나 수치를 나타낼 수 있으며, y축은 고령화 지수와 같은 다른 인구 통계 지표를 나타낼 수 있습니다. 
산점도는 데이터에서 추세, 상관 관계 또는 패턴을 식별하는 데 유용합니다.
'''
문구4 = f'''
클러스터 막대 그래프

네번째 그래프는 클러스터 형식의 막대 그래프를 보여주며, 각 클러스터는 다른 범주(예를 들어 지역 또는 시간 기간)를 나타낼 수 있고, 클러스터 내의 막대는 부범주(가능한 연령 그룹)를 대표할 수 있습니다. 
이 그래프 유형은 주요 범주들 간의 부범주들을 비교하는 데 유용합니다.
'''
문구5 = '''
버블 산점도

마지막 그래프는 버블 크기가 세 번째 변수(예를 들어 인구 규모)를 나타내는 버블 산점도로 보입니다. 
이 유형의 차트는 축상의 두 수치 변수와 버블 크기에 의해 나타나는 세 번째 차원의 데이터에 대한 정보를 제공할 수 있습니다.
'''

def main():
    fontRegistered()
    fontNames = [f.name for f in fm.fontManager.ttflist]
    font = st.selectbox("폰트 선택", unique(fontNames))
    
    st.subheader('고령화 지수 관련 데이터를 분석 및 활용하는 홈페이지입니다.')
    st.divider()
    two.노령화지수분포그래프(font)
    st.write(문구1)
    
    st.divider()
    two.시도별고령인구그래프(font)
    st.write(문구2)
    
    st.divider()
    two.시도별노령화지수평균(font)
    st.write(문구3)
    
    st.divider()
    two.노령화지수총인구수관계그래프(font)
    st.write(문구4)
    
    st.divider()
    two.고령화지수유소년관계그래프(font)
    st.write(문구5)
    
    pass


if __name__ == '__main__':
    main()
    