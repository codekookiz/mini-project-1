import streamlit as st

def show_app_info():
    # 🚗 CI 로고 + 타이틀
    st.markdown("""
    <h1 style="display:flex; align-items:center;">
        <img src="https://www.hyundai.com/etc/designs/hyundai/ww/en/images/common/logo.png" 
             alt="현대자동차 로고" 
             style="height:40px; margin-right:10px;">
        분석 대시보드
    </h1>
    """, unsafe_allow_html=True)

    # 📌 앱 소개
    st.markdown("### 📌 앱 소개")
    st.markdown("""
    본 애플리케이션은 **고객 데이터를 기반으로 연령대, 지역, 차량 선호도를 분석**하여 **맞춤형 마케팅 전략**을 도출하는 데이터 대시보드입니다.  
    이를 통해 **비즈니스 인사이트를 확보하고 차량 판매 전략을 최적화**할 수 있습니다.
    """)

    # 🔥 주요 기능
    st.markdown("### 🔥 주요 기능")
    st.markdown("""
    - **연령대별 고객 분석**: 특정 연령층의 차량 구매 패턴 및 선호도 분석
    - **지역별 고객 분포 분석**: 수도권과 지방 고객의 차이 분석 및 맞춤형 전략 제공
    - **차량 유형별 선호도 분석**: 전기차, SUV, 세단 등 고객 선호도 변화 확인
    - **맞춤형 마케팅 인사이트 제공**: 데이터 기반의 효과적인 마케팅 전략 도출
    """)

    # 🛠️ 사용 기술
    st.markdown("### 🛠️ 사용 기술")
    st.markdown("""
    - **Python** (Streamlit, Pandas, Matplotlib, Seaborn)
    - **데이터 분석** (Pandas, NumPy)
    - **시각화** (Matplotlib, Seaborn)
    - **웹 배포** (Streamlit Cloud)
    """)

    # 📊 데이터 분석 내용
    st.markdown("### 📊 데이터 분석 내용")
    st.markdown("""
    - **연령대별 분석**: 30~40대 고객이 가장 많은 비중을 차지하며, 가족 단위 차량 교체 수요 증가
    - **지역별 분석**: 서울·경기 지역에 고객이 집중되며, 수도권 중심의 마케팅 필요
    - **차량 유형별 분석**: SUV와 중형 차량 선호도가 높으며, 전기차 구매율이 증가하는 추세
    """)

    # 📌 참고 자료
    st.markdown("### 📌 참고 자료")
    st.markdown("""
    - KATECH Insight  
    - 국토교통부 자동차 등록 통계  
    - 현대자동차·기아 연구 보고서
    """)

if __name__ == "__main__":
    show_app_info()
