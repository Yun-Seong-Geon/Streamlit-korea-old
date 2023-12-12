import streamlit as st
from st_pages import Page, show_pages, add_page_title
from st_aggrid import AgGrid
from streamlit_lottie import st_lottie 

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

def 로딩화면():     
        st_lottie('https://lottie.host/50a998dc-fe29-4b90-90fc-b11311423df7/jGAtYypzAZ.json')
        
def main():
    로딩화면()


if __name__ == '__main__':
    main()
