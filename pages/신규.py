import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 고객 데이터 불러오기
df = pd.read_csv("data/고객db_전처리.csv")

# 🚗 신규 고객 맞춤형 서비스
st.title("🚗 신규 고객 웰컴 패키지 & 서비스 혜택")
st.write("처음 차량을 구매한 고객에게 특별한 웰컴 혜택을 제공합니다! 🎁")
st.markdown("---")

# 💰 신규 고객의 누적 소비 금액 입력
purchase_amount = st.number_input("🔢 누적 소비 금액 입력 (단위: 만 원)", min_value=0, step=100, value=3000)

# 🎁 웰컴 패키지 혜택 적용 (소비 금액에 따른 차등 제공)
if purchase_amount >= 8000:
    coupon_count = 5
    gift = "프리미엄 차량용 방향제 + 가죽 키케이스 + 차량 정비 키트"
elif purchase_amount >= 5000:
    coupon_count = 3
    gift = "고급 차량용 방향제 + 로고 키체인"
elif purchase_amount >= 3000:
    coupon_count = 2
    gift = "브랜드 차량용 방향제"
else:
    coupon_count = 1
    gift = "기본 차량용 방향제"

# ✅ 웰컴 패키지 상세
st.subheader("🎁 웰컴 패키지 혜택")
st.markdown(f"""
- **첫 서비스 혜택:** 🚗
  - 첫 정기점검, 세차 또는 소모품 교체 서비스에 대해 **무료/할인 쿠폰 {coupon_count}개 제공**
- **브랜드 기념품:** 🎀
  - {gift} 제공
- **맞춤형 커뮤니케이션:** 💌
  - 이메일 & 문자 메시지로 혜택 안내 및 맞춤형 서비스 추천
""")

st.markdown("---")

# 📧 맞춤형 커뮤니케이션 발송
st.subheader("📩 이메일 & 문자 발송")
st.write("")
col1, col2, _ = st.columns([1, 1, 8])
with col1:
    email_sent = st.button("📧 이메일 발송")
with col2:
    sms_sent = st.button("📩 문자 발송")

if email_sent:
    st.success("✅ 이메일 발송 완료!")
if sms_sent:
    st.success("✅ 문자 발송 완료!")

# 📊 맞춤형 커뮤니케이션 발송 건수 시각화
dates = pd.date_range(start="2025-03-01", end="2025-03-31")
np.random.seed(42)
email_counts = np.random.randint(140, 180, size=len(dates))
sms_counts = np.random.randint(70, 90, size=len(dates))

df_comm = pd.DataFrame({"날짜": dates, "이메일 발송 건수": email_counts, "문자 발송 건수": sms_counts})
df_melted = df_comm.melt(id_vars="날짜", var_name="발송 유형", value_name="발송 건수")

fig_comm = px.line(df_melted, x="날짜", y="발송 건수", color="발송 유형", markers=True,
                   title="📧 2025년 3월 맞춤형 커뮤니케이션 발송 건수")
fig_comm.update_layout(xaxis_title="날짜", yaxis_title="발송 건수", hovermode="x unified")
st.plotly_chart(fig_comm, use_container_width=True)

st.markdown("---")

seminar_data = {
    "세미나 제목": [
        "차량 관리 워크숍", "정비 팁 세미나", "안전 운전 강의",
        "고객 Q&A 세션", "신제품 소개", "고급 차량 유지보수 가이드", 
        "연비 절약 및 친환경 운전법", "고객 맞춤형 금융 상담", "자동차 보험의 모든 것", "프리미엄 차량 시승 체험"
    ],
    "시작일": [
        "2025-03-20 09:30", "2025-03-20 11:00", "2025-03-20 14:00", "2025-03-20 15:30", "2025-03-21 10:00",
        "2025-03-21 13:00", "2025-03-21 16:00", "2025-03-22 09:30", "2025-03-22 12:00", "2025-03-22 15:00"
    ],
    "종료일": [
        "2025-03-20 11:00", "2025-03-20 12:30", "2025-03-20 16:30", "2025-03-20 17:00", "2025-03-21 11:30",
        "2025-03-21 14:30", "2025-03-21 17:30", "2025-03-22 11:00", "2025-03-22 13:30", "2025-03-22 16:30"
    ],
    "진행 방식": [
        "온라인", "오프라인", "온라인", "오프라인", "온라인",
        "오프라인", "온라인", "오프라인", "온라인", "오프라인"
    ],
    "장소": [
        "Zoom 미팅", "서울 강남 컨퍼런스룸", "Webex", "부산 해운대 센터", "Teams",
        "서울 강북 서비스센터", "Zoom 미팅", "부산 VIP 라운지", "Webex", "서울 프리미엄 쇼룸"
    ],
    "잔여석": [10, 5, 3, 8, 0, 4, 6, 9, 2, 5],
    "세미나 설명": [
        "🚗 차량 관리 기본 지식 및 유지보수 팁 제공 (오일 교체, 타이어 관리 등 필수 정보 포함)",
        "🛠️ 정비 전문가와 함께하는 실전 팁 공개 (고객이 직접 체험할 수 있는 워크샵 진행)",
        "🚦 안전 운전을 위한 핵심 가이드 및 사고 예방 교육 (야간 운전, 비상 시 대처 방법 포함)",
        "❓ 실시간 Q&A를 통해 궁금증 해결 (자동차 구매, 정비, 금융 관련 질문 가능)",
        "🆕 신제품의 주요 기능 및 활용법 소개 (최신 차량 모델 및 혁신 기술 설명)",
        "🔧 고급 차량 유지보수 가이드 (고급 브랜드 차량 유지 및 관리법 심층 강의)",
        "⛽ 연비 절약 및 친환경 운전법 (연료 절약 기술 및 친환경 운전 습관 제안)",
        "💰 고객 맞춤형 금융 상담 (리스, 할부, 무이자 금융 상품 비교 및 추천)",
        "🛡️ 자동차 보험의 모든 것 (보험 보장 범위, 추천 보험 상품, 클레임 처리 방법 설명)",
        "🚘 프리미엄 차량 시승 체험 (고급 차량을 직접 시승하고 특성을 비교 분석하는 시간)"
    ]
}
df_seminar = pd.DataFrame(seminar_data)
df_seminar["시작일"] = pd.to_datetime(df_seminar["시작일"])
df_seminar["종료일"] = pd.to_datetime(df_seminar["종료일"])

# 신청 마감 메시지 생성
df_seminar["마감_메시지"] = df_seminar["잔여석"].apply(lambda x: "<br>🚫 신청 마감됨" if x == 0 else "")

# Plotly Timeline 생성
fig_seminar = px.timeline(df_seminar, 
                          x_start="시작일", x_end="종료일", y="세미나 제목", color="진행 방식",
                          title="📅 세미나 일정 타임라인", labels={"진행 방식": "진행 방식"}, 
                          hover_data=["장소", "잔여석", "마감_메시지"])

# Hover 템플릿 업데이트
fig_seminar.update_traces(hovertemplate="<b>%{y}</b><br>📍 장소: %{customdata[0]}<br>🪑 잔여석: %{customdata[1]}%{customdata[2]}")

# Y축 정렬 및 가이드선 추가
fig_seminar.update_yaxes(autorange="reversed", showgrid=True, gridcolor="lightgray")
fig_seminar.update_xaxes(showgrid=True, gridcolor="lightgray", griddash="dot")

# 레이아웃 업데이트
fig_seminar.update_layout(xaxis_title="시간", yaxis_title="세미나 제목", hovermode="closest")

# Streamlit에서 차트 출력
st.plotly_chart(fig_seminar, use_container_width=True)

st.markdown("---")

# 🎟️ 세미나 선택 및 신청 기능
st.subheader("🎟️ 세미나 신청")
st.write("")
selected_seminar = st.radio("참여하고 싶은 세미나를 선택하세요", df_seminar["세미나 제목"].tolist())
selected_row = df_seminar[df_seminar["세미나 제목"] == selected_seminar].iloc[0]

st.write("")

st.markdown("#### 📌 **세미나 상세 정보**")
st.write(f"**ℹ️ 세미나 설명:** {selected_row['세미나 설명']}")
st.write(f"**📅 일정:** {selected_row['시작일'].strftime('%Y-%m-%d %H:%M')} ~ {selected_row['종료일'].strftime('%H:%M')}")
st.write(f"**📍 장소:** {selected_row['장소']}")
st.write(f"**🪑 잔여석:** {selected_row['잔여석']}")

# 신청하기 버튼 및 처리
if st.button("✅ 신청하기"):
    if selected_row["잔여석"] > 0:
        df_seminar.loc[df_seminar["세미나 제목"] == selected_seminar, "잔여석"] -= 1
        st.success("✅ 신청 완료되었습니다!")
    else:
        st.warning("❌ 신청이 마감되었습니다. 다음 기회를 이용해주세요.")

st.markdown("---")
st.markdown("##### 🚀 신규 고객을 위한 다양한 서비스와 혜택을 계속해서 제공해드릴 예정입니다!")