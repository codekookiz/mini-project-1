import streamlit as st
import pandas as pd


# 🎯 VIP 고객을 위한 프로모션 타이틀
st.title("🚀 VIP 고객 맞춤 프로모션 & 프라이빗 스케줄")
st.write("VIP 고객을 대상으로 맞춤형 할인 혜택과 프라이빗 이벤트를 제공합니다.")

# 🎯 VIP 고객의 누적 구매 금액 입력
purchase_amount = st.number_input("🔢 누적 구매 금액 입력 (단위: 만 원)", min_value=0, step=100, value=5000)

# 🎯 VIP 등급 결정
if purchase_amount >= 20000:
    grade = "🏆 RVIP (Royal VIP)"
    discount = 10
    extra_benefits = "✨ VIP 전용 엠블럼 + 프리미엄 가죽 시트 + 전용 멤버십 + 초특급 맞춤 서비스 제공"
elif purchase_amount >= 10000:
    grade = "🥇 VVIP"
    discount = 7
    extra_benefits = "💎 프리미엄 가죽 시트 업그레이드 + VIP 전용 엠블럼 제공 + 맞춤형 컨시어지 서비스"
elif purchase_amount >= 5000:
    grade = "🥈 VIP"
    discount = 5
    extra_benefits = "🎖️ VIP 전용 엠블럼 제공 + 프리미엄 서비스 우선 예약권"
else:
    grade = "💼 일반 고객"
    discount = 0
    extra_benefits = "❌ 추가 혜택 없음"

# 🎯 프로모션 적용 결과 출력
st.markdown("---")
st.subheader("📌 VIP 고객 맞춤 프로모션 적용 결과")
st.write(f"**누적 구매 금액:** {purchase_amount:,}만 원")
st.write(f"**고객 등급:** {grade}")
st.write(f"**적용 할인율:** {discount}%")
st.write(f"**추가 제공 혜택:** {extra_benefits}")

# 🎯 할인 적용 후 예상 결제 금액 계산
if discount > 0:
    final_price = purchase_amount * (1 - discount / 100)
    st.write(f"**💰 할인 적용 후 예상 결제 금액:** {final_price:,.0f}만 원")
else:
    st.write("❌ 할인이 적용되지 않습니다.")

st.markdown("---")
st.write("🎉 **VIP 고객만을 위한 특별한 혜택을 제공합니다!** 😊")

# 🎯 VIP 프로모션 옵션 선택
promotion = st.radio("🏆 원하는 VIP 프로모션을 선택하세요.", 
                     ["🚗 VIP 전용 ‘프라이빗 차량 체험 패키지’", 
                      "🏠 VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’",
                      "🎭 ‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’",
                      "🌎 VIP ‘커넥티드 라이프스타일 멤버십’"])

# 🚗 1️⃣ VIP 전용 ‘프라이빗 차량 체험 패키지’
if promotion == "🚗 VIP 전용 ‘프라이빗 차량 체험 패키지’":
    st.subheader("🚗 VIP 전용 ‘프라이빗 차량 체험 패키지’")
    st.write("""
    ✅ **VIP 고객 전용 ‘프라이빗 테스트 드라이브’ 제공**
    - 특정 하이엔드 모델(제네시스, BMW, 벤츠, 포르쉐 등) 대상으로 진행  
    - VIP 고객이 관심 있는 차량을 **7일간 무료 체험 후 구매 결정 가능**  
    - 체험 후 구매할 경우 **최대 5% 추가 할인 혜택 제공**  
    """)

# 🏠 2️⃣ VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’
elif promotion == "🏠 VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’":
    st.subheader("🏠 VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’")
    st.write("""
    ✅ **VIP 고객 전용 차량 보관 & 즉시 출고 서비스**
    - VIP 고객이 **자주 사용하는 차량을 사전 예약 후 차고지에 보관**  
    - 필요할 때 **즉시 차량을 출고할 수 있도록 대기 상태 유지**  
    ✅ **장기 보관 후 구매 시 추가 혜택**
    - VIP 고객이 장기 보관 후 차량을 구매할 경우 **보관료 20 ~ 40% 차감 혜택 제공**  
    - 차량 보관료 : 고급차 (Luxury/스포츠카) 80만 ~ 150만원, 슈퍼카 (Supercar) 150만 ~ 300만원  
    """)

# 🎭 3️⃣ ‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’
elif promotion == "🎭 ‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’":
    st.subheader("🎭 ‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’")
    st.write("""
    ✅ **VIP 고객 초청 ‘프라이빗 브랜드 이벤트’**
    - 고급 레스토랑에서 진행하는 **VIP 초청 시승회 & 네트워킹 디너**  
    - 유명 레이서와 함께하는 **서킷 체험 이벤트** 진행  
    """)

# 🌎 4️⃣ VIP ‘커넥티드 라이프스타일 멤버십’
elif promotion == "🌎 VIP ‘커넥티드 라이프스타일 멤버십’":
    st.subheader("🌎 VIP ‘커넥티드 라이프스타일 멤버십’")
    st.write("""
    ✅ **VIP 전용 컨시어지 서비스 운영**
    - 차량 정비, 세차, 보험, 유지보수를 전담하는 **프리미엄 컨시어지 서비스** 제공  
    ✅ **VIP 고객 전용 글로벌 렌터카 & 모빌리티 서비스 연계**
    - 해외 출장 시, VIP 고객에게 **프리미엄 렌터카 서비스 무료 제공**  
    """)

import streamlit as st
import pandas as pd
import calendar
from datetime import datetime, timedelta




# 🎯 진행 중인 VIP 이벤트 데이터 (최대 6개월 일정 제공)
today = datetime.today()
vip_event_data = pd.DataFrame({
    "이벤트 제목": [
        "🏎️ 프라이빗 럭셔리 드라이브 체험", "🏌️‍♂️ VIP 초청 골프 라운딩", "🛥️ VVIP 요트 디너", 
        "🍽️ 로얄 패밀리 런치", "🚗 프라이빗 시승 & 맞춤 상담", "🚖 VIP 리무진 픽업 서비스"
    ],
    "일정": [
        (today + timedelta(days=10)).strftime("%Y-%m-%d"), 
        (today + timedelta(days=20)).strftime("%Y-%m-%d"), 
        (today + timedelta(days=35)).strftime("%Y-%m-%d"), 
        (today + timedelta(days=50)).strftime("%Y-%m-%d"), 
        (today + timedelta(days=75)).strftime("%Y-%m-%d"), 
        (today + timedelta(days=90)).strftime("%Y-%m-%d")
    ],
    "장소": [
        "한강 프라이빗 드라이브 코스", "제주 최고급 골프장", "부산 요트 클럽", 
        "서울 프라이빗 레스토랑", "전국 주요 대리점", "VIP 고객 지정 장소"
    ],
    "참여 가능 등급": [
        "모든 VIP", "VVIP, RVIP", "RVIP", "VIP, VVIP, RVIP", "모든 VIP", "RVIP"
    ],
    "예약 가능 여부": ["가능", "예약 마감", "가능", "가능", "가능", "예약 마감"],
    "잔여석": [5, 0, 3, 8, 10, 0]
})

# 📅 월별 이벤트 정리
vip_event_data["월"] = vip_event_data["일정"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").month)
monthly_events = vip_event_data.groupby("월")

# 🎯 월별 이벤트 캘린더 표시
st.markdown("---")
st.markdown("## 📅 VIP 월별 프라이빗 이벤트 스케줄")

# 🔄 월 선택 드롭다운
selected_month = st.selectbox("📆 월을 선택하세요.", sorted(vip_event_data["월"].unique()))

# 선택한 월의 이벤트만 필터링
filtered_events = vip_event_data[vip_event_data["월"] == selected_month]

# 📆 캘린더 형식으로 이벤트 정렬
st.markdown(f"### 📅 {calendar.month_name[selected_month]} VIP 이벤트 일정")

# 🏷️ 이벤트 데이터프레임 출력 (예약 가능 여부 및 잔여석 포함)
st.dataframe(filtered_events[["이벤트 제목", "일정", "장소", "참여 가능 등급", "예약 가능 여부", "잔여석"]])

# 🎯 선택한 이벤트 상세 정보 표시
st.markdown("---")
st.subheader("📍 현재 진행 중인 이벤트 상세 정보")

event_selection = st.radio("📌 자세히 보고 싶은 이벤트를 선택하세요.", filtered_events["이벤트 제목"].tolist())

# 선택한 이벤트 데이터 가져오기
selected_event = filtered_events[filtered_events["이벤트 제목"] == event_selection].iloc[0]

st.write(f"**📅 일정:** {selected_event['일정']}")
st.write(f"**📍 장소:** {selected_event['장소']}")
st.write(f"**👤 참여 가능 등급:** {selected_event['참여 가능 등급']}")
st.write(f"**🛎️ 예약 가능 여부:** {selected_event['예약 가능 여부']}")
st.write(f"**🎟️ 잔여석:** {selected_event['잔여석']}석")

# 예약 가능 여부에 따라 버튼 표시
if selected_event["예약 가능 여부"] == "가능" and selected_event["잔여석"] > 0:
    if st.button("✅ 예약하기"):
        st.success("예약이 완료되었습니다! 🎉")
else:
    st.warning("❌ 해당 이벤트는 예약이 마감되었습니다.")

# 🏎️ 프라이빗 럭셔리 드라이브 체험
if event_selection == "🏎️ 프라이빗 럭셔리 드라이브 체험":
    st.write("""
    ✅ **VVIP 및 RVIP 고객을 위한 최고급 스포츠카 및 럭셔리 세단 드라이브 체험**  
    - 🏎️ 페라리, 람보르기니, 롤스로이스 등 최고급 차량 제공  
    - 🛣️ 프라이빗 드라이브 코스 (한강 및 서울 주요 도로)  
    - 📸 전문가 촬영 서비스 및 기념 사진 제공  
    """)

# 🏌️‍♂️ VIP 초청 골프 라운딩
elif event_selection == "🏌️‍♂️ VIP 초청 골프 라운딩":
    st.write("""
    ✅ **VVIP 및 RVIP 고객 대상 최고급 골프장에서 프라이빗 네트워킹 라운딩**  
    - ⛳ 제주도 최고급 골프장에서 진행  
    - 🥂 골프 후 프라이빗 디너 파티 제공  
    - 👤 유명 프로 골퍼와의 프라이빗 레슨 포함  
    """)

# 🛥️ VVIP 요트 디너
elif event_selection == "🛥️ VVIP 요트 디너":
    st.write("""
    ✅ **RVIP 고객을 위한 프라이빗 요트 디너 파티**  
    - 🍷 최고급 와인과 코스 요리 제공  
    - 🛥️ 부산 요트 클럽에서 진행  
    - 🎶 라이브 공연 및 VIP 고객 네트워킹  
    """)

# 🍽️ 로얄 패밀리 런치
elif event_selection == "🍽️ 로얄 패밀리 런치":
    st.write("""
    ✅ **VIP 및 VVIP 고객 가족을 위한 프라이빗 럭셔리 다이닝 이벤트**  
    - 🥂 서울 최고급 레스토랑 프라이빗 룸에서 진행  
    - 🍽️ 미슐랭 셰프가 직접 준비하는 코스 요리  
    - 🎁 가족 맞춤형 선물 제공  
    """)

# 🚗 프라이빗 시승 & 맞춤 상담
elif event_selection == "🚗 프라이빗 시승 & 맞춤 상담":
    st.write("""
    ✅ **VIP 고객 맞춤형 차량 시승 및 컨설팅 제공**  
    - 🚘 최신 하이엔드 모델 시승 가능 (제네시스, 벤츠, 포르쉐 등)  
    - 🏢 전국 주요 대리점에서 진행  
    - 👨‍💼 전문 컨설턴트와 1:1 맞춤 상담 서비스  
    """)

# 🚖 VIP 리무진 픽업 서비스
elif event_selection == "🚖 VIP 리무진 픽업 서비스":
    st.write("""
    ✅ **RVIP 고객 대상 전용 리무진 픽업 및 이동 서비스 제공**  
    - 🚘 벤츠, 롤스로이스 전용 리무진 제공  
    - 🏡 고객이 원하는 장소에서 픽업 후 목적지까지 이동  
    - 🥂 프라이빗 음료 및 스낵 제공  
    """)

st.markdown("---")
st.write("🚀 **VIP 고객만을 위한 차별화된 프리미엄 혜택을 제공합니다!** 🎖️")

