# π΄π»ββοΈ μμΈμ λ°λ¦μ΄ λμ¬λκ³Ό λμ¬λ μμΈ‘ π


## π Project Explanation
* λ μ§μ λ μ¨, μ¬λ¬κ°μ§ νκ²½μ΄ κΈ°μλ μμ κ±° λμ¬λμ λ°μ΄ν°λ₯Ό ν¬ν¨νκ³  μμ΅λλ€.
* μΈκ³΅μ§λ₯ λͺ¨λΈμ pkl νμΌννμ¬ μ§ννμμ΅λλ€.
* μμΈμ λ°λ¦μ΄μ λμ¬λμ λΆμνμ¬ μμΈ‘ λ° μ°¨νΈλ‘ λ³΄μ¬μ£Όλ μ±μλλ€.
* EDAλ₯Ό λλ¬λ³΄μλ©΄ λ°μ΄ν°λ³λ‘ λΆμλ μ°¨νΈλ₯Ό νμΈνμ€ μ μμ΅λλ€.
* MLμ μΈκ³΅μ§λ₯μ΄ νμ΅νμ¬ λ μ¨μ λ°λΌ μμΈ‘ν λμ¬λμ νμΈνμ€ μ μμ΅λλ€.
* μμΈμ λ°λ¦μ΄ λμ¬λ μμΈ‘ κ²½μ§λνμ λ°μ΄ν°λ₯Ό μ΄μ©νμμ΅λλ€.
* AWS EC2λ₯Ό μ΄μ©νμ¬ μλ²λ₯Ό κ΄λ¦¬νμμ΅λλ€.
* Github Actionsλ₯Ό μ΄μ©ν CI/CDλ₯Ό μ¬μ©νμμ΅λλ€.
* μ μ§λ³΄μμμμ μμνκ² νκΈ° μν΄μ λ€λ₯Έ νμΌμμ ν¨μλ₯Ό λ§λ€κ³  κ·Έ ν¨μλ₯Ό importν΄μ μμμ νμμ΅λλ€.

## πhyunsungKR
<a href="https://github.com/hyunsungKR/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/></a> <a href="https://hyunsungstory.tistory.com/"><img src="https://img.shields.io/badge/Tistory-466BB0?style=flat-square&logo=Tistory&logoColor=white"/></a>

## πLanguages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

## π Library
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> 

<img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/scikit-learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/> <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=SciPy&logoColor=white"/>   

## πTool
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/> 

## πCode block
```python
 # κ²°μΈ‘μΉ μ κ±°
train=train.dropna()
```
```python
# μκ΄ κ³μ
plt.figure(figsize = (12, 12))
sb.heatmap(train.corr(), annot = True)
plt.show()
```
```python
# μκ°λ λ³λ‘ νκ·  λͺκ°κ° λμ¬ λμλμ§ νμΈ.
train.groupby(['hour'])['count'].mean()
```

## π ML
* Using Model : from sklearn.linear_model import LinearRegression
```python
# X,yλ‘ λΆλ¦¬
X=train.iloc[:,[2,3,4]]
y=train['count']
```
```python
# Training / Test μμΌλ‘ λΆλ¦¬
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=19)
```
```python
# λͺ¨λΈλ§ κ³Όμ 
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
```
```python
# joblib λΌμ΄λΈλ¬λ¦¬λ‘ μ μ₯
import joblib
joblib.dump(regressor,'regressor2.pkl')
```





## π URL
  - http://ec2-3-36-77-30.ap-northeast-2.compute.amazonaws.com:8501/

## π Screen Shot
![image](https://user-images.githubusercontent.com/120348500/208594640-9bfb3de6-6f38-446e-91bf-c2f0339a558d.png)
![image](https://user-images.githubusercontent.com/120348500/208594695-93fe2f53-f990-4775-ac3a-84236ad645a9.png)
![image](https://user-images.githubusercontent.com/120348500/208594739-c5f96bf9-1ea5-4c7c-bf2b-a31b7d7c3196.png)
![image](https://user-images.githubusercontent.com/120348500/208594810-d1728dd9-9d47-4c59-9668-ec41a8f8525c.png)
![image](https://user-images.githubusercontent.com/120348500/208594857-f99ce906-738d-4f14-a6df-aeb1023cb6b6.png)


## π Reference

* λ©μΈνλ©΄ λμμ : https://youtu.be/bk21QVW51LQ
* μμΈμ λ°λ¦μ΄ λ°μ΄ν° : https://dacon.io/competitions/open/235576/data
