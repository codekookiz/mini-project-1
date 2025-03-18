import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
from dotenv import load_dotenv
import os

def get_api_key():
    key = os.environ.get('KAKAO_API_KEY')
    if key is None:
        key = st.secrets.get('KAKAO_API_KEY')
    return key

KAKAO_API_KEY = get_api_key()

url = "https://dapi.kakao.com/v2/local/search/keyword.json"
headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
params = {"query": "현대자동차 대리점", "size": 5}

response = requests.get(url, headers=headers, params=params)
st.write(response.status_code, response.text)

# 대리점 검색 함수
def search_dealership(query, x=None, y=None):
    # 입력받은 검색어에 "현대자동차 대리점" 추가
    query = query + " 현대자동차 대리점"
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": query, "size": 5}
    if x and y:
        params["x"] = x
        params["y"] = y
        params["radius"] = 10000  # 반경 10km 검색
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["documents"]
    else:
        return []

# 지점 검색 함수
def search_branch(query, x=None, y=None):
    # 입력받은 검색어에 "현대자동차 지점" 추가
    query = query + " 현대자동차 지점"
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": query, "size": 5}
    if x and y:
        params["x"] = x
        params["y"] = y
        params["radius"] = 10000  # 반경 10km 검색
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["documents"]
    else:
        return []

# Streamlit UI 구성
st.title("대리점 및 지점 검색")

# Streamlit 탭 생성 (대리점찾기, 지점 찾기)
tabs = st.tabs(["대리점찾기", "지점 찾기"])

# 탭1: 대리점찾기
with tabs[0]:
    st.header("대리점찾기")
    # 채팅 스타일 입력 위젯
    search_query = st.chat_input("검색어를 입력하세요:", key="dealership_chat")
    if search_query:
        st.write(f"🔍 '{search_query}' 검색 결과:")
        results = search_dealership(search_query)
        if results:
            # 첫 번째 검색 결과를 기준으로 지도 생성
            first_place = results[0]
            map_center = [float(first_place["y"]), float(first_place["x"])]
            m = folium.Map(location=map_center, zoom_start=13)
            # 검색된 장소에 마커 추가
            for place in results:
                folium.Marker(
                    location=[float(place["y"]), float(place["x"])],
                    popup=f"{place['place_name']}<br>{place['road_address_name'] if place['road_address_name'] else place['address_name']}",
                    tooltip=place["place_name"],
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(m)
            folium_static(m)
        else:
            st.write("검색 결과가 없습니다.")

# 탭2: 지점 찾기
with tabs[1]:
    st.header("지점 찾기")
    # 채팅 스타일 입력 위젯
    search_query_branch = st.chat_input("검색어를 입력하세요:", key="branch_chat")
    if search_query_branch:
        st.write(f"🔍 '{search_query_branch}' 검색 결과:")
        results = search_branch(search_query_branch)
        if results:
            # 첫 번째 검색 결과를 기준으로 지도 생성
            first_place = results[0]
            map_center = [float(first_place["y"]), float(first_place["x"])]
            m = folium.Map(location=map_center, zoom_start=13)
            # 검색된 장소에 마커 추가
            for place in results:
                folium.Marker(
                    location=[float(place["y"]), float(place["x"])],
                    popup=f"{place['place_name']}<br>{place['road_address_name'] if place['road_address_name'] else place['address_name']}",
                    tooltip=place["place_name"],
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(m)
            folium_static(m)
        else:
            st.write("검색 결과가 없습니다.")
