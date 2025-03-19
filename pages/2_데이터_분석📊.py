import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Streamlit 페이지 설정
st.set_page_config(page_title="고객 분석 대시보드", layout="wide")

# 데이터 로드
DATA_FILE = "data/고객db_전처리.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE, encoding="utf-8-sig").fillna(0)

df = load_data()

# 탭 생성
tab1, tab2 = st.tabs(["고객 데이터 분석", "판매 데이터 분석"])

# 고객 데이터 분석 탭
with tab1:
    subtab1, subtab2, subtab3, subtab4, subtab5, subtab6 = st.tabs(
        ["연령대별 고객 분포", "지역별 고객 분포", "연령대별 선호 차량 모델", 
         "연령대별 친환경 차량 선호도", "성별 및 연령대별 차량 선호도", "고객 등급 분석"]
    )

    # 연령대 정렬을 위한 순서 지정
    age_order = sorted(df['연령대'].unique())

    # 연령대별 고객 분포 (막대 그래프 + 선 그래프)
    with subtab1:
        st.subheader("연령대별 고객 분포")

        age_count = df["연령대"].value_counts().reset_index()
        age_count.columns = ["연령대", "고객 수"]
        age_count = age_count.sort_values('연령대')

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Bar(x=age_count["연령대"], y=age_count["고객 수"], name="고객 수", 
                text=age_count["고객 수"], textposition='outside', 
                marker_color='rgba(255, 182, 193, 0.8)',  # 연한 핑크색
                marker_line_color='rgba(255, 105, 180, 1)',  # 진한 핑크색 테두리
                marker_line_width=1.5),
            secondary_y=False,
)

        fig.add_trace(
            go.Scatter(x=age_count["연령대"], y=age_count["고객 수"], name="추세선", 
                    mode='lines+markers', 
                    line=dict(color='rgb(255, 20, 147)', width=4),  # 진한 핑크색 선
                    marker=dict(size=10, 
                                symbol='diamond', 
                                color='rgb(255, 105, 180)',  # 마커 색상
                                line=dict(color='rgb(255, 255, 255)', width=2))),  # 마커 테두리
            secondary_y=True,
        )


        fig.update_layout(
            title_text="연령대별 고객 분포",
            xaxis_title="연령대",
            yaxis_title="고객 수",
            legend_title="범례",
            barmode='group',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(size=14)
        )

        fig.update_xaxes(categoryorder='array', categoryarray=age_order, tickangle=45)
        fig.update_yaxes(range=[0, max(age_count["고객 수"]) * 1.1], secondary_y=True)

        st.plotly_chart(fig, use_container_width=True)

        st.write("""
        
        ## 연령대별 고객 분포 분석

        ### 1. 20대 초반: 고객 수 적음, 구매력 부족
        #### 경제적 여건상 차량 구매보다 대중교통 및 공유 차량 이용 선호

        ###### - **고객 수 가장 적음**: 해당 연령층은 경제적 자립 이전 단계로 차량 구매 수요가 낮음.
        ###### - **대체 이동수단 이용**: 대중교통, 카셰어링 및 렌터카 활용 비율이 높으며, 일부 고객은 중고차를 선택하는 경향이 있음.
        ###### - **신차 구매율 낮음**: 자금 부담으로 인해 신차보다는 저렴한 경차나 소형 중고차 구매가 주를 이룸.

        ---

        ### 2. 20대 중반~30대 초반: 고객 수 증가, 첫차 구매 활성화
        #### 취업 및 경제적 안정화에 따른 차량 구매 증가

        ###### - **고객 수 급격한 증가**: 취업 이후 이동 편의성을 고려해 첫차 구매가 활발해짐.
        ###### - **경제형 차량 선호**: 소형 SUV 및 준중형 세단 중심으로 신차 구매가 증가.
        ###### - **유지비 고려한 선택**: 연비와 유지보수가 중요한 요소로 작용하며, 초기 구매 비용이 낮은 모델 선호.

        ---

        ### 3. 30대 후반~50대 초반: 고객 수 최대, 프리미엄 차량 수요 증가
        #### 경제적 안정과 가족 중심 소비 패턴 반영

        ###### - **고객 수 정점 도달**: 직장 생활이 안정되면서 신차 구매가 활발해지는 연령대.
        ###### - **패밀리카 및 중대형 SUV 선호**: 결혼과 가족 형성에 따라 중형·대형 SUV, 미니밴 수요 증가.
        ###### - **프리미엄 브랜드 구매 증가**: 경제력이 높아지면서 브랜드 가치와 고급 옵션을 고려한 소비 경향이 뚜렷해짐.

        ---

        ### 4. 50대 후반~60대 이후: 고객 수 감소, 실용성과 유지보수 중심 소비
        #### 경제적 부담 고려 및 차량 유지 기간 증가

        ###### - **고객 수 점진적 감소**: 은퇴 및 경제적 변화로 인해 신차 구매보다는 기존 차량 유지에 초점.
        ###### - **내구성과 유지보수 고려**: 유지보수 비용이 낮고, 신뢰할 수 있는 브랜드의 차량 선호.
        ###### - **여가 및 레저 차량 수요 증가**: 자녀 독립 이후 여행 및 여가용 차량 구매 증가.
        
        """)

    # 지역별 고객 분포 (파이 차트)
    with subtab2:
        st.subheader("지역별 고객 분포")

        region_count = df["거주 지역"].value_counts()

        fig = go.Figure(data=[go.Pie(labels=region_count.index, values=region_count.values, hole=.3)])
        fig.update_layout(
            title_text="지역별 고객 분포",
            font=dict(size=14),
            legend_title="지역",
            plot_bgcolor='rgba(0,0,0,0)'
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')

        st.plotly_chart(fig, use_container_width=True)

    # 연령대별 선호 차량 모델 (히트맵)
    with subtab3:
        st.subheader("연령대별 선호 차량 모델")

        model_pref = pd.crosstab(df['연령대'], df['최근 구매 제품'])
        model_pref = model_pref.reindex(age_order)

        fig = px.imshow(model_pref, 
                        labels=dict(x="차량 모델", y="연령대", color="선호도"),
                        x=model_pref.columns,
                        y=model_pref.index,
                        color_continuous_scale="Viridis")

        fig.update_layout(
            title_text="연령대별 선호 차량 모델",
            xaxis_title="차량 모델",
            yaxis_title="연령대",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)

    # 연령대별 친환경 차량 선호도 (막대 그래프)
    with subtab4:
        st.subheader("연령대별 친환경 차량 선호도")

        eco_pref = df[df['연료 구분'].isin(['전기', '하이브리드'])].groupby('연령대')['연료 구분'].count().reset_index()
        eco_pref.columns = ['연령대', '친환경 차량 구매 수']
        eco_pref = eco_pref.sort_values('연령대')

        fig = px.bar(eco_pref, x='연령대', y='친환경 차량 구매 수', 
                     title='연령대별 친환경 차량 선호도',
                     labels={'친환경 차량 구매 수': '구매 수'},
                     color='친환경 차량 구매 수',
                     color_continuous_scale=px.colors.sequential.Viridis)

        fig.update_layout(
            xaxis_title="연령대",
            yaxis_title="친환경 차량 구매 수",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)

    # 성별 및 연령대별 차량 선호도 (그룹화된 막대 그래프)
    with subtab5:
        st.subheader("성별 및 연령대별 차량 선호도")

        gender_age_pref = df.groupby(['성별', '연령대'])['최근 구매 제품'].count().reset_index()
        gender_age_pref.columns = ['성별', '연령대', '구매 수']

        fig = px.bar(gender_age_pref, x='연령대', y='구매 수', color='성별', barmode='group',
                     title='성별 및 연령대별 차량 선호도',
                     labels={'구매 수': '구매 수'},
                     color_discrete_sequence=px.colors.qualitative.Set1)

        fig.update_layout(
            xaxis_title="연령대",
            yaxis_title="구매 수",
            legend_title="성별",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)

    # 고객 등급 분석 (도넛 차트)
    with subtab6:
        st.subheader("고객 등급 분석")

        grade_count = df['고객 등급'].value_counts()

        fig = go.Figure(data=[go.Pie(labels=grade_count.index, values=grade_count.values, hole=.5)])
        fig.update_layout(
            title_text="고객 등급 분포",
            annotations=[dict(text='고객 등급', x=0.5, y=0.5, font_size=20, showarrow=False)],
            font=dict(size=14),
            legend_title="고객 등급",
            plot_bgcolor='rgba(0,0,0,0)'
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')

        st.plotly_chart(fig, use_container_width=True)

# 판매 데이터 분석 탭
with tab2:
    subtab1, subtab2, subtab3, subtab4 = st.tabs(
        ["시기 및 연료 구분별 판매 대수", "고객 구분별 차량 구매 현황", "고객 구분별 평균 거래 금액", "분기별 차량 판매 요일"]
    )

    # 시기 및 연료 구분별 판매 대수 (막대 그래프)
    with subtab1:
        st.subheader("시기 및 연료 구분별 판매 대수")
        fuel_data = df.groupby(["최근 구매 시점", "연료 구분"]).size().reset_index(name="판매 대수")

        fig = px.bar(fuel_data, x="최근 구매 시점", y="판매 대수", color="연료 구분", barmode="group",
                     title="시기 및 연료 구분별 판매 대수",
                     color_discrete_sequence=px.colors.qualitative.Bold)
        
        fig.update_layout(
            xaxis_title="구매 시점",
            yaxis_title="판매 대수",
            legend_title="연료 구분",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)

    # 고객 구분별 차량 구매 현황 (스택 막대 그래프)
    with subtab2:
        st.subheader("고객 구분별 차량 구매 현황")
        customer_data = df.groupby(["연령대", "고객 구분"]).size().reset_index(name="구매 수")
        customer_data = customer_data.pivot(index="연령대", columns="고객 구분", values="구매 수").fillna(0)
        customer_data = customer_data.reindex(age_order)

        fig = go.Figure()
        for col in customer_data.columns:
            fig.add_trace(go.Bar(x=customer_data.index, y=customer_data[col], name=col))

        fig.update_layout(
            title_text="고객 구분별 차량 구매 현황",
            xaxis_title="연령대",
            yaxis_title="구매 수",
            barmode='stack',
            legend_title="고객 구분",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)

    # 고객 구분별 평균 거래 금액 (히트맵)
    with subtab3:
        st.subheader("고객 구분별 평균 거래 금액")
        price_data = df.pivot_table(index="연령대", columns="고객 구분", values="최근 거래 금액", aggfunc="mean").fillna(0)
        price_data = price_data.reindex(age_order)

        fig = px.imshow(price_data, 
                        labels=dict(x="고객 구분", y="연령대", color="평균 거래 금액"),
                        x=price_data.columns,
                        y=price_data.index,
                        color_continuous_scale="Plasma")

        fig.update_layout(
            title_text="고객 구분별 평균 거래 금액",
            xaxis_title="고객 구분",
            yaxis_title="연령대",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)

    # 분기별 차량 판매 요일 (스택 영역 그래프)
    with subtab4:
        st.subheader("분기별 차량 판매 요일")
        weekday_data = df.groupby(["최근 구매 시점", "최근 구매 요일"]).size().reset_index(name="판매 대수")
        weekday_data = weekday_data.pivot(index="최근 구매 시점", columns="최근 구매 요일", values="판매 대수").fillna(0)

        fig = go.Figure()
        for col in weekday_data.columns:
            fig.add_trace(go.Scatter(
                x=weekday_data.index, y=weekday_data[col],
                mode='lines',
                stackgroup='one',
                name=col
            ))

        fig.update_layout(
            title_text="분기별 차량 판매 요일",
            xaxis_title="구매 시점",
            yaxis_title="판매 대수",
            legend_title="구매 요일",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)
