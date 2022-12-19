import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

regressor = joblib.load('data/regressor.pkl')

def run_ml_app():
    st.subheader('따릉이 대여수 예측')

    train = pd.read_csv('data/train.csv')
    train=train.dropna()

    if st.button('데이터 보기'):

        st.dataframe(train)
    
        with st.expander('데이터프레임 컬럼 상세 설명') :
            st.subheader('데이터프레임 컬럼 상세 설명')
            st.text('id : 고유 id')
            st.text('hour : 시간)')
            st.text('temperature : 기온)')
            st.text('precipitation : 비가 오지 않았으면 0, 비가 오면 1)')
            st.text('windspeed : 풍속(평균)')
            st.text('humidity : 습도')
            st.text('visibility : 시정(視程), 시계(視界)(특정 기상 상태에 따른 가시성을 의미)')
            st.text('ozone : 오존')
            st.text('pm10 : 미세먼지(머리카락 굵기의 1/5에서 1/7 크기의 미세먼지)')
            st.text('pm2.5 : 미세먼지(머리카락 굵기의 1/20에서 1/30 크기의 미세먼지)')
            st.text('count : 시간에 따른 따릉이 대여 수')
    
    rain = st.radio('1시간 전 기준 비가 왔나요?',['네','아니오'])
    if rain == '아니오':
        rain = 0
    else :
        rain = 1
    
    temp = st.number_input('기온 입력'-25,40)

    wind = st.number_input('풍속 입력',0,20)

    new_data=np.array([temp,rain,wind])

    new_data = new_data.reshape(1,3)

    y_pred = regressor.predict(new_data)

    y_pred = round(y_pred[0],1)

    st.info('예측한 따릉이 대여 갯수는 {}입니다.'.format(y_pred))

    print(y_pred)

    

