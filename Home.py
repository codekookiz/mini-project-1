import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

st.set_page_config(page_title="현대자동차 고객 추천 시스템", layout="wide")

# 메인 화면 구성
st.title("🚗 현대자동차 고객 추천 시스템")
st.image("images/car.png", use_container_width=True)
st.write("이 앱은 머신러닝을 활용하여 고객에게 맞춤형 차량을 추천하는 시스템입니다.")

# 🔹 카카오톡 상담 기능 (오픈채팅방 연동)
st.sidebar.markdown("### 💬 현대자동차 카카오톡 상담")

# 🔹 오픈채팅방 링크 설정 (여기에 본인의 카카오톡 오픈채팅 링크를 입력하세요)
kakao_open_chat_link = "https://open.kakao.com/o/sKl8ocmh"  # 여기에 본인 오픈채팅 링크 입력

# 🔹 오픈채팅방 버튼 추가
kakao_chat_button = f"""
<a href="{kakao_open_chat_link}" target="_blank">
    <img src="https://developers.kakao.com/assets/img/about/logos/kakaotalksharing/kakaotalk_sharing_btn_medium.png" width="100">
</a>
"""
st.sidebar.markdown(kakao_chat_button, unsafe_allow_html=True)

st.sidebar.write("📌 버튼을 클릭하면 현대자동차 상담 오픈채팅방으로 이동합니다.")

# 🔹 추가로 사용자가 직접 입력할 수 있는 상담 요청 메시지 필드 제공
st.sidebar.write("또는, 상담 내용을 입력하고 오픈채팅방에 복사하여 보내세요.")
user_message = st.sidebar.chat_input("상담 내용을 입력하세요:")

# 🔹 사용자가 입력할 경우 자동으로 복사 내용 표시
if user_message:
    st.sidebar.write("✅ 아래 내용을 복사하여 오픈채팅방에 입력하세요:")
    st.sidebar.code(user_message, language="text")

