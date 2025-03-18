import streamlit as st

st.title("현대자동차 친환경차 보조금 안내")

st.write("아래 버튼을 클릭하면 현대자동차 친환경차 보조금 페이지로 이동합니다.")

if st.button("현대자동차 보조금 안내 페이지 보기"):
    st.markdown("[현대자동차 보조금 페이지](https://www.hyundai.com/kr/ko/e/vehicles/eco-incentive?utm_source=hyundaicom&utm_medium=display&utm_campaign=2023_quickwin&utm_content=gnb)", unsafe_allow_html=True)
