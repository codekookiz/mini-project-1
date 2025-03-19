import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sb
import time
from datetime import datetime
import calendar
from matplotlib import font_manager, rc
import platform
import os


# 한글 폰트 설정
plt.rcParams["axes.unicode_minus"] = False

if platform.system() == "Darwin":  # macOS
    rc("font", family="AppleGothic")
elif platform.system() == "Windows":  # Windows
    font_path = "C:/Windows/Fonts/malgun.ttf"  # 맑은 고딕
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc("font", family=font_name)
elif platform.system() == "Linux":  # Linux (Ubuntu, Docker 등)
    font_path = "fonts/NanumGothic.ttf"
    if not os.path.exists(font_path):
        st.error("NanumGothic.ttf 폰트 파일이 존재하지 않습니다. 'fonts' 폴더 내에 폰트 파일을 확인하세요.")
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc("font", family=font_name)


st.title("📈 마케팅 전략")

st.write("이 페이지에서는 세그먼트에 따른 마케팅 전략을 추천합니다.")

df = pd.read_csv("data/고객db_전처리.csv")

st.markdown("---")

# 1. 신용카드 이용 구매 유도 위해 카드사 제휴 확대
st.subheader("🚗 신용카드 이용 구매 유도 위해 카드사 제휴 확대")

# 카드사 제휴의 이점
st.write("## 카드사 제휴 확대 이점")
st.markdown("""
✅ **할부 혜택 제공** : 장기 무이자 할부 가능  
✅ **포인트 적립 및 사용** : 차량 구매 시 포인트 적립 및 활용 가능  
✅ **자동차 유지비 관련 혜택** : 보험, 정비, 주유비 할인 가능  
✅ **전기차 충전 혜택 제공** : EV 충전소 이용 할인 적용  
✅ **특정 차량 구매 시 추가 혜택** : 특정 차종 구매 시 맞춤형 혜택 제공  
""")

# 카드사 제휴 확대 예시
st.write("## 카드사 제휴 확대 예시")
st.markdown("""
🔹 현대카드, 롯데카드, 우리카드, 하나카드 등 주요 카드사와 제휴 협약  
🔹 카드사별 맞춤형 할부 혜택 및 포인트 적립 혜택 제공  
🔹 카드사별 할인 혜택 강화 및 연계 프로모션 진행  
🔹 자동차 구매 시 전용 카드 혜택 지원  
""")

# 카드사 제휴 현황
st.write("## 카드사 제휴 현황")

card_df = pd.DataFrame({
    "카드사": ["현대카드", "롯데카드", "우리카드", "하나카드"],
    "할인 혜택 (%)": [10, 5, 3, 4]
})

# 표 크기 조절 및 가운데 정렬 적용
def format_table(df):
    return df.style.set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'center'), ('font-size', '14px')]},
        {'selector': 'td', 'props': [('text-align', 'center'), ('font-size', '13px')]},
        {'selector': 'table', 'props': [('width', '60%'), ('margin', 'auto')]}])

st.write(format_table(card_df))

# 카드사별 주요 혜택
st.write("## 카드사별 주요 혜택")

st.markdown("""
### 🔹 현대카드 (Hyundai Card)  
✅ **자동차 구매 & 할부 혜택 특화** : 장기 무이자 할부 제공  
✅ **포인트 적립 + 추가 할인** : 특정 차종 구매 시 추가 혜택  
✅ **전기차 충전 혜택** : EV 충전소 할인 적용  
✅ **VIP 정비 쿠폰 제공** : 현대카드 고객 전용  

### 🔹 롯데카드 (Lotte Card)  
✅ **자동차 유지비 절감** : 보험료, 주유비, 정비비 할인  
✅ **렌터카 할인 이벤트** : 롯데렌터카와 연계 가능  
✅ **할부 혜택 연장 (최대 36개월)** : 일부 대리점과 연계 가능  
✅ **구매 시 5% 캐시백 제공**  

### 🔹 우리카드 (Woori Card)  
✅ **자동차 전용 카드 출시 가능성** : 기아, 현대차 일부 모델 할부 지원  
✅ **전기차 충전소 혜택** : 전기차 충전 포인트 적립 가능  
✅ **주유비 할인** : SK/GS칼텍스 연계  
✅ **추가 할인 (3~5%) + 포인트 적립 강화**  

### 🔹 하나카드 (Hana Card)  
✅ **최대 60개월 장기 할부 지원**  
✅ **자동차 보험 할인** : 삼성화재, DB손해보험 연계 가능  
✅ **주유비 & 자동차 유지비 할인 연계 가능**  
✅ **프리미엄 차량 구매 시 추가 혜택** : 제네시스, 수입차  
""")

# 카드사별 혜택 비교 시각화
st.write("## 카드사별 혜택 비교 시각화")

# 카드사별 주요 혜택 데이터
benefit_data = {
    "카드사": ["현대카드", "롯데카드", "우리카드", "하나카드"],
    "할부 혜택 (최대 개월 수)": [60, 36, 48, 60],
    "포인트 적립 (%)": [5, 3, 4, 2],
    "주유비 할인 (%)": [7, 5, 6, 5],
    "전기차 충전 혜택 (%)": [10, 4, 8, 6]
}

benefit_df = pd.DataFrame(benefit_data)

fig2, ax2 = plt.subplots(figsize=(12, 6))
sb.barplot(data=benefit_df.melt(id_vars=["카드사"], var_name="혜택 유형", value_name="비율"), 
           x="카드사", y="비율", hue="혜택 유형", palette="coolwarm", ax=ax2)
ax2.set_title("카드사별 주요 혜택 비교", fontsize=14, fontweight='bold')
ax2.set_xlabel("카드사", fontsize=12, labelpad=10)
ax2.set_ylabel("혜택 비율 (%)", fontsize=12)
ax2.legend(title="혜택 유형", fontsize=10, title_fontsize=12, loc='upper right', ncol=1, frameon=True)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.tick_params(axis='x', labelrotation=0)

st.pyplot(fig2)
st.markdown("---")

# 2. 카테고리별 마케팅 전략 수립

st.subheader("카테고리별 마케팅 전략 수립")

marketing_class = st.selectbox("마케팅 전략 구분", ["-", "연령대별", "지역별", "고객 등급별"])

if marketing_class == "지역별":
    st.write("")

    col1, col2 = st.columns([1, 1])
    with col1 : 
        # 연료 구분 정렬 순서 지정
        fuel_order = ["전기", "하이브리드", "플러그인 하이브리드", "휘발유", "디젤", "수소"]

        # "연료 구분"을 Categorical 타입으로 변경하여 순서 지정
        df["연료 구분"] = pd.Categorical(df["연료 구분"], categories=fuel_order, ordered=True)

        # 데이터 그룹화 및 시각화를 위한 준비
        region_df = df.groupby(["거주 지역", "연료 구분"])["연번"].count().unstack()

        fig1, ax = plt.subplots(figsize=(12, 8))
        region_df.reindex(columns=fuel_order).plot(kind="barh", stacked=True, ax=ax)

        ax.set_title("거주 지역별 판매 차량 유형")
        ax.set_xlabel("판매 대수")
        ax.set_ylabel("거주 지역")

        st.pyplot(fig1)

    with col2:
        # 스캐터 플롯 생성
        fig2, ax = plt.subplots(figsize=(10, 6))
        scatter = sb.scatterplot(data=df, x="1인당 GDP (만 원)", y="인구 밀도", hue="거주 지역", palette="Set2", s=100, ax=ax)

        # 각 점 옆에 해당 거주 지역 표시
        for i in range(len(df)):
            ax.annotate(df["거주 지역"][i], (df["1인당 GDP (만 원)"][i], df["인구 밀도"][i]), 
                        textcoords="offset points", xytext=(5,5), ha='left', fontsize=9)

        ax.set_title("1인당 GDP와 인구 밀도에 따른 거주 지역")
        ax.set_xlabel("1인당 GDP (만 원)")
        ax.set_ylabel("인구 밀도")

        st.pyplot(fig2)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("""
        **분석 결과**  
        - 차량 구매 건수 : 서울, 수원, 광주, 청주, 울산 등이 높은 편
            - 인구 밀도가 높거나 1인당 평균 소득이 높다는 점이 영향을 미친 것으로 보임
        - 전기차 및 하이브리드 차량 구매 건수 : 전반적으로 높지 않음
            - 서울, 포항, 울산 등이 그나마 많은 편
        """)
    with col2:
        st.write("""
        **분석 결과**  
        - 주요 타겟팅 할 만한 지역 선정
            - 1인당 GDP가 높거나 인구 밀도가 높은 지역 : 서울, 수원, 울산, 성남, 천안
            - 추후 차량 구매 촉진이 유리한 환경이라고 판단됨
        """)

    st.subheader("")

    # 타겟 지역 선택
    st.subheader("🎯 타겟 지역별 마케팅 전략")

    region = st.selectbox("타겟 지역 선택", ["-", "서울특별시", "경기도 수원시", "울산광역시", "경기도 성남시", "충청남도 천안시"])

    age_order = ["20대 초반", "20대 중반", "20대 후반", "30대 초반", "30대 중반", "30대 후반", "40대 초반", "40대 중반", "40대 후반",
             "50대 초반", "50대 중반", "50대 후반", "60대 초반", "60대 중반", "60대 후반", "70대 초반"]

    df["연령대"] = pd.Categorical(df["연령대"], categories=age_order, ordered=True)

    # 지역에 따른 마케팅 전략 추천
    analysis = {
        "서울특별시": "\n\n- 1. 20대 중반이 가장 많이 구매 : 주 타겟층\n   - 선호 차량 유형 : 중형 SUV/세단\n- 2. 전 연령대에 걸쳐 판매 가능성 : 40대부터 60대까지 꾸준한 소비\n   - 선호 차량 유형 : 중형 SUV/세단\n- 3. 이미 130개 이상의 대리점/지점 존재\n    - 전시장 확대보다는 더욱 다양한 차량 라인업 제공이 필요\n",
        "경기도 수원시": "\n\n- 1. 40대 초반과 60대 중반이 가장 많이 구매 : 주 타겟층\n  - 선호 차량 유형 : 준중형 세단\n- 2. 전반적으로 중형~준중형 사이즈 차량 수요 높음\n    - 차종 역시 세단 선호도가 높음\n",
        "울산광역시": "\n\n- 1. 30대 후반과 50대 중반 : 주 타겟층\n    - 중형 SUV 선호\n- 2. 비교적 전 연령대에서 고른 구매 수요를 보임\n   - 중형 SUV 및 세단 선호도 높음\n- 3. SUV의 선호도가 타지역에 비해 두드러짐\n    - SUV 라인업 확대 필요\n",
        "경기도 성남시": "\n\n- 1. 40대 초반과 50대 중후반 : 주 타겟층\n  - 중형 세단 선호\n- 2. 40대 이상의 연령대에서 주된 구매 수요를 보임\n  - 준중형/중형 세단 선호도 높음\n- 3. 30대 이하의 연령대에서 차량 구매 수요가 낮은 편\n  - 저가 전략 혹은 젊은 세대를 위한 마케팅 필요\n",
        "충청남도 천안시": "\n\n- 1. 40대 후반 : 주 타겟층\n    - 준중형 세단/해치백 선호\n- 2. 전반적인 수요가 높지 않음\n    - 사람들의 차량 구매를 유도할 수 있는 마케팅 필요\n"
    }

    strategy = {
        "서울특별시": "\n\n- SNS 광고\n     - 20대를 위한 YOUNG 마케팅이 필요\n     - 다른 연령대를 위한 차량 라인업 홍보 역시 SNS 통해 실시\n- 중형 SUV/세단 라인업 확대\n   - 전 연령대에서의 활발한 구매 촉진을 위해 판매량이 높은 차량 라인업 확대에 집중\n",
        "경기도 수원시": "\n\n- 전통적 미디어(신문, TV 등)를 통한 광고\n     - 40대와 60대를 위한 패밀리카 마케팅이 필요\n- 준중형 세단 라인업 확대\n     - 판매량이 높은 세단의 장점을 강조하는 마케팅\n",
        "울산광역시": "\n\n- 패밀리카 및 SUV 라인업 홍보\n     - 30대와 50대를 위한 SUV 위주 마케팅 필요\n- SUV 라인업 확대 필요\n    - SUV의 선호도가 높은 만큼 라인업 확대로 판매량 증대 가능\n",
        "경기도 성남시": "\n\n- 40대와 50대를 위해 친숙한 이미지 강조하는 마케팅\n   - 현대자동차의 익숙하면서도 안정적인 이미지 강조\n  - 중형 세단 라인업 홍보\n- 젊은 세대를 위한 저가 전략 마케팅\n   - 30대 이하 연령대의 저조한 구매 수요를 증대하기 위한 전략 필요\n",
        "충청남도 천안시": "\n\n- 차량 구매 유도를 위한 저가/할인 마케팅 전략\n    - 전반적으로 차량 구매 수요가 그리 높지 않기 때문에 이를 유도하기 위해 할인 혜택 마케팅 필요\n- 디자인/성능 등에서 사람들의 이목을 끌 수 있는 마케팅\n    - 차량에 관심이 낮은 사람들의 차량 구매 관심도를 조금이나마 높일 수 있는 방안\n"
    }

    col1, col2 = st.columns([1, 1])
    with col1:
        # 지역의 나이대에 따른 선호 차량 사이즈 및 유형
        # 해당 지역만 추출
        city = df.loc[df["거주 지역"] == region, :]

        # 연령대별 선호 차량 사이즈 및 유형 집계
        size_counts = city.groupby("연령대")["차량 사이즈"].value_counts().unstack()
        type_counts = city.groupby("연령대")["차량 유형"].value_counts().unstack()

        if region != "-":
            # 시각화 - 연령대별 선호 차량 사이즈
            fig, ax = plt.subplots(figsize=(10, 5))
            size_counts.plot(kind="bar", stacked=True, colormap="viridis", alpha=0.85, ax=ax)

            ax.set_title(f"{region} 연령대별 선호 차량 사이즈")
            ax.set_xlabel("연령대")
            ax.set_ylabel("선호 차량 수")
            ax.legend(title="차량 사이즈")
            ax.set_xticklabels(size_counts.index, rotation=60)
            ax.grid(axis="y", linestyle="--", alpha=0.7)

            st.pyplot(fig)        

            st.write("")

            st.write("📢 **분석 결과**:", analysis[region])
    with col2:
        if region != "-":
            # 시각화 - 연령대별 선호 차량 유형
            fig, ax = plt.subplots(figsize=(10, 5))
            type_counts.plot(kind="bar", stacked=True, colormap="plasma", alpha=0.85, ax=ax)

            ax.set_title(f"{region} 연령대별 선호 차량 유형")
            ax.set_xlabel("연령대")
            ax.set_ylabel("선호 차량 수")
            ax.legend(title="차량 유형")
            ax.set_xticklabels(type_counts.index, rotation=60)
            ax.grid(axis="y", linestyle="--", alpha=0.7)

            st.pyplot(fig)

            st.write("")

            st.write("🚀 **잠재적 마케팅 전략**:", strategy[region])
    if region != "-":
        st.text("")

        st.session_state['search_query'] = region

        # '4_매장_찾기.py'로 이동하는 링크 제공
        st.page_link("pages/4_매장_찾기🗺️.py", label="지점 및 정비소 찾기", icon="🛞")

        st.markdown("---")

        # 주요 지역 선택
        st.markdown("## 주요 지역별 차량 구매 분석 & 맞춤형 마케팅 전략")
        st.write("주요 지역별 차량 구매 성향을 분석하고 맞춤형 마케팅 전략을 제시합니다.")

        # 주요 지역별 고객 분석 데이터
        analysis = {
            "서울특별시": """
            - 1. 20대 중반이 가장 많이 구매 : 주 타겟층
            - 선호 차량 유형 : 중형 SUV/세단
            - 2. 전 연령대에 걸쳐 판매 가능성 : 40대부터 60대까지 꾸준한 소비
            - 선호 차량 유형 : 중형 SUV/세단
            - 3. 이미 130개 이상의 대리점/지점 존재
            - 전시장 확대보다는 더욱 다양한 차량 라인업 제공이 필요
            """,
            "경기도 수원시": """
            - 1. 40대 초반과 60대 중반이 가장 많이 구매 : 주 타겟층
            - 선호 차량 유형 : 준중형 세단
            - 2. 전반적으로 중형~준중형 사이즈 차량 수요 높음
            - 차종 역시 세단 선호도가 높음
            """,
            "울산광역시": """
            - 1. 30대 후반과 50대 중반 : 주 타겟층
            - 중형 SUV 선호
            - 2. 비교적 전 연령대에서 고른 구매 수요를 보임
            - 중형 SUV 및 세단 선호도 높음
            - 3. SUV의 선호도가 타지역에 비해 두드러짐
            - SUV 라인업 확대 필요
            """,
            "경기도 성남시": """
            - 1. 40대 초반과 50대 중후반 : 주 타겟층
            - 중형 세단 선호
            - 2. 40대 이상의 연령대에서 주된 구매 수요를 보임
            - 준중형/중형 세단 선호도 높음
            - 3. 30대 이하의 연령대에서 차량 구매 수요가 낮은 편
            - 저가 전략 혹은 젊은 세대를 위한 마케팅 필요
            """,
            "충청남도 천안시": """
            - 1. 40대 후반 : 주 타겟층
            - 준중형 세단/해치백 선호
            - 2. 전반적인 수요가 높지 않음
            - 사람들의 차량 구매를 유도할 수 있는 마케팅 필요
            """
        }

        # 주요 지역별 마케팅 전략 데이터
        strategy = {
            "서울특별시": """
            - SNS 광고
            - 20대를 위한 YOUNG 마케팅이 필요
            - 다른 연령대를 위한 차량 라인업 홍보 역시 SNS 통해 실시
            - 중형 SUV/세단 라인업 확대
            - 전 연령대에서의 활발한 구매 촉진을 위해 판매량이 높은 차량 라인업 확대에 집중
            """,
            "경기도 수원시": """
            - 전통적 미디어(신문, TV 등)를 통한 광고
            - 40대와 60대를 위한 패밀리카 마케팅이 필요
            - 준중형 세단 라인업 확대
            - 판매량이 높은 세단의 장점을 강조하는 마케팅
            """,
            "울산광역시": """
            - 패밀리카 및 SUV 라인업 홍보
            - 30대와 50대를 위한 SUV 위주 마케팅 필요
            - SUV 라인업 확대 필요
            - SUV의 선호도가 높은 만큼 라인업 확대로 판매량 증대 가능
            """,
            "경기도 성남시": """
            - 40대와 50대를 위해 친숙한 이미지 강조하는 마케팅
            - 현대자동차의 익숙하면서도 안정적인 이미지 강조
            - 중형 세단 라인업 홍보
            - 젊은 세대를 위한 저가 전략 마케팅
            - 30대 이하 연령대의 저조한 구매 수요를 증대하기 위한 전략 필요
            """,
            "충청남도 천안시": """
            - 차량 구매 유도를 위한 저가/할인 마케팅 전략
            - 전반적으로 차량 구매 수요가 그리 높지 않기 때문에 이를 유도하기 위해 할인 혜택 마케팅 필요
            - 디자인/성능 등에서 사람들의 이목을 끌 수 있는 마케팅
            - 차량에 관심이 낮은 사람들의 차량 구매 관심도를 조금이나마 높일 수 있는 방안
            """
        }

        # 선택한 주요 지역의 분석 및 전략 출력
        st.markdown("---")
        st.subheader(f"{region} 고객 분석")
        st.markdown(analysis[region])

        st.markdown("---")
        st.subheader(f"{region} 맞춤형 마케팅 전략")
        st.markdown(strategy[region])

        # 추가 마케팅 캠페인 제안
        st.markdown("---")
        st.subheader(f"{region} 맞춤형 마케팅 캠페인 제안")

        campaign_ideas = {
            "서울특별시": "- 인플루언서 협업을 통한 젊은 층 타겟팅\n- SNS 챌린지를 활용한 브랜드 인지도 향상\n- 최신 모델 체험 이벤트 진행",
            "경기도 수원시": "- 가족 단위 구매자 대상 패밀리카 패키지 할인 제공\n- 지역 신문 및 라디오 광고 활용\n- 시승 행사 개최를 통한 차량 직접 체험 기회 제공",
            "울산광역시": "- SUV 시승 이벤트 및 오프로드 체험 행사 개최\n- 지역 유통점 및 자동차 매장과 협업하여 공동 마케팅 진행\n- 친환경 차량 프로모션으로 시장 확대",
            "경기도 성남시": "- 40대 이상 타겟 고객을 위한 금융 프로그램 제공\n- 지역 기반 고객 대상 특별 리워드 프로그램 도입\n- 저가형 모델 한정 프로모션 이벤트 실행",
            "충청남도 천안시": "- 지역 페스티벌 및 행사에서 차량 전시 및 체험 공간 제공\n- 저가 모델의 혜택 강조한 디지털 광고 캠페인\n- 구매 유도를 위한 장기 할부 옵션 및 보조금 지원 홍보"
        }

        st.markdown(campaign_ideas[region])

        st.markdown("---")
        st.write("**지역별 맞춤형 마케팅 전략을 활용하여 효과적인 시장 공략이 가능합니다!**")
        
elif marketing_class == "연령대별":
    # 연료 구분 정렬 순서 지정
    fuel_order = ["전기", "하이브리드", "플러그인 하이브리드", "휘발유", "디젤", "수소"]
    
    age_order = ["20대 초반", "20대 중반", "20대 후반", "30대 초반", "30대 중반", "30대 후반", "40대 초반", "40대 중반", "40대 후반",
              "50대 초반", "50대 중반", "50대 후반", "60대 초반", "60대 중반", "60대 후반", "70대 초반"]

    df["연료 구분"] = pd.Categorical(df["연료 구분"], categories=fuel_order, ordered=True)
    df["연령대"] = pd.Categorical(df["연령대"], categories=age_order, ordered=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        # 데이터 그룹화 및 시각화를 위한 준비
        age_df = df.groupby(["연령대", "연료 구분"])["연번"].count().unstack()

        fig, ax = plt.subplots(figsize=(12, 8))
        age_df.reindex(columns=fuel_order).plot(kind="barh", stacked=True, ax=ax)

        ax.set_title("연령대별 판매 차량 유형")
        ax.set_xlabel("판매 대수")
        ax.set_ylabel("연령대")

        st.pyplot(fig)

    with col2:
        size_counts = df.groupby("최근 구매 연도")["고객 등급"].value_counts().unstack().fillna(0)

        # 시각화 - 고객 등급별 최근 차량 구매 연도
        fig, ax = plt.subplots(figsize=(10, 5))

        size_counts.plot(kind="line", marker="o", colormap="viridis", alpha=0.85, ax=ax)

        ax.set_xticks(size_counts.index)
        ax.set_xticklabels(size_counts.index, rotation=0)

        ax.set_title(f"연도별 차량 구매 건수")
        ax.set_xlabel("연도")
        ax.set_ylabel("선호 차량 수")
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        st.pyplot(fig)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("""
        **분석 결과**  
        - 휘발유 차량의 높은 점유율  
            - 전 연령대에서 휘발유 차량이 가장 많이 판매됨  
            - 특히 40대 초반~50대 초반 연령대에서 가장 큰 비중을 차지  
        - 디젤 차량의 강세  
            - 60대 후반~70대 초반의 고연령층에서 디젤 차량이 높은 비중을 차지  
            - 젊은 연령층으로 갈수록 디젤 차량의 비중이 점차 감소하는 경향  
        - 수소 차량의 점유율 증가  
            - 50대 이상 연령층에서 수소차 비중이 높은 편  
            - 20~30대에서는 수소 차량이 상대적으로 적음
        - 젊은 층의 전기차/하이브리드 구매  
            - 젊은 층 (20~30대)에서만 일부 판매  
            - 연령대가 올라갈수록 전기차 및 하이브리드 판매 비율이 줄어듦
        """)
    with col2:
        st.write("""
        **분석 결과**
        - 일반 고객의 감소와 VIP 고객의 증가
            - 일반 고객의 감소는 기존 일반 고객의 신규 차량 구매가 활발하다는 의미
            - 차량 재구매 시 혜택을 더욱 확대할 필요가 있음
        - 신규 고객 유입 증가
            - 신규 고객의 지속적인 유입을 위한 마케팅 전략 필요
        """)

    st.subheader("")

    # 타겟 연령대 선택
    st.subheader("🎯 연령대별 마케팅 전략")

    age_group = st.selectbox("타겟 연령대 선택", ["-", "20대", "30대", "40대", "50대", "60대 이상"])

    # 연령대에 따른 마케팅 전략 추천
    analysis = {
        "20대": "\n\n- 1. 중형 세단/SUV 선호\n- 2. 전기 및 하이브리드 차량의 선호도가 낮음\n    - 연비보다는 주행 성능이나 연료 충전 편의성을 더 중요하게 생각할 가능성\n- 3.	대형 및 해치백 차량은 인기가 낮음\n    - 가격, 실용성, 유지 비용 등의 요인이 반영된 결과\n",
        "30대": "\n\n- 1. 중형 SUV 선호\n    - SUV에서 친환경 연료(수소) 선호도 증가\n- 2. 프리미엄 및 대형 차량 수요 증가\n    - 경제적인 여유 확보로 인한 결과물로 보임\n",
        "40대": "\n\n- 1.중형과 대형 차량 선호\n     - 중형 차량 중 수소 연료 선호도 높음 (친환경 차량 수요 증가)\n      - 패밀리카, 브랜드 가치, 유지비 등을 고려하는 구매 경향\n- 2. 해치백은 거의 선택되지 않음\n    - 주행 안전성과 실내 공간을 고려하는 성향\n",
        "50대": "\n\n- 1. 친환경 연료(수소, 하이브리드) 선호도 다른 연령대에 비해 높음\n     - 연료 효율성과 유지비 절감을 고려하여 하이브리드 및 플러그인 하이브리드 선택 증가\n",
        "60대 이상": "\n\n- 1. 타 연령대에 비해 높은 디젤 선호도\n   - 디젤 차량의 연료 효율성 및 주행 안정성을 중시하는 경향\n    - 디젤 차량의 승차감에 익숙한 장년층의 특성이 반영됨\n- 2. 전기 및 하이브리드 차량의 선호도 낮음\n   - 전기 및 하이브리드 차량의 충전 인프라 부족 및 주행 거리 등의 문제로 인한 선호도 저하\n"
    }

    strategy = {
        "20대": "\n\n- 전기 및 하이브리드 차량의 장점을 강조하는 마케팅 전략\n   - 보조금 및 충전 인프라 홍보 필요\n- 중형 세단/SUV 라인업 확대\n    - 중형 세단/SUV의 선호도가 높은 만큼 라인업 확대로 판매량 증대 가능\n- 대형 및 해치백 차량 저가 모델 출시\n    - 저가형 대형 및 해치백 차량 출시로 인기 증대 가능",
        "30대": "\n\n- 중형 SUV 라인업 확대\n    - 중형 SUV의 선호도가 높은 만큼 라인업 확대로 판매량 증대 가능\n- 프리미엄 및 대형 차량 라인업 확대\n    - 경제적 여유가 있는 30대를 위한 프리미엄 및 대형 차량 라인업 확대 필요",
        "40대": "\n\n- 수소 연료 차량 홍보\n     - 수소 연료 차량의 친환경성을 강조하는 마케팅\n- 패밀리카 및 브랜드 가치 강조\n     - 친숙한 이미지 기반으로 패밀리어 마케팅 실시\n- 대형 및 해치백 차량 홍보 확대\n    - 카고 공간 및 주행 안전성을 강조하는 패밀리 마케팅 전략",
        "50대": "\n\n- 친환경 연료 차량 홍보\n     - 친환경 연료의 장점을 강조하는 마케팅 전략\n- 연료 효율성 및 유지비 절감을 강조하는 마케팅\n     - 연료 효율성 및 유지비 절감을 강조하는 마케팅 전략\n- 수소 및 하이브리드 차량 라인업 확대\n    - 친환경 연료 차량의 선호도가 높은 만큼 라인업 확대로 판매량 증대 가능",
        "60대 이상": "\n\n- 디젤 차량 홍보\n    - 디젤 차량의 연료 효율성 및 주행 안정성을 강조하는 마케팅 전략\n- 전기 및 하이브리드 차량의 장점을 강조하는 마케팅\n    - 전기 및 하이브리드 차량의 장점을 강조하는 마케팅 전략\n     - 디젤 차량 이용 시 환경 부담금 발생한다는 점 강조"
    }

    # 연령대에 따른 선호 차량 사이즈 및 유형
    # 해당 연령대만 추출
    if age_group == "60대 이상":
        gen = df.loc[(df["연령대"].str.split(" ").str[0]).isin(["60대", "70대"]), :]
    else:
        gen = df.loc[df["연령대"].str.split(" ").str[0] == age_group, :]

    # 고객 등급별 선호 차량 사이즈 및 유형 집계
    size_counts = gen.groupby("차량 사이즈")["연료 구분"].value_counts().unstack()
    type_counts = gen.groupby("차량 유형")["연료 구분"].value_counts().unstack()

    col1, col2 = st.columns([1, 1])
    with col1:
        if age_group != "-":
            # 시각화 - 고객 등급별 선호 차량 사이즈
            fig, ax = plt.subplots(figsize=(10, 5))
            size_counts.plot(kind="bar", stacked=True, colormap="viridis", alpha=0.85, ax=ax)

            ax.set_title(f"{age_group} 고객 등급별 선호 차량 사이즈")
            ax.set_xlabel("차량 사이즈")
            ax.set_ylabel("선호 차량 수")
            ax.legend(title="연료 구분")
            ax.set_xticklabels(size_counts.index, rotation=0)
            ax.grid(axis="y", linestyle="--", alpha=0.7)

            st.pyplot(fig)

            st.write("")
            st.write("📢 **분석 결과**:", analysis[age_group])
    with col2:
        if age_group != "-":
            # 시각화 - 고객 등급별 선호 차량 유형
            fig, ax = plt.subplots(figsize=(10, 5))
            type_counts.plot(kind="bar", stacked=True, colormap="plasma", alpha=0.85, ax=ax)

            ax.set_title(f"{age_group} 고객 등급별 선호 차량 유형")
            ax.set_xlabel("차량 유형")
            ax.set_ylabel("선호 차량 수")
            ax.legend(title="연료 구분")
            ax.set_xticklabels(type_counts.index, rotation=0)
            ax.grid(axis="y", linestyle="--", alpha=0.7)

            st.pyplot(fig)

            st.write("")
            st.write("🚀 **잠재적 마케팅 전략**:", strategy[age_group])

    st.write("")
    st.markdown("---")
    
    if age_group != "-":
        #  연령대 선택
        st.markdown("## 연령대별 차량 구매 분석 & 맞춤형 마케팅 전략")
        st.write("연령대별 차량 구매 성향을 분석하고 맞춤형 마케팅 전략을 제시합니다.")

        #  연령대별 고객 분석 데이터
        analysis = {
            "20대": """
            - 1️⃣ **중형 세단 & SUV 선호**  
            - 2️⃣ **전기 및 하이브리드 차량 선호도 낮음**  
            - 연비보다는 **주행 성능 및 충전 편의성**을 더 중요하게 생각하는 경향  
            - 3️⃣ **대형 및 해치백 차량 선호도 낮음**  
            - 가격, 실용성, 유지 비용 등을 고려하는 구매 패턴  
            """,
            "30대": """
            - 1️⃣ **중형 SUV 선호 & 수소 연료 관심 증가**  
            - 2️⃣ **프리미엄 & 대형 차량 수요 증가**  
            - 경제적 여유 확보로 인해 **고급 브랜드 선호도 증가**  
            """,
            "40대": """
            - 1️⃣ **중형 & 대형 차량 선호**  
            - **가족 차량으로 SUV 및 세단 인기**  
            - **수소 연료에 대한 관심 증가** (친환경 차량 수요 확대)  
            - 2️⃣ **해치백 차량은 거의 선택되지 않음**  
            - 주행 안전성과 실내 공간을 고려하는 경향  
            """,
            "50대": """
            - 1️⃣ **친환경 연료 (수소, 하이브리드) 선호 증가**  
            - 연료 효율성과 유지비 절감을 고려하는 경향  
            """,
            "60대 이상": """
            - 1️⃣ **디젤 차량 선호도 높음**  
            - 연료 효율성 및 주행 안정성을 중요하게 고려  
            - 기존 디젤 차량 운전 습관 유지 경향  
            - 2️⃣ **전기 및 하이브리드 차량 선호도 낮음**  
            - 충전 인프라 부족 및 주행 거리 문제로 인해 거부감 있음  
            """
        }

        #  연령대별 마케팅 전략 데이터
        strategy = {
            "20대": """
            - **전기 및 하이브리드 차량 마케팅 강화**  
            - 보조금 및 충전 인프라 개선 홍보  
            - **중형 세단/SUV 라인업 확대**  
            - 20대의 선호도가 높은 만큼 라인업 확대로 판매량 증대  
            - **합리적인 가격 및 금융 혜택 제공**  
            - **20대 경제적 부담 완화**를 위한 **무이자 할부 및 리스 프로그램 운영**  
            """,
            "30대": """
            - **프리미엄 & 대형 차량 마케팅 확대**  
            - **고급 브랜드 진입 유도** (G70, G80 등)  
            - **SUV 친환경 모델 홍보**  
            - **NEXO(수소차)** 및 **하이브리드 SUV 홍보**  
            """,
            "40대": """
            - **패밀리카 & 친환경 SUV 홍보**  
            - 브랜드 가치, 유지비 절감 강조  
            - **수소 연료 차량 캠페인 진행**  
            - 친환경 차량 구매 혜택 홍보  
            """,
            "50대": """
            - **친환경 하이브리드 차량 홍보**  
            - 연료 효율성과 유지비 절감 강조  
            - **고급 세단 & SUV 프로모션**  
            - 50대 이상 고객을 위한 맞춤형 VIP 서비스 제공  
            """,
            "60대 이상": """
            - **디젤 차량의 경제성 강조**  
            - 주행 안정성 및 연료 효율성 홍보  
            - **전기차 및 하이브리드 차량 전환 유도**  
            - 환경 부담금, 보조금 혜택 홍보  
            """
        }

        #  선택한 연령대의 분석 및 전략 출력
        st.markdown("---")
        st.subheader(f" {age_group} 고객 분석")
        st.markdown(analysis[age_group])

        st.markdown("---")
        st.subheader(f" {age_group} 맞춤형 마케팅 전략")
        st.markdown(strategy[age_group])

        #  추가 마케팅 캠페인 제안
        st.markdown("---")
        st.subheader(f" {age_group} 맞춤형 마케팅 캠페인 제안")

        if age_group == "20대":
            st.write("""
            **SNS 마케팅 & 트렌디한 광고**  
            - 유튜브, 인스타그램을 통한 **젊은 감성의 광고 캠페인**  
            - **인플루언서 & 유명 유튜버 협업 진행**  
            """)

        elif age_group == "30대":
            st.write("""
            **프리미엄 브랜드 캠페인**  
            - 30대 소비자에게 G70, G80 등 **럭셔리 브랜드의 가치를 강조**  
            - **가족 중심 SUV 광고 캠페인 진행**  
            """)

        elif age_group == "40대":
            st.write("""
            **친환경 차량 & 패밀리카 중심 마케팅**  
            - **하이브리드 & 전기차 보조금 혜택 홍보**  
            - **패밀리카 중심 브랜드 가치 강조**  
            """)

        elif age_group == "50대":
            st.write("""
            **하이브리드 & 대형 SUV 캠페인**  
            - **연비 절감 효과 홍보**  
            - **VIP 서비스 & 유지보수 혜택 강조**  
            """)

        elif age_group == "60대 이상":
            st.write("""
            **디젤 & 하이브리드 차량 홍보**  
            - **경제성 & 유지비 절감 효과 홍보**  
            - **전기차 전환 유도 캠페인 진행**  
            """)

        st.markdown("---")
        st.write(" **연령대별 맞춤형 마케팅 전략을 활용하여 효과적인 시장 공략이 가능합니다!** ")

elif marketing_class == "고객 등급별":
    marketing_order = ["신규", "일반", "VIP"]
    fuel_order = ["전기", "하이브리드", "플러그인 하이브리드", "휘발유", "디젤", "수소"]
    size_order = ["준중형", "중형", "준대형", "대형", "프리미엄"]

    df["고객 등급"] = pd.Categorical(df["고객 등급"], categories=marketing_order, ordered=True)
    df["연료 구분"] = pd.Categorical(df["연료 구분"], categories=fuel_order, ordered=True)
    df["차량 사이즈"] = pd.Categorical(df["차량 사이즈"], categories=size_order, ordered=True)

    # 데이터 그룹화 및 시각화를 위한 준비
    grade_df = df.groupby(["고객 등급", "연료 구분"])["연번"].count().unstack()
    seg_df = df.groupby(["고객 등급", "차량 사이즈"])["연번"].count().unstack()

    col1, col2 = st.columns([1, 1])
    with col1:
        fig, ax = plt.subplots(figsize=(12, 8))
        grade_df.reindex(columns=fuel_order).plot(kind="bar", stacked=True, ax=ax)

        ax.set_title("고객 등급별 판매 차량의 연료 구분")
        ax.set_xlabel("고객 등급")
        ax.set_ylabel("판매 대수")
        ax.set_xticklabels(grade_df.index, rotation=0)

        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(12, 8))
        seg_df.reindex(columns=size_order).plot(kind="bar", stacked=True, ax=ax)

        ax.set_title("고객 등급별 판매 차량 유형")
        ax.set_xlabel("판매 대수")
        ax.set_ylabel("연령대")
        ax.set_xticklabels(seg_df.index, rotation=0)

        st.pyplot(fig)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("""
        **분석 결과**  
    - 전반적으로 낮은 하이브리드 차량 구매율  
        - 일반 고객은 하이브리드, 플러그인 하이브리드 차량도 상대적으로 많이 구매  
        - VIP 고객은 친환경 차량을 거의 선택하지 않음  
            - 높은 유지 비용과 성능 등의 요인이 반영된 결과  
    - 신규 고객은 친환경 차량을 거의 선택하지 않음  
        - 차량 신규 구매 고객의 경우 성능과 내구성을 가장 중요하게 생각하는 경향
        """)
    with col2:
        st.write("""
    **분석 결과**  
- 모든 고객 등급에서 중형 차량이 가장 많이 판매  
    - 준중형 및 대형 차량 수요도 높은 편  
- 전반적으로 친환경 차량에 대한 수요가 낮음
    - 친환경 차량의 이미지 개선과 성능 향상이 필요한 시점  
    - 이에 대한 적극적인 마케팅과 홍보가 필요  
    - 친환경 차량 판매에 대한 국가적 지원 역시 유치 가능할 것으로 보임
    """)

    st.subheader("")

    # 타겟 고객 등급 선택
    st.subheader("🎯 고객 등급별 마케팅 전략")

    grade = st.selectbox("타겟 고객 등급 선택", ["-", "신규", "일반", "VIP"])

    # 연령대에 따른 마케팅 전략 추천
    analysis = {
        "신규": "\n\n- 1. 하이브리드 차량 선호도 매우 낮음\n    - 연료 효율성 및 유지비 절감을 중시하는 경향\n- 2. 해치백 구매 수요 없음\n    - 주행 안정성 및 실내 공간을 중시하는 경향이 반영됨\n",
        "일반": "\n\n- 1. 비교적 친환경/하이브리드 차량 수요가 높은 편\n- 2. 준대형 사이즈 차량에서는 플러그인 하이브리드 선호도 높음\n    - 유지비와 연료 효율성을 중시하는 경향\n",
        "VIP": "\n\n- 1. 중형 세단 선호도 높음\n    - 중형 세단의 안정성 및 승차감을 중시하는 경향\n- 2. 친환경 연료 차량에 비해 휘발유/디젤 선호도가 높음\n    - 친환경 연료 차량의 성능 및 안정성에 대한 의구심이 반영된 결과\n"
    }

    strategy = {
        "신규": "\n\n- 하이브리드 차량의 장점을 강조하는 마케팅\n    - 연료 효율성 및 유지비 절감을 중시하는 신규 고객을 위한 마케팅 전략\n- 해치백 라인업 확대\n    - 주행 안정성 및 실내 공간을 중시하는 신규 고객을 위한 저가형 해치백 라인업 확대\n",
        "일반": "\n\n- 중형/준중형 차량 할인 & 혜택 프로모션\n   - 하이브리드 & 플러그인 하이브리드 홍보 강화 (세금 혜택 & 충전 크레딧)\n   - 하이브리드 및 플러그인 하이브리드 차량의 연료 효율성 및 유지비 절감 마케팅\n- 일반 고객 맞춤형 금융 & 유지보수 서비스 제공\n",
        "VIP": "\n\n- 중형 & 세단 중심 프로모션\n   - 프리미엄 중형 & 세단 모델 업그레이드 패키지 제공\n    - 상위 트림(고급 옵션 포함) 프로모션\n- SUV 홍보 전략 필요\n    - SUV 모델의 연료 효율성 & 유지보수 혜택 강조\n"
    }

    # 고객 등급에 따른 선호 차량 사이즈 및 유형
    # 해당 고객 등급만 추출
    seg = df.loc[df["고객 등급"] == grade, :]

    # 고객 등급별 선호 차량 사이즈 및 유형 집계
    size_counts = seg.groupby("차량 사이즈")["연료 구분"].value_counts().unstack()
    type_counts = seg.groupby("차량 유형")["연료 구분"].value_counts().unstack()

    col1, col2 = st.columns([1, 1])
    with col1:
        if grade != "-":
            # 시각화 - 고객 등급별 선호 차량 사이즈
            fig, ax = plt.subplots(figsize=(10, 5))
            size_counts.plot(kind="bar", stacked=True, colormap="viridis", alpha=0.85, ax=ax)

            ax.set_title(f"{grade} 고객 선호 차량 사이즈")
            ax.set_xlabel("차량 사이즈")
            ax.set_ylabel("선호 차량 수")
            ax.legend(title="연료 구분")
            ax.set_xticklabels(size_counts.index, rotation=0)
            ax.grid(axis="y", linestyle="--", alpha=0.7)

            st.pyplot(fig)

            st.write("")
            st.write("📢 **분석 결과**:", analysis[grade])
    with col2:
        if grade != "-":
            # 시각화 - 고객 등급별 선호 차량 유형
            fig, ax = plt.subplots(figsize=(10, 5))
            type_counts.plot(kind="bar", stacked=True, colormap="plasma", alpha=0.85, ax=ax)

            ax.set_title(f"{grade} 고객 선호 차량 유형")
            ax.set_xlabel("차량 유형")
            ax.set_ylabel("선호 차량 수")
            ax.legend(title="연료 구분")
            ax.set_xticklabels(type_counts.index, rotation=0)
            ax.grid(axis="y", linestyle="--", alpha=0.7)

            st.pyplot(fig)

            st.write("")
            st.write("🚀 **잠재적 마케팅 전략**:", strategy[grade])
    
    st.markdown("---")

    if grade == "신규":
        # 🚗 신규 고객 맞춤형 서비스
        st.markdown("## 🚗 신규 고객 웰컴 패키지 & 서비스 혜택")
        st.write("처음 차량을 구매한 고객에게 특별한 웰컴 혜택을 제공합니다! 🎁")
        
        # 💰 신규 고객의 누적 소비 금액 입력
        purchase_amount = st.number_input("🔢 누적 소비 금액 입력 (단위: 만 원)", min_value=0, step=100, value=3000)

        st.markdown("---")

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
            st.info("각 고객에게 혜택 안내 이메일을 전송 중입니다. 잠시만 기다려주세요.")
            
            progress_bar = st.progress(0)
            for percent in range(1, 101):
                time.sleep(0.01)  # 실제 전송 과정에서는 API 호출 등이 이루어질 수 있음
                progress_bar.progress(percent)
            
            st.success("✅ 모든 고객에게 할인 혜택 안내 이메일을 성공적으로 전송하였습니다.")
        if sms_sent:
            st.info("각 고객에게 혜택 안내 문자를 전송 중입니다. 잠시만 기다려주세요.")
            
            progress_bar = st.progress(0)
            for percent in range(1, 101):
                time.sleep(0.01)  # 실제 전송 과정에서는 API 호출 등이 이루어질 수 있음
                progress_bar.progress(percent)
            
            st.success("✅ 모든 고객에게 할인 혜택 안내 문자를 성공적으로 전송하였습니다.")

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

        # 🚗 신규 회원 세미나 프로모션 안내
        st.subheader("🎓 신규 고객 전용 세미나 프로모션")
        st.write("""
        🚀 **신규 고객을 위한 특별한 기회!**  
        처음 차량을 구매한 고객님들을 위해 차량 관리, 정비, 금융 상담 등 다양한 주제의 **프리미엄 세미나**를 무료로 제공합니다.  
        """)

        st.write("")

        st.markdown("""
        #### 📢 신규 회원 전용 세미나 혜택 🎉
        ✅ **전문가와 함께하는 실전 강의**  
        ✅ **차량 유지보수 및 관리 노하우 전수**  
        ✅ **최신 차량 기술 및 친환경 운전법 안내**  
        ✅ **프리미엄 차량 시승 체험 가능!**  
        ✅ **신청자 전원 특별 웰컴 기프트 제공 🎁**
        """)

        st.markdown("---")

        seminar_data = {
            "세미나 제목": [
                "차량 관리 워크숍", "정비 팁 세미나", "안전 운전 강의", "차량 관리 워크숍", "정비 팁 세미나",
                "고객 Q&A 세션", "신제품 소개", "고급 차량 유지보수 가이드", "신제품 소개", "고급 차량 유지보수 가이드", 
                "연비 절약 및 친환경 운전법", "고객 맞춤형 금융 상담", "자동차 보험의 모든 것", "프리미엄 차량 시승 체험"
            ],
            "시작일": [
                "2025-03-20 09:30", "2025-03-20 11:00", "2025-03-20 14:00", "2025-03-21 12:30", "2025-03-21 09:30", "2025-03-20 14:00",
                "2025-03-21 10:00", "2025-03-21 13:00", "2025-03-22 16:00", "2025-03-22 09:00", "2025-03-21 13:00", "2025-03-22 09:00",
                "2025-03-22 12:00", "2025-03-22 15:00"
            ],
            "종료일": [
                "2025-03-20 12:00", "2025-03-20 15:30", "2025-03-20 16:30", "2025-03-21 16:00", "2025-03-21 15:30", "2025-03-20 17:00",
                "2025-03-21 12:30", "2025-03-21 15:30", "2025-03-22 18:00", "2025-03-22 15:30", "2025-03-21 16:00", "2025-03-22 15:30",
                "2025-03-22 14:00", "2025-03-22 18:30"
            ],
            "진행 방식": [
                "온라인", "오프라인", "온라인", "온라인", "오프라인",
                "오프라인", "온라인", "오프라인", "온라인", "오프라인",
                "온라인", "온라인", "오프라인", "오프라인"
            ],
            "장소": [
                "Zoom 미팅", "서울 강남 컨퍼런스룸", "Webex", "부산 해운대 센터", "대구 동성로 서비스센터",
                "서울 강북 서비스센터", "Zoom 미팅", "부산 VIP 라운지", "Webex", "인천 서구 컨퍼런스룸",
                "Teams", "Teams", "성남 모란 컨퍼런스룸", "서울 강남 프리미엄 쇼룸"
            ],
            "잔여석": [10, 5, 3, 8, 7, 0, 6, 9, 2, 5, 7, 3, 1, 0],
            "세미나 설명": [
                "🚗 차량 관리 기본 지식 및 유지보수 팁 제공 (오일 교체, 타이어 관리 등 필수 정보 포함)",
                "🛠️ 정비 전문가와 함께하는 실전 팁 공개 (고객이 직접 체험할 수 있는 워크샵 진행)",
                "🚦 안전 운전을 위한 핵심 가이드 및 사고 예방 교육 (야간 운전, 비상 시 대처 방법 포함)",
                "🚗 차량 관리 기본 지식 및 유지보수 팁 제공 (오일 교체, 타이어 관리 등 필수 정보 포함)",
                "🛠️ 정비 전문가와 함께하는 실전 팁 공개 (고객이 직접 체험할 수 있는 워크샵 진행)",
                "❓ 실시간 Q&A를 통해 궁금증 해결 (자동차 구매, 정비, 금융 관련 질문 가능)",
                "🆕 신제품의 주요 기능 및 활용법 소개 (최신 차량 모델 및 혁신 기술 설명)",
                "🔧 고급 차량 유지보수 가이드 (고급 브랜드 차량 유지 및 관리법 심층 강의)",
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

        # 📌 세미나 제목 선택
        selected_seminar = st.selectbox("참여하고 싶은 세미나를 선택하세요", df_seminar["세미나 제목"].unique().tolist())

        # 해당 세미나의 가능한 일정을 필터링
        seminar_options = df_seminar[df_seminar["세미나 제목"] == selected_seminar]
        date_options = seminar_options["시작일"].dt.strftime('%Y-%m-%d %H:%M').tolist()

        # 📅 세미나 일시 선택
        selected_date = st.selectbox("참여하고 싶은 세미나 일시를 선택하세요", date_options)

        # 선택한 일시에 해당하는 세미나 정보 가져오기
        selected_row = seminar_options[seminar_options["시작일"].dt.strftime('%Y-%m-%d %H:%M') == selected_date].iloc[0]

        st.write("")

        # 📌 세미나 상세 정보 출력
        st.markdown("#### 📌 **세미나 상세 정보**")
        st.write(f"**ℹ️ 세미나 설명:** {selected_row['세미나 설명']}")
        st.write(f"**📅 일정:** {selected_row['시작일'].strftime('%Y-%m-%d %H:%M')} ~ {selected_row['종료일'].strftime('%H:%M')}")
        st.write(f"**📍 장소:** {selected_row['장소']}")
        st.write(f"**🪑 잔여석:** {selected_row['잔여석']}")

        # 신청하기 버튼 및 처리
        if selected_row["잔여석"] > 0:
            if st.button("✅ 신청하기"):
                st.success("✅ 신청 완료되었습니다!")
        else:
            st.warning("❌ 신청이 마감되었습니다. 다음 기회를 이용해주세요.")

        st.markdown("---")
        st.markdown("##### 🚀 신규 고객을 위한 다양한 서비스와 혜택을 계속해서 제공해드릴 예정입니다!")
    elif grade == "일반":
        # 🚗 일반 고객 대상 재구매 할인 혜택
        st.markdown("## 🚗 일반 고객 대상 재구매 할인 혜택 제공")
        st.write("재구매를 고려하는 고객을 위한 특별 할인 혜택을 제공합니다! 🎁")

        # 💰 일반 고객의 누적 구매 금액 입력
        purchase_amount = st.number_input("🔢 누적 구매 금액 입력 (단위: 만 원)", min_value=0, step=100, value=3000)
        st.markdown("---")

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


        # 📋 일반 고객 리스트
        st.subheader("📋 일반 고객 리스트")
        normal_client = df.loc[df["고객 등급"] == "일반", ["이름", "휴대폰 번호", "이메일"]]
        normal_client.reset_index(drop=True, inplace=True)
        st.dataframe(normal_client)

        st.markdown("---")

        # ✅ 일반 고객을 위한 추가 프로모션 상세 설명
        st.subheader("🎟️ 일반 고객을 위한 추가 프로모션")

        st.markdown("""
        1️⃣ **🚘 프리미엄 차량 시승 프로그램**
        - 고객이 관심 있는 **고급 차량을 최대 7일간 무료로 시승**할 수 있는 기회 제공
        - **페라리, 벤틀리, BMW M 시리즈 등 프리미엄 차량 포함**
        - 시승 후 **구매 결정 시 추가 할인 제공 (최대 5% 추가 할인)**
        - **트랙 주행 체험권 & 드라이빙 클래스 초청** 포함

        2️⃣ **🎤 일반 고객 전용 VIP 초청 행사**
        - **VIP 네트워킹 런치 초청**: 미슐랭 레스토랑에서 브랜드 대표 및 자동차 전문가와의 만남
        - **신차 발표 & 럭셔리 시승 이벤트 초대**: 새로운 모델을 누구보다 빠르게 체험할 기회
        - **자동차 전문가 & 유명 레이서와 함께하는 토크쇼**: 자동차 트렌드와 기술에 대한 심층 강의

        3️⃣ **🔧 서비스 패키지 업그레이드**
        - 일반 고객에게 **기본 차량 정비 패키지를 프리미엄 정비 패키지로 무료 업그레이드**
        - **🚗 무료 차량 픽업 & 정비 후 딜리버리 서비스 제공**
        - **1년간 엔진 오일 무상 교체 & 브레이크 패드 할인 제공**

        4️⃣ **🎁 한정판 굿즈 & 컬렉터블 아이템 제공**
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
    elif grade == "VIP":
        # VIP 고객 맞춤 프로모션 타이틀
        st.markdown("## VIP 고객 맞춤 프로모션 & 프라이빗 스케줄")
        st.write("VIP 고객을 대상으로 맞춤형 할인 혜택과 프라이빗 이벤트를 제공합니다.")

        #  VIP 고객의 누적 구매 금액 입력
        purchase_amount = st.number_input("🔢 누적 구매 금액 입력 (단위: 만 원)", min_value=0, step=100, value=5000)

        #  VIP 등급 결정 및 맞춤 혜택 제공
        if purchase_amount >= 30000:
            grade = "💎 Prestige VIP"
            discount = 12
            extra_benefits = "✨ 최고급 리무진 서비스 + 프라이빗 럭셔리 요트 디너 + 최고급 골프장 초청"
        elif purchase_amount >= 20000:
            grade = "🏆 Royal VIP"
            discount = 10
            extra_benefits = "💎 VIP 전용 라운지 + 프리미엄 가죽 시트 업그레이드 + 개인 맞춤 컨시어지 서비스"
        elif purchase_amount >= 10000:
            grade = "🌟 Exclusive VIP"
            discount = 7
            extra_benefits = "🎖️ VIP 전용 이벤트 초대 + 맞춤형 차량 시승 + 우선 예약 혜택"
        elif purchase_amount >= 5000:
            grade = "🔹 Premium Member"
            discount = 5
            extra_benefits = " VIP 전용 차량 보관 서비스 + 무료 정기 차량 점검"
        else:
            grade = "💼 일반 고객"
            discount = 0
            extra_benefits = "❌ 추가 혜택 없음"

        if purchase_amount >= 10000:
            format_purchase = format(purchase_amount, ",")
            purchase_1 = format_purchase[:-5] + "억 "
            purchase_2 = format_purchase[-5:] + "만 "
            if purchase_2.startswith("0"):
                if purchase_2 == "0,000만 ":
                    format_purchase = purchase_1
                else:
                    format_purchase = purchase_1 + purchase_2.lstrip("0,").lstrip("0")
            else:
                format_purchase = purchase_1 + purchase_2
        else:
            format_purchase = format(purchase_amount, ",") + "만 "

        # 프로모션 적용 결과 출력
        st.markdown("---")
        st.subheader(" VIP 고객 맞춤 프로모션 적용 결과")
        st.write(f"**누적 구매 금액:** {format_purchase}원")
        st.write(f"**고객 등급:** {grade}")
        st.write(f"**적용 할인율:** {discount}%")
        st.write(f"**추가 제공 혜택:** {extra_benefits}")

        #  할인 적용 후 예상 결제 금액 계산
        if discount > 0:
            final_price = round(purchase_amount * (1 - discount / 100))
            format_final = ""
            if final_price >= 10000:
                format_final = format(final_price, ",")
                final_1 = format_final[:-5] + "억 "
                final_2 = format_final[-5:] + "만 "
                if final_2.startswith("0"):
                    if final_2 == "0,000만 ":
                        format_final = final_1
                    else:
                        format_final = final_1 + final_2.lstrip("0,").lstrip("0")
                else:
                    format_final = final_1 + final_2
            else:
                format_final = format(final_price, ",") + "만 "
                
            st.write(f"**💰 할인 적용 후 예상 결제 금액:** {format_final}원")
        else:
            st.write("❌ 할인이 적용되지 않습니다.")

        st.markdown("---")
        st.markdown("### 🎉 **VIP 이상 고객만을 위한 맞춤형 컨시어지 서비스!** 😊")

        # VIP 프로모션 옵션 선택
        promotion = st.radio(" 원하는 VIP 프로모션을 선택하세요.", 
                            [" 프라이빗 차량 체험 패키지 ", 
                            " 차고지 예약 & 맞춤형 차량 보관 서비스 ",
                            " 익스클루시브 이벤트 & 개인 맞춤형 혜택 ",
                            " 커넥티드 라이프스타일 멤버십 "])

        #  1️⃣ VIP 전용 ‘프라이빗 차량 체험 패키지’
        if promotion == " 프라이빗 차량 체험 패키지 ":
            st.subheader(" 프라이빗 차량 체험 패키지 ")
            st.write("""
            **VIP 고객 전용 ‘프라이빗 테스트 드라이브’ 제공**
            - 특정 하이엔드 모델(제네시스, BMW, 벤츠, 포르쉐 등) 대상으로 진행  
            - VIP 고객이 관심 있는 차량을 **7일간 무료 체험 후 구매 결정 가능**  
            - 체험 후 구매할 경우 **최대 5% 추가 할인 혜택 제공**  
            """)

        #  2️⃣ VIP 전용 ‘차고지 예약 & 맞춤형 차량 보관 서비스’
        elif promotion == " 차고지 예약 & 맞춤형 차량 보관 서비스 ":
            st.subheader(" 차고지 예약 & 맞춤형 차량 보관 서비스 ")
            st.write("""
            **VIP 고객 전용 차량 보관 & 즉시 출고 서비스**
            - VIP 고객이 **자주 사용하는 차량을 사전 예약 후 차고지에 보관**  
            - 필요할 때 **즉시 차량을 출고할 수 있도록 대기 상태 유지**  
            **장기 보관 후 구매 시 추가 혜택**
            - VIP 고객이 장기 보관 후 차량을 구매할 경우 **보관료 20 ~ 40% 차감 혜택 제공**  
            - 차량 보관료 : 고급차 (Luxury/스포츠카) 80만 ~ 150만원, 슈퍼카 (Supercar) 150만 ~ 300만원  
            """)

        #  3️⃣ ‘VIP 익스클루시브 이벤트 & 개인 맞춤형 혜택’
        elif promotion == " 익스클루시브 이벤트 & 개인 맞춤형 혜택 ":
            st.subheader(" 익스클루시브 이벤트 & 개인 맞춤형 혜택 ")
            st.write("""
            **VIP 고객 초청 ‘프라이빗 브랜드 이벤트’**
            - 고급 레스토랑에서 진행하는 **VIP 초청 시승회 & 네트워킹 디너**  
            - 유명 레이서와 함께하는 **서킷 체험 이벤트** 진행  
            """)

        #  4️⃣ VIP ‘커넥티드 라이프스타일 멤버십’
        elif promotion == " 커넥티드 라이프스타일 멤버십 ":
            st.subheader(" 커넥티드 라이프스타일 멤버십 ")
            st.write("""
            **VIP 전용 컨시어지 서비스 운영**
            - 차량 정비, 세차, 보험, 유지보수를 전담하는 **프리미엄 컨시어지 서비스** 제공  
            **VIP 고객 전용 글로벌 렌터카 & 모빌리티 서비스 연계**
            - 해외 출장 시, VIP 고객에게 **프리미엄 렌터카 서비스 무료 제공**  
            """)

        st.markdown("---")
        st.markdown("### 🎉 **VVIP 이상 고객만을 위한 맞춤형 컨시어지 서비스!** 😊")

        #  고정된 6개월 VIP 이벤트 일정 생성
        vip_event_data = pd.DataFrame({
            "이벤트 제목": [
                " 프라이빗 럭셔리 드라이브 체험", " VIP 초청 골프 라운딩", " Prestige VIP 요트 디너", 
                " Royal VIP 런치", " Exclusive VIP 시승 & 맞춤 상담", "Prestige VIP 리무진 픽업 서비스",
                " 하이엔드 스포츠카 드라이브", "프리미엄 골프 멤버십 체험", " VIP 요트 선상 파티",
                " 미슐랭 셰프의 다이닝 경험", "VIP 하이브리드 모델 시승", " 글로벌 공항 VIP 리무진 서비스",
                " 클래식카 드라이빙 투어", " 해외 골프 투어 패키지", " 초호화 크루즈 나이트"
            ],
            "일정": [
                "2025-04-05", "2025-04-18", "2025-05-10",
                "2025-05-25", "2025-06-08", "2025-06-22",
                "2025-07-06", "2025-07-20", "2025-08-05",
                "2025-08-22", "2025-09-10", "2025-09-28",
                "2025-10-12", "2025-10-27", "2025-11-15"
            ],
            "장소": [
                "한강 프라이빗 드라이브 코스", "제주 최고급 골프장", "부산 요트 클럽",
                "서울 프라이빗 레스토랑", "전국 주요 대리점", "VIP 고객 지정 장소",
                "서울 드라이빙 클럽", "제주 프리미엄 골프장", "부산 마리나 요트 선착장",
                "미슐랭 3스타 레스토랑", "전국 주요 대리점", "해외 공항 VIP 터미널",
                "서울 클래식카 박물관", "하와이 골프 투어", "지중해 크루즈 선착장"
            ],
            "참여 가능 등급": [
                "Exclusive VIP", "Royal VIP", "Prestige VIP",
                "Royal VIP, Prestige VIP", "Exclusive VIP", "Prestige VIP",
                "Exclusive VIP", "Royal VIP", "Prestige VIP",
                "Royal VIP, Prestige VIP", "Exclusive VIP", "Prestige VIP",
                "Exclusive VIP", "Royal VIP", "Prestige VIP"
            ],
            "예약 가능 여부": [
                "가능", "예약 마감", "가능", "가능", "가능", "예약 마감",
                "가능", "가능", "예약 마감", "가능", "가능", "예약 마감",
                "가능", "가능", "가능"
            ],
            "잔여석": [5, 0, 3, 8, 10, 0, 7, 5, 0, 9, 6, 0, 4, 8, 10]
        })

        # 월별 분류
        vip_event_data["월"] = vip_event_data["일정"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").month)
        monthly_events = vip_event_data.groupby("월")

        #  월별 이벤트 캘린더 표시
        st.markdown("####  VIP 월별 프라이빗 이벤트 스케줄")

        #  월 선택 드롭다운
        selected_month = st.selectbox(" 월을 선택하세요.", sorted(vip_event_data["월"].unique()))

        # 선택한 월의 이벤트만 필터링
        filtered_events = vip_event_data[vip_event_data["월"] == selected_month]

        #  캘린더 형식으로 이벤트 정렬
        st.markdown(f"###  {calendar.month_name[selected_month]} VIP 이벤트 일정")

        #  보기 편한 이벤트 테이블 정리
        styled_df = filtered_events[["이벤트 제목", "일정", "장소", "참여 가능 등급", "예약 가능 여부", "잔여석"]].copy()


        styled_df = styled_df.style.set_table_styles([
            {'selector': 'thead th', 'props': [('background-color', '#4F81BD'), ('color', 'white'), ('font-weight', 'bold')]},
            {'selector': 'tbody td', 'props': [('text-align', 'center')]},
            {'selector': 'th', 'props': [('text-align', 'center')]},
        ]).format({'잔여석': "{:,.0f}석"})  # 잔여석 숫자 서식 적용

        # 📋 보기 편한 테이블 출력
        st.table(styled_df)
        #  선택한 이벤트 상세 정보 표시
        st.markdown("---")
        st.subheader(" 현재 진행 중인 이벤트 상세 정보")

        #  이벤트 선택
        event_selection = st.radio(
            " 자세히 보고 싶은 이벤트를 선택하세요.", 
            filtered_events["이벤트 제목"].tolist(), 
            key="event_selection"
        )

        # 선택한 이벤트 데이터 가져오기
        selected_event = filtered_events[filtered_events["이벤트 제목"] == event_selection].iloc[0]

        #  상세 설명 추가
        st.markdown("---")
        st.subheader(f"🎟️ {selected_event['이벤트 제목']} 상세 정보")

        # 일정 및 기본 정보
        st.write(f" **일정:** {selected_event['일정']}")
        st.write(f" **장소:** {selected_event['장소']}")
        st.write(f" **참여 가능 등급:** {selected_event['참여 가능 등급']}")
        st.write(f" **예약 가능 여부:** {selected_event['예약 가능 여부']}")
        st.write(f" **잔여석:** {selected_event['잔여석']}석")

        #  프라이빗 럭셔리 드라이브 체험
        if event_selection == " 프라이빗 럭셔리 드라이브 체험":
            st.write("""
            ✨ **프라이빗 럭셔리 드라이브 체험**
            
            -  **페라리, 람보르기니, 벤틀리 등 최고급 스포츠카 시승**
            -  **서울 한강 및 한적한 교외 드라이브 코스 포함**
            -  **전문 포토그래퍼가 촬영하는 럭셔리 드라이빙 기념사진 제공**
            -  **시승 후 프라이빗 레스토랑에서 고급 다이닝**
            -  **VIP 한정 기념품 제공 (럭셔리 키체인 & 프리미엄 시승권)**
            """)

        #  VIP 초청 골프 라운딩
        elif event_selection == " VIP 초청 골프 라운딩":
            st.write("""
            **VIP 초청 골프 라운딩**
            
            -  **제주도 최고급 골프 리조트에서 진행**
            -  **프라이빗 라운지에서 샴페인 리셉션**
            -  **세계적인 프로 골퍼와 함께하는 원포인트 레슨**
            -  **VIP 골프 굿즈 제공 (맞춤형 골프볼 & 고급 캐디백)**
            -  **라운딩 후 고급 프렌치 다이닝에서 VIP 디너**
            """)

        #  Prestige VIP 요트 디너
        elif event_selection == " Prestige VIP 요트 디너":
            st.write("""
            **Prestige VIP 요트 디너**
            
            -  **부산 요트 클럽에서 3시간 프라이빗 요트 투어**
            -  **미슐랭 셰프가 준비하는 최고급 디너 제공**
            -  **재즈 라이브 공연 & 샴페인 파티**
            -  **프라이빗 바에서 프리미엄 칵테일 서비스**
            -  **전문 포토그래퍼의 스냅 촬영 & 인스타그램 기념사진**
            """)

        #  Royal VIP 런치
        elif event_selection == " Royal VIP 런치":
            st.write("""
            **Royal VIP 런치**
            
            -  **서울 최고의 미슐랭 3스타 레스토랑에서 진행**
            -  **최고급 와인 & 맞춤형 코스 요리 제공**
            -  **클래식 연주와 함께하는 럭셔리 점심**
            -  **참석 고객에게 프리미엄 기프트 박스 제공**
            """)

        #  Exclusive VIP 시승 & 맞춤 상담
        elif event_selection == " Exclusive VIP 시승 & 맞춤 상담":
            st.write("""
            **Exclusive VIP 시승 & 맞춤 상담**
            
            -  **벤츠, 포르쉐, 테슬라 최신 모델 시승 기회 제공**
            -  **전국 주요 대리점에서 맞춤형 차량 상담**
            -  **VIP 고객만을 위한 특별 금융 혜택 안내**
            -  **시승 고객 한정, 프리미엄 차량 케어 패키지 증정**
            """)

        #  Prestige VIP 리무진 픽업 서비스
        elif event_selection == " Prestige VIP 리무진 픽업 서비스":
            st.write("""
            **Prestige VIP 리무진 픽업 서비스**
            
            -  **롤스로이스, 벤츠 마이바흐 전용 리무진 서비스 제공**
            -  **VIP 고객이 원하는 장소에서 맞춤형 픽업**
            -  **차량 내 프리미엄 음료 & 고급 간식 제공**
            -  **예약 고객에게 고급 브랜드 기념품 제공**
            """)

        # 예약 버튼 (예약 가능 시 활성화)
        if selected_event["예약 가능 여부"] == "가능" and selected_event["잔여석"] > 0:
            if st.button("✅ 예약하기", key="reservation_button"):
                st.success(f"✅ {selected_event['이벤트 제목']} 예약이 완료되었습니다! 🎉")
        else:
            st.warning("❌ 해당 이벤트는 예약이 마감되었습니다.")

        st.markdown("---")
        st.write(" **VIP 고객만을 위한 차별화된 프리미엄 혜택을 제공합니다!** 🎖️")