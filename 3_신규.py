import streamlit as st
import pandas as pd
import time

# 일반 고객 대상 재구매 할인 혜택 제공
# 일반 고객 : 최근 6개월 이내 차량 구매 기록이 없고, 구매 이력이 1회인 고객
st.write("## 일반 고객 대상 재구매 할인 혜택 제공")
st.subheader("재구매 할인 혜택 안내 시스템")

# 할인 혜택 상세 내용
st.markdown("""
- **할인율:** 차종에 따라 최대 500만원 할인
- **할인 기간:** 2025년 4월 1일 ~ 2025년 12월 31일
- **추가 혜택:**  
    - 무상 차량 점검 쿠폰 (엔진 오일 교환, 에어컨 필터 교환 등)
    - 차량 보호 패키지 (내/외부 세차, 도배 보호 코팅 등)
""")

st.markdown("### 일반 고객 선정 기준")
st.markdown("""
- **구매 이력:** 단 1회 구매 기록 보유  
- **최근 구매일:** 최근 6개월 이내 구매 기록 없음
""")

normal_client = df.loc[df["고객 등급"] == "일반", ["이름", "휴대폰 번호", "이메일"]]
normal_client.reset_index(drop=True, inplace=True)

st.markdown("### 일반 고객 리스트")
st.dataframe(normal_client)

st.markdown("### 할인 혜택 안내 예시 (이메일 및 문자)")
col1, col2 = st.columns(2)
with col1:
    st.image("images/email_sample.png", caption="할인 안내 이메일 예시")
with col2:
    st.image("images/sms_sample.png", caption="할인 안내 문자 예시")

if st.button("할인 혜택 발송 시작"):
    st.info("각 고객에게 할인 혜택 안내 메시지를 전송 중입니다. 잠시만 기다려주세요.")
    
    # 발송 시뮬레이션: 진행 상태 표시
    progress_bar = st.progress(0)
    for percent in range(1, 101):
        time.sleep(0.01)  # 실제 전송 과정에서는 API 호출 등이 이루어질 수 있음
        progress_bar.progress(percent)
    
    st.success("모든 고객에게 할인 혜택 안내 메시지를 성공적으로 전송하였습니다.")