import streamlit as st
import pandas as pd
import time

df = pd.read_csv("data/고객db_전처리.csv")

# 신규 고객에 대한 서비스 혜택 제공
# 신규 고객 : 최근 6개월 이내 첫 구매 이력이 있는 고객
st.write("## 신규 고객 대상 프로모션 1 : 웰컴 패키지 제공")
st.subheader("서비스 혜택 세부 내용")

# 서비스 혜택 상세 내용
st.markdown("""
- **최초 무료 서비스:**
""")

st.markdown("### 일반 고객 선정 기준")
st.markdown("""
- **구매 이력:** 단 1회 구매 기록 보유  
- **최근 구매일:** 최근 6개월 이내 구매 기록 없음
""")

new_client = df.loc[df["고객 등급"] == "신규", ["이름", "휴대폰 번호", "이메일"]]
new_client.reset_index(drop=True, inplace=True)

st.markdown("### 일반 고객 리스트")
st.dataframe(new_client)

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

st.markdown("---")