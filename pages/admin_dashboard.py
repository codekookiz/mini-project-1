import streamlit as st

st.set_page_config(page_title="현대자동차 관리자 페이지", layout="wide")

st.title("현대자동차 관리자 페이지")

# 차량 목록 및 가격 데이터 (풀옵션 가격 적용)
car_prices = {
    "Avante (CN7 N)": 41430000,
    "Avante (CN7 HEV)": 33940000,
    "Grandeur (GN7 HEV)": 59820000,
    "G80 (RG3)": 90060000,
    "Santa-Fe ™": 54700000,
    "Santa-Fe (MX5 PHEV)": 56300000,
    "Tucson (NX4 PHEV)": 44850000,
    "Palisade (LX2)": 63770000,
    "IONIQ (AE EV)": 79410000,
    "IONIQ 6 (CE)": 50600000,
    "NEXO (FE)": 72240000,
    "G90 (HI)": 142870000,
    "G70 (IK)": 51130000,
    "i30 (PD)": 28500000,
    "GV80 (RS4)": 104600000,
    "G90 (RS4)": 183270000
}

# 지역별 전기차 보조금 데이터
ev_subsidies = {
    "서울특별시": 9000000,
    "부산광역시": 10500000,
    "대구광역시": 11000000,
    "인천광역시": 10600000,
    "광주광역시": 11000000,
    "대전광역시": 12000000,
    "울산광역시": 10500000,
    "경기도 수원시": 10500000,
    "경기도 성남시": 11000000,
    "충청북도 청주시": 14000000,
    "충청남도 천안시": 14000000,
    "전라북도 전주시": 15000000,
    "전라남도 목포시": 15500000,
    "경상북도 포항시": 13000000,
    "경상남도 창원시": 13000000
}

# 재구매 할인 데이터
rebuy_discounts = {
    "G80 (RG3)": 2000000,
    "GV80 (RS4)": 3000000,
    "Palisade (LX2)": 1500000,
    "스타리아": 1500000
}

tab1, tab2, tab3, tab4 = st.tabs(["프로모션 조회", "할부 계산 및 혜택 비교", "PDF 다운로드", "고객 화면 전송"])

# 1️⃣ 프로모션 조회 (탭 1)
with tab1:
    st.subheader("현재 진행 중인 프로모션")

    col1, col2 = st.columns(2)

    with col1:
        customer_name = st.text_input("고객 이름")
        selected_model = st.selectbox("차량 모델 선택", list(car_prices.keys()))
        customer_type = st.radio("구분 선택", ["개인", "법인"])
        region = st.selectbox("거주 지역 선택", list(ev_subsidies.keys()))
        is_rebuy = st.checkbox("재구매 고객 여부")
        has_children = st.checkbox("다자녀 혜택 적용 (미취학 아동 3명 이상)")

    with col2:
        st.subheader("혜택 상세")
        
        # 다자녀 혜택
        if has_children:
            st.write("- **다자녀 가구 혜택 적용:** 무이자 할부 제공, 카시트 증정")
        
        # 전기차 보조금 확인
        if "IONIQ" in selected_model or "NEXO" in selected_model:
            ev_subsidy = ev_subsidies.get(region, 0)
            st.write(f"- **전기차 보조금:** 최대 {ev_subsidy:,.0f} 원")

        # 재구매 할인 확인
        if is_rebuy:
            discount = rebuy_discounts.get(selected_model, 0)
            if discount > 0:
                st.write(f"- **재구매 할인:** {discount:,.0f} 원 적용")
            else:
                st.write("- **재구매 할인:** 해당 차종은 추가 할인이 없습니다.")

# 2️⃣ 할부 계산기 & 혜택 비교 (탭 2)
with tab2:
    st.subheader("할부 계산 및 혜택 비교")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**할부 조건 1**")
        car1 = st.selectbox("차량 선택 1", list(car_prices.keys()), key="car1")
        price1 = car_prices[car1]  # 선택 시 자동 입력
        discount1 = rebuy_discounts.get(car1, 0)
        total_price1 = price1 - discount1  # 재구매 할인 적용
        st.write(f"**차량 가격:** {total_price1:,.0f} 원")

        down_payment1 = st.slider("선수금 비율 (%)", 0, 50, 30, key="down1")
        months1 = st.selectbox("할부 기간 (개월)", [12, 24, 36, 48, 60], key="months1")
        rate1 = st.selectbox("할부 금리 (%)", [0, 1.9, 2.5, 3.9], key="rate1")

        monthly1 = (total_price1 * (1 - down_payment1 / 100)) * (1 + (rate1 / 100) * (months1 / 12)) / months1
        st.write(f"**예상 월 납입금:** {monthly1:,.0f} 원")

    with col2:
        st.write("**할부 조건 2**")
        car2 = st.selectbox("차량 선택 2", list(car_prices.keys()), key="car2")
        price2 = car_prices[car2]  # 선택 시 자동 입력
        discount2 = rebuy_discounts.get(car2, 0)
        total_price2 = price2 - discount2  # 재구매 할인 적용
        st.write(f"**차량 가격:** {total_price2:,.0f} 원")

        down_payment2 = st.slider("선수금 비율 (%)", 0, 50, 30, key="down2")
        months2 = st.selectbox("할부 기간 (개월)", [12, 24, 36, 48, 60], key="months2")
        rate2 = st.selectbox("할부 금리 (%)", [0, 1.9, 2.5, 3.9], key="rate2")

        monthly2 = (total_price2 * (1 - down_payment2 / 100)) * (1 + (rate2 / 100) * (months2 / 12)) / months2
        st.write(f"**예상 월 납입금:** {monthly2:,.0f} 원")

# 3️⃣ PDF 다운로드 (탭 3)
with tab3:
    st.subheader("고객 혜택 PDF 다운로드")
    if st.button("PDF 생성 및 다운로드"):
        st.success("PDF가 생성되었습니다. 다운로드 링크가 제공됩니다.")

# 4️⃣ 고객 화면 전송 (탭 4)
with tab4:
    st.subheader("고객 화면 전송")

    st.write("직원이 조회한 혜택을 고객이 직접 확인할 수 있도록 새 창에서 보여줍니다.")

    link_url = "/customer_view.py"
    html_code = f'<a href="{link_url}" target="_blank">고객 화면 열기</a>'
    st.markdown(html_code, unsafe_allow_html=True)
