import streamlit as st
import pandas as pd
import time

# 고객 데이터 불러오기
df = pd.read_csv("data/고객db_전처리.csv")

# 🚗 일반 고객 대상 재구매 할인 혜택
st.title("🚗 일반 고객 대상 재구매 할인 혜택 제공")
st.write("재구매를 고려하는 고객을 위한 특별 할인 혜택을 제공합니다! 🎁")
st.markdown("---")

# ✅ 일반 고객 선정 기준
st.subheader("✅ 일반 고객 선정 기준")
st.markdown("""
- **구매 이력:** 단 **1회 구매 기록 보유**
- **최근 구매일:** **최근 6개월 이내 구매 기록 없음**
""")

st.markdown("---")

# 📋 일반 고객 리스트
st.subheader("📋 일반 고객 리스트")
normal_client = df.loc[df["고객 등급"] == "일반", ["이름", "휴대폰 번호", "이메일"]]
normal_client.reset_index(drop=True, inplace=True)
st.dataframe(normal_client)

st.markdown("---")

# 💰 일반 고객의 누적 구매 금액 입력
purchase_amount = st.number_input("🔢 누적 구매 금액 입력 (단위: 만 원)", min_value=0, step=100, value=3000)

# 🎯 할인 혜택 상세 안내 (누적 구매 금액에 따라 차등 제공)
if purchase_amount >= 10000:
    discount = "500만원 할인 + 5% 캐시백"
    perks = "💎 프리미엄 시승 체험 (최대 7일) + VIP 초청 행사 + 한정판 굿즈 제공"
elif purchase_amount >= 7000:
    discount = "400만원 할인 + 3% 캐시백"
    perks = "🏆 럭셔리 차량 시승 체험 (최대 5일) + 정비 패키지 업그레이드"
elif purchase_amount >= 5000:
    discount = "300만원 할인 + 2% 캐시백"
    perks = "🚘 고급 차량 시승 체험 (최대 3일) + 엔진오일 교환 1년 무상 제공"
elif purchase_amount >= 3000:
    discount = "200만원 할인 + 포인트 적립 (구매 금액의 5%)"
    perks = "🔧 무상 차량 점검 쿠폰 + 차량 보호 패키지 제공"
else:
    discount = "100만원 할인"
    perks = "🚗 기본 차량 점검 및 세차 쿠폰 제공"

st.subheader("🎯 재구매 할인 혜택 안내")
st.markdown(f"""
- **할인 혜택:** {discount}
- **할인 기간:** 2025년 4월 1일 ~ 2025년 12월 31일
- **추가 혜택:** {perks}
""")

st.markdown("---")

# ✅ 일반 고객을 위한 추가 프로모션 상세 설명
st.subheader("🎟️ 일반 고객을 위한 추가 프로모션")

st.markdown("""
2️⃣ **🚘 프리미엄 차량 시승 프로그램**
   - 고객이 관심 있는 **고급 차량을 최대 7일간 무료로 시승**할 수 있는 기회 제공
   - **페라리, 벤틀리, BMW M 시리즈 등 프리미엄 차량 포함**
   - 시승 후 **구매 결정 시 추가 할인 제공 (최대 5% 추가 할인)**
   - **트랙 주행 체험권 & 드라이빙 클래스 초청** 포함

3️⃣ **🎤 일반 고객 전용 VIP 초청 행사**
   - **VIP 네트워킹 런치 초청**: 미슐랭 레스토랑에서 브랜드 대표 및 자동차 전문가와의 만남
   - **신차 발표 & 럭셔리 시승 이벤트 초대**: 새로운 모델을 누구보다 빠르게 체험할 기회
   - **자동차 전문가 & 유명 레이서와 함께하는 토크쇼**: 자동차 트렌드와 기술에 대한 심층 강의

4️⃣ **🔧 서비스 패키지 업그레이드**
   - 일반 고객에게 **기본 차량 정비 패키지를 프리미엄 정비 패키지로 무료 업그레이드**
   - **🚗 무료 차량 픽업 & 정비 후 딜리버리 서비스 제공**
   - **1년간 엔진 오일 무상 교체 & 브레이크 패드 할인 제공**

5️⃣ **🎁 한정판 굿즈 & 컬렉터블 아이템 제공**
   - 재구매 고객에게 **한정판 브랜드 키체인, 머그컵, 미니카 제공**
   - 한정판 브랜드 의류(재킷, 모자 등) 선물
   - **럭셔리 차량 브랜드와의 콜라보 굿즈 증정 (예: 포르쉐 x 테크아트 키링)**
""")

st.markdown("---")

# 📩 할인 혜택 안내 메시지 발송
st.subheader("📩 할인 혜택 안내 메시지")
st.write("일반 고객에게 이메일과 문자 메시지로 할인 혜택을 안내합니다.")
col1, col2, _ = st.columns([1, 1, 8])
with col1:
    email_sent = st.button("📧 이메일 발송")
with col2:
    sms_sent = st.button("📩 문자 발송")

if email_sent:
    st.info("각 고객에게 할인 혜택 안내 이메일을 전송 중입니다. 잠시만 기다려주세요.")
    
    progress_bar = st.progress(0)
    for percent in range(1, 101):
        time.sleep(0.01)  # 실제 전송 과정에서는 API 호출 등이 이루어질 수 있음
        progress_bar.progress(percent)
    
    st.success("✅ 모든 고객에게 할인 혜택 안내 이메일을 성공적으로 전송하였습니다.")
if sms_sent:
    st.info("각 고객에게 할인 혜택 안내 문자를 전송 중입니다. 잠시만 기다려주세요.")
    
    progress_bar = st.progress(0)
    for percent in range(1, 101):
        time.sleep(0.01)  # 실제 전송 과정에서는 API 호출 등이 이루어질 수 있음
        progress_bar.progress(percent)
    
    st.success("✅ 모든 고객에게 할인 혜택 안내 문자를 성공적으로 전송하였습니다.")

st.markdown("---")

# 📌 할인 혜택 안내 예시 (이메일 및 문자)
st.subheader("📌 할인 혜택 안내 예시")
col1, col2, _ = st.columns([3, 6, 1])
with col1:
    st.image("images/email_sample.png", caption="📧 할인 안내 이메일 예시")
with col2:
    st.image("images/sms_sample.png", caption="📩 할인 안내 문자 예시")

st.markdown("---")
st.markdown("##### 🚀 일반 고객을 위한 특별한 혜택을 제공해드립니다!")