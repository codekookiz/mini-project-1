import streamlit as st

st.set_page_config(page_title="현대자동차 고객 추천 시스템", layout="wide")

# 메인 화면 구성
st.markdown("""
<h1 style="display:flex; align-items:center;">
    <img src="https://www.hyundai.com/etc/designs/hyundai/ww/en/images/common/logo.png" 
         alt="현대자동차 로고" 
         style="height:40px; margin-right:10px;">
    고객추천 시스템
</h1>
""", unsafe_allow_html=True)
st.write("이 앱은 머신러닝을 활용하여 고객에게 맞춤형 차량을 추천하는 시스템입니다.")

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

# 본인의 카카오톡 채널 ID 입력
channel_public_id = "_xfxhjXn"  # 올바른 채널 ID 반영

# 카카오톡 "채널 추가 버튼" & "채팅하기 버튼" HTML & JavaScript 코드
kakao_buttons = f"""
<style>
/* 버튼 컨테이너 스타일 (가로 정렬) */
.kakao-buttons-container {{
    display: flex;
    justify-content: center; /* 가운데 정렬 */
    align-items: center;
    gap: 15px; /* 버튼 간 간격 */
    margin-top: 20px; /* 위쪽 여백 */
    z-index: 1000;
}}

.kakao-button {{
    flex: 0 1 auto; /* 버튼 크기 자동 조정 */
}}
</style>

<!-- 버튼 컨테이너 -->
<div class="kakao-buttons-container">
    <!-- 카카오 채널 추가 버튼 -->
    <div id="kakao-talk-channel-add-button" class="kakao-button"
         data-channel-public-id="{channel_public_id}"
         data-size="large"
         data-support-multiple-densities="true"></div>

    <!-- 카카오 채팅하기 버튼 -->
    <div id="kakao-talk-channel-chat-button" class="kakao-button"
         data-channel-public-id="{channel_public_id}"
         data-title="consult"
         data-size="large"
         data-color="yellow"
         data-shape="pc"
         data-support-multiple-densities="true"></div>
</div>

<!-- 카카오톡 JavaScript SDK -->
<script>
  window.kakaoAsyncInit = function() {{
    Kakao.Channel.createAddChannelButton({{
      container: '#kakao-talk-channel-add-button'
    }});
    Kakao.Channel.createChatButton({{
      container: '#kakao-talk-channel-chat-button'
    }});
  }};

  (function(d, s, id) {{
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = 'https://t1.kakaocdn.net/kakao_js_sdk/2.7.4/kakao.channel.min.js';
    js.integrity = 'sha384-8oNFBbAHWVovcMLgR+mLbxqwoucixezSAzniBcjnEoumhfIbMIg4DrVsoiPEtlnt';
    js.crossOrigin = 'anonymous';
    fjs.parentNode.insertBefore(js, fjs);
  }})(document, 'script', 'kakao-js-sdk');
</script>
"""

# Streamlit에서 JavaScript 코드 실행 (버튼이 짤리지 않도록 높이 확보)
st.components.v1.html(kakao_buttons, height=100)