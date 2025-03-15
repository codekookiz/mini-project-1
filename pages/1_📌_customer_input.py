# 1_📌_customer_input.py
#
#     고객 추천 모델 페이지 : 고객이 정보를 입력하면 그에 따른 차량 종류 추천하는 시스템
#         - 5개 모델 제작 : 각각 정확도는 98% 정도이지만, 추천 차량이 약간씩 다름
#             - 입력 정보 : 거주 지역, 예산, 차량 사이즈, 차량 유형, 연료 구분
#             - 출력 정보 : 추천 차종 (1~5개)
#                - 5개 모델의 연산 결과를 하나의 리스트로 제작, 해당 리스트 내 유니크한 값들을 모두 추천
#         - 신용 카드로 구매할 시 10% 포인트로 제공한다는 것 공지하면서, 가격대가 조금 더 높은 차량 목록 자연스럽게 추천
#         - 전기차가 아닌 차종 선택 시 대안이 될 수 있는 전기차 추천 동반 : 지역에 따른 보조금 차이 반영하여 추천
#
#     화면에 보여질 내용
#         - 정보 입력란 5개 : 예산, 거주 지역, 차량 사이즈, 차량 유형, 연료 구분
#             - 예산 : 직접 입력
#             - 나머지 4개 : 드롭다운 메뉴 선택
#         - 추천 받기 버튼 : 추천 결과를 보여주는 버튼
#         - 결과 출력 : 추천 결과를 1개~5개까지 보여줌 -> 순위 없이 결과 리스트 내부의 값들을 랜덤 순서로 보여줌
#         - 신용 카드 혜택 안내 : 10% 포인트 제공
#             - 팝업창 혹은 info 메시지 형태 : 약간의 딜레이(로딩 동그라미) 후 리스트 보여줌
#             - 버튼 형태 : 클릭 시 가격대 조금 더 높은 차량 N개 정보 보여줌
#         - 전기차 추천 : 전기차가 아닌 차종 선택 시 대안으로 전기차 추천
#             - 지역에 따른 보조금 차이 반영하여 자동으로 추천 : 1~3대 추천


import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 모델 로드 함수 (경로 수정)
def load_models():
    model_dir = "model/model"  # model 폴더 안에 있는 model 폴더 반영
    models = {
        "dtc": joblib.load(f"{model_dir}/dtc.pkl"),
        "rfc": joblib.load(f"{model_dir}/rfc.pkl"),
        "gbc": joblib.load(f"{model_dir}/gbc.pkl"),
        "lgb": joblib.load(f"{model_dir}/lgb.pkl"),
        "cb": joblib.load(f"{model_dir}/cb.pkl")
    }
    return models

# 모델 로드
models = load_models()

st.title("고객 정보 입력 & 차량 추천")

# 사용자 입력
budget = st.number_input("예산 입력 (단위: 만원)", min_value=3300, max_value=200000, step=500)
region = st.selectbox("거주 지역", ['인천광역시', '광주광역시', '부산광역시', '전라남도 목포시', '경기도 수원시', '울산광역시', '서울특별시',
       '경상남도 창원시', '전라북도 전주시', '충청북도 청주시', '경기도 성남시', '경상북도 포항시',
       '충청남도 천안시', '대구광역시', '대전광역시'])
car_size = st.selectbox("차량 사이즈", ["소형", "준중형", "중형", "대형", "SUV"])
car_type = st.selectbox("차량 유형", ["세단", "SUV", "트럭", "스포츠카"])
fuel_type = st.selectbox("연료 구분", ["가솔린", "디젤", "전기", "하이브리드", "플러그인하이브리드", "수소"])

# 추천 버튼
if st.button("추천 받기"):
    # 사용자 입력 데이터를 모델이 예측할 수 있는 형태로 변환
    user_data = np.array([[budget, region, car_size, car_type, fuel_type]])

    # 각 모델을 통해 추천 결과 생성
    recommended_cars = []
    for model_name, model in models.items():
        pred = model.predict(user_data)[0]  # 모델 예측
        recommended_cars.append(pred)

    # 중복 제거 및 정렬
    recommended_cars = list(set(recommended_cars))

    # 결과 출력
    st.subheader("추천 차량 리스트")
    st.write(", ".join(recommended_cars))

    # 추가 혜택 제공 (예: 신용카드 혜택 안내)
    st.info("신용카드로 구매 시 10% 포인트 적립 혜택을 받을 수 있습니다.")
