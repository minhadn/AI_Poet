from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
import os

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
openai_api_key = os.getenv('OPENAI_API_KEY')
chat_model = ChatOpenAI(api_key=openai_api_key)

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        # 메서드 이름을 generate()로 변경해보세요
        result = chat_model.generate(prompt=subject + "에 대한 시를 써줘.")
        st.write(result)
