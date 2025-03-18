import json
import re
import os
import time
import streamlit as st
import requests
from huggingface_hub import InferenceClient

# 📌 Hugging Face API 토큰 가져오기 (`secrets.toml`에서 불러오기)
def get_huggingface_token():
    try:
        return st.secrets["HUGGINGFACE_API_TOKEN"]
    except KeyError:
        st.warning("❌ Hugging Face API 토큰이 설정되지 않았습니다. `.streamlit/secrets.toml` 파일을 확인하세요.")
        return None

# 📌 Google Gemma-2-9B-IT 모델 API 호출 (3회 재시도)
def generate_text_via_api(prompt: str, model_name: str = "google/gemma-2-9b-it"):
    """Hugging Face API를 사용하여 텍스트를 생성합니다."""
    token = get_huggingface_token()
    if token is None:
        return "❌ API 토큰이 설정되지 않았습니다. `.streamlit/secrets.toml` 파일을 확인하세요."

    client = InferenceClient(model=model_name, api_key=token)

    max_retries = 3  # 최대 3회 재시도
    for attempt in range(max_retries):
        try:
            response = client.text_generation(prompt=prompt)
            return response
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2)  # 2초 대기 후 재시도
                st.warning(f"🔄 Hugging Face 서버 응답 없음. {attempt+1}/{max_retries}회 재시도 중...")
            else:
                return "❌ 현재 Hugging Face 서버가 응답하지 않습니다. 나중에 다시 시도하세요."

# 📌 사용자 입력 정리 (불필요한 단어 제거)
def clean_input(text: str) -> str:
    return re.sub(r"\b(해줘|알려줘|설명해 줘|추천해 줘|말해 줘)\b", "", text, flags=re.IGNORECASE).strip()

# 📌 자동차 기본 정보 및 가격/옵션 비교 기능
def get_car_info_based_on_question(user_input: str) -> str:
    """사용자의 질문을 분석하여 자동차 정보를 제공합니다."""
    clean_text = clean_input(user_input)
    prompt = f"""
    사용자의 질문을 바탕으로 자동차 정보를 제공합니다.
    - 사용자 질문: "{clean_text}"
    - 자동차의 구동 방식(4륜, 전륜, 후륜)에 대한 설명을 포함하세요.
    - 차량 금액 및 옵션별 가격 차이를 정확하게 설명하세요.
    - 특정 차량과 다른 차량 간 차이점도 설명하세요.

    예시:
    - 질문: "4륜이랑 전륜이나 후륜에 대해 설명해줘"
    - 답변:
      1. **전륜구동(FWD)**: 앞바퀴가 동력을 전달받아 움직이는 방식. 연비가 좋고, 눈길이나 빗길에서 안정적.
      2. **후륜구동(RWD)**: 뒷바퀴가 동력을 받아 주행. 스포츠카나 고급 세단에 많이 사용되며, 고속 주행 성능이 뛰어남.
      3. **사륜구동(AWD, 4WD)**: 네 바퀴가 모두 동력을 받아 주행. 오프로드 주행 성능이 우수하며, 눈길이나 산길에서 안정적.

    - 질문: "현대 아이오닉 6 옵션별 금액 차이 알려줘"
    - 답변:
      1. **스탠다드 트림**: 4,800만원, 주행거리 400km, 기본 편의 기능 제공
      2. **프리미엄 트림**: 5,300만원, 주행거리 450km, 고급 내장재 및 첨단 보조 시스템 포함
      3. **최고급 트림(풀옵션)**: 5,900만원, 주행거리 500km, 자율주행 기능 및 최고급 사양 포함
    """
    return generate_text_via_api(prompt)

# 🚀 Streamlit UI
st.title("🚗 AI 자동차 정보 시스템")

# 사용자 질문 입력
st.subheader("📋 자동차 관련 질문 입력")
user_question = st.text_area("🚀 원하는 자동차 관련 정보를 입력하세요!", placeholder="예: 4륜이랑 전륜/후륜의 차이점은?")

# 🚀 검색 버튼
if st.button("검색하기"):
    if user_question.strip() == "":
        st.warning("❗ 질문을 입력해주세요!")
    else:
        with st.spinner("답변을 생성 중입니다..."):
            time.sleep(3)
            st.success("✅ 답변이 생성되었습니다.")

        response = get_car_info_based_on_question(user_question)
        st.subheader("🔍 자동차 정보")
        st.write(response)