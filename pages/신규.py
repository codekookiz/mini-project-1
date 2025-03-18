import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("data/고객db_전처리.csv")

# 신규 고객에 대한 서비스 혜택 제공
# 신규 고객 : 최근 6개월 이내 첫 구매 이력이 있는 고객
st.write("## 웰컴 패키지 제공")
st.subheader("서비스 혜택 세부 내용")

st.markdown("""
- **첫 서비스 혜택:**
  - 첫 정기점검, 세차 또는 소모품 교체 서비스에 대해 무료/할인 쿠폰 제공
- **브랜드 기념품:**
  - 차량용 방향제, 로고가 새겨진 키체인, 청소용품 등을 포함한 브랜드 기념품 제공
  - 브랜드 이미지 강화 및 브랜드에 대한 긍정적인 첫인상 형성
- **맞춤형 커뮤니케이션:**
  - 웰컴 패키지 안내 이메일/문자 메시지 발송 : 구체적인 사용 방법 및 유의사항 안내
  - 고객의 차량 종류나 구매 시기 등 데이터 활용해 맞춤형 혜택 제시
""")

st.write("## 차량 구매가 처음인 고객을 위한 커뮤니티 혜택")
st.markdown("""
- **교육 및 세미나 개최:**
  - 차량 관리, 정비 팁, 안전 운전 강의 등 주제로 정기적인 온·오프라인 세미나/워크숍 제공
  - 실시간 Q&A 세션을 통해 고객이 직접 궁금증 해소
- **참여 인센티브:**
  - 이벤트 참가자에게 할인 쿠폰, 포인트 적립 또는 다음 서비스 예약 시 사용할 수 있는 특별 혜택 제공
  - 이벤트 참여 인증(예: SNS 포스팅) 시 추가 혜택을 제공 : 자연스러운 바이럴 마케팅 효과
- **온/오프라인 통합 운영:**
  - 오프라인 이벤트와 연계된 온라인 콘텐츠(녹화 영상, 자료집 등) 제공 : 추가적인 정보 제공
""")

new_client = df.loc[df["고객 등급"] == "신규", ["이름", "휴대폰 번호", "이메일"]]
new_client.reset_index(drop=True, inplace=True)

st.markdown("### 신규 고객 리스트")
st.dataframe(new_client)

# --- 맞춤형 커뮤니케이션 상세 발송 건수 ---
st.markdown("#### 맞춤형 커뮤니케이션 상세 발송 건수")
# 2025년 3월 1일부터 3월 31일까지의 일별 데이터 생성 (난수 활용, seed 고정)
dates = pd.date_range(start="2025-03-01", end="2025-03-31")
np.random.seed(42)
email_counts = np.random.randint(140, 180, size=len(dates))
sms_counts = np.random.randint(70, 90, size=len(dates))

df_comm = pd.DataFrame({
    "날짜": dates,
    "이메일 발송 건수": email_counts,
    "문자 발송 건수": sms_counts
})

# 1) 데이터 Long Format으로 변환
df_melted = df_comm.melt(id_vars="날짜", var_name="variable", value_name="발송 건수")

# 2) Plotly Express로 한 그래프 안에 여러 선을 겹쳐서 표시
fig_comm = px.line(
    df_melted, 
    x="날짜", 
    y="발송 건수", 
    color="variable",       # variable 값(이메일/문자)에 따라 선 색상 구분
    markers=True,
    title="2025년 3월 맞춤형 커뮤니케이션 발송 건수"
)

fig_comm.update_layout(
    xaxis_title="날짜",
    yaxis_title="발송 건수",
    hovermode="x unified"
)

st.plotly_chart(fig_comm, use_container_width=True)

# --- 상세 세미나 일정 타임라인 (날짜 선택 없이 전체 일정 표시) ---
st.markdown("#### 상세 세미나 일정 타임라인")
# 세미나 일정 데이터: 장소 정보 포함
seminar_data = {
    "세미나 제목": [
        "차량 관리 워크숍", "정비 팁 세미나", "안전 운전 강의",
        "고객 Q&A 세션", "신제품 소개", "전문가 패널 토론", 
        "서비스 후기 공유", "고객 맞춤형 상담", "신규 고객 환영회", "서비스 체험 이벤트"
    ],
    "시작일": [
        "2025-03-20 09:30", "2025-03-20 11:00", "2025-03-21 14:00",
        "2025-03-21 15:00", "2025-03-22 10:00", "2025-03-22 13:30", 
        "2025-03-22 15:00", "2025-03-23 10:00", "2025-03-24 18:00", "2025-03-25 09:00"
    ],
    "종료일": [
        "2025-03-20 13:00", "2025-03-20 12:30", "2025-03-21 17:30",
        "2025-03-21 18:00", "2025-03-22 11:30", "2025-03-22 15:00", 
        "2025-03-22 16:30", "2025-03-23 14:00", "2025-03-24 20:00", "2025-03-25 15:00"
    ],
    "진행 방식": [
        "온라인", "오프라인", "온라인", "오프라인", "온라인", 
        "오프라인", "온라인", "오프라인", "온라인", "오프라인"
    ],
    "장소": [
        "Zoom 미팅", "서울 강남 컨퍼런스룸", "Webex", 
        "부산 해운대 센터", "Teams", "대구 동성로 컨퍼런스룸", 
        "Zoom 미팅", "인천 컨벤션 센터", "서울 코엑스", "광주 문화센터"
    ]
}
df_seminar = pd.DataFrame(seminar_data)
df_seminar["시작일"] = pd.to_datetime(df_seminar["시작일"])
df_seminar["종료일"] = pd.to_datetime(df_seminar["종료일"])

# Plotly 타임라인 차트 생성
fig_seminar = px.timeline(
    df_seminar, 
    x_start="시작일", 
    x_end="종료일", 
    y="세미나 제목", 
    color="진행 방식",
    title="세미나 일정 타임라인 (상세)",
    labels={"진행 방식": "진행 방식"},
    hover_data=["장소"]
)
# y축을 역순으로 하여 위쪽에 먼저 진행하는 이벤트가 표시되도록 함
fig_seminar.update_yaxes(autorange="reversed")
fig_seminar.update_layout(
    xaxis_title="세미나 시간",
    yaxis_title="세미나 제목",
    hovermode="closest",
    transition_duration=500
)
st.plotly_chart(fig_seminar, use_container_width=True)