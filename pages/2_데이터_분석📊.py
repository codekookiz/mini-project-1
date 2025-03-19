import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit 페이지 설정
st.set_page_config(page_title="고객 분석 대시보드", layout="wide")

# ✅ 데이터 로드
DATA_FILE = "data/고객db_전처리.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE, encoding="utf-8-sig").fillna(0)

df = load_data()

# 🚀 **탭 생성**
tab1, tab2 = st.tabs(["고객 데이터 분석", "판매 데이터 분석"])

# 📊 **고객 데이터 분석 탭**
with tab1:
    subtab1, subtab2, subtab3, subtab4, subtab5, subtab6 = st.tabs(
        ["연령대별 고객 분포", "지역별 고객 분포", "연령대별 선호 차량 모델", 
         "연령대별 친환경 차량 선호도", "성별 및 연령대별 차량 선호도", "고객 등급 분석"]
    )

    # ✅ 연령대별 고객 분포 (막대 그래프)
    with subtab1:
        st.subheader("연령대별 고객 분포")
        age_count = df["연령대"].value_counts().reset_index()
        age_count.columns = ["연령대", "고객 수"]

        fig = px.bar(age_count, x="연령대", y="고객 수", text="고객 수",
                     labels={"연령대": "연령대", "고객 수": "고객 수"},
                     title="연령대별 고객 분포", color="고객 수",
                     color_continuous_scale="Blues")
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 지역별 고객 분포 (히트맵)
    with subtab2:
        st.subheader("지역별 고객 분포")
        region_data = df.groupby("거주 지역")["고객 등급"].count().reset_index()
        region_data.columns = ["거주 지역", "고객 수"]

        fig = px.bar(region_data, x="거주 지역", y="고객 수", text="고객 수",
                     labels={"거주 지역": "거주 지역", "고객 수": "고객 수"},
                     title="지역별 고객 분포", color="고객 수",
                     color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 연령대별 선호 차량 모델 (막대 그래프)
    with subtab3:
        st.subheader("연령대별 선호 차량 모델")
        model_data = df.groupby(["연령대", "최근 구매 제품"]).size().reset_index(name="구매 수")
        fig = px.bar(model_data, x="연령대", y="구매 수", color="최근 구매 제품", barmode="group",
                     title="연령대별 선호 차량 모델", labels={"구매 수": "구매 수"})
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 연령대별 친환경 차량 선호도 (막대 그래프)
    with subtab4:
        st.subheader("연령대별 친환경 차량 선호도")
        eco_data = df[df["연료 구분"].isin(["전기", "수소", "하이브리드"])]
        eco_count = eco_data.groupby(["연령대", "연료 구분"]).size().reset_index(name="구매 수")

        fig = px.bar(eco_count, x="연령대", y="구매 수", color="연료 구분", barmode="group",
                     title="연령대별 친환경 차량 선호도")
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 성별 및 연령대별 차량 선호도 (막대 그래프)
    with subtab5:
        st.subheader("성별 및 연령대별 차량 선호도")
        gender_data = df.groupby(["연령대", "성별"]).size().reset_index(name="구매 수")

        fig = px.bar(gender_data, x="연령대", y="구매 수", color="성별", barmode="group",
                     title="성별 및 연령대별 차량 선호도")
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 고객 등급 분석 (히트맵)
    with subtab6:
        st.subheader("고객 등급 분석")
        tier_data = df.pivot_table(index="연령대", columns="고객 등급", values="고객 구분", aggfunc="count").fillna(0)
        fig = px.imshow(tier_data, labels={"color": "고객 수"}, color_continuous_scale="Oranges")
        st.plotly_chart(fig, use_container_width=True)

# 📈 **판매 데이터 분석 탭**
with tab2:
    subtab1, subtab2, subtab3, subtab4 = st.tabs(
        ["시기 및 연료 구분별 판매 대수", "고객 구분별 차량 구매 현황", "고객 구분별 평균 거래 금액", "분기별 차량 판매 요일"]
    )

    # ✅ 시기 및 연료 구분별 판매 대수 (막대 그래프)
    with subtab1:
        st.subheader("시기 및 연료 구분별 판매 대수")
        fuel_data = df.groupby(["최근 구매 시점", "연료 구분"]).size().reset_index(name="판매 대수")

        fig = px.bar(fuel_data, x="최근 구매 시점", y="판매 대수", color="연료 구분", barmode="group",
                     title="시기 및 연료 구분별 판매 대수")
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 고객 구분별 차량 구매 현황 (막대 그래프)
    with subtab2:
        st.subheader("고객 구분별 차량 구매 현황")
        customer_data = df.groupby(["연령대", "고객 구분"]).size().reset_index(name="구매 수")

        fig = px.bar(customer_data, x="연령대", y="구매 수", color="고객 구분", barmode="group",
                     title="고객 구분별 차량 구매 현황")
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 고객 구분별 평균 거래 금액 (히트맵)
    with subtab3:
        st.subheader("고객 구분별 평균 거래 금액")
        price_data = df.pivot_table(index="연령대", columns="고객 구분", values="최근 거래 금액", aggfunc="mean").fillna(0)
        fig = px.imshow(price_data, labels={"color": "평균 거래 금액"}, color_continuous_scale="Greens")
        st.plotly_chart(fig, use_container_width=True)

    # ✅ 분기별 차량 판매 요일 (막대 그래프)
    with subtab4:
        st.subheader("분기별 차량 판매 요일")
        weekday_data = df.groupby(["최근 구매 시점", "최근 구매 요일"]).size().reset_index(name="판매 대수")

        fig = px.bar(weekday_data, x="최근 구매 시점", y="판매 대수", color="최근 구매 요일", barmode="group",
                     title="분기별 차량 판매 요일")
        st.plotly_chart(fig, use_container_width=True)
