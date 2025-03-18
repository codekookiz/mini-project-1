import streamlit as st

st.set_page_config(page_title="고객 혜택 조회", layout="wide")

st.title("고객 혜택 조회")

st.subheader("선택한 차량의 프로모션 혜택")
st.write("고객님이 선택하신 차량에 대한 혜택이 아래에 표시됩니다.")

selected_model = st.selectbox("차량 모델 선택", ["G80", "팰리세이드", "스타리아"])

if selected_model == "G80":
    st.write("- 개별소비세 3.5% 인하")
    st.write("- 최대 300만 원 추가 할인 제공")
    st.write("- 60개월 무이자 할부 가능")
elif selected_model == "팰리세이드":
    st.write("- 다자녀 가구 특별 무이자 할부 제공")
    st.write("- 신차 구매 시 프리미엄 카시트 증정")
    st.write("- 뒷좌석 모니터 옵션 30% 할인")
else:
    st.write("- 법인 및 사업자 특별 리스 할인 제공")
    st.write("- 계약 유지 후 상위 차종 변경 가능")
    st.write("- 공식 서비스센터 1년 무료 점검 혜택")

st.subheader("할부 조건")
st.write("직원이 설정한 할부 조건이 여기에 표시됩니다.")
