import streamlit as st

st.title("📈 마케팅 전략")

st.write("이 페이지에서는 고객 세그먼트별 마케팅 전략을 추천합니다.")

# 마케팅 대상 선택
age_group = st.selectbox("타겟 연령대 선택", ["20대", "30대", "40대", "50대"])

# 마케팅 전략 추천 (샘플)
strategy = {
    "20대": "SNS 광고 & 무료 샘플 제공",
    "30대": "구독형 멤버십 할인 제공",
    "40대": "VIP 멤버십 혜택 확대",
    "50대": "전통 미디어 광고 강화"
}
st.write("📢 추천 마케팅 전략:", strategy[age_group])
