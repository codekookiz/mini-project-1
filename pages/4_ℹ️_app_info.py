# 4_ℹ️_app_info.py
#
#     앱 개발 정보 화면 : 앱 개발 과정 세부적으로 설명
#         - 데이터 전처리 과정
#             - 어떤 컬럼을 추가/수정했는지 하나하나 설명
#                 - 왜 추가했는지도
#                 - 도출 방법에 대해서도
#             - 데이터 정제 과정
#                 - 이상치 처리 방법 : 구매 일자가 2025-12-01인 데이터 삭제
#         - 예측 모델 제작 과정
#                 - 학습한 모델
#                     - LogisticRegression, SVC, DecisionTreeClassifier, RandomForestClassifier, GradientBoostingClassifier
#                     - GaussianNB, KNeighborsClassifier, LGBMClassifier, CatBoostClassifier
#                 - 최종 선택 모델 : Decision Tree, Random Forest, Gradient Boosting, LightGBM, CatBoost
#                     - 정확도 : 0.9305
#         - 데이터 분석 과정
#                 - 어떤 데이터를 분석했는지
#                     - 분석 목적
#                     - 분석 방법
#         - 시각화 과정
#                 - 어떤 라이브러리를 사용해 시각화를 했는지
#         - 기타 사항
#                 - 추가적인 정보
#                 - 앱 만드는 과정에서 겪은 문제점과 해결 방법
#                 - 한계점과 앞으로 개선해야 할 부분


# app_info.py

# app_info.py

import streamlit as st

def show_app_info():
    st.markdown("""
    # 🚗 고객 데이터 분석 대시보드
    
    ## 📌 앱 소개
    본 애플리케이션은 **고객 데이터를 기반으로 연령대, 지역, 차량 선호도를 분석**하여 **맞춤형 마케팅 전략**을 도출하는 데이터 대시보드입니다.  
    이를 통해 **비즈니스 인사이트를 확보하고 차량 판매 전략을 최적화**할 수 있습니다.

    ## 🔥 주요 기능
    - **연령대별 고객 분석**: 특정 연령층의 차량 구매 패턴 및 선호도 분석
    - **지역별 고객 분포 분석**: 수도권과 지방 고객의 차이 분석 및 맞춤형 전략 제공
    - **차량 유형별 선호도 분석**: 전기차, SUV, 세단 등 고객 선호도 변화 확인
    - **맞춤형 마케팅 인사이트 제공**: 데이터 기반의 효과적인 마케팅 전략 도출

    ## 🛠️ 사용 기술
    - **Python** (Streamlit, Pandas, Matplotlib, Seaborn)
    - **데이터 분석** (Pandas, NumPy)
    - **시각화** (Matplotlib, Seaborn)
    - **웹 배포** (Streamlit Cloud)

    ## 📊 데이터 분석 내용
    - **연령대별 분석**: 30~40대 고객이 가장 많은 비중을 차지하며, 가족 단위 차량 교체 수요 증가
    - **지역별 분석**: 서울·경기 지역에 고객이 집중되며, 수도권 중심의 마케팅 필요
    - **차량 유형별 분석**: SUV와 중형 차량 선호도가 높으며, 전기차 구매율이 증가하는 추세

    ## 📌 참고 자료
    - KATECH Insight
    - 국토교통부 자동차 등록 통계
    - 현대자동차·기아 연구 보고서
    """)

if __name__ == "__main__":
    show_app_info()
