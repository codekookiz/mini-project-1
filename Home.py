# 중요! 스트림릿 실행 코드 : 터미널에서 streamlit run Home.py
# 서버에서 돌아가는 것 확인해보고 싶다면 : https://mini-project-1-23bmqdpdnx9ctd2y38o9nx.streamlit.app/

import streamlit as st
import os

st.set_page_config(
    page_title="현대자동차 고객 분석 시스템",
    page_icon="./images/favicon.ico",
    layout="wide"  # 와이드 레이아웃 설정
)

# 현대자동차 로고 & 제목
st.markdown("""
<h1 style="display:flex; align-items:center;">
    <img src="https://www.hyundai.com/etc/designs/hyundai/ww/en/images/common/logo.png" 
         alt="현대자동차 로고" 
         style="height:40px; margin-right:10px;">
    고객 분석 시스템
</h1>
""", unsafe_allow_html=True)

st.write("이 앱은 머신러닝을 활용하여 고객 정보를 분석하고 맞춤형 마케팅 전략을 수립하는 시스템입니다.")


st.write("")

# 🚙 주요 기능 메뉴 (2열 레이아웃)
col1, col2 = st.columns(2)

with col1:
    st.markdown("###  주요 기능")
    st.markdown("""
    -  **고객 분석** : AI 기반 구매 패턴 분석
    -  **차량 추천** : 고객 맞춤형 차량 추천 서비스
    -  **판매점 찾기** : 가까운 지점 및 정비소 검색
    -  **구매 혜택** : 카드사 제휴 혜택 비교
    """)

with col2:
    st.markdown("###  최신 고객 트렌드")
    st.markdown("""
    -  **인기 차종** : 3년 동안 가장 많이 판매된 차량
    -  **구매 패턴** : 연령별 선호 모델 분석
    -  **할부 이용율** : 카드사별 무이자 할부 비율
    """)

# 🚗 차량 이미지 캐러셀 (Swiper.js 활용)
car_data = [
    {"name": "IONIQ 9", "url": "https://www.hyundai.com/contents/mainbanner/main_kv_ioniq9-pc.png"},
    {"name": "Palisade", "url": "https://www.hyundai.com/contents/mainbanner/Main-KV_Car_PALISADE.png"},
    {"name": "Tucson", "url": "https://www.hyundai.com/contents/mainbanner/Main-KV_Car_TUCSON.png"},
    {"name": "Sonata", "url": "https://www.hyundai.com/contents/mainbanner/main_sonata_25my_w.png"},
]

carousel_html = f"""
<div class="swiper-container">
    <div class="swiper-wrapper">
        {''.join(f'<div class="swiper-slide"><img src="{car["url"]}" alt="{car["name"]}" style="width:100%; height:300px; object-fit:contain; border-radius:10px;"></div>' for car in car_data)}
    </div>
    <div class="swiper-pagination"></div>
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
</div>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.js"></script>
<script>
    var swiper = new Swiper('.swiper-container', {{
        loop: true,
        autoplay: {{
            delay: 2000,
            disableOnInteraction: false
        }},
        navigation: {{
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        }},
        pagination: {{
            el: '.swiper-pagination',
            clickable: true
        }},
    }});
</script>
"""

st.components.v1.html(carousel_html, height=400)

# 💡 푸터 (2개 컬럼으로 나누기)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("####  데이터 출처")
    st.markdown("""
     **기본 데이터셋** : 하이에듀 고객 DB  
     **추가 데이터** : [현대자동차 공식 웹사이트](https://www.hyundai.com)
    """)

with col2:
    st.markdown("####  현대자동차 고객 분석 시스템")
    st.markdown("""
     **기본 데이터셋** :   [현대자동차 공식 웹사이트](https://www.hyundai.com)  
     서울특별시 강남구 테헤란로 231 현대자동차 본사  
    """, unsafe_allow_html=True)
