import streamlit as st
import pandas as pd

# 🚀 Streamlit 페이지 설정
st.set_page_config(page_title="VIP 고객 맞춤 프로모션", layout="wide")

# 🎨 스타일 적용
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #FFD700;
            text-align: center;
        }
        .subtitle {
            font-size: 24px;
            font-weight: bold;
            color: #FFA500;
        }
        .highlight {
            font-size: 20px;
            font-weight: bold;
            color: #008080;
        }
        .vip-section {
            background-color: #F5F5F5;
            padding: 15px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 🏆 VIP 고객 프로모션 타이틀
st.markdown('<p class="title">🚀 VIP 고객을 위한 맞춤형 프로모션</p>', unsafe_allow_html=True)
st.write("VIP 고객의 누적 구매 금액에 따라 맞춤형 할인 혜택을 제공합니다.")

# 📌 VIP 고객의 누적 구매 금액 입력
purchase_amount = st.number_input("💰 누적 구매 금액 입력 (단위: 만 원)", min_value=0, step=100, value=5000)

# 🎯 VIP 등급 결정
if purchase_amount >= 20000:
    grade = "🔥 RVIP (Royal VIP)"
    discount = 10
    extra_benefits = "VIP 전용 엠블럼 + 프리미엄 가죽 시트 + 전용 멤버십 + 초특급 맞춤 서비스 제공"
    st.success(f"✨ 당신은 **{grade}** 등급입니다! 최고의 혜택을 누릴 수 있습니다.")
elif purchase_amount >= 10000:
    grade = "💎 VVIP"
    discount = 7
    extra_benefits = "프리미엄 가죽 시트 업그레이드 + VIP 전용 엠블럼 제공 + 맞춤형 컨시어지 서비스"
    st.warning(f"🏆 당신은 **{grade}** 등급입니다! 특별한 혜택을 제공합니다.")
elif purchase_amount >= 5000:
    grade = "⭐ VIP"
    discount = 5
    extra_benefits = "VIP 전용 엠블럼 제공 + 프리미엄 서비스 우선 예약권"
    st.info(f"🌟 당신은 **{grade}** 등급입니다! 혜택을 확인해보세요.")
else:
    grade = "🚗 일반 고객"
    discount = 0
    extra_benefits = "추가 혜택 없음"
    st.error(f"🚨 현재 등급: **{grade}** (VIP 혜택을 받으려면 누적 구매 금액을 늘려보세요!)")

# 📌 VIP 프로모션 적용 결과
st.markdown("---")
st.subheader("📌 VIP 고객 맞춤 프로모션 적용 결과")
st.write(f"💰 **누적 구매 금액:** {purchase_amount:,}만 원")
st.write(f"🏆 **고객 등급:** {grade}")
st.write(f"🎁 **적용 할인율:** {discount}%")
st.write(f"🎉 **추가 제공 혜택:** {extra_benefits}")

# 📉 할인 적용 후 예상 결제 금액 계산
if discount > 0:
    final_price = purchase_amount * (1 - discount / 100)
    st.write(f"💳 **할인 적용 후 예상 결제 금액:** {final_price:,.0f}만 원")
else:
    st.write("❌ 할인이 적용되지 않습니다.")

st.markdown("---")
st.write("🚀 **VIP 고객만을 위한 특별한 혜택을 제공합니다! 😊**")

# 🎯 VIP 프로모션 옵션 선택
promotion = st.radio("🎈 원하는 VIP 프로모션을 선택하세요.", 
                     ["VIP 전용 ‘프라이빗 차량 체험 패키지’", 
                      "VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’",
                      "‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’",
                      "VIP ‘커넥티드 라이프스타일 멤버십’"])

# 🚗 1️⃣ VIP 전용 ‘프라이빗 차량 체험 패키지’
if promotion == "VIP 전용 ‘프라이빗 차량 체험 패키지’":
    st.subheader("🚗 VIP 전용 ‘프라이빗 차량 체험 패키지’")
    st.write("""
    ✅ **VIP 고객 전용 ‘프라이빗 테스트 드라이브’ 제공**
    - 특정 하이엔드 모델(제네시스, BMW, 벤츠, 포르쉐 등) 대상으로 진행  
    - VIP 고객이 관심 있는 차량을 **7일간 무료 체험 후 구매 결정 가능**  
    - 체험 후 구매할 경우 **최대 5% 추가 할인 혜택 제공**  
    """)

# 🚗 2️⃣ VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’
elif promotion == "VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’":
    st.subheader("🏠 VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’")
    st.write("""
    ✅ **VIP 고객 전용 차량 보관 & 즉시 출고 서비스**
    - VIP 고객이 **자주 사용하는 차량을 사전 예약 후 차고지에 보관**  
    - 필요할 때 **즉시 차량을 출고할 수 있도록 대기 상태 유지**  
    ✅ **장기 보관 후 구매 시 추가 혜택**
    - VIP 고객이 장기 보관 후 차량을 구매할 경우 **보관료 20 ~ 40% 차감 혜택 제공**  
    - 차량 보관료 : 고급차 (Luxury/스포츠카) 80만 ~ 150만원, 슈퍼카 (Supercar) 150만 ~ 300만원  
    """)

# 💎 3️⃣ ‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’
elif promotion == "‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’":
    st.subheader("💎 ‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’")
    st.write("""
    ✅ **VIP 고객 초청 ‘프라이빗 브랜드 이벤트’**
    - 고급 레스토랑에서 진행하는 **VIP 초청 시승회 & 네트워킹 디너**  
    - 유명 레이서와 함께하는 **서킷 체험 이벤트** 진행  
    """)

# 🏎 4️⃣ VIP ‘커넥티드 라이프스타일 멤버십’
elif promotion == "VIP ‘커넥티드 라이프스타일 멤버십’":
    st.subheader("🏎 VIP ‘커넥티드 라이프스타일 멤버십’")
    st.write("""
    ✅ **VIP 전용 컨시어지 서비스 운영**
    - 차량 정비, 세차, 보험, 유지보수를 전담하는 **프리미엄 컨시어지 서비스** 제공  
    ✅ **VIP 고객 전용 글로벌 렌터카 & 모빌리티 서비스 연계**
    - 해외 출장 시, VIP 고객에게 **프리미엄 렌터카 서비스 무료 제공**  
    """)

st.markdown("---")
st.markdown('<p class="title">🚀 **VIP 고객만을 위한 차별화된 프리미엄 혜택을 제공합니다!**</p>', unsafe_allow_html=True)
