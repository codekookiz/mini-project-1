import streamlit as st

st.set_page_config(page_title="현대자동차 고객 추천 시스템", layout="wide")

# 메인 화면 구성
st.title("🚗 현대자동차 고객 추천 시스템")
st.image("images/car.png", use_container_width=True)
st.write("이 앱은 머신러닝을 활용하여 고객에게 맞춤형 차량을 추천하는 시스템입니다.")

# 🔹 오픈채팅방 링크 설정 (여기에 본인의 카카오톡 오픈채팅 링크를 입력하세요)
kakao_open_chat_link = "https://open.kakao.com/o/sKl8ocmh"  # 여기에 본인 오픈채팅 링크 입력

# 🔹 플로팅 버튼 & "상담 하기" 텍스트 추가
floating_button = f"""
<style>
.floating-container {{
    position: fixed;
    bottom: 20px;
    right: 20px;
    text-align: center;
    z-index: 1000;
}}

.floating-text {{
    font-size: 16px;
    font-weight: bold;
    color: #333;
    margin-bottom: 5px;
}}

.floating-btn {{
    background: none;
    border: none;
    cursor: pointer;
}}

.floating-btn img {{
    width: 60px;  /* 크기 조절 가능 */
    height: 60px;
    border-radius: 50%;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
}}
</style>

<div class="floating-container">
    <div class="floating-text">💬 상담 하기</div>
    <a href="{kakao_open_chat_link}" target="_blank" class="floating-btn">
        <img src="https://developers.kakao.com/assets/img/about/logos/kakaotalksharing/kakaotalk_sharing_btn_medium.png">
    </a>
</div>
"""

st.markdown(floating_button, unsafe_allow_html=True)
