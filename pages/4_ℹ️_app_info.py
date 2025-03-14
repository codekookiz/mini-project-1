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


import streamlit as st

st.title("ℹ️ 고객 추천 시스템 소개")
st.write("이 앱은 머신러닝을 활용하여 고객에게 맞춤형 제품을 추천합니다.")

st.image("images/banner.png", use_container_width=True)

st.write("📌 **개발팀:** AI Solutions")
st.write("📧 **문의:** support@company.com")
