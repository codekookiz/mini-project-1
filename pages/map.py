import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
from dotenv import load_dotenv
import os
import time

# .env 파일 로드 (API 키 보안 강화)
load_dotenv()
API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")  # .env 파일에 저장된 API 키 불러오기

# Google Geocoding API로 주소 -> 위도/경도 변환
def get_lat_lon(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return f"{location['lat']},{location['lng']}"
    return "37.5665,126.9780"  # 기본값 (서울)

# Google Places API 요청 함수
def get_hyundai_dealerships(location, radius=50000):
    """Google Places API를 사용하여 현대자동차 대리점 검색"""
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "keyword": "현대자동차 대리점",
        "key": API_KEY
    }
    
    places = []
    while True:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("status") != "OK":
            st.error(f"Google Places API 요청 실패: {data.get('status')}")
            return []

        if "results" in data:
            places.extend(data["results"])

        # Google Places API는 한 번 요청에 최대 20개만 반환 → 추가 요청 필요
        next_page_token = data.get("next_page_token")
        if next_page_token:
            time.sleep(2)  # Google API의 next_page_token 활성화를 위해 대기
            params["pagetoken"] = next_page_token
        else:
            break
    
    return places

# Streamlit UI
st.title("🚗 현대자동차 전국 대리점 지도")

# 사용자가 검색할 위치 입력
user_location = st.text_input("🔍 검색할 위치 (예: 서울, 부산, 대전 등)", "서울")

# 검색 버튼
if st.button("대리점 검색"):
    # 입력된 지역을 위도/경도로 변환
    location = get_lat_lon(user_location)

    # Google Places API 호출
    places = get_hyundai_dealerships(location)
    st.write("API 응답 데이터:", places)

    # 지도 생성
    map_center = list(map(float, location.split(",")))  # 중심 좌표 설정
    m = folium.Map(location=map_center, zoom_start=10)

    # 지도에 마커 추가
    if places:
        for place in places:
            name = place["name"]
            lat = place["geometry"]["location"]["lat"]
            lng = place["geometry"]["location"]["lng"]
            
            folium.Marker(
                location=[lat, lng],
                popup=name,
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(m)

    # 지도 출력
    folium_static(m)
