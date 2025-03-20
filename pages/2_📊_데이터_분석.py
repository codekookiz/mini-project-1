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

st.title("데이터 분석")

age_order = ["20대 초반", "20대 중반", "20대 후반", "30대 초반", "30대 중반", "30대 후반",
             "40대 초반", "40대 중반", "40대 후반", "50대 초반", "50대 중반", "50대 후반",
             "60대 초반", "60대 중반", "60대 후반", "70대 초반"]

quarter_order = ["2023 1분기", "2023 2분기", "2023 3분기", "2023 4분기", "2024 1분기",
                "2024 2분기", "2024 3분기", "2024 4분기", "2025 1분기"]

# 탭 생성
tab1, tab2 = st.tabs(["고객 데이터 분석", "판매 데이터 분석"])

# 고객 데이터 분석 탭
with tab1:
    subtab1, subtab2, subtab3, subtab4, subtab5 = st.tabs(
        ["연령대별 고객 분포", "지역별 고객 분포", "연령대별 선호 차량 모델", 
         "연령대별 친환경 차량 선호도", "성별 및 연령대별 차량 선호도"]
    )

    with subtab1:
        st.subheader("연령대별 고객 분포 분석")

        age_count = df["연령대"].value_counts().reset_index()
        age_count.columns = ["연령대", "고객 수"]
        age_count["연령대"] = pd.Categorical(age_count["연령대"], categories=age_order, ordered=True)
        age_count = age_count.sort_values("연령대")

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Bar(x=age_count["연령대"], y=age_count["고객 수"], name="고객 수", 
                text=age_count["고객 수"], textposition='outside', 
                marker_color='rgba(0, 32, 91, 0.7)',
                marker_line_color='rgba(0, 0, 128, 1)',
                marker_line_width=1.5),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=age_count["연령대"], y=age_count["고객 수"], name="추세선", 
                    mode='lines+markers', 
                    line=dict(color='rgb(25, 25, 112)', width=2),
                    marker=dict(size=5, symbol='diamond', 
                                color='rgb(65, 105, 225)',
                                line=dict(color='rgb(255, 255, 255)', width=1))),
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
        
        # y축 범위 설정: 최대값보다 더 큰 값으로 설정
        max_value = max(age_count["고객 수"])
        fig.update_yaxes(range=[0, max_value + 5], secondary_y=False, showgrid=False)
        fig.update_yaxes(range=[0, max_value + 5], secondary_y=True, showgrid=False)

        st.plotly_chart(fig, use_container_width=True)

        st.info('#### 연령대별 고객 분포 분석 결과')

        st.write("""


        #### 1. 20대 초반: 고객 수 적음, 구매력 부족
        경제적 여건상 차량 구매보다 대중교통 및 공유 차량 이용 선호

        - **고객 수 가장 적음**: 해당 연령층은 경제적 자립 이전 단계로 차량 구매 수요가 낮음.
        - **대체 이동수단 이용**: 대중교통, 카셰어링 및 렌터카 활용 비율이 높으며, 일부 고객은 중고차를 선택하는 경향이 있음.
        - **신차 구매율 낮음**: 자금 부담으로 인해 신차보다는 저렴한 경차나 소형 중고차 구매가 주를 이룸.

        &nbsp;

        #### 2. 20대 중반~30대 초반: 고객 수 증가, 첫차 구매 활성화
        취업 및 경제적 안정화에 따른 차량 구매 증가

        - **고객 수 급격한 증가**: 취업 이후 이동 편의성을 고려해 첫차 구매가 활발해짐.
        - **경제형 차량 선호**: 소형 SUV 및 준중형 세단 중심으로 신차 구매가 증가.
        - **유지비 고려한 선택**: 연비와 유지보수가 중요한 요소로 작용하며, 초기 구매 비용이 낮은 모델 선호.

        &nbsp;

        #### 3. 30대 후반~50대 초반: 고객 수 최대, 프리미엄 차량 수요 증가
        경제적 안정과 가족 중심 소비 패턴 반영

        - **고객 수 정점 도달**: 직장 생활이 안정되면서 신차 구매가 활발해지는 연령대.
        - **패밀리카 및 중대형 SUV 선호**: 결혼과 가족 형성에 따라 중형·대형 SUV, 미니밴 수요 증가.
        - **프리미엄 브랜드 구매 증가**: 경제력이 높아지면서 브랜드 가치와 고급 옵션을 고려한 소비 경향이 뚜렷해짐.

        &nbsp;

        #### 4. 50대 후반~60대 이후: 고객 수 감소, 실용성과 유지보수 중심 소비
        경제적 부담 고려 및 차량 유지 기간 증가

        - **고객 수 점진적 감소**: 은퇴 및 경제적 변화로 인해 신차 구매보다는 기존 차량 유지에 초점.
        - **내구성과 유지보수 고려**: 유지보수 비용이 낮고, 신뢰할 수 있는 브랜드의 차량 선호.
        - **여가 및 레저 차량 수요 증가**: 자녀 독립 이후 여행 및 여가용 차량 구매 증가.
        """)



    # 지역별 고객 분포 (파이 차트)
    with subtab2:
        st.subheader("지역별 고객 분포 분석")

        region_count = df["거주 지역"].value_counts()

        fig = go.Figure(data=[go.Pie(labels=region_count.index, values=region_count.values, hole=.3)])
        fig.update_layout(
            title_text="지역별 고객 분포",
            font=dict(size=14),
            legend_title="지역",
            plot_bgcolor='rgba(0,0,0,0)',
            height=700,  # 차트 높이 증가
            width=900,   # 차트 너비 증가
            legend=dict(
                orientation="h",  # 가로형 레전드
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5
            )
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont=dict(size=12)  # 텍스트 크기 조정
        )

        st.plotly_chart(fig, use_container_width=False)  # use_container_width=False로 크기 고정

        

        st.info('#### 지역별 고객 분포 분석 결과')
        st.write("""
                 
        #### 1. 서울특별시: 고객 수 최다
        수도권 중심의 높은 인구 밀도와 경제활동 집중

        - **높은 인구 밀도와 경제력**: 서울은 인구가 가장 많고 경제 활동이 집중되어 있어 고객 수가 압도적으로 많음.
        - **다양한 소비 패턴**: 젊은 층부터 중장년층까지 다양한 고객층이 분포하며, 프리미엄 및 실용적 소비 패턴이 혼재됨.
        - **편리한 교통과 접근성**: 대중교통이 발달해 있지만 차량 이용률도 높아 자동차 관련 수요도 많음.

        &nbsp;

        #### 2. 경기/부산/광주 등 대도시: 고객 수 상위권
        대규모 인구 거주 및 경제 활동 중심지

        - **경기도 (수원, 성남)**: 서울과 가까운 베드타운 역할을 하면서도 자체 경제력이 강해 고객 수가 많음.
        - **부산광역시**: 해양 물류와 관광 산업이 발달하며, 차량 보유율도 높아 고객 수가 많음.
        - **광주광역시**: 호남권의 중심 도시로, 인구가 많고 지역 내 경제 활동이 활발하여 고객 분포가 높은 편.

        &nbsp;

        #### 3. 대전/대구/울산 등 중위권 도시: 안정적인 고객 수 유지
        산업 및 공업 중심지로 일정한 고객층 확보

        - **대전광역시**: 행정 중심 도시로 공무원 및 안정적인 경제활동 인구가 많아 꾸준한 고객층 유지.
        - **대구광역시**: 섬유 및 제조업이 발달하며 중장년층의 차량 이용률이 높음.
        - **울산광역시**: 자동차 및 조선업 중심지로, 경제 활동이 활발한 계층에서 차량 이용률이 높음.

        &nbsp;

        #### 4. 전주/청주/천안 등 중소도시: 고객 수 점진적 증가
        지역 경제 성장과 인구 증가에 따른 영향

        - **청주, 천안**: 수도권 접근성이 높아 인구 유입이 많으며, 차량 이용 수요 증가.
        - **전주**: 전통 문화와 신도시 개발이 병행되며 차량 보유율이 높아짐.
        - **목포, 창원**: 지역 내 산업 및 관광 발전과 함께 고객층이 점진적으로 증가하는 추세.

        &nbsp;

        #### 5. 소도시 및 기타 지역: 고객 수 적음
        인구 밀집도가 낮고 대중교통 의존도 높음

        - **창원, 포항**: 공업 중심 도시지만 대중교통 이용률이 상대적으로 높음.
        - **목포, 전주**: 대도시에 비해 경제 및 산업 규모가 작아 고객 수가 적음.
        - **기타 지역**: 인구 유출과 산업 구조 변화로 인해 고객 수가 상대적으로 적은 편.
        """)



        

    # 연령대별 선호 차량 모델 (히트맵)
    with subtab3:
        st.subheader("연령대별 선호 차량 모델 분석")

        model_pref = pd.crosstab(df['최근 구매 제품'], df['연령대'])
        model_pref = model_pref.reindex(columns=age_order)

        # 데이터 정규화 (0-1 사이의 값으로)
        model_pref_normalized = model_pref.div(model_pref.max(axis=1), axis=0)

        fig = px.imshow(model_pref_normalized, 
                        labels=dict(x="연령대", y="차량 모델", color="선호도"),
                        x=model_pref.columns,
                        y=model_pref.index,
                        color_continuous_scale="Blues",  # 파란색 계열 색상
                        aspect="auto")  # 비율 자동 조정

        fig.update_layout(
            title_text="연령대별 선호 차량 모델",
            xaxis_title="연령대",
            yaxis_title="차량 모델",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)',
            height=800,  # 높이 조정
            width=1000   # 너비 조정
        )

        # x축 레이블 회전
        fig.update_xaxes(tickangle=45)

        # 각 셀에 값 표시
        fig.update_traces(text=model_pref.values, 
                        texttemplate="%{text}", 
                        textfont={"size": 10})

        st.plotly_chart(fig, use_container_width=True)
        st.info('#### 연령대별 선호 차량 모델 분석 결과')

        st.write("""

        ### 1. 20대: 실용성과 트렌드를 반영한 선택
        경제적 부담이 적은 모델과 스포츠 드라이빙에 대한 선호

        - **G70 (IK)의 인기**: 20대 초반에서는 G70 (IK)의 선호도가 가장 높으며, 스포츠 드라이빙을 즐기는 경향이 있음.
        - **Santa-Fe™ 수요**: SUV에 대한 관심도 증가하며, 실용성을 고려한 Santa-Fe™ 구매 비율도 높은 편.
        - **20대 중반에서 Avante (CN7 N) 인기**: Santa-Fe™ 다음으로 Avante (CN7 N)의 선호도가 높으며, 경제성과 주행 성능을 고려한 선택이 많음.
        - **트렌디한 디자인과 최신 기술 반영**: 차량 선택 시 디자인과 최신 기술이 반영된 모델에 대한 관심이 큼.

        &nbsp;

        ### 2. 30대: 다양한 차량 선택과 실용성
        패밀리카 및 고성능 세단 선택 비율 증가

        - **G70 (IK) 및 G80 (RG3)의 수요 증가**: 경제력이 높아지면서 프리미엄 브랜드 차량(G70, G80) 선택이 늘어남.
        - **패밀리카로 Santa-Fe™ 선택**: 가정이 있는 30대는 공간 활용성이 좋은 SUV 모델 선호.
        - **NEXO (FE) 도입 증가**: 친환경 차량에 대한 관심 증가로 인해 수소차 NEXO를 선택하는 비율도 상승.

        &nbsp;

        ### 3. 40대~50대: 고급 세단 및 실용적 SUV 선호
        경제적 여유와 실용성을 모두 고려한 차량 선택

        - **G80 (RG3)의 강세**: 중장년층에서 G80의 구매 비율이 가장 높으며, 고급 세단 선호 경향이 강함.
        - **Santa-Fe™ 및 NEXO (FE) 구매 증가**: SUV 및 친환경 차량을 고려하는 비율 증가.
        - **G70 (IK) 구매도 꾸준**: 운전의 재미를 원하는 고객층에서 여전히 인기가 있음.

        &nbsp;

        ### 4. 60대 이상: 프리미엄 차량 및 친환경차 선호
        안정성과 편안함을 고려한 선택

        - **G80 (RG3) 및 Santa-Fe™ 선택**: 고급 세단과 SUV가 주를 이루며, 장거리 운행을 고려한 안정성 높은 차량 선호.
        - **NEXO (FE) 관심 증가**: 연료비 절감 및 친환경 트렌드 반영으로 수소차에 대한 관심이 높아지는 추세.
        - **차량 유지 비용도 중요한 요소**: 유지 관리가 쉬운 차량을 선호하는 경향이 있음.
        """)
            


    # 연령대별 친환경 차량 선호도 (스택트 바 차트)
    with subtab4:
        st.subheader("연령대별 친환경 차량 선호도 분석")

        # 데이터 준비 (연료 유형별로 분리)
        eco_types = ["전기", "수소", "하이브리드"]
        eco_pref = df[df['연료 구분'].isin(eco_types)]
        eco_pref = eco_pref.groupby(['연령대', '연료 구분']).size().reset_index(name='구매 수')
        eco_pref["연령대"] = pd.Categorical(eco_pref["연령대"], categories=age_order, ordered=True)
        eco_pref = eco_pref.sort_values('연령대')

        # 그래프 생성
        fig = px.bar(eco_pref, 
                    x='연령대', 
                    y='구매 수', 
                    color='연료 구분',
                    title='연령대별 친환경 차량 선호도',
                    labels={'구매 수': '구매 수'},
                    color_discrete_sequence=['#00CC96', '#6495ED', '#FFA15A'],  # 전기(녹색), 수소(파란색), 하이브리드(주황)
                    barmode='stack')

        # 레이아웃 설정
        fig.update_layout(
            xaxis_title="연령대",
            yaxis_title="총 구매 수",
            legend_title="연료 유형",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(tickangle=45, showgrid=False),
            yaxis=dict(showgrid=False),
            hovermode='x unified'
        )

        # 값 레이블 및 애니메이션 추가
        fig.update_traces(texttemplate='%{y}', 
                        textposition='inside',
                        textfont_size=12,
                        marker_line_width=1.5,
                        marker_line_color='white')

        st.plotly_chart(fig, use_container_width=True)
        st.info('#### 연령대별 친환경 차량 선호도 분석 결과')

        st.write("""
    
            ### 1. 20대: 관심 증가 단계  
            젊은 층의 친환경 차량에 대한 관심 상승  

            - **경제성 고려**: 유지비 절감 및 정부 지원 혜택에 대한 관심이 높음.  
            - **트렌디한 이미지 선호**: 전기차 및 수소차의 미래지향적 디자인과 혁신성에 매력을 느낌.  
            - **충전 인프라 고려**: 충전소 부족 문제로 구매 결정에 신중함.  

            &nbsp;

            ### 2. 30대~40대: 실용성과 경제성 중시  
            가족 및 직장 생활을 고려한 선택  

            - **연비 절감 효과 중시**: 장거리 출퇴근 및 가족 차량으로 사용 시 유지비 절감 효과 중요.  
            - **SUV 친환경 모델 인기**: Santa-Fe™ HEV, NEXO 등 실용성과 친환경성을 갖춘 모델 선호.  
            - **충전 인프라 안정성 필요**: 충전소 및 유지보수 관련 편의성이 중요한 구매 요소.  

            &nbsp;

            ### 3. 50대: 높은 친환경 차량 수요  
            경제적 여유와 지속 가능성 고려  

            - **고급 친환경 모델 선호**: G80 전기차, 수소차 등 프리미엄 친환경 모델 수요 증가.  
            - **환경 보호 가치 중시**: 자녀 세대에 대한 배려 및 환경 보호 관점에서 친환경 차량 선택.  
            - **세제 혜택 및 충전 편의성 고려**: 세금 감면, 충전소 접근성 등이 중요한 요소로 작용.  

            &nbsp;

            ### 4. 60대 이상: 제한적인 관심  
            경제성보다는 익숙한 차량 유지  

            - **내연기관 차량 선호 지속**: 기존 차량 유지 비용 절감 차원에서 교체를 미루는 경향.  
            - **충전 인프라 이용 어려움**: 충전 방식 및 절차에 대한 불편함을 느끼는 경우가 많음.  
            - **하이브리드 차량 선호**: 전기차보다는 기존 운전 습관과 유사한 하이브리드 모델을 고려.  
            """)




        # 성별 및 연령대별 차량 선호도 (그룹화된 막대 그래프)
        with subtab5:
            st.subheader("성별 및 연령대별 차량 선호도 분석")

            gender_age_pref = df.groupby(['성별', '연령대'])['최근 구매 제품'].count().reset_index()
            gender_age_pref.columns = ['성별', '연령대', '구매 수']
            gender_age_pref["연령대"] = pd.Categorical(gender_age_pref["연령대"], categories=age_order, ordered=True)
            gender_age_pref = gender_age_pref.sort_values('연령대')

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
            st.info('#### 성별 및 연령대별 차량 선호도 분석 결과')


            st.write("""

            ### 1. 20대 중반 여성 소비자의 높은 구매율
            20대 중반 여성의 차량 구매 비율이 두드러지게 높음

            - **20대 중반 여성의 구매량이 남성보다 월등히 높음**: 해당 연령대에서 여성 소비자의 구매가 가장 활발하게 이루어짐.
            - **20대 후반부터 남성 구매율 증가**: 20대 후반부터 남성의 구매 비율이 점차 증가하는 경향을 보임.

            &nbsp;

            ### 2. 30~40대 남성의 강한 구매력
            30~40대에서는 남성의 구매 비율이 상대적으로 높음

            - **30대 중후반부터 남성이 우세**: 30대 초반까지는 여성 소비자와 유사한 수준이나, 이후 남성의 구매가 강세를 보임.
            - **40대 남성이 가장 많은 차량을 구매**: 40대 남성이 전체 연령대 중 가장 높은 구매량을 기록함.

            &nbsp;

            ### 3. 50대 이후 여성 구매 비율 증가
            50대 후반부터 여성 소비자의 차량 구매 비율이 높아지는 경향이 나타남

            - **50대 초반까지 남성이 우세**: 50대 초반까지는 남성이 다소 우세하나, 이후 여성 구매 비율이 점진적으로 증가함.
            - **60대 이후 남녀 균형 회복**: 60대 이후부터 남성과 여성의 구매 비율이 비슷해지는 모습을 보임.
            """)

# 판매 데이터 분석 탭
with tab2:
    subtab1, subtab2, subtab3, subtab4, subtab5 = st.tabs(
        [ "시기 및 연료 구분별 판매 대수", "고객 구분별 차량 구매 현황", "고객 구분별 평균 거래 금액", "분기별 차량 판매 요일","고객 등급 분석"]
    )

    # 시기 및 연료 구분별 판매 대수 (그룹화된 막대 그래프)
    with subtab1:
        st.subheader("시기 및 연료 구분별 판매 대수 분석")
        fuel_data = df.groupby(["최근 구매 시점", "연료 구분"]).size().reset_index(name="판매 대수")

        fig = px.bar(fuel_data, x="최근 구매 시점", y="판매 대수", color="연료 구분", barmode="group",
                    title="시기 및 연료 구분별 판매 대수",
                    color_discrete_sequence=px.colors.qualitative.Set2)
        
        fig.update_layout(
            xaxis_title="구매 시점",
            yaxis_title="판매 대수",
            legend_title="연료 구분",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)
        st.info('#### 시기 및 연료 구분별 판매 대수 분석 결과')

        st.write("""

        ### 1. 20~30대 초반: VIP 고객 비율 높음
        경제력을 갖춘 젊은 층이 프리미엄 서비스를 선호하는 경향

        - **소득 증가 및 소비 패턴 변화**: 20~30대 초반은 빠르게 경제적 자립을 이루며 프리미엄 서비스에 대한 수요가 증가.
        - **소셜 미디어와 트렌드**: 20대는 소셜 미디어와 온라인 쇼핑을 적극 활용하며, 프리미엄 혜택을 통해 차별화된 경험을 선호.
        - **경험 중심의 소비**: 물질적 소비보다는 경험을 중시하며, 고급 레스토랑, 특급 호텔 등 프리미엄 경험을 선호.

        &nbsp;

        ### 2. 30대 후반~50대 초반: VIP 고객 유지, 일반 고객 감소
        경제적 여유가 생기면서 일반 등급에서 VIP 등급으로 전환되는 경향

        - **경제적 여유와 안정**: 직장 생활에서 일정한 경제적 안정기를 맞이하며, 소비에 있어서 질을 중시.
        - **VIP 등급으로의 전환**: 경제적 여유가 생기면 더 나은 서비스와 제품을 선호하며, 기존의 일반 고객에서 VIP 고객으로 전환되는 경향.
        - **사회적 지위와 대인 관계**: 사회적 지위가 확립되면서 브랜드의 프리미엄 서비스를 통해 지위와 품격을 강조하려는 경향.

        &nbsp;

        ### 3. 50대 후반~60대 이후: VIP 고객 유지, 일반 고객 증가
        은퇴 이후 경제적 부담을 고려한 소비 패턴 변화

        - **은퇴 후 경제적 여유와 실용성**: 은퇴 후 생활을 고려한 실용적 소비를 선호하며, 고급 서비스보다는 실용적인 혜택을 선호.
        - **로열티 프로그램과 혜택**: 할인 혜택, 포인트 시스템 등 장기적인 비용 절감이 가능한 로열티 프로그램을 선호. 건강과 관련된 서비스나 편의성이 높은 제품에 대한 관심이 증가.
        - **건강과 편안함을 중시하는 소비**: 건강에 관심이 많아지고, 자녀가 독립한 후 여행이나 취미 활동을 위한 소비가 증가하는 경향.
        """)

    # 고객 구분별 차량 구매 현황 (스택 막대 그래프)
    with subtab2:
        st.subheader("고객 구분별 차량 구매 현황 분석")
        customer_data = df.groupby(["연령대", "고객 구분"]).size().reset_index(name="구매 수")
        customer_data = customer_data.pivot(index="연령대", columns="고객 구분", values="구매 수").fillna(0)
        customer_data = customer_data.reindex(age_order)

        fig = px.bar(customer_data, x=customer_data.index, y=customer_data.columns, 
                    title="고객 구분별 차량 구매 현황",
                    labels={'value': '구매 수', 'variable': '고객 구분'},
                    color_discrete_sequence=px.colors.qualitative.Pastel)

        fig.update_layout(
            xaxis_title="연령대",
            yaxis_title="구매 수",
            barmode='stack',
            legend_title="고객 구분",
            font=dict(size=14),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True)
        st.info('#### 고객 구분별 차량 구매 현황 분석 결과')

        st.write("""

        ### 1. 2023년 1분기 ~ 2023년 3분기: 전통 연료 차량 중심, 친환경차 수요 증가 준비 단계
        초기 시장 진입 단계에서 전통 연료(휘발유, 디젤) 차량이 주도, 친환경차는 낮은 판매량 유지

        - **휘발유와 디젤 차량의 안정적 수요**: 초기 시장에서는 휘발유와 디젤 차량이 주요 판매를 차지하며, 소비자들이 전통적인 연료 차량에 대한 선호도를 유지.
        - **친환경차의 낮은 판매량**: 전기차, 하이브리드, 플러그인 하이브리드 등 친환경차는 여전히 낮은 판매량을 기록하며, 초기 시장에서 소비자들의 신뢰를 얻는 데 시간이 필요.
        - **법인 고객 중심의 구매 증가**: 법인 고객의 초기 투자가 이루어지며, 친환경차 도입에 대한 테스트 및 파일럿 프로그램이 진행될 가능성.

        &nbsp;

        ### 2. 2023년 4분기 ~ 2024년 2분기: 친환경차 수요 증가, 전통 연료 차량과 경쟁 심화
        시장 안정화 단계에서 전기차와 하이브리드 차량의 판매량 증가

        - **전기차와 하이브리드 차량의 성장**: 정부 보조금 정책과 소비자 인식 변화로 인해 전기차와 하이브리드 차량의 판매량이 꾸준히 증가.
        - **휘발유와 디젤 차량의 점진적 감소**: 전통 연료 차량의 판매량은 점진적으로 감소하며, 친환경차가 시장 점유율을 확대.
        - **정부 정책 및 지원 효과**: 친환경차 구매 보조금 및 세제 혜택 등이 소비자들의 구매 결정을 촉진하는 중요한 요인으로 작용.

        &nbsp;

        ### 3. 2024년 3분기 ~ 2025년 1분기: 친환경차 시장 성숙 단계
        전기차와 하이브리드 차량이 주요 시장을 주도하며, 플러그인 하이브리드 수요 증가

        - **전기차와 하이브리드 차량의 안정적 성장**: 친환경차가 주요 선택지로 자리 잡으며, 소비자들의 신뢰를 얻음.
        - **플러그인 하이브리드 수요 증가**: 플러그인 하이브리드는 전통 연료와 친환경 기술을 결합한 모델로서 소비자들에게 실용성과 효율성을 제공하며 수요가 증가.
        - **경쟁 심화**: 다양한 브랜드에서 출시된 친환경 모델들이 경쟁하면서 가격 경쟁력과 기술 혁신이 중요한 요소로 부각.
        """)

        # 고객 구분별 평균 거래 금액 (스택 막대 그래프)
        with subtab3:
            st.subheader("고객 구분별 평균 거래 금액 분석")

            # 데이터 준비
            price_data = df.pivot_table(
                index="연령대", 
                columns="고객 구분", 
                values="최근 거래 금액", 
                aggfunc="mean"
            ).fillna(0)

            # 데이터 재구성
            price_data = price_data.reset_index().melt(id_vars="연령대", var_name="고객 구분", value_name="평균 거래 금액")
            price_data["연령대"] = pd.Categorical(price_data["연령대"], categories=age_order, ordered=True)
            price_data = price_data.sort_values('연령대')

            # 스택 막대 그래프 생성
            fig = px.bar(
                price_data,
                x="연령대",
                y="평균 거래 금액",
                color="고객 구분",
                title="고객 구분별 평균 거래 금액",
                labels={"평균 거래 금액": "평균 거래 금액(만 원)", "연령대": "연령대", "고객 구분": "고객 구분"},
                color_discrete_sequence=px.colors.qualitative.Set2,  # Set2 색상 팔레트 사용
                barmode="stack"
            )

            # 레이아웃 설정
            fig.update_layout(
                xaxis_title="연령대",
                yaxis_title="평균 거래 금액(만 원)",
                legend_title="고객 구분",
                font=dict(size=14),
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(tickangle=45)
            )

            st.plotly_chart(fig, use_container_width=True)
            st.info('#### 고객 구분별 평균 거래 금액 분석 결과')

            st.write("""
            ### 1. 2023년 1분기 ~ 2023년 3분기: 개인 고객 초기 구매량 감소, 법인 고객 증가 추세
            초기 시장 진입 단계에서 개인 고객의 구매 저조 및 법인 고객의 투자 시작

            - **개인 고객 구매량 감소**: 2023년 1분기 초기에는 개인 고객의 구매량이 상대적으로 적음. 시장 진입 초기 단계에서 소비 심리가 위축되었을 가능성이 있음.
            - **법인 고객 투자 시작**: 법인 고객의 구매량은 꾸준히 증가하는 추세. 새로운 시장에 대한 초기 투자 및 사업 확장을 위한 차량 구매가 이루어지고 있음을 시사.
            - **시장 변화에 대한 불확실성**: 초기 시장에서는 소비자들의 반응을 예측하기 어려워 개인 고객들이 구매를 망설이는 경향이 있음.

            &nbsp;

            ### 2. 2023년 4분기 ~ 2024년 2분기: 개인 고객 구매량 증가, 법인 고객 주춤
            시장 안정화 단계에서 개인 고객의 구매 증가 및 법인 고객의 투자 보류

            - **개인 고객 구매량 증가**: 2023년 4분기부터 개인 고객의 구매량이 점차 증가. 시장이 안정화되고 있음을 나타내며, 소비자 신뢰도 상승 및 긍정적인 입소문 효과로 해석 가능.
            - **법인 고객 투자 보류**: 법인 고객의 구매량은 2023년 4분기부터 주춤하는 경향. 초기 투자 이후 시장 상황을 관망하며 추가 투자를 보류하고 있을 가능성.
            - **정부 정책 및 지원 효과**: 정부의 친환경차 보조금 정책이나 세제 혜택 등이 개인 고객의 구매를 촉진하는 요인으로 작용했을 수 있음.

            &nbsp;

            ### 3. 2024년 3분기 ~ 2025년 1분기: 개인 고객 구매량 유지, 법인 고객 소폭 감소
            시장 성숙 단계에서 개인 고객의 안정적인 구매 및 법인 고객의 효율성 추구

            - **개인 고객 구매량 유지**: 2024년 3분기 이후 개인 고객의 구매량은 비교적 안정적으로 유지. 시장이 성숙 단계에 접어들었음을 시사.
            - **법인 고객 효율성 추구**: 법인 고객의 구매량은 소폭 감소하는 경향. 초기 투자 이후 효율성을 높이기 위해 차량 운영 방식을 개선하고 있을 가능성.
            - **친환경차 시장 경쟁 심화**: 다양한 브랜드의 친환경차 출시 및 경쟁 심화로 인해 개인 고객들의 선택 폭이 넓어짐. 이는 특정 브랜드에 대한 충성도를 낮추는 요인으로 작용할 수 있음.
            """)




        # 분기별 차량 판매 요일 (그룹화된 막대 차트)
        with subtab4:
            st.subheader("분기별 차량 판매 요일")

            # 데이터 준비
            weekday_data = df.groupby(["최근 구매 시점", "최근 구매 요일"]).size().reset_index(name="판매 대수")

            # 최근 구매 시점에 quarter_order 적용
            weekday_data["최근 구매 시점"] = pd.Categorical(
                weekday_data["최근 구매 시점"],
                categories=quarter_order,
                ordered=True
            )

            # 지정된 카테고리 순서대로 정렬
            weekday_data = weekday_data.sort_values("최근 구매 시점")

            # 그래프 생성
            fig = px.bar(
                weekday_data,
                x="최근 구매 시점",
                y="판매 대수",
                color="최근 구매 요일",
                barmode="group",  # 그룹화된 막대 그래프
                title="분기별 차량 판매 요일",
                labels={"최근 구매 시점": "구매 시점", "판매 대수": "판매 대수"},
                color_discrete_sequence=['#1E88E5', '#FFC107']
            )

            # 레이아웃 설정
            fig.update_layout(
                xaxis_title="구매 시점 (분기)",
                yaxis_title="판매 대수",
                legend_title="구매 요일",
                font=dict(size=14),
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(tickangle=45),
                uniformtext_minsize=12
            )

            st.plotly_chart(fig, use_container_width=True)
            st.info('#### 분기별 차량 판매 요일 분석 결과')
            st.write("""

            ### 1. 30대 중반 ~ 40대 초반: 법인 고객의 평균 거래 금액 증가
            이 연령대에서 법인 고객의 평균 거래 금액이 급증하는 패턴을 보임

            - **법인 고객의 대형 거래**: 30대 중반 ~ 40대 초반에서 법인 고객의 평균 거래 금액이 높아지는 것으로 보아, 이 연령대에서 기업이 차량을 대량 구매하는 경향이 있음.
            - **법인 차량 운용 증가**: 이 시기의 법인 고객들은 업무용 차량 또는 리스 차량을 대량 구매하는 트렌드를 보이며, 비즈니스 확장과 관련이 있을 가능성이 큼.
            - **개인 고객과의 차이**: 개인 고객의 평균 거래 금액은 법인 고객에 비해 상대적으로 일정한 패턴을 유지하고 있음.

            &nbsp;

            ### 2. 20대 후반 ~ 30대 초반: 개인 고객의 평균 거래 금액 감소
            젊은 연령대에서 상대적으로 낮은 평균 거래 금액을 보임

            - **경제적 부담**: 20대 후반 ~ 30대 초반 개인 고객의 평균 거래 금액이 낮은 이유는 경제적 부담이 상대적으로 크기 때문일 가능성이 높음.
            - **소형차 및 중고차 선호**: 해당 연령대에서는 상대적으로 가격이 저렴한 소형차나 중고차 구매를 선호하는 경향이 있을 수 있음.
            - **신차보다는 리스 및 금융상품 활용**: 젊은 소비자층은 직접 구매보다 리스나 장기 렌트 등의 금융상품을 더 적극적으로 활용할 가능성이 있음.

            &nbsp;

            ### 3. 50대 이상: 안정적인 개인 고객 구매 패턴
            중장년층의 개인 고객들은 꾸준한 평균 거래 금액을 유지

            - **고급 차량 선호**: 50대 이상 개인 고객들은 상대적으로 높은 금액의 차량을 꾸준히 구매하는 경향이 있으며, 이는 프리미엄 브랜드 선호와 관련이 있을 가능성이 있음.
            - **법인 고객과의 차이**: 법인 고객은 연령대별로 큰 변동성이 있지만, 개인 고객은 연령이 높아질수록 비교적 일정한 패턴을 유지.
            - **구매력 확보**: 중장년층 개인 고객들은 경제적 안정성이 높아 신차 구매에 대한 부담이 적고, 지속적인 수요를 형성.
            """)



    # 고객 등급 분석 (도넛 차트)
    with subtab5:
        st.subheader("고객 등급 분석")

        grade_count = df['고객 등급'].value_counts()

        fig = go.Figure(data=[go.Pie(labels=grade_count.index, values=grade_count.values, hole=.5,
                                    marker_colors=px.colors.qualitative.Pastel)])
        fig.update_layout(
            title_text="고객 등급 분포",
            annotations=[dict(text='고객 등급', x=0.5, y=0.5, font_size=20, showarrow=False)],
            font=dict(size=14),
            legend_title="고객 등급",
            plot_bgcolor='rgba(0,0,0,0)'
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')

        st.plotly_chart(fig, use_container_width=True)
        st.info('#### 고객 등급 분석 결과')
        st.write("""

            ### 1. 평일과 주말의 판매량 차이
            평일과 주말의 판매량에서 뚜렷한 차이가 나타남

            - **평일 판매량 우세**: 전반적으로 평일의 판매량이 주말보다 높은 경향을 보임. 이는 평일에 정기적인 구매가 발생하는 기업 고객이나 직장인들의 소비가 반영된 결과일 가능성이 큼.
            - **주말 판매량 증가 시점**: 특정 분기(예: 2023년 2분기, 2024년 1분기)에서 주말 판매량이 상대적으로 증가하는 패턴을 보이며, 이는 프로모션이나 계절적 요인과 관련이 있을 가능성이 있음.
            - **소비 패턴 분석 필요**: 주말의 판매량이 상대적으로 낮기 때문에, 주말 프로모션 강화나 주말 구매 유인을 위한 마케팅 전략이 필요할 수 있음.

            &nbsp;

            ### 2. 분기별 판매량 변화
            전체적인 분기별 판매량 변동성이 존재함

            - **평일 판매량의 급증**: 2023년 1분기에서 2023년 2분기로 넘어가면서 평일 판매량이 급격히 증가하며, 이후 비교적 높은 수준을 유지함.
            - **일부 분기에서 하락세**: 2024년 1분기 이후 일부 분기(2024년 2분기 등)에서 판매량이 감소하는 경향이 보이며, 이는 경기 변화 또는 시즌별 영향일 가능성이 있음.
            - **2024년 하반기 판매량 반등**: 2024년 3분기부터 다시 판매량이 증가하며, 이는 특정한 마케팅 활동이나 소비자의 계절적 구매 성향과 관련이 있을 가능성이 큼.

            &nbsp;

            ### 3. 마케팅 전략 개선 방향
            판매량 변동성을 줄이고, 주말 소비를 유도할 필요성이 있음

            - **주말 판매 촉진**: 주말 판매량을 증가시키기 위해 특정 이벤트, 할인 프로모션, 특별 혜택 제공 등의 전략이 필요함.
            - **일정한 판매량 유지 전략**: 2024년 2분기와 같이 판매량이 감소하는 시점을 분석하여, 그에 대한 대응책 마련이 필요함.
            - **고객 맞춤형 마케팅**: 평일과 주말의 구매층 차이를 분석하여, 기업 고객과 개인 고객을 대상으로 맞춤형 마케팅을 강화하는 것이 효과적일 것으로 보임.
            """)
