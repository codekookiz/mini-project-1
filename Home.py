# Home.py
#
#     앱 소개 화면 : 간단하게 앱 기능 소개, 앱 사용 방법 등 공지
#         - 앱 개요 소개
#             - 제작 목적
#             - ...
#         - 앱 기능 소개
#         - 앱 예상 사용자


# 중요! 스트림릿 실행 코드 : 터미널에서 streamlit run Home.py
# 서버에서 돌아가는 것 확인해보고 싶다면 : https://mini-project-1-23bmqdpdnx9ctd2y38o9nx.streamlit.app/


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

import streamlit as st

st.set_page_config(page_title="현대자동차", layout="wide")

# 메인 화면 구성
st.title("📌 고객 추천 시스템")
st.image("images/car.png", use_container_width=True)
st.write("이 앱은 머신러닝을 활용하여 고객에게 맞춤형 차량을 추천하는 시스템입니다.")

# 사이드바 네비게이션
st.sidebar.title("📂 페이지 탐색")
st.sidebar.page_link("pages/1_📌_customer_input.py", label="📌 고객 정보 입력 & 제품 추천")
st.sidebar.page_link("pages/2_📊_analysis.py", label="📊 분석 대시보드")
st.sidebar.page_link("pages/3_📈_marketing.py", label="📈 마케팅 전략")
st.sidebar.page_link("pages/4_ℹ️_app_info.py", label="ℹ️ 앱 소개")
