import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

plt.rc('font', family='AppleGothic')  # Mac 기본 한글 폰트
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 데이터 로드
df = pd.read_csv("data/고객db_전처리.csv")

# 날짜 데이터 변환
df["최근 구매 날짜"] = pd.to_datetime(df["최근 구매 날짜"])

# Streamlit 페이지 설정
st.set_page_config(page_title="고객 분석 대시보드", layout="wide")
st.title("📊 고객 분석 대시보드")
st.write("이 페이지에서는 고객 데이터를 분석하고 인사이트를 제공합니다.")

# 고객 연령대별 분포 시각화
st.subheader("연령대별 고객 분포")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["연령대"], bins=10, kde=True, color="blue", ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_xlabel("연령대")
ax.set_ylabel("고객 수")
st.pyplot(fig)

# 구매 유형별 선호도 분석
st.subheader("구매 유형별 선호도")
fig, ax = plt.subplots(figsize=(8, 5))
df["선호 거래 방식"].value_counts().plot(kind="bar", color=["skyblue", "salmon", "lightgreen"], ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_xlabel("구매 유형")
ax.set_ylabel("고객 수")
st.pyplot(fig)

# 지역별 고객 수 분석
st.subheader("지역별 고객 수")
fig, ax = plt.subplots(figsize=(8, 5))
df["거주 지역"].value_counts().plot(kind="barh", color="orange", ax=ax)
ax.set_xlabel("지역")
ax.set_ylabel("고객 수")
st.pyplot(fig)

# 차량 브랜드 & 모델별 선호도 분석 (연령대별 상위 5개 모델)
st.subheader("고객 연령대별 선호 차량 모델 분석")

# 연령대별 상위 5개 차량 모델 선정
top_models = df.groupby(["연령대", "최근 구매 제품"]).size().reset_index(name="count")
top_models = top_models.sort_values(["연령대", "count"], ascending=[True, False])
top_models = top_models.groupby("연령대").head(5)  # 각 연령대에서 상위 5개 모델 선택

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_models, x="연령대", y="count", hue="최근 구매 제품", palette="coolwarm", ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_xlabel("연령대")
ax.set_ylabel("선호 차량 모델 수")
ax.set_title("연령대별 선호 차량 모델 (상위 5개)")
st.pyplot(fig)

import squarify

st.subheader("연령대별 선호 차량 모델 비율 (Treemap)")

# 연령대별 차량 모델 비율 계산
model_counts = df["최근 구매 제품"].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
squarify.plot(sizes=model_counts.values, label=model_counts.index, alpha=0.7, color=sns.color_palette("Set2", len(model_counts)))
ax.set_title("연령대별 선호 차량 모델 비율")
ax.axis("off")
st.pyplot(fig)



# 전기차 vs. 내연기관차 구매 트렌드 비교
st.subheader("최근 3년간 전기차 구매 증가율 vs. 내연기관 차량 구매율 비교")
recent_years = df[df["최근 구매 날짜"] >= (df["최근 구매 날짜"].max() - pd.DateOffset(years=3))]
ev_vs_ice = recent_years["연료 구분"].value_counts()
fig, ax = plt.subplots(figsize=(8, 5))
ev_vs_ice.plot(kind="bar", color=["green", "gray"], ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_xlabel("차량 유형")
ax.set_ylabel("구매 수")
ax.set_title("최근 3년간 전기차 vs. 내연기관차 구매 비교")
st.pyplot(fig)

# 연령대별 친환경 차량 선호도 분석
st.subheader("연령대별 친환경 차량 선호도")
# 친환경 차량 유형 목록
eco_friendly_types = ["전기", "수소", "하이브리드", "플러그인하이브리드"]

ev_preference = df[df["연료 구분"].isin(eco_friendly_types)].groupby("연령대")["연료 구분"].count()
fig, ax = plt.subplots(figsize=(8, 5))
ev_preference.plot(kind="bar", color="lightgreen", ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_xlabel("연령대")
ax.set_ylabel("친환경 차량 구매 수")
ax.set_title("연령대별 친환경 차량 구매 선호도")
st.pyplot(fig)

# 전체 요약
st.write("데이터를 기반으로 다양한 고객 분석을 제공합니다.")
