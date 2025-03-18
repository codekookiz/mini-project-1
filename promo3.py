import streamlit as st

st.title("다자녀 가구 특별 프로모션")

# 탭 구성
tab1, tab2, tab3, tab4 = st.tabs(["프로모션 설명", "무이자 할부 계산기", "추가 혜택 계산기", "상담 예약"])

# 탭1: 프로모션 설명
with tab1:
    st.subheader("다자녀 가구 특별 프로모션 안내")

    st.markdown("""
    ### 대상
    - 미취학 아동 3명 이상을 둔 가구
    - 대상 차량: 펠리세이드, 스타리아 등 대형 패밀리 SUV 및 미니밴

    ### 주요 혜택
    **1. 무이자 할부 혜택**  
    - 2월, 3월, 6월, 12월 총 4회의 무이자 할부 적용  
    - 할부 기간: 12개월, 24개월, 36개월, 48개월, 60개월 중 선택 가능  
      
    **2. 자녀 안전 지원**  
    - 신차 구매 시 프리미엄 카시트 1개 무료 제공  
    - 추가 카시트 구매 시 할인 제공 (최대 20%)  

    **3. 추가 옵션 혜택**  
    - 차량 구매 시 뒷좌석 모니터 옵션 30% 할인 제공  

    ### 추가 혜택
    - 현대자동차 고객 서비스센터에서 가족 전용 정기점검 서비스 1년 무료 제공  
    - 다자녀 고객 전용 전시장 상담 예약 우선 배정  
    """)

    st.image("https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2024/10/31/event-hmc-ev-zero-burden-promotion-2411-list-thumb-352x233.jpg",
             caption="다자녀 가구 특별 프로모션")

# 탭2: 무이자 할부 계산기
with tab2:
    st.subheader("무이자 할부 계산기")

    # 차량 가격 입력
    car_price = st.number_input("차량 가격 입력 (원)", value=55000000, step=1000000)

    # 할부 기간 선택
    installment_months = st.selectbox("할부 기간 선택 (개월)", [12, 24, 36, 48, 60])

    # 무이자 할부 적용 계산
    monthly_payment = car_price / installment_months

    # 결과 출력
    st.write(f"총 차량 가격: {car_price:,.0f} 원")
    st.write(f"선택한 할부 기간: {installment_months} 개월")
    st.write(f"예상 월 납입금 (무이자 할부 적용): {monthly_payment:,.0f} 원")

# 탭3: 추가 혜택 계산기 (뒷좌석 모니터 할인)
with tab3:
    st.subheader("추가 혜택 계산기")

    # 기본 가격
    monitor_price = 1500000  # 뒷좌석 모니터 옵션 가격

    # 할인 적용 (30% 할인)
    monitor_discount = monitor_price * 0.3  
    final_monitor_price = monitor_price - monitor_discount

    # 결과 출력
    st.write(f"뒷좌석 모니터 옵션 할인 적용 후 가격: {final_monitor_price:,.0f} 원")

# 탭4: 상담 예약 신청
with tab4:
    st.subheader("상담 예약 신청")

    name = st.text_input("이름 입력")
    phone = st.text_input("연락처 입력")
    preferred_date = st.date_input("상담 희망 날짜 선택")
    preferred_time = st.time_input("상담 희망 시간 선택")

    if st.button("상담 신청하기"):
        if name and phone:
            st.success(f"{name}님, {preferred_date} {preferred_time}에 상담 예약이 접수되었습니다.")
        else:
            st.warning("이름과 연락처를 입력해주세요.")
