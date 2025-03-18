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

# 대리점 검색 함수
def search_dealership(query, x=None, y=None):
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
tabs = st.tabs(["대리점 찾기", "지점 찾기"])

# ✅ 🔹 상세 정보 팝업 HTML 생성 함수
def create_popup_html(place):
    place_name = place["place_name"]
    address = place["road_address_name"] if place["road_address_name"] else place["address_name"]
    phone = place["phone"] if place["phone"] else "전화번호 없음"
    url = f"https://map.kakao.com/link/to/{place_name},{place['y']},{place['x']}"
    
    popup_html = f"""
    <div style="width:300px;">
        <h4 style="margin-bottom:5px;">🔹 {place_name}</h4>
        <p><strong>📍 주소:</strong> {address}</p>
        <p><strong>📞 전화:</strong> {phone}</p>
        <a href="{url}" target="_blank" style="color:blue; text-decoration:none; font-weight:bold;">
            🗺️ 길찾기
        </a>
    </div>
    """
    return popup_html

# 탭1: 대리점 찾기
with tabs[0]:
    st.header("🔍 대리점 찾기")
    search_query = st.chat_input("검색어를 입력하세요:", key="dealership_chat")
    if search_query:
        st.write(f"🔍 '{search_query}' 검색 결과:")
        results = search_dealership(search_query)
        if results:
            first_place = results[0]
            map_center = [float(first_place["y"]), float(first_place["x"])]
            m = folium.Map(location=map_center, zoom_start=13)
            for place in results:
                folium.Marker(
                    location=[float(place["y"]), float(place["x"])],
                    popup=folium.Popup(create_popup_html(place), max_width=300),
                    tooltip=place["place_name"],
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(m)
            folium_static(m)
        else:
            st.write("🚫 검색 결과가 없습니다.")

# 탭2: 지점 찾기
with tabs[1]:
    st.header("🔍 지점 찾기")
    search_query_branch = st.chat_input("검색어를 입력하세요:", key="branch_chat")
    if search_query_branch:
        st.write(f"🔍 '{search_query_branch}' 검색 결과:")
        results = search_branch(search_query_branch)
        if results:
            first_place = results[0]
            map_center = [float(first_place["y"]), float(first_place["x"])]
            m = folium.Map(location=map_center, zoom_start=13)
            for place in results:
                folium.Marker(
                    location=[float(place["y"]), float(place["x"])],
                    popup=folium.Popup(create_popup_html(place), max_width=300),
                    tooltip=place["place_name"],
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(m)
            folium_static(m)
        else:
            st.write("🚫 검색 결과가 없습니다.")