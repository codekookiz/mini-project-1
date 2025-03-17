import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import os

# 로컬 환경에서 사용할 폰트 (Mac 기준)
if os.name == 'posix':  # Mac 환경에서
    plt.rcParams['font.family'] = 'AppleGothic'  # Mac 기본 한글 폰트
else:
    plt.rcParams['font.family'] = 'NanumGothic'  # 배포 환경에서 사용될 한글 폰트

plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 데이터 로드
df = pd.read_csv("data/고객db_전처리.csv")

# 날짜 데이터 변환
df["최근 구매 날짜"] = pd.to_datetime(df["최근 구매 날짜"])

# Streamlit 페이지 설정
st.set_page_config(page_title="고객 분석 대시보드", layout="wide")

# 페이지 제목
st.title("분석 대시보드")

tab1, tab2 = st.tabs(["고객 데이터 분석", "판매 데이터 분석"])

with tab1 :
    # 고객 데이터 분석 섹션
    st.header("고객 데이터 분석")
    st.write("고객 데이터 기반의 분석 인사이트를 제공합니다.")

    # 분석 개요 섹션
    with st.expander("분석 개요 보기"):
        st.write("""
        **프로젝트 목표**  
        - 고객의 연령대, 거주 지역, 구매 선호도를 분석하여 비즈니스 인사이트 제공  
        - 전기차 및 내연기관차의 트렌드 변화 확인  
        - 데이터 기반으로 마케팅 전략 최적화  

        **사용된 데이터**  
        - 고객 연령대, 거주 지역, 선호 차량 모델, 연료 유형, 최근 구매 날짜 등  
        """)

    st.text("")

    # 연령대 정렬을 위한 순서 지정
    age_order = [
        "20대 초반", "20대 중반", "20대 후반",
        "30대 초반", "30대 중반", "30대 후반",
        "40대 초반", "40대 중반", "40대 후반",
        "50대 초반", "50대 중반", "50대 후반",
        "60대 초반", "60대 중반", "60대 후반",
        "70대 초반", "70대 중반", "70대 후반"
    ]

    col1, col2 = st.columns([0.9, 1])  # 좌우 여백 추가
    with col1:
        # ---- 연령대별 고객 분포 ----
        st.subheader("연령대별 고객 분포")
        st.write("고객의 연령대별 분포를 히스토그램으로 표현했습니다.")  

        # 연령대 정렬 후 시각화
        df["연령대"] = pd.Categorical(df["연령대"], categories=age_order, ordered=True)
        fig1, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(df.sort_values("연령대")["연령대"], kde=True, color="blue", ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.set_xlabel("연령대")
        ax.set_ylabel("고객 수")
        st.pyplot(fig1)

        st.write("""
        **분석 결과 및 활용 방안**  
        - 특정 연령대(30~40대)에 고객이 집중됨  
        - 이 연령대에 맞춘 타겟 마케팅 전략이 효과적일 가능성 높음  
        - 가족 단위 차량 프로모션, 장기 렌트 혜택 제공 가능
        """)
    with col2:
        # ---- 지역별 고객 수 분석 ----
        st.subheader("지역별 고객 분포")
        st.write("고객들이 거주하는 지역별 분포를 나타냅니다.") 

        fig2, ax = plt.subplots(figsize=(8, 5))
        df["거주 지역"].value_counts().plot(kind="barh", color="orange", ax=ax)
        ax.set_xlabel("지역")
        ax.set_ylabel("고객 수") 
        st.pyplot(fig2)

        st.write("""
        **분석 결과 및 활용 방안**  
        - 특정 지역(서울, 경기)에 고객이 집중됨  
        - 해당 지역에서 차량 전시회 및 시승 이벤트 기획 가능  
        - 지방 거주 고객 대상, 비대면 서비스(라이브 상담, 온라인 계약 등) 확대 필요
        """)

    st.markdown("---")
    
    # 연령대별 상위 3개 차량 모델 선정
    top_models = df.groupby(["연령대", "최근 구매 제품"]).size().reset_index(name="count")
    top_models = top_models.sort_values(["연령대", "count"], ascending=[True, False])
    top_models = top_models.groupby("연령대").head(3)  # 각 연령대에서 상위 3개 모델 선택

    eco_friendly_types = ["전기", "수소", "하이브리드", "플러그인하이브리드"]
    ev_preference = df[df["연료 구분"].isin(eco_friendly_types)].groupby("연령대")["연료 구분"].count()

    col1, col2 = st.columns([1, 1])  # 좌우 여백 추가
    with col1:
        # ---- 차량 브랜드 & 모델별 선호도 분석 ----
        st.subheader("고객 연령대별 선호 차량 모델 분석")
        st.write("연령대별로 선호하는 상위 3개 차량 모델을 선정하여 시각화했습니다.")

        fig1, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top_models, x="연령대", y="count", hue="최근 구매 제품", palette="coolwarm", ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.set_xlabel("연령대")
        ax.set_ylabel("선호 차량 모델 수")
        ax.set_title("연령대별 선호 차량 모델 (상위 3개)")
        st.pyplot(fig1)

        st.write("""
        **분석 결과 및 활용 방안**  
        - 20~30대는 소형 및 스포츠카 선호, 40대 이상은 SUV 및 세단 선호  
        - 젊은 고객층 대상, 스포티한 디자인과 최신 기술 강조  
        - 40대 이상 고객 대상, 가족용 SUV 및 하이브리드 차량 프로모션 강화
        """)
    with col2:
        # ---- 연령대별 친환경 차량 선호도 분석 ----
        st.subheader("연령대별 친환경 차량 선호도")
        st.write("각 연령대별 친환경 차량(전기, 수소, 하이브리드, 플러그인하이브리드)의 선호도를 분석했습니다.")   

        fig2, ax = plt.subplots(figsize=(8, 5))
        ev_preference.plot(kind="bar", color="lightgreen", ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.set_xlabel("연령대")
        ax.set_ylabel("친환경 차량 구매 수")
        ax.set_title("연령대별 친환경 차량 구매 선호도")
        st.pyplot(fig2)
    
        st.write("""
        **분석 결과 및 활용 방안**  
        - 30~50대 고객층에서 친환경 차량 선호도가 높음  
        - 친환경 차량 보조금 및 충전소 혜택을 강조한 마케팅 필요  
        - 연령대별 맞춤형 친환경 차량 옵션 제공 가능
        """)

    # ---- 전체 요약 ----
    # st.subheader("결론 및 요약")
    # st.write("""
    # - 특정 연령대에서 고객 수가 집중되는 경향이 보인다.  
    # - 구매 유형별로 선호도가 다르게 나타나며, 이를 바탕으로 마케팅 전략을 세울 수 있다.  
    # - 연령대별 선호 차량 모델을 분석하여 타겟 마케팅에 활용 가능하다.  
    # - 최근 3년간 전기차 구매 비율이 상승했으며, 친환경 차량에 대한 선호도가 증가하고 있다.  
    # """)





st.markdown("---")




with tab2 :
    # 판매 데이터 분석 섹션
    st.header("판매 데이터 분석")
    st.write("판매 데이터 기반의 분석 인사이트를 제공합니다.")

    col1, col2 = st.columns([1, 1])  # 좌우 여백 추가
    with col1:
        # ---- 구매 유형별 선호도 ----
        st.subheader("구매 유형별 선호도")
        st.write("고객들이 선호하는 구매 유형을 분석하여 그래프로 표현했습니다.")

        fig, ax = plt.subplots(figsize=(8, 5))
        df["선호 거래 방식"].value_counts().plot(kind="bar", color=["skyblue", "salmon", "lightgreen"], ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.set_xlabel("구매 유형")
        ax.set_ylabel("고객 수")
        st.pyplot(fig)

        st.write("""
        **분석 결과 및 활용 방안**  
        - 대다수 고객이 온라인 및 대리점을 통한 구매를 선호  
        - 온라인 프로모션 강화 및 대리점별 특화 혜택 제공 필요  
        - 오프라인 고객 대상, 추가적인 서비스 패키지 제공 가능
        """)
    with col2:
        pass

    # ---- 구매 유형별 선호도 ----
    st.subheader("구매 유형별 선호도")
    st.write("고객들이 선호하는 구매 유형을 분석하여 그래프로 표현했습니다.")

    fig, ax = plt.subplots(figsize=(8, 5))
    df["선호 거래 방식"].value_counts().plot(kind="bar", color=["skyblue", "salmon", "lightgreen"], ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.set_xlabel("구매 유형")
    ax.set_ylabel("고객 수")
    st.pyplot(fig)

    st.write("""
    **분석 결과 및 활용 방안**  
    - 대다수 고객이 온라인 및 대리점을 통한 구매를 선호  
    - 온라인 프로모션 강화 및 대리점별 특화 혜택 제공 필요  
    - 오프라인 고객 대상, 추가적인 서비스 패키지 제공 가능
    """)

    # ---- 전기차 vs. 내연기관차 구매 트렌드 비교 ----
    st.subheader("최근 3년간 전기차 구매 증가율 vs. 내연기관 차량 구매율 비교")
    st.write("최근 3년간 전기차와 내연기관 차량의 구매 트렌드를 비교했습니다.")

    recent_years = df[df["최근 구매 날짜"] >= (df["최근 구매 날짜"].max() - pd.DateOffset(years=3))]
    ev_vs_ice = recent_years["연료 구분"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    ev_vs_ice.plot(kind="bar", color=["green", "gray"], ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.set_xlabel("차량 유형")
    ax.set_ylabel("구매 수")
    ax.set_title("최근 3년간 전기차 vs. 내연기관차 구매 비교")
    st.pyplot(fig)

    st.write("""
    **분석 결과 및 활용 방안**  
    - 최근 3년간 전기차 판매량이 꾸준히 증가   
    - 내연기관차보다 전기차 구매 비율이 높아지는 추세 
    - 전기차 관련 금융 혜택 및 충전소 인프라 확장 필요
    """)

    st.warning("근거가 부족한 분석, 다시 확인 필요")