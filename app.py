import openai  # openai 패키지를 임포트
import streamlit as st
import os

# API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']

# 앱 제목
st.title("나만의 레시피를 소개합니다")

# 음식재료 입력 받기
title = st.text_input("어떤 재료를 가지고 계십니까")

# 레시피 생성 버튼
if st.button("레시피 생성하기"):
    response = openai.Completion.create(
        engine="gpt-4",  # 최신 모델을 사용합니다.
        prompt=f"이 재료들로 할 수 있는 요리 레시피를 알려줘: {title}",
        max_tokens=150
    )

    result = response.choices[0].text.strip()
    st.write(result)
