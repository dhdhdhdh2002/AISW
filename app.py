import os
from openai import OpenAI
import streamlit as st


os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),)


#앱 제목
st.title("나만의 레시피를 소개합니다")

#음식재료 입력 받기
title = st.text_input("어떤 재료를 가지고 계십니까")

#음식재료 출력
if st.button("레시피 생성하기"):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "food",
            },
            {
                "role": "system",
                "content": "입력받은 재로로 할 수 있는 맛있는 요리 레시피를 알려줘",
            }
        ],
        model="gpt-4o",
    )

    result = chat_completion.choices[0].message.content
    st.write(result)\
import os
from openai import OpenAI
import streamlit as st


os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),)


#앱 제목
st.title("나만의 레시피를 소개합니다")

#음식재료 입력 받기
title = st.text_input("어떤 재료를 가지고 계십니까")

#음식재료 출력
if st.button("레시피 생성하기"):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "food",
            },
            {
                "role": "system",
                "content": "입력받은 재로로 할 수 있는 맛있는 요리 레시피를 알려줘",
            }
        ],
        model="gpt-4o",
    )

    result = chat_completion.choices[0].message.content
    st.write(result)
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "food",
        },
        {
            "role": "system",
            "content": "입력받은 재로로 할 수 있는 맛있는 요리 레시피를 알려줘",
        }
    ],
    model="gpt-4o",
)

print(chat_completion.choices[0].message.content)
API_open_key = "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"
print(API_open_key)
OPENAI_API_KEY = "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"