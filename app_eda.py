import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

# 각 운영체제에 따른 한글 출력
# 리눅스의 경우 해당 글꼴이 설치되어있어야 합니다.
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = 'c:/windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')
else:
    print('Unknown system... sorry~~~~')

def display_column_descriptions():
    st.subheader('데이터프레임 컬럼 상세 설명')
    st.text('id : 고유 id')
    st.text('hour : 시간')
    st.text('hour_bef_temperature : 1시간 전 기온')
    st.text('hour_bef_precipitation : 1시간 전 비 정보, 비가 오지 않았으면 0, 비가 오면 1')
    st.text('hour_bef_windspeed : 1시간 전 풍속(평균)')
    st.text('hour_bef_humidity : 1시간 전 습도')
    st.text('hour_bef_visibility : 1시간 전 시정(視程), 시계(視界)(특정 기상 상태에 따른 가시성을 의미')
    st.text('hour_bef_ozone : 1시간 전 오존')
    st.text('hour_bef_pm10 : 1시간 전 미세먼지(머리카락 굵기의 1/5에서 1/7 크기의 미세먼지)')
    st.text('hour_bef_pm2.5 : 1시간 전 미세먼지(머리카락 굵기의 1/20에서 1/30 크기의 미세먼지)')
    st.text('count : 시간에 따른 따릉이 대여 수')




def run_eda_app() :

    st.subheader('데이터 분석')
    train = pd.read_csv('data/train.csv')
    train=train.dropna()
    if st.button('데이터 보기'):

        st.dataframe(train)
    
        with st.expander('데이터프레임 컬럼 상세 설명') :
            display_column_descriptions()
    
    st.subheader('시간대별 대여')

    if st.button('시간대별 대여 보기') :

        fig1 = plt.figure()
        train.groupby(['hour'])['count'].mean().plot()
        plt.axvline(x=8,color='r')
        plt.axvline(x=18,color='r')
        plt.text(6, 150, 'go work')
        plt.text(16, 150, 'leave work')
        st.pyplot(fig1)

    
    chart_list = ['라인 차트','영역 차트','바 차트']
    column_menu=train.columns[2:]
    selected_chart=st.selectbox('차트를 선택하세요.',chart_list)
    with st.expander('데이터프레임 컬럼 상세 설명') :
        display_column_descriptions()

    if selected_chart == chart_list[0]:
        choice_list=st.multiselect('컬럼을 선택하세요.',column_menu)
        train_selected=train[choice_list]
        st.line_chart(train_selected)

    elif selected_chart == chart_list[1]:
        choice_list=st.multiselect('컬럼을 선택하세요.',column_menu)
        train_selected=train[choice_list]
        st.area_chart(train_selected)

    elif selected_chart == chart_list[2]:
        choice_list=st.multiselect('컬럼을 선택하세요.',column_menu)
        train_selected=train[choice_list]
        st.bar_chart(train_selected)

    st.subheader('최대 / 최소 데이터 확인하기')
    column_list = train.columns[2:]
    selected_column=st.selectbox('컬럼을 선택하세요.',column_list)
    train_min=(train.loc[train[selected_column]==train[selected_column].min(),])
    train_max=(train.loc[train[selected_column]==train[selected_column].max(),])

    st.text('최대값 데이터입니다.')
    st.dataframe(train_max)
    st.text('최소값 데이터입니다.')
    st.dataframe(train_min)


    if st.button('상관계수 차트 보기') :
        st.subheader('상관 관계 분석')
        st.text('상관 계수란? 상관관계 분석에서 두 변수 간에 선형 관계의 정도를 수량화하는 측도입니다.')
        fig2=plt.figure()
        train_corr=train[column_list].corr()
        sb.heatmap(data=train_corr,cmap='coolwarm',annot=True,fmt='.1f',linewidths=0.8,vmin=-1,vmax=1)
        st.pyplot(fig2)
        with st.expander('데이터프레임 컬럼 상세 설명') :
            display_column_descriptions()










