import streamlit as st

st.title("🚗 현대자동차 가격 할인 및 금융 혜택 프로모션")

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📌 할인 혜택", "📊 견적 계산기", "💰 월 납입금 계산기"])

# 외부 이미지 URL 사용
image_url = "https://www.genesis.com/content/dam/genesis-p2/kr/assets/models/g80/25my/exterior/genesis-kr-g80-fl-exterior-standard-side-profile-large.png"
st.image(image_url, caption="현대자동차 G80 (RG3) 프로모션")

st.markdown("""
### ✅ 개별소비세 인하 적용 (3.5%)  
- G80 (RG3) 개별소비세 5% → **3.5% 인하 적용**  
- 최종 소비자 가격: **82,750,000원** (개소세 적용)  

### ✅ 특별 현금 할인  
- 신학기 특별 할인 적용 (2월~3월 한정)  
- 최대 **300만 원 추가 할인 제공**  

### ✅ 무이자 할부 및 금융 혜택  
- **최대 60개월 특별 금리 적용 (최저 1.9%)**  
- **12개월 / 24개월 무이자 할부 가능**  
""")

with tab1:
    st.header("✅ 개별소비세 인하 및 특별 할인")
    st.markdown("""
    - **개별소비세 인하:** 3.5% 할인 적용  
    - **신학기 특별 할인:** 최대 300만 원 추가 할인  
    - **무이자 할부 / 저금리 할부 제공**  
    """)

with tab2:
    st.header("📊 프로모션 견적 계산기")
    car_price = st.number_input("📌 차량 가격 입력 (원)", value=82750000, step=1000000)
    tax_discount = st.slider("📌 개별소비세 인하율 (%)", 0, 5, 3)
    discount_amount = car_price * (tax_discount / 100)
    final_price = car_price - discount_amount
    additional_discount = st.slider("📌 추가 할인율 (%)", 0, 10, 5)
    final_price -= final_price * (additional_discount / 100)
    st.write(f"🚗 개별소비세 인하 후 가격: **{final_price:,.0f} 원**")

with tab3:
    st.header("💰 월 납입금 계산기")
    down_payment_ratio = st.slider("📌 선수금 비율 (%)", 0, 50, 30)
    down_payment = final_price * (down_payment_ratio / 100)
    loan_amount = final_price - down_payment
    installment_months = st.slider("📌 할부 기간 (개월)", 12, 60, 36)
    interest_rate = st.radio("📌 할부 금리 선택", ["무이자 (0%)", "저금리 (1.9%)", "저금리 (2.5%)"])
    interest = 0 if interest_rate == "무이자 (0%)" else (1.9 if interest_rate == "저금리 (1.9%)" else 2.5)
    monthly_payment = (loan_amount * (1 + (interest / 100) * (installment_months / 12))) / installment_months
    st.write(f"💵 예상 월 납입금: **{monthly_payment:,.0f} 원**")
