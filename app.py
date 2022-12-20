import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app


st.set_page_config(page_title='ddareungi')


def main() :
    st.header('🚴🏻‍♀️ 서울시 따릉이 대여량과 대여량 예측')
    with st.sidebar:
        st.image('http://love.seoul.go.kr/Pds/Board/seoul_news_write/Editor/0501_03_02.png')
        menu = option_menu("App Menu", ["Home", "EDA", "ML"],
                            icons=['house', 'bar-chart', 'kanban'],
                            menu_icon="bi bi-menu-up", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"}, })
    if menu == 'Home' :
        run_home_app()
    elif menu == 'EDA' :
        run_eda_app()
    elif menu == 'ML' :
        run_ml_app()

if __name__ == '__main__' :
    main()