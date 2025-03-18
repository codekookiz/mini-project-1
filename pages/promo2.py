import streamlit as st

st.title("장기렌터카 및 리스 프로모션")

# 탭 구성
tab1, tab2, tab3, tab4 = st.tabs(["프로모션 설명", "렌터카 vs 리스 비교", "월 납입금 계산기", "상담 신청 및 추가 혜택"])

# 탭1: 프로모션 설명
with tab1:
    st.subheader("장기렌터카 & 리스 프로모션 안내")

    st.markdown("""
    ### 개요
    장기렌터카와 리스를 이용하면 초기 부담을 줄이고, 세제 혜택을 받을 수 있습니다.
    현대자동차는 고객에게 유리한 조건으로 다양한 혜택을 제공합니다.

    ### 주요 혜택
    **1. 보증 연장 서비스 제공**  
    - 차량 핵심 부품 보장 (5년/16만 km)

    **2. 보험료 할인 및 세제 혜택**  
    - 장기렌터카: 보험료 포함, 취득세·등록세 부담 없음  
    - 리스: 법인 및 사업자 세제 혜택 가능  

    **3. 상위 차종 변경 혜택**  
    - 리스 유지 후 상위 차종 변경 시 계약 해지 수수료 30% 감면  
    - 1년 이상 유지 후 변경 시 수수료 면제  

    **4. 법인 및 사업자 대상 특별 혜택**  
    - 월 납입 비용 비용 처리 가능  
    """)

    st.image("https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2024/10/31/event-hmc-ev-zero-burden-promotion-2411-list-thumb-352x233.jpg",
             caption="현대자동차 장기렌터카 및 리스 프로모션")

# 탭2: 장기렌터카 vs 리스 비교
with tab2:
    st.subheader("장기렌터카 vs 리스 비교")

    data = {
        "구분": ["소유권", "세금 (취득세, 등록세)", "보험료", "월 납입 방식", "잔존가치", "법인 비용 처리"],
        "장기렌터카": ["렌터카 회사 소유", "없음 (렌터카 포함)", "포함 (고객 부담 없음)", "렌탈료 납부", "없음", "가능"],
        "리스": ["리스사 소유 (일부 인수 가능)", "일부 있음", "고객 부담", "리스료 납부", "있음 (계약 종료 후 인수 가능)", "가능 (운용리스 시)"]
    }

    st.table(data)

    st.markdown("""
    ### 장기렌터카 특징  
    - 차량 유지 및 보험 부담을 줄이고 월 납입금만 지불  
    - 계약 종료 후 차량 반납, 잔존가치 부담 없음  
    - 초기 비용 없이 차량 이용 가능  

    ### 리스 특징  
    - 개인·법인 명의로 차량 소유 가능 (운용 리스)  
    - 계약 종료 후 차량 인수 가능 (잔존가치 지불 후)  
    - 사업자의 경우 비용 처리 가능 (리스료 전액 경비 처리)  
    """)

# 탭3: 렌터카 & 리스 월 납입금 계산기
with tab3:
    st.subheader("월 납입금 계산기")

    car_price = st.number_input("차량 가격 입력 (원)", value=55000000, step=1000000)

    rental_type = st.radio("이용 유형 선택", ["장기렌터카", "리스"])

    down_payment_ratio = st.slider("선수금 비율 (%)", 0, 50, 30)
    down_payment = car_price * (down_payment_ratio / 100)
    loan_amount = car_price - down_payment

    contract_months = st.slider("계약 기간 (개월)", 12, 60, 36)

    interest_rate = 0
    if rental_type == "리스":
        interest_rate = st.slider("리스 이자율 (%)", 0.0, 5.0, 2.5, step=0.1)

    if rental_type == "리스":
        monthly_payment = (loan_amount * (1 + (interest_rate / 100) * (contract_months / 12))) / contract_months
    else:
        monthly_payment = loan_amount / contract_months

    st.write("### 예상 월 납입금")
    st.write(f"선수금: {down_payment:,.0f} 원")
    st.write(f"계약 기간: {contract_months} 개월")
    st.write(f"적용 금리: {interest_rate}% (리스일 경우 적용)")
    st.write(f"예상 월 납입금: {monthly_payment:,.0f} 원")

# 탭4: 상담 신청 및 추가 혜택
with tab4:
    st.subheader("상담 신청 및 추가 혜택")

    st.markdown("""
    ### 추가 프로모션 혜택
    - 리스 유지 후 상위 차종 변경 시 계약 해지 수수료 30% 감면  
    - 1년 이상 유지 후 차종 변경 시 수수료 면제  
    - 법인 고객 대상 추가 할인 제공  
    """)

    name = st.text_input("이름 입력")
    phone = st.text_input("연락처 입력")
    preferred_date = st.date_input("상담 희망 날짜 선택")
    preferred_time = st.time_input("상담 희망 시간 선택")

    if st.button("상담 신청하기"):
        if name and phone:
            st.success(f"{name}님, {preferred_date} {preferred_time}에 상담 예약이 접수되었습니다.")
        else:
            st.warning("이름과 연락처를 입력해주세요.")
