import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
import os

def get_api_key():
    key = os.environ.get('KAKAO_API_KEY')
    if key is None:
        key = st.secrets.get('KAKAO_API_KEY')
    return key

KAKAO_API_KEY = get_api_key()

# 1) 대리점 검색 함수
def search_dealership(query, x=None, y=None):
    query = query + " 현대자동차 대리점"
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": query, "size": 5}
    if x and y:
        params["x"] = x
        params["y"] = y
        params["radius"] = 10000
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["documents"]
    else:
        return []

# 2) 지점 검색 함수
def search_branch(query, x=None, y=None):
    query = query + " 현대자동차 지점"
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": query, "size": 5}
    if x and y:
        params["x"] = x
        params["y"] = y
        params["radius"] = 10000
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["documents"]
    else:
        return []

# 3) 상세 정보 팝업 HTML 생성 함수
def create_popup_html(place):
    place_name = place["place_name"]
    address = place["road_address_name"] if place["road_address_name"] else place["address_name"]
    phone = place["phone"] if place["phone"] else "전화번호 없음"
    detail_url = place["place_url"]
    directions_url = f"https://map.kakao.com/link/to/{place_name},{place['y']},{place['x']}"
    
    popup_html = f"""
    <div style="width:300px;">
        <h4 style="margin-bottom:5px;">🔹 {place_name}</h4>
        <p><strong>📍 주소:</strong> {address}</p>
        <p><strong>📞 전화:</strong> {phone}</p>
        <p>
          <a href="{detail_url}" target="_blank" style="color:blue; text-decoration:none; font-weight:bold;">
            📷 상세보기
          </a>
          &nbsp;|&nbsp;
          <a href="{directions_url}" target="_blank" style="color:blue; text-decoration:none; font-weight:bold;">
            🗺️ 길찾기
          </a>
        </p>
    </div>
    """
    return popup_html

# ------------------------------
# 4) Streamlit UI
# ------------------------------
st.title("대리점 및 지점 검색")

# 모란 지역 (디폴트 지도 중심)
DEFAULT_LOCATION = [37.41114, 127.12952]

tabs = st.tabs(["대리점 찾기", "지점 찾기"])

# ------------------------------
# 탭1: 대리점 찾기
# ------------------------------
with tabs[0]:
    st.header("🔍 대리점 찾기")

    # 좌(지도 + 검색어) : 우(결과 리스트) = 2 : 1 비율
    col_map, col_list = st.columns([2, 1])

    with col_map:
        # 지도 위에 검색어 입력
        search_query = st.text_input("검색어를 입력하세요 (예: '성남', '모란', '분당'):",
                                     key="dealership_input")

        # 기본 지도 (검색어 없으면 모란)
        if not search_query:
            m = folium.Map(location=DEFAULT_LOCATION, zoom_start=13)
            folium_static(m)
        else:
            # 검색 수행
            results = search_dealership(search_query)
            if results:
                # 지도 중심을 첫 번째 결과로
                first_place = results[0]
                map_center = [float(first_place["y"]), float(first_place["x"])]
                m = folium.Map(location=map_center, zoom_start=13)

                for i, place in enumerate(results, start=1):
                    folium.Marker(
                        location=[float(place["y"]), float(place["x"])],
                        popup=folium.Popup(create_popup_html(place), max_width=300),
                        tooltip=f"{i}. {place['place_name']}",
                        icon=folium.Icon(color="blue", icon="info-sign")
                    ).add_to(m)

                folium_static(m)
            else:
                st.warning("🚫 검색 결과가 없습니다.")

    with col_list:
        if search_query:
            results = search_dealership(search_query)
            if results:
                st.write(f"**검색 결과 ({len(results)}개)**")
                for i, place in enumerate(results, start=1):
                    st.write(f"**{i}. {place['place_name']}**")
                    st.caption(f"{place['road_address_name'] or place['address_name']}")
                    if place["phone"]:
                        st.caption(f"📞 {place['phone']}")
                    st.write("---")
        else:
            st.info("아직 검색어가 없습니다.")

# ------------------------------
# 탭2: 지점 찾기
# ------------------------------
with tabs[1]:
    st.header("🔍 지점 찾기")

    col_map2, col_list2 = st.columns([2, 1])

    with col_map2:
        # 지도 위에 검색어 입력
        search_query_branch = st.text_input("검색어를 입력하세요 (예: '성남', '모란', '분당'):",
                                            key="branch_input")

        # 기본 지도 (검색어 없으면 모란)
        if not search_query_branch:
            m2 = folium.Map(location=DEFAULT_LOCATION, zoom_start=13)
            folium_static(m2)
        else:
            # 검색 수행
            results_branch = search_branch(search_query_branch)
            if results_branch:
                first_place = results_branch[0]
                map_center = [float(first_place["y"]), float(first_place["x"])]
                m2 = folium.Map(location=map_center, zoom_start=13)

                for i, place in enumerate(results_branch, start=1):
                    folium.Marker(
                        location=[float(place["y"]), float(place["x"])],
                        popup=folium.Popup(create_popup_html(place), max_width=300),
                        tooltip=f"{i}. {place['place_name']}",
                        icon=folium.Icon(color="blue", icon="info-sign")
                    ).add_to(m2)

                folium_static(m2)
            else:
                st.warning("🚫 검색 결과가 없습니다.")

    with col_list2:
        if search_query_branch:
            results_branch = search_branch(search_query_branch)
            if results_branch:
                st.write(f"**검색 결과 ({len(results_branch)}개)**")
                for i, place in enumerate(results_branch, start=1):
                    st.write(f"**{i}. {place['place_name']}**")
                    st.caption(f"{place['road_address_name'] or place['address_name']}")
                    if place["phone"]:
                        st.caption(f"📞 {place['phone']}")
                    st.write("---")
        else:
            st.info("아직 검색어가 없습니다.")
