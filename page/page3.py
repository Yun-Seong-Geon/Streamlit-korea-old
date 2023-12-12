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
        Page("./page/page_code.py", "그래프 코드 확인", ":books:"),
        Page("./page/page3.py",'데이터분석 설명' ,icon="💪"),
    ]
)

data = pd.read_csv('경상남도 김해시_통계지수_노령화지수_20211231.csv',encoding = 'CP949')

문구1 = '''
이 그래프는 한국의 고령화지수 퍼센트를 빈도로 나타내 비교한 것입니다.
'고령화 지수(퍼센트)'는 해당 지역의 인구 중 65세 이상 인구가 차지하는 비율을 나타냅니다.
이 비율은 한국의 모든 퍼센트를 나타냅니다. \n

분석 결과에 따르면, 고령화 지수는 균일하게 분포되어 있지 않습니다.
고령화지수가 100에서 200퍼센트 사이가 가장 빈도가 높으며 점차 줄어드는 추세입니다.\n

'''
문구2 = '''
이 막대 그래프는 한국의 다양한 시도들에서 고령 인구 비율을 비교한 것입니다. 
'고령인구 비율'은 해당 지역의 인구 중 65세 이상 인구가 차지하는 비율을 나타냅니다. 
이 비율은 각 시도의 총 인구수에 대한 고령 인구의 수를 백분율로 환산하여 구합니다.\n

분석 결과에 따르면, 각 시도의 고령 인구 비율은 상당히 균일하게 분포되어 있지 않습니다. 

어떤 시도는 비교적 낮은 고령 인구 비율을 보이는 반면, 다른 시도는 높은 비율을 보입니다. 이러한 차이는 각 지역의 인구 구조, 경제 활동, 사회 복지 정책, 의료 접근성 등 
다양한 요소에 의해 영향을 받을 수 있습니다.\n

또한, 고령 인구 비율이 높은 지역은 노인 인구에 대한 사회적 서비스와 지원을 강화할 필요가 있을 수 있으며, 이는 의료, 주거, 일자리 창출, 
여가 활동 등 다양한 분야에서 노인 친화적 정책을 구현해야 할 필요성을 시사합니다. \n

막대 그래프 상의 오차 막대는 각 시도별 고령 인구 비율 측정값의 불확실성을 나타냅니다. 
오차 막대가 큰 지역은 해당 비율의 추정치가 더 불확실하며, 이는 인구 통계 데이터의 샘플링 오류, 기록 오류, 또는 인구 변동성 등으로 인해 발생할 수 있습니다. \n

이 데이터는 향후 인구 고령화에 대비한 정책 결정, 지역 사회 서비스의 계획 및 배치, 
그리고 고령화가 진행됨에 따라 발생할 수 있는 사회적, 경제적 문제에 대한 연구에 중요한 기초 자료를 제공합니다. 
'''
문구3 = '''
세 번째 그래프는 두 변수 사이의 관계를 보여주는 산점도입니다. 
x축은 총 인구수이며, y축은 고령화 지수입니다. \n
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
    font = st.selectbox("폰트 선택 (한글의 경우 'SKYBORI'를 선택해주세요) ", unique(fontNames))
    
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
    