import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
from dotenv import load_dotenv
import os
import time

# .env 파일 로드 (API 키 보안 강화)
load_dotenv()
API_KEY = "AIzaSyC9b_hcLeX739CwRnG1orE1vgOCDoPtaDY"

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
        "keyword": "현대자동차",
        "type": "car_dealer",
        "key": API_KEY
    }

    # 요청 URL 출력 (브라우저에서 직접 확인 가능)
    print(f"🔍 요청 URL: {url}?location={params['location']}&radius={params['radius']}&keyword={params['keyword']}&type={params['type']}&key={params['key']}")

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "OK":
        print(f"❌ API 요청 실패: {data.get('status')} - {data.get('error_message', 'No details')}")
        return []

    return data.get("results", [])

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
    
    # 검색 결과가 없는 경우 메시지 출력
    if not places:
        st.warning("검색된 대리점이 없습니다.")
    else:
        st.write(f"총 {len(places)}개의 대리점을 찾았습니다.")

    # 지도 생성
    map_center = list(map(float, location.split(",")))  # 중심 좌표 설정
    m = folium.Map(location=map_center, zoom_start=10)

    # 지도에 마커 추가
    for place in places:
        name = place["name"]
        lat = place["geometry"]["location"]["lat"]
        lng = place["geometry"]["location"]["lng"]

        folium.Marker(
            location=[lat, lng],
            popup=name,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    # 📌 folium_static → st_folium 변경
    st_folium(m, width=700, height=500)