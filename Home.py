import streamlit as st

st.set_page_config(page_title="현대자동차 고객 추천 시스템", layout="wide")

# 메인 화면 구성
st.title("🚗 현대자동차 고객 추천 시스템")
st.write("이 앱은 머신러닝을 활용하여 고객에게 맞춤형 차량을 추천하는 시스템입니다.")

# 차량 이미지 데이터
car_data = [
    {"name": "Avante (CN7 N)", "url": "https://www.hyundai.com/contents/vr360/CN17/exterior/PM2/001.png"},
    {"name": "G70 (IK)", "url": "https://www.genesis.com/content/dam/genesis-p2/kr/assets/models/g70/renewal/exterior/color/genesis-kr-g70-sport-color-glossy-makalu-gray-small.png"},
    {"name": "G80 (RG3)", "url": "https://macarong.net/resources/images/car/img_report_car_top_%EC%A0%9C%EB%84%A4%EC%8B%9C%EC%8A%A4_%EB%8D%94%20%EC%98%AC%20%EB%89%B4%20G80(RG3).png"},
    {"name": "G90 (HI)", "url": "https://inv.assets.sincrod.com/ChromeColorMatch/us/WHITE_cc_2025GSC021924261_01_1280_PH3.jpg"},
    {"name": "G90 (RS4)", "url": "https://autoimg.danawa.com/photo/4016/model_360.png"},
    {"name": "Grandeur (GN7 HEV)", "url": "https://www.hyundai.com/contents/vr360/GN06/exterior/NY9/001.png"},
    {"name": "IONIQ (AE EV)", "url": "https://autoimg.danawa.com/photo/3720/model_360.png"},
    {"name": "IONIQ 6 (CE)", "url": "https://autoimg.danawa.com/photo/4087/model_360.png"},
    {"name": "NEXO (FE)", "url": "https://www.hyundai.com/contents/vr360/FE04/exterior/TW3/001.png"},
    {"name": "Palisade (LX2)", "url": "https://autoimg.danawa.com/photo/4190/model_360.png"},
    {"name": "Santa-Fe ™", "url": "https://s7d1.scene7.com/is/image/hyundai/2025-santa-fe-sel-fwd-hampton-gray-vehicle-browse-hero:Browse?fmt=webp-alpha"},
    {"name": "Santa-Fe (MX5 PHEV)", "url": "https://www.hyundai.com/contents/vr360/MX05/exterior/YBM/001.png"},
    {"name": "Tucson (NX4 PHEV)", "url": "https://ci.encarmagazine.com/2023/08/s01.jpg?resize=640:*"},
    {"name": "i30 (PD)", "url": "https://file.carisyou.com/upload/2018/09/19/FILE_201809191120516660.png"},
]

# Swiper.js를 활용한 캐러셀 HTML 코드
carousel_html = f"""
<div class="swiper-container">
    <div class="swiper-wrapper">
        {''.join(f'<div class="swiper-slide"><img src="{car["url"]}" alt="{car["name"]}" style="width:80%; height:300px; object-fit:contain; border-radius:10px;"></div>' for car in car_data)}
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
            delay: 1500,  // 1.5초마다 변경
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

# 캐러셀 표시
st.components.v1.html(carousel_html, height=400)

# 🔹 오픈채팅방 링크 설정
kakao_open_chat_link = "https://open.kakao.com/o/sKl8ocmh"  # 본인의 오픈채팅 링크 입력

# 🔹 플로팅 버튼 & "상담 하기" 텍스트 추가
floating_button = f"""
<style>
.floating-container {{
    position: fixed;
    bottom: 20px;
    right: 20px;
    text-align: center;
    z-index: 1000;
}}

.floating-text {{
    font-size: 16px;
    font-weight: bold;
    color: #333;
    margin-bottom: 5px;
}}

.floating-btn {{
    background: none;
    border: none;
    cursor: pointer;
}}

.floating-btn img {{
    width: 60px;
    height: 60px;
    border-radius: 50%;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
}}
</style>

<div class="floating-container">
    <div class="floating-text">💬 상담 하기</div>
    <a href="{kakao_open_chat_link}" target="_blank" class="floating-btn">
        <img src="https://developers.kakao.com/assets/img/about/logos/kakaotalksharing/kakaotalk_sharing_btn_medium.png">
    </a>
</div>
"""

st.markdown(floating_button, unsafe_allow_html=True)
