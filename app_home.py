import streamlit as st
from PIL import Image

def run_home_app():

    st.write('📝 이 앱은 서울시 따릉이의 대여량을 분석하여 예측 및 차트로 보여주는 앱입니다.')
    st.write('📝 EDA를 눌러보시면 데이터별로 분석된 차트를 확인하실 수 있습니다.')
    st.write('📝 ML은 인공지능이 학습하여 날씨,시간에따라 예측한 대여량을 확인하실 수 있습니다.')
    st.video('https://youtu.be/bk21QVW51LQ',start_time=10,format='video/mp4')