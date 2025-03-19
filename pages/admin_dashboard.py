import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="현대자동차 관리자 페이지", layout="wide")

# ✅ 파일 경로 확인 및 데이터 불러오기
file_path = "data/차량정보.csv"
df = pd.read_csv(file_path)

# ✅ 전기차 보조금 데이터
ev_subsidies = {
    "서울특별시": 9000000, "부산광역시": 10500000, "대구광역시": 11000000,
    "인천광역시": 10600000, "광주광역시": 11000000, "대전광역시": 12000000,
    "울산광역시": 10500000, "경기도 수원시": 10500000, "경기도 성남시": 11000000,
    "충청북도 청주시": 14000000, "충청남도 천안시": 14000000, "전라북도 전주시": 15000000,
    "전라남도 목포시": 15500000, "경상북도 포항시": 13000000, "경상남도 창원시": 13000000
}

# ✅ 다자녀 혜택 (적용 가능한 차량)
multi_child_cars = ["Palisade (LX2)", "Santa-Fe (MX5 PHEV)", "Tucson (NX4 PHEV)"]

# ✅ 재구매 할인 데이터
rebuy_discounts = {
    "G80 (RG3)": 2000000, "GV80 (RS4)": 3000000,
    "Palisade (LX2)": 1500000, "스타리아": 1500000
}

# ✅ 법인 혜택
corporate_benefits = """
✅ 부가세 환급 및 감가상각 적용 가능  
✅ 법인 차량 단체 보험료 할인 제공  
✅ 운용 리스를 통한 유지비 절감 및 관리 편의성 제공  
"""

# ✅ UI 구성
st.title("현대자동차 관리자 페이지")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["프로모션 조회", "할부 계산 및 혜택 비교", "PDF 다운로드", "고객 화면 전송"])

# ✅ 1️⃣ 프로모션 조회 (탭 1)
with tab1:
    subtab1, subtab2 = st.tabs(["개인 고객", "법인 고객"])

    with subtab1:
        col1, col2 = st.columns([1, 1.5])

        with col1:
            is_rebuy = st.checkbox(f"재구매 고객 여부 (해당 차량: {', '.join(rebuy_discounts.keys())})")
            has_children = st.checkbox(f"다자녀 혜택 적용 (해당 차량: {', '.join(multi_child_cars)})")
            ev_promo = st.checkbox(f"전기차 프로모션 적용 (해당 차량: {', '.join(df[df['연료 구분'].isin(['전기', '플러그인 하이브리드', '수소'])]['최근 구매 제품'].unique())})")

            customer_name = st.text_input("고객 이름")

            # ✅ 차량 선택 리스트 필터링
            filtered_cars = df["최근 구매 제품"].unique()  # 기본값: 모든 차량
            if has_children:
                filtered_cars = [car for car in multi_child_cars if car in filtered_cars]  # 다자녀 혜택 가능 차량
            if is_rebuy:
                filtered_cars = [car for car in rebuy_discounts.keys() if car in filtered_cars]  # 재구매 혜택 가능 차량
            if ev_promo:
                filtered_cars = df[df["연료 구분"].isin(["전기", "플러그인 하이브리드", "수소"])]["최근 구매 제품"].unique()

            # ✅ 차량 선택 (필터링된 리스트 기반)
            selected_model = st.selectbox("차량 모델 선택", filtered_cars)

            region = st.selectbox("거주 지역 선택", list(ev_subsidies.keys()))

        with col2:
            st.subheader("개인 고객 혜택 상세")

            # ✅ 선택한 차량 정보 가져오기
            selected_car_info = df[df["최근 구매 제품"] == selected_model].iloc[0]
            car_price = selected_car_info["최근 거래 금액"]
            fuel_type = selected_car_info["연료 구분"]
            car_image_url = selected_car_info["모델 사진"]  # 차량 이미지 URL 가져오기
            final_price = car_price  # 최종 가격 초기화

            # ✅ 다자녀 혜택 적용
            if has_children and selected_model in multi_child_cars:
                st.write("- **다자녀 가구 혜택 적용:** 무이자 할부 제공, 뒷좌석 모니터 30% 할인")
                final_price -= 1000000  # 감면 적용

            # ✅ 전기차 혜택 적용
            ev_subsidy = 0
            if fuel_type in ["전기", "플러그인 하이브리드", "수소"]:
                ev_subsidy = ev_subsidies.get(region, 0)
                st.write(f"- **전기차 보조금:** 최대 {ev_subsidy:,.0f} 원 적용")
                final_price -= ev_subsidy  # 보조금 적용

                # ✅ 전기차 추가 프로모션 (충전 크레딧 및 옵션 할인)
                st.write("- **충전기 무료 설치 또는 충전 크레딧 50만 원 지급**")
                st.write("- **전기차 보험료 할인 (최대 10%) 적용 가능**")
                st.write("- **현대차 금융 이용 시 추가 이자 할인 (최대 1.5%) 제공**")

            # ✅ 재구매 할인 적용
            discount = rebuy_discounts.get(selected_model, 0)
            if is_rebuy and discount > 0:
                st.write(f"- **재구매 할인:** {discount:,.0f} 원 적용")
                final_price -= discount

            # ✅ 차량 이미지 표시
            st.image(car_image_url, caption=f"{selected_model} 이미지", use_container_width=True)

            st.write(f"**최종 적용 가격:** {final_price:,.0f} 원")

    with subtab2:
        col3, col4 = st.columns([1, 1.5])

        with col3:
            st.write("법인 고객 관련 입력란")

        with col4:
            st.subheader("법인 고객 혜택")
            st.write(corporate_benefits)



st.markdown("---")
col1, col2, col3 = st.columns(3)

# ✅ 1️⃣ 다자녀 프로모션
with col1:
    st.subheader("👨‍👩‍👧‍👦 다자녀 혜택")
    if has_children and selected_model in multi_child_cars:
        st.markdown("✅ **다자녀 혜택 적용 가능**")
        st.markdown("- 무이자 할부 제공")
        st.markdown("- 뒷좌석 모니터 30% 할인")

        # ✅ 다자녀 추가 혜택 선택 (4가지 중 2가지 선택 가능)
        st.subheader("📌 추가 혜택 선택 (최대 2개)")
        options = [
            "프리미엄 카시트 1개 무료 증정",
            "차량용 공기청정기 제공",
            "뒷좌석 모니터 50% 할인",
            "가족 차량 정기 점검 1년 무료"
        ]
        selected_benefits = st.multiselect("추가 혜택 선택", options, max_selections=2)

        if selected_benefits:
            st.markdown("**선택한 추가 혜택:**")
            for benefit in selected_benefits:
                st.markdown(f"- {benefit}")
    else:
        st.markdown("❌ 다자녀 혜택 적용 대상이 아닙니다.")

# ✅ 2️⃣ 전기차 프로모션
with col2:
    st.subheader("⚡ 전기차 혜택")
    ev_subsidy = 0
    if fuel_type in ["전기", "플러그인 하이브리드", "수소"]:
        ev_subsidy = ev_subsidies.get(region, 0)
        st.markdown("✅ **전기차 보조금 적용 가능**")
        st.markdown(f"- 거주 지역 ({region}) 기준 최대 **{ev_subsidy:,.0f} 원** 지원")
        st.markdown("- 충전기 설치 지원 가능")
    else:
        st.markdown("❌ 전기차 혜택 대상이 아닙니다.")

# ✅ 3️⃣ 법인 프로모션
with col3:
    st.subheader("🏢 법인 차량 혜택")
    st.markdown("✅ **법인 고객을 위한 특별 혜택**")
    st.markdown("- 부가세 환급 및 감가상각 적용 가능")
    st.markdown("- 법인 차량 단체 보험료 할인 제공")
    st.markdown("- 운용 리스를 통한 유지비 절감 및 관리 편의성 제공")

st.markdown("---")

# ✅ 최종 할인 및 가격 정리
st.subheader("📌 최종 할인 및 가격 정리")
if has_children and selected_model in multi_child_cars:
    st.markdown(f"**다자녀 혜택 적용:** ✅")
if fuel_type in ["전기", "플러그인 하이브리드", "수소"]:
    st.markdown(f"**전기차 보조금:** {ev_subsidy:,.0f} 원 적용")
if is_rebuy and discount > 0:
    st.markdown(f"**재구매 할인:** {discount:,.0f} 원 적용")

st.markdown(f"### 🚘 최종 적용 가격: {final_price:,.0f} 원")