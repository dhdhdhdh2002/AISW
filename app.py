import os
import openai
import streamlit as st

# 환경 변수로 API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']
api_key = os.environ.get("OPENAI_API_KEY")

# OpenAI 클라이언트 설정
openai.api_key = api_key

# 앱 제목
st.title("나만의 레시피를 소개합니다")

# 음식재료 입력 받기
title = st.text_input("어떤 재료를 가지고 계십니까")

# 음식재료 출력
if st.button("레시피 생성하기"):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-4",  # 올바른 모델 이름
        messages=[
            {
                "role": "user",
                "content": title,  # 사용자가 입력한 재료 사용
            },
            {
                "role": "system",
                "content": "입력받은 재료로 할 수 있는 맛있는 요리 레시피를 알려줘",
            }
        ]
    )

    result = chat_completion.choices[0].message['content']
    st.write(result)
