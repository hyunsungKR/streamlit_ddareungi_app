# 🚴🏻‍♀️ 서울시 따릉이 대여량과 대여 예측 👀

## 📌 Project Explanation
* 날짜와 날씨, 여러가지 환경이 기입된 자전거 대여량의 데이터를 포함하고 있습니다.
* 인공지능 모델은 pkl 파일화하여 진행하였습니다.
* 서울시 따릉이의 대여량을 분석하여 예측 및 차트로 보여주는 앱입니다.
* EDA를 눌러보시면 데이터별로 분석된 차트를 확인하실 수 있습니다.
* ML은 인공지능이 학습하여 날씨에 따라 예측한 대여량을 확인하실 수 있습니다.
* 서울시 따릉이 대여량 예측 경진대회의 데이터를 이용하였습니다.
* AWS EC2를 이용하여 서버를 관리하였습니다.
* Github Actions를 이용한 CI/CD를 사용하였습니다.

## 📌hyunsungKR
<a href="https://github.com/hyunsungKR/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/></a> <a href="https://hyunsungstory.tistory.com/"><img src="https://img.shields.io/badge/Tistory-466BB0?style=flat-square&logo=Tistory&logoColor=white"/></a>

## 📌Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

## 📌 Library
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> 

<img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/scikit-learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/> <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=SciPy&logoColor=white"/>   

## 📌Tool
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/> 

## 📌Code block
```python
 # 결측치 제거
train=train.dropna()
```
```python
# 상관 계수
plt.figure(figsize = (12, 12))
sb.heatmap(train.corr(), annot = True)
plt.show()
```
```python
# 시간대 별로 평균 몇개가 대여 되었는지 확인.
train.groupby(['hour'])['count'].mean()
```

## 📌 ML
* Using Model : from sklearn.linear_model import LinearRegression
```python
# X,y로 분리
X=train.iloc[:,[2,3,4]]
y=train['count']
```
```python
# Training / Test 셋으로 분리
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=19)
```
```python
# 모델링 과정
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
```
```python
# joblib 라이브러리로 저장
import joblib
joblib.dump(regressor,'regressor2.pkl')
```





## 📌 URL
  - http://ec2-3-36-77-30.ap-northeast-2.compute.amazonaws.com:8501/

## 📌 Screen Shot
![image](https://user-images.githubusercontent.com/120348500/208594640-9bfb3de6-6f38-446e-91bf-c2f0339a558d.png)
![image](https://user-images.githubusercontent.com/120348500/208594695-93fe2f53-f990-4775-ac3a-84236ad645a9.png)
![image](https://user-images.githubusercontent.com/120348500/208594739-c5f96bf9-1ea5-4c7c-bf2b-a31b7d7c3196.png)
![image](https://user-images.githubusercontent.com/120348500/208594810-d1728dd9-9d47-4c59-9668-ec41a8f8525c.png)
![image](https://user-images.githubusercontent.com/120348500/208594857-f99ce906-738d-4f14-a6df-aeb1023cb6b6.png)


## 📌 Reference

* 메인화면 동영상 : https://youtu.be/bk21QVW51LQ
* 서울시 따릉이 데이터 : https://dacon.io/competitions/open/235576/data
