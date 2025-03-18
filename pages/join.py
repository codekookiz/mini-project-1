import streamlit as st

# CSS로 카드 이미지 스타일 정의 (둥근 모서리, 클릭 커서 등)
st.markdown(
    """
    <style>
    .card-img {
        border-radius: 15px;
        width: 100%;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .card-img:hover {
        transform: scale(1.05);
    }
    .card-container {
        padding: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def render_card(img_url, link_url):
    """
    카드 한 장의 HTML을 생성합니다.
    이미지 클릭 시 link_url을 팝업 창으로 열도록 구현합니다.
    """
    card_html = f"""
    <div class="card-container">
        <a href="{link_url}" target="_blank">
            <img class="card-img" src="{img_url}" alt="이미지">
        </a>
    </div>
    """
    return card_html

st.title("카드 뉴스 예시")

# 카드에 표시할 이미지 URL
card_images = [
    "https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2025/02/28/event-hmc-visit-showroom-suv-2503-banner-739x489.jpg",
    "https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2025/02/27/event-hmg-driving-experience-invite-nurburgring-24-list-thumb-352x233.jpg",
    "https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2025/02/28/event-hyundai-tradein-2025-banner-739x489.jpg"
]

# 클릭 시 팝업으로 열릴 링크 (여기서는 이미지 링크와 다르게 설정 가능)
card_links = [
    "https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2025/03/13/event-hmc-visit-showroom-suv-2503-page-pc-1120xa-03.jpg",
    "https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2025/02/27/event-hmg-driving-experience-invite-nurburgring-24-page-pc-1120xa.jpg",
    "https://www.hyundai.com/content/dam/hyundai/kr/ko/data/event/2025/02/28/event-hyundai-tradein-2025-page-pc-1120xa-01.png"
]

# 이미지 아래에 표시할 텍스트
top_texts = [
    "3월 팰리세이드 SUV 런치 이벤트\n2025.02.28 ~ 2025.04.06",
    "아반떼N, 아이오닉5N 슈퍼코프 이벤트\n2025.02.27 ~ 2025.03.30",
    "트레이드-인 투어 안내\n2025.02.28 ~ 2025.03.31"
]

cols = st.columns(3)
for col, img_url, link_url, text in zip(cols, card_images, card_links, top_texts):
    with col:
        st.markdown(render_card(img_url, link_url), unsafe_allow_html=True)
        st.write(text)

st.markdown("---")

# 아래 부분에 3x2 총 6개의 카드 (두 줄에 각각 3개씩)
st.subheader("진행중인 프로모션")
cards = ["유알엘을 넣으세요"] * 6
pages = ["page4", "page5", "page6", "page7", "page8", "page9"]

# 6개의 카드를 3열씩 두 줄로 배치
for i in range(0, 6, 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        with col:
            st.markdown(render_card(cards[idx], pages[idx]), unsafe_allow_html=True)

# 스위치 페이지 기능은 query parameter나 st.experimental_set_query_params 등으로 확장 가능합니다.
