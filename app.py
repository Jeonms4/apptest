import streamlit as st
import pandas as pd
import numpy as np

st.title("Hi")

st.header("목차")

st.subheader("1. LLM이란")
st.write("대형 언어 모델(Large language model, LLM) 또는 거대 언어 모델은 수많은 파라미터(보통 수십억 웨이트 이상)를 보유한 인공 신경망으로 구성되는 언어 모델이다.")
st.subheader("2. LLM 실습")

if st.button("여기 눌러보세요"):
    st.write("Data Loading....")
    #데이터 로딩 함수는 여기에!

st.write("당신의 성별은?")

checkbox_btn1 = st.checkbox('남')
checkbox_btn2 = st.checkbox('여')

if checkbox_btn1:
    st.write("남성입니다.")

if checkbox_btn2:
    st.write("여성입니다")

selected_item = st.radio("Radio Part", ("짜장", "짬뽕", "볶음밥"))

if selected_item == "짜장":
    st.write("짜장면")
elif selected_item == "짬뽕":
    st.write("짬뽕")
elif selected_item == "볶음밥":
    st.write("볶음밥")
else:
    st.write("메뉴를 고르세요")

option = st.selectbox('학년을 고르세요', ['1학년', '2학년', '3학년'])

st.write('You selected', option)

multi_select = st.multiselect('전공', ['경영', '경제', '회계', '화학', '복수전공은 2개 이상 선택 가능'])
st.write('Yout selected', multi_select)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values', values)

df=pd.DataFrame({"이름":['홍일동', '홍이동', '홍삼동', '홍사동', '홍오동']})
st.table(df)

