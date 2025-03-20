import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
import time

# 커스텀 메시지 함수: 이미지와 배경, 글자색을 지정하여 눈에 띄게 만듭니다.
def custom_message(message, msg_type="success"):
    if msg_type == "success":
        image_url = "https://img.icons8.com/color/48/000000/checked--v1.png"
        background = "#d4edda"
        color = "#155724"
    elif msg_type == "info":
        image_url = "https://img.icons8.com/color/48/000000/info--v1.png"
        background = "#d1ecf1"
        color = "#0c5460"
    elif msg_type == "error":
        image_url = "https://img.icons8.com/color/48/000000/high-importance.png"
        background = "#f8d7da"
        color = "#721c24"
    elif msg_type == "promotion1":
        image_url = "https://img.icons8.com/color/48/000000/gift--v1.png"
        background = "#fff4e5"
        color = "#8a6d3b"
    elif msg_type == "promotion2":
        image_url = "https://img.icons8.com/color/48/000000/prize.png"
        background = "#fff4e5"
        color = "#8a6d3b"
    elif msg_type == "question":
        image_url = "https://img.icons8.com/color/48/000000/help.png"
        background = "#e2e3e5"
        color = "#383d41"
    else:
        image_url = ""
        background = "#ffffff"
        color = "#000000"
    html_string = f'''
    <div style="display: flex; align-items: center; padding: 15px; border-radius: 8px; background-color: {background}; margin: 10px 0;">
        <img src="{image_url}" style="width: 48px; height: 48px; margin-right: 15px;">
        <span style="font-size: 22px; font-weight: bold; color: {color};">{message}</span>
    </div>
    '''
    st.markdown(html_string, unsafe_allow_html=True)

base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, "..", "model", "models")

def load_model(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {path}")
    return joblib.load(path)

data_dir = os.path.join(base_dir, "..", "data")
data_path = os.path.join(data_dir, "고객db_전처리.csv")

def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {path}")
    return pd.read_csv(path)

df = load_data(data_path)

st.title("고객 정보 입력 & 차량 추천")

st.markdown("---")

budget = st.number_input("구매 예산을 입력하세요. (단위: 만원)", step=500, value=5000)
region = st.selectbox("거주 지역이 어떻게 되시나요?", [
    '서울특별시', '부산광역시', '인천광역시', '대구광역시', '광주광역시', '대전광역시',
    '울산광역시', '경기도 수원시', '경기도 성남시', '충청남도 천안시', '충청북도 청주시',
    '전라북도 전주시', '전라남도 목포시', '경상북도 포항시', '경상남도 창원시'
])
car_size = st.selectbox("선호하시는 차량 사이즈가 무엇인가요?", ["준중형", "중형", "준대형", "대형", "프리미엄"])
car_type = st.selectbox("선호하시는 차량 유형은 무엇인가요?", ["세단", "SUV", "해치백"])
fuel_type = st.selectbox("어떤 연료 구분의 차량을 찾고 계신가요?", ["디젤", "수소", "전기", "플러그인 하이브리드", "하이브리드", "휘발유"])

custom_message("[신용카드 혜택]" + "\n\n" + "구매 시 최대 10% 포인트 적립 혜택을 누리세요!", "promotion1")
custom_message("[현대카드 이용자 혜택]" + "\n\n" + "추첨을 통해 현대카드 슈퍼콘서트 2025 VIP 티켓을 드립니다!", "promotion2")

st.write("")

if st.button("추천 받기"):
    with st.spinner("추천 결과를 생성 중입니다..."):
        time.sleep(3)
        custom_message("🎉 고객님을 위한 추천 결과가 생성되었습니다! 🚀", "success")
    
    st.balloons()

    region_list = {
        "경기도 성남시": [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        "경기도 수원시": [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        "경상남도 창원시": [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        "경상북도 포항시": [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        "광주광역시": [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        "대구광역시": [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        "대전광역시": [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        "부산광역시": [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        "서울특별시": [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        "울산광역시": [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        "인천광역시": [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        "전라남도 목포시": [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        "전라북도 전주시": [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        "충청남도 천안시": [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        "충청북도 청주시": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    }

    car_size_list = {
        "대형": [1,0,0,0,0],
        "준대형": [0,1,0,0,0],
        "준중형": [0,0,1,0,0],
        "중형": [0,0,0,1,0],
        "프리미엄": [0,0,0,0,1]
    }

    car_type_list = {
        "SUV": [1,0,0],
        "세단": [0,1,0],
        "해치백": [0,0,1]
    }

    fuel_type_list = {
        "디젤": [1,0,0,0,0,0],
        "수소": [0,1,0,0,0,0],
        "전기": [0,0,1,0,0,0],
        "플러그인 하이브리드": [0,0,0,1,0,0],
        "하이브리드": [0,0,0,0,1,0],
        "휘발유": [0,0,0,0,0,1]
    }

    user_data = np.hstack([budget * 10000, region_list[region], car_size_list[car_size], car_type_list[car_type]]).reshape(1, -1)[0]
    user_data = np.array(user_data).reshape(1, 24)

    if fuel_type not in ["수소", "플러그인 하이브리드", "하이브리드"]:
        dtc_path = os.path.join(model_dir, f"DecisionTree {fuel_type} 모델.pkl")
        rfc_path = os.path.join(model_dir, f"RandomForest {fuel_type} 모델.pkl")
        gbc_path = os.path.join(model_dir, f"GradientBoosting {fuel_type} 모델.pkl")
        lgb_path = os.path.join(model_dir, f"LightGBM {fuel_type} 모델.pkl")

        dtc = load_model(dtc_path)
        rfc = load_model(rfc_path)
        gbc = load_model(gbc_path)
        lgb = load_model(lgb_path)

        recom_list = []
        recom_list.append(dtc.predict(user_data)[0])
        recom_list.append(rfc.predict(user_data)[0])
        recom_list.append(gbc.predict(user_data)[0])
        recom_list.append(lgb.predict(user_data)[0])
        recom_list = list(set(recom_list))
    else:
        if fuel_type == "수소":
            recom_list = ["NEXO (FE)"]
        elif fuel_type == "플러그인 하이브리드":
            recom_list = ["Santa-Fe (MX5 PHEV)", "Tucson (NX4 PHEV)"]
        else:
            recom_list = ["Grandeur (GN7 HEV)"]

    car_list = {
        "Avante (CN7 N)": "아반떼 CN7 N\n - 가격: 2,485만원\n - 연비: 15.1km/L\n - 배기량: 1,598cc\n - 최대출력: 123마력\n - 최대토크: 15.0kg.m",
        "Avante (CN7 HEV)": "아반떼 CN7 HEV\n - 가격: 2,785만원\n - 연비: 19.2km/L\n - 배기량: 1,598cc\n - 최대출력: 105마력\n - 최대토크: 17.0kg.m\n",
        "Grandeur (GN7 HEV)": "그랜저 GN7 HEV\n - 가격: 3,785만원\n - 연비: 14.6km/L\n - 배기량: 1,999cc\n - 최대출력: 159마력\n - 최대토크: 19.3kg.m\n",
        "G80 (RG3)": "G80 RG3\n - 가격: 6,750만원\n - 연비: 10.5km/L\n - 배기량: 3,778cc\n - 최대출력: 315마력\n - 최대토크: 40.0kg.m\n",
        "Santa-Fe ™": "Santa-Fe ™\n - 가격: 3,870만원\n - 연비: 14.6km/L\n - 배기량: 1,598cc\n - 최대출력: 159마력\n - 최대토크: 19.3kg.m\n",
        "Santa-Fe (MX5 PHEV)": "Santa-Fe MX5 PHEV\n - 가격: 4,785만원\n - 연비: 15.1km/L\n - 배기량: 1,598cc\n - 최대출력: 123마력\n - 최대토크: 15.0kg.m\n",
        "Tucson (NX4 PHEV)": "Tucson NX4 PHEV\n - 가격: 3,785만원\n - 연비: 19.2km/L\n - 배기량: 1,598cc\n - 최대출력: 105마력\n - 최대토크: 17.0kg.m\n",
        "Palisade (LX2)": "Palisade LX2\n - 가격: 3,785만원\n - 연비: 14.6km/L\n - 배기량: 1,999cc\n - 최대출력: 159마력\n - 최대토크: 19.3kg.m\n",
        "IONIQ (AE EV)": "IONIQ AE EV\n - 가격: 6,750만원\n - 연비: 10.5km/L\n - 배기량: 3,778cc\n - 최대출력: 315마력\n - 최대토크: 40.0kg.m\n",
        "IONIQ 6 (CE)": "IONIQ 6 CE\n - 가격: 3,870만원\n - 연비: 14.6km/L\n - 배기량: 1,598cc\n - 최대출력: 159마력\n - 최대토크: 19.3kg.m\n",
        "NEXO (FE)": "NEXO FE\n - 가격: 4,785만원\n - 연비: 15.1km/L\n - 배기량: 1,598cc\n - 최대출력: 123마력\n - 최대토크: 15.0kg.m\n",
        "G90 (HI)": "G90 HI\n - 가격: 3,785만원\n - 연비: 19.2km/L\n - 배기량: 1,598cc\n - 최대출력: 105마력\n - 최대토크: 17.0kg.m\n",
        "G70 (IK)": "G70 IK\n - 가격: 3,785만원\n - 연비: 14.6km/L\n - 배기량: 1,999cc\n - 최대출력: 159마력\n - 최대토크: 19.3kg.m\n",
        "i30 (PD)": "i30 PD\n - 가격: 6,750만원\n - 연비: 10.5km/L\n - 배기량: 3,778cc\n - 최대출력: 315마력\n - 최대토크: 40.0kg.m\n",
        "GV80 (RS4)": "GV80 RS4\n - 가격: 3,870만원\n - 연비: 14.6km/L\n - 배기량: 1,598cc\n - 최대출력: 159마력\n - 최대토크: 19.3kg.m\n",
        "G90 (RS4)": "G90 RS4\n - 가격: 4,785만원\n - 연비: 15.1km/L\n - 배기량: 1,598cc\n - 최대출력: 123마력\n - 최대토크: 15.0kg.m\n"
    }
    
    min_price_list = {
        "Avante (CN7 N)": "3,309만원",
        "Avante (CN7 HEV)": "2,485만원",
        "Grandeur (GN7 HEV)": "4,267만원",
        "G80 (RG3)": "8,275만원",
        "Santa-Fe ™": "3,492만원",
        "Santa-Fe (MX5 PHEV)": "3,870만원",
        "Tucson (NX4 PHEV)": "3,205만원",
        "Palisade (LX2)": "4,383만원",
        "IONIQ (AE EV)": "6,715만원",
        "IONIQ 6 (CE)": "3,695만원",
        "NEXO (FE)": "6,950만원",
        "G90 (HI)": "1억 2,960만원",
        "G70 (IK)": "4,398만원",
        "i30 (PD)": "1,855만원",
        "GV80 (RS4)": "6,945만원",
        "G90 (RS4)": "1억 7,520만원"
    }

    recom_list = [i for i in recom_list if int(min_price_list[i].rstrip("만원").replace(",", "")) <= budget]

    tab1, tab2 = st.tabs(["추천 차량 리스트", "전기차 추천"])

    with tab1:
        if len(recom_list) != 0:
            st.subheader("추천 차량 리스트")
            columns_per_row = 3  
            if fuel_type not in ["수소", "플러그인 하이브리드", "하이브리드"]:
                num_cars = len(recom_list)
            else:
                num_cars = 1 if fuel_type in ["수소", "하이브리드"] else 2

            header_titles = [f"추천 차량 {i+1}" for i in range(min(columns_per_row, num_cars))]
            table_header = "| " + " | ".join(header_titles) + " |\n"
            table_header += "| " + " | ".join(["---"] * min(columns_per_row, num_cars)) + " |\n"

            img_rows = []
            text_rows = []

            if fuel_type not in ["수소", "플러그인 하이브리드", "하이브리드"]:
                for idx, car_name in enumerate(recom_list):
                    image_url = df.loc[df['최근 구매 제품'] == car_name, '모델 사진'].to_numpy()[0]
                    img_tag = f'<img src="{image_url}" width="320">' if image_url else "이미지 없음"
                    fuel = df.loc[df['최근 구매 제품'] == car_name, '연료 구분'].to_numpy()[0]
                    price = f"{min_price_list.get(car_name, '가격 정보 없음')}~"
                    mileage = df.loc[df['최근 구매 제품'] == car_name, '차량 연비'].to_numpy()[0]
                    engine = df.loc[df['최근 구매 제품'] == car_name, '배기량'].to_numpy()[0]
                    power = df.loc[df['최근 구매 제품'] == car_name, '최대 출력'].to_numpy()[0]
                    summary = f"**{car_name}**<br>연료 구분: {fuel}<br>가격: {price}<br>연비: {mileage}<br>배기량: {engine}<br>최대 출력: {power}"
                    img_rows.append(img_tag)
                    text_rows.append(summary)
                    if (idx + 1) % columns_per_row == 0 or idx == num_cars - 1:
                        img_row = "| " + " | ".join(img_rows) + " |\n"
                        text_row = "| " + " | ".join(text_rows) + " |\n"
                        table_header += img_row + text_row
                        img_rows, text_rows = [], []
            else:
                for idx, car_name in enumerate(recom_list):
                    image_url = df.loc[df['최근 구매 제품'] == car_name, '모델 사진'].to_numpy()[0]
                    img_tag = f'<img src="{image_url}" width="320">' if image_url else "이미지 없음"
                    fuel = df.loc[df['최근 구매 제품'] == car_name, '연료 구분'].to_numpy()[0]
                    price = f"{min_price_list.get(car_name, '가격 정보 없음')}~"
                    mileage = df.loc[df['최근 구매 제품'] == car_name, '차량 연비'].to_numpy()[0]
                    engine = df.loc[df['최근 구매 제품'] == car_name, '배기량'].to_numpy()[0]
                    power = df.loc[df['최근 구매 제품'] == car_name, '최대 출력'].to_numpy()[0]
                    summary = f"**{car_name}**<br>연료 구분: {fuel}<br>가격: {price}<br>연비: {mileage}<br>배기량: {engine}<br>최대 출력: {power}"
                    img_rows.append(img_tag)
                    text_rows.append(summary)
                    if (idx + 1) % columns_per_row == 0 or idx == num_cars - 1:
                        img_row = "| " + " | ".join(img_rows) + " |\n"
                        text_row = "| " + " | ".join(text_rows) + " |\n"
                        table_header += img_row + text_row
                        img_rows, text_rows = [], []
            st.markdown(table_header, unsafe_allow_html=True)
        else:
            custom_message("😢 죄송합니다. 예산 내에 맞는 차량이 없습니다. 조건을 확인해주세요!", "error")
            custom_message("🔍 전기차는 어떠신가요? '전기차 추천' 탭을 클릭해 확인해보세요!", "question")
    
    with tab2:
        if fuel_type in ["전기", "플러그인 하이브리드", "하이브리드"]:
            custom_message("⚡ 이미 전기차를 선택하셨네요! 다른 전기차 옵션도 한 번 확인해보세요!", "info")
            recom_elec = df.loc[(df["최근 거래 금액"] <= budget * 10000) & (df["연료 구분"].isin(["전기", "플러그인 하이브리드", "하이브리드"])), "최근 구매 제품"].unique()
            recom_elec = recom_elec.tolist()
            for car in recom_list:
                if car in recom_elec:
                    recom_elec.remove(car)
            recom_elec = list(set(recom_elec))[:3]
            with st.spinner("추천 결과를 생성 중입니다..."):
                time.sleep(3)
            columns_per_row = 3  
            num_cars = len(recom_elec)
            if num_cars > 0:
                st.subheader("전기차 추천 리스트")
                header_titles = [f"추천 차량 {i+1}" for i in range(min(columns_per_row, num_cars))]
                table_header = "| " + " | ".join(header_titles) + " |\n"
                table_header += "| " + " | ".join(["---"] * min(columns_per_row, num_cars)) + " |\n"
                img_rows = []
                text_rows = []
                for idx, car_name in enumerate(recom_elec):
                    image_url = df.loc[df['최근 구매 제품'] == car_name, '모델 사진'].to_numpy()[0]
                    img_tag = f'<img src="{image_url}" width="320">' if image_url else "이미지 없음"
                    fuel_type_val = df.loc[df['최근 구매 제품'] == car_name, '연료 구분'].to_numpy()[0]
                    price = f"{min_price_list.get(car_name, '가격 정보 없음')}~"
                    mileage = df.loc[df['최근 구매 제품'] == car_name, '차량 연비'].to_numpy()[0]
                    power = df.loc[df['최근 구매 제품'] == car_name, '최대 출력'].to_numpy()[0]
                    summary = f"**{car_name}**<br>연료 구분: {fuel_type_val}<br>가격: {price}<br>연비: {mileage}<br>최대 출력: {power}"
                    img_rows.append(img_tag)
                    text_rows.append(summary)
                    if (idx + 1) % columns_per_row == 0 or idx == num_cars - 1:
                        img_row = "| " + " | ".join(img_rows) + " |\n"
                        text_row = "| " + " | ".join(text_rows) + " |\n"
                        table_header += img_row + text_row
                        img_rows, text_rows = [], []
                st.markdown(table_header, unsafe_allow_html=True)
        else:
            elec_car_compen = {
                "서울특별시": 9000000,
                "부산광역시": 10500000,
                "대구광역시": 11000000,
                "인천광역시": 10600000,
                "광주광역시": 11000000,
                "대전광역시": 12000000,
                "울산광역시": 10500000,
                "경기도 수원시": 10500000,
                "경기도 성남시": 11000000,
                "충청북도 청주시": 14000000,
                "충청남도 천안시": 14000000,
                "전라북도 전주시": 15000000,
                "전라남도 목포시": 15500000,
                "경상북도 포항시": 13000000,
                "경상남도 창원시": 13000000
            }

            def comma(x):
                return format(x, ',')
            
            compen = elec_car_compen[region]

            recom_elec = df.loc[(df["최근 거래 금액"] <= budget * 10000 + compen) & (df["연료 구분"].isin(["전기", "플러그인 하이브리드", "하이브리드"])), "최근 구매 제품"].unique()[:3]
            with st.spinner("추천 결과를 생성 중입니다..."):
                time.sleep(3)
                custom_message(
                    f"""
                    ✨ 최적의 전기차 추천 리스트가 준비되었습니다! 
                    <span style="font-size: 16px; color: #555;">\n\n(💡 {region} 지역의 전기차 보조금: **{comma(elec_car_compen[region])}원**)</span>
                    """,
                    "info"
                )

            columns_per_row = 3  
            num_cars = len(recom_elec)
            if num_cars > 0:
                st.subheader("전기차 추천 리스트")
                header_titles = [f"추천 차량 {i+1}" for i in range(min(columns_per_row, num_cars))]
                table_header = "| " + " | ".join(header_titles) + " |\n"
                table_header += "| " + " | ".join(["---"] * min(columns_per_row, num_cars)) + " |\n"
                img_rows = []
                text_rows = []
                for idx, car_name in enumerate(recom_elec):
                    image_url = df.loc[df['최근 구매 제품'] == car_name, '모델 사진'].to_numpy()[0]
                    img_tag = f'<img src="{image_url}" width="320">' if image_url else "이미지 없음"
                    fuel_type_val = df.loc[df['최근 구매 제품'] == car_name, '연료 구분'].to_numpy()[0]
                    price = f"{min_price_list.get(car_name, '가격 정보 없음')}~"
                    mileage = df.loc[df['최근 구매 제품'] == car_name, '차량 연비'].to_numpy()[0]
                    power = df.loc[df['최근 구매 제품'] == car_name, '최대 출력'].to_numpy()[0]
                    summary = f"**{car_name}**<br>연료 구분: {fuel_type_val}<br>가격: {price}<br>연비: {mileage}<br>최대 출력: {power}"
                    img_rows.append(img_tag)
                    text_rows.append(summary)
                    if (idx + 1) % columns_per_row == 0 or idx == num_cars - 1:
                        img_row = "| " + " | ".join(img_rows) + " |\n"
                        text_row = "| " + " | ".join(text_rows) + " |\n"
                        table_header += img_row + text_row
                        img_rows, text_rows = [], []
                st.markdown(table_header, unsafe_allow_html=True)
            else:
                custom_message("😢 죄송합니다. 예산 내에 맞는 차량이 없습니다. 조건을 확인해주세요!", "error")