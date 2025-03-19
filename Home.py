# 중요! 스트림릿 실행 코드 : 터미널에서 streamlit run Home.py
# 서버에서 돌아가는 것 확인해보고 싶다면 : https://mini-project-1-23bmqdpdnx9ctd2y38o9nx.streamlit.app/

import streamlit as st
import os

st.set_page_config(
    page_title="현대자동차 고객 분석 시스템",  # 웹사이트 제목
    page_icon="./images/favicon.ico",  # 파비콘 적용
)
# 메인 화면 구성
st.markdown("""
<h1 style="display:flex; align-items:center;">
    <img src="https://www.hyundai.com/etc/designs/hyundai/ww/en/images/common/logo.png" 
         alt="현대자동차 로고" 
         style="height:40px; margin-right:10px;">
    고객 분석 시스템
</h1>
""", unsafe_allow_html=True)
st.write("이 앱은 머신러닝을 활용하여 고객 정보를 분석하고 마케팅 전략을 수립하는 시스템입니다.")

# 차량 이미지 데이터
car_data = [
    {"name": "IONIQ 9", "url": "https://www.hyundai.com/contents/mainbanner/main_kv_ioniq9-pc.png"},
    {"name": "Palisade", "url": "https://www.hyundai.com/contents/mainbanner/Main-KV_Car_PALISADE.png"},
    {"name": "Tucson", "url": "https://www.hyundai.com/contents/mainbanner/Main-KV_Car_TUCSON.png"},
    {"name": "Sonata", "url": "https://www.hyundai.com/contents/mainbanner/main_sonata_25my_w.png"},
    {"name": "IONIQ 5 N", "url": "https://www.hyundai.com/contents/mainbanner/Main-KV_Car_IONIQ-5-N.png"},
    {"name": "Santa Fe", "url": "https://www.hyundai.com/contents/mainbanner/main-santafe-25my-kv-w.png"},
    {"name": "Casper Electric", "url": "https://www.hyundai.com/contents/mainbanner/Main-KV_Car_CASPER-Electric.png"},
]

# Swiper.js를 활용한 캐러셀 HTML 코드
carousel_html = f"""
<div class="swiper-container">
    <div class="swiper-wrapper">
        {''.join(f'<div class="swiper-slide"><img src="{car["url"]}" alt="{car["name"]}" style="width:100%; height:300px; object-fit:contain; border-radius:10px;"></div>' for car in car_data)}
    </div>
    <div class="swiper-pagination"></div>
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
</div>

<!-- Swiper.js 라이브러리 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.js"></script>
<script>
    var swiper = new Swiper('.swiper-container', {{
        loop: true,
        autoplay: {{
            delay: 2000,  // 1.5초마다 변경
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
<!-- 캐러셀 아래 공간 확보 -->
<div style="height: 80px;"></div>

<!-- 캐러셀 아래 메뉴 -->
<div class="menu-container">
    <div class="menu-item">
        <img src="https://cdn-icons-png.flaticon.com/128/747/747376.png" class="menu-icon">
        <p>견적내기</p>
    </div>
    <div class="menu-item">
        <img src="https://cdn-icons-png.flaticon.com/128/535/535239.png" class="menu-icon">
        <p>구매상담</p>
    </div>
    <div class="menu-item">
        <img src="https://cdn-icons-png.flaticon.com/128/3135/3135715.png" class="menu-icon">
        <p>시승신청</p>
    </div>
    <div class="menu-item">
        <img src="https://cdn-icons-png.flaticon.com/128/684/684809.png" class="menu-icon">
        <p>판매처 검색</p>
    </div>
    <div class="menu-item">
        <img src="https://cdn-icons-png.flaticon.com/128/929/929564.png" class="menu-icon">
        <p>구매혜택</p>
    </div>
    <div class="menu-item">
        <img src="https://cdn-icons-png.flaticon.com/128/3208/3208721.png" class="menu-icon">
        <p>정비예약</p>
    </div>
</div>

<style>
.menu-container {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px; /* 간격 증가 */
    margin-top: 50px; /* 위쪽 여백 증가 */
    padding-bottom: 80px; /* 하단 공간 추가 (스크롤 필요 시 대비) */
    position: relative; /* 메뉴가 가려지는 문제 해결 */
}}

.menu-item {{
    text-align: center;
    font-size: 16px;
    flex: 1 1 160px; /* 반응형 조정 */
}}

.menu-icon {{
    width: 55px;
    height: 55px;
}}
</style>

"""


# 캐러셀 표시
st.components.v1.html(carousel_html, height=400)

