import streamlit as st
import pandas as pd

st.set_page_config(page_title="프로젝트 정보", layout="wide")

st.title("자동화된 차량 추천 및 프로모션 관리 시스템")

st.markdown("## 1. 프로젝트 개요")
st.write("""
본 프로젝트는 현대자동차 고객 및 판매 데이터를 기반으로 **자동화된 차량 추천 및 프로모션 관리 시스템**을 구축하는 것을 목표로 합니다.
프로젝트에서 사용된 기술 영역은 다음과 같습니다:

- **데이터 전처리 및 가공**: 원본 데이터의 정제, 컬럼명 및 데이터 타입 수정, 이상치 보정과 신규 컬럼 추가를 통해 분석 효율성을 극대화
- **인공지능 모델 학습 및 최적화**: 연료 구분별로 최적화된 머신러닝 모델(Decision Tree, Random Forest, Gradient Boosting, Light GBM 등)을 활용하여 맞춤형 차량 추천 시스템 구현
- **Streamlit 기반 웹 애플리케이션 개발**: 직관적인 UI/UX를 제공하는 대시보드와 PWA 지원 웹 앱을 통해 고객 맞춤 서비스와 프로모션 정보를 손쉽게 전달
- **보안 강화 및 자동 배포**: secrets 관리와 GitHub Actions를 활용한 CI/CD 파이프라인 구축으로 보안성을 확보하고 신속한 업데이트를 지원
""")

st.markdown("---")

st.markdown("## 2. 데이터 전처리 및 가공")
st.write("")
st.write("""
### 데이터셋 정보
- 내용 : 현대자동차 회원 및 판매 데이터 (**고객db_확장본3.csv**)
- 총 데이터 수 : 292개
- 컬럼 정보
    - 이름, 생년월일, 성별, 휴대폰번호, 고객 세그먼트 등 고객 정보
    - 차량 구분, 구매한 제품, 구매 날짜, 거래 금액, 거래 방식 등 판매 정보
- 추가 데이터 출처 : **[현대자동차 공식 홈페이지](https://www.hyundai.com/kr/ko/e)**
""")

st.write("")

st.write("""
### 데이터 전처리 주요 내용 : Pandas, NumPy 활용
- 컬럼명 변환
    - 영문 컬럼명 제거
        - "이름 (Name)" -> "이름", "가입일 (Registration Date)" -> "가입일" 등
    - 의미가 모호한 컬럼명 수정
        - "고객 세그먼트" -> "고객 등급", "제품 구매 빈도" -> "차량 구매 횟수" 등
- 밸류 데이터타입 변환
    - "최근 거래 금액" : 데이터타입 변환 (str -> int)
    - "현재 나이" : 기존 "생년월일" 컬럼 이용해 연산 후 데이터타입 변환 (datetime -> int)
- 기존 원본 데이터에는 불완전한 정보가 포함되어 있으며, 이상치 존재
    - 직접 데이터 조작을 통한 이상치 처리
        - "제품 구매 날짜" : 미래의 날짜로 기록된 데이터 존재
            - "2025-12-01" -> 해당 데이터 삭제
    - 데이터 매핑을 통해 이상치 수정
        - "차량 유형" : 실제 차량 정보와 어긋나는 분류 상태
            - "G80 (RG3)" : "픽업트럭" -> "대형 세단"으로 수정
        - "최근 거래 금액" : 실제 차량 가격과 크게 어긋나는 데이터 존재
            - 차종별 실제 최소 가격과 최대 가격 사이의 범위 중 랜덤 값을 생성하여 대체 : np.random.randint()
            - "G80 (RG3)" : "30240000" -> "86000000"으로 수정
- 신규 컬럼 추가
    - 기존 컬럼을 활용한 신규 컬럼 추가
        - "차량 유형" : "차량 사이즈"와 "차량 유형"으로 분리
        - "연령대" : "현재 나이"를 기반으로 연령대 분류
    - 데이터 수집을 통한 신규 컬럼 추가
        - "연료 구분" : **[현대자동차 홈페이지](https://www.hyundai.com/kr/ko/e/all-vehicles)**
        - "모델 사진" : 구글 이미지 검색
""")

st.write("""
#### 전처리된 데이터를 CSV 파일로 저장하여 학습 및 예측 모델에서 활용 (파일명 : **고객db_전처리.csv**)
""")

st.write("######")

st.markdown("### 주요 전처리 작업")
prep_data = {
    "전처리 작업" : ["컬럼명 수정", "이상치 제거", "신규 컬럼 추가", "피치 스케일링"],
    "세부 내용" : ["영문 컬럼명 제거, 의미가 모호한 컬럼명 수정", "직접 데이터 조작, 데이터 매핑", "기존 컬럼 조작, 실제 데이터 수집", "데이터 정규화"]
}

prep_df = pd.DataFrame(prep_data, index=["1", "2", "3", "4"])

col1, col2 = st.columns(2)
with col1:
    st.dataframe(prep_df)

st.markdown("---")

st.markdown("## 3. 보안 설정 및 자동 배포")
st.write("""
### 보안 강화 및 GitHub 자동 배포
- API 키를 보호하기 위해 `.env` 파일을 사용하려 했으나, Streamlit과의 호환성 문제로 인해 `secrets.toml` 파일을 활용하는 방식으로 변경
    - API 키 : KAKAO_API_KEY = "API_KEY" 형태로 저장
- Streamlit Cloud 환경에서 자동화된 CI/CD 파이프라인 구축
    - Deploy 키 활용하여 Streamlit Cloud와 GitHub Repository 연동
""")

st.markdown("### GitHub 자동 배포 흐름")
st.markdown("""
1. 로컬 개발 환경에서 코드 변경
    - 로컬 환경에서 코드 변경 및 테스트
    - `secrets.toml` 파일을 활용하여 API 키 관리
2. GitHub Repository에 코드 푸시
    - 코드 변경 사항을 GitHub에 푸시
    - `.gitignore`에 `secrets.toml` 파일 추가하여 보안 강화
3. 자동 배포 (Streamlit Cloud)
    - GitHub에 푸시된 코드를 자동으로 배포
    - Streamlit Cloud를 통해 웹 애플리케이션 호스팅
""")

st.markdown("---")

st.markdown("## 4. 인공지능 학습 및 모델 최적화")
st.write("""
### 머신러닝 모델링 과정
- 사용자의 입력 데이터를 기반으로, 추천 차량의 제품명을 도출하는 Classificaion 문제
    - 입력 데이터 : 거주 지역, 구매 예산, 차량 선호 사이즈, 차량 선호 유형, 선호 연료 유형
    - 출력 데이터 : 추천 차량 제품명
- 인코딩 실시
    - 범주형 데이터로 구성된 입력 데이터를 수치형 데이터로 변환
        - 변환 컬럼 : "거주 지역", "차량 사이즈", "차량 유형", "연료 구분"
        - 변환 방법 : `get_dummies()` -> One-Hot Encoding
- 인코딩 완료한 데이터를 기반으로, 특정 연료 구분(예 : 디젤)에 해당하는 데이터 추출하여 학습 진행
    - 각 연료 구분에 대하여 9가지의 인공지능 모델을 활용
        - `LogisticRegression`, `Support Vector Classification`, `Decision Tree Classifier`,
        - `Random Forest Classifier`, `Gradient Boosting Classifier`, `Gaussian Naive Bayes`,
        - `K-Neighbors Classifier`, `Light GBM Classifier`, `Cat Boost Classifier`
    - 각 모델의 성능을 평가하여 가장 높은 성능을 보인 모델을 최종 선정
""")

st.write("""
### 모델 제작 특이점
- **연료 구분별 모델링** : 연료 구분에 따라 모델링을 실시하여, 연료별 차량 추천 모델을 개별적으로 구축함
    - 하나의 모델로 추천 시스템을 구축할 경우 선호하는 연료 유형과 다른 연료 유형의 차량이 추천될 수 있음
- **모델 부분 구축** : 수소, 플러그인 하이브리드, 하이브리드 유형에 대해서는 모델 개발을 진행하지 않음
    - **수소** : 데이터셋 내에 수소 차량은 NEXO(FE) 모델만 존재
        - 모델 개발 필요성이 없음
    - **플러그인 하이브리드** : 데이터셋 내에 플러그인 하이브리드 차량은 Santa-Fe (MX5 PHEV), Tucson (NX4 PHEV) 모델 2종 존재
        - 총 데이터 개수가 3개로, Train/Test 데이터셋 분리 이후 모델 학습이 불가능하여 모델 개발을 진행하지 않음
    - **하이브리드** : 데이터셋 내에 하이브리드 차량은 Grandeur (GN7 HEV) 모델만 존재
        - 모델 개발 필요성이 없음
""")

st.markdown("### 테스트한 머신러닝 모델 정확도")
model_data = {
    "디젤 모델": ["91.7%", "91.7%", "100%", "100%", "100%", "91.7%", "91.7%", "91.7%", "100%"],
    "전기 모델": ["100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%"],
    "휘발유 모델": ["27.3%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%"]
}

df = pd.DataFrame(model_data, index=["Logistic Regression", "Support Vector Classification", "Decision Tree Classifier",
                                     "Random Forest Classifier", "Gradient Boosting Classifier", "Gaussian Naive Bayes",
                                     "K-Neighbors Classifier", "Light GBM Classifier", "Cat Boost Classifier"])

def highlight_rows(row):
    highlight_color = "background-color: lightyellow"

    highlight_rows_list = ["Decision Tree Classifier", "Random Forest Classifier",
                           "Gradient Boosting Classifier", "Light GBM Classifier"]

    if row.name in highlight_rows_list:
        return [highlight_color] * len(row)
    else:
        return [""] * len(row)

model_styled_df = df.style.apply(highlight_rows, axis=1)

col1, col2 = st.columns(2)
with col1:
    st.dataframe(model_styled_df)

st.markdown("### 최종 모델 선정")
st.write("""
- 전반적으로 높은 정확도를 기록하였으나, 모든 모델을 사용하기에 처리 부하가 커질 우려가 있었음
    - 따라서, **Decision Tree**, **Random Forest**, **Gradient Boosting**, **Light GBM** 모델을 사용하기로 결정함
    - 총 모델의 개수는 **4종류(모델 유형)** X **3종류(연료 유형)** = 12개
- 12개 모델을 `.pkl` 파일로 저장하여 프로젝트에서 활용이 가능하도록 함
""")

st.markdown("---")

st.markdown("## 5. Streamlit 기반 웹 애플리케이션 구축")
st.write("""
### Streamlit 활용
- 고객이 원하는 차량을 추천하고, 프로모션 정보를 제공하는 대시보드를 Streamlit으로 구축함.
- 직관적인 UI/UX를 설계하여 사용자가 쉽게 차량을 선택하고 혜택을 비교할 수 있도록 함.
- Progressive Web App(PWA) 형태로 개발하여 모바일과 PC에서 모두 원활하게 동작하도록 구현함.
""")

st.write("")

st.markdown("### 주요 기능")
app_data = {
    "주요 기능": ["차량 추천 시스템", "기존 데이터 분석", "마케팅 전략 수립", "매장 찾기 서비스", "관리자 서비스"],
    "상세 설명": ["인공지능 모델을 활용한 맞춤형 차량 추천", "고객과 판매 데이터를 기반으로 한 데이터 분석", "고객 정보를 바탕으로 한 프로모션 전략 수립",
              "검색 지역의 매장을 찾을 수 있는 서비스", "고객 상담 및 프로모션 관리를 위한 직원용 시스템"]
}

df = pd.DataFrame(app_data)

st.dataframe(df, hide_index=True)

st.write("")

st.markdown("### 페이지별 기능 소개")
st.write("""
#### 1. 차량 추천
- 사용자가 입력한 정보를 기반으로, 추천 차량을 제공
- 선호하는 연료 유형에 따라, 해당 연료 유형에 대한 모델을 활용하여 추천
- 추천 차량의 이미지와 정보를 제공
    - 입력한 정보 범주에 해당하는 차량 추천
    - 결과값이 없을 경우, "추천할 차량이 없습니다" 메시지 출력
        - 전기차 옵션 선택 유도 메시지 출력
- 전기차 추천 탭 선택 시 지역별 보조금 안내 정보 제공
    - 입력한 예산에 보조금을 더한 값 범위에 해당하는 전기 차량 추천

#### 2. 데이터 분석
- 고객 데이터와 판매 데이터를 분석하여, 고객의 성향을 파악
    - 성별, 연령대, 차량 구매 횟수 등의 정보를 시각화하여 제공
    - 고객의 성향을 바탕으로, 마케팅 전략을 수립
         
#### 3. 마케팅 전략 수립
- 고객 데이터를 기반으로, 마케팅 및 프로모션 전략을 제공
    - 카드사 제휴 및 혜택 정보 제공, 마케팅 전략 수립에 활용
    - 고객 정보를 바탕으로, 맞춤형 프로모션 개발
        - 연령대, 지역, 고객 등급 기반
        - 고객 세분화 실시
         
#### 4. 매장 찾기
- 사용자가 입력한 지역에 해당하는 매장을 찾아주는 서비스
    - 사용자가 입력한 지역의 매장 정보를 제공
    - 매장의 위치, 연락처, 영업시간 등의 정보를 제공
         - 카카오맵 API 활용
         - 지도 내 입력 결과 클릭 시 세부 정보 및 길찾기 서비스 제공

#### 5. 관리자 서비스
- 관리자 페이지를 통해, 고객 정보 관리 및 프로모션 정보 관리
    - 고객 정보 기반으로 적용 가능한 맞춤형 프로모션 정보 제공
    - 할부 및 리스 관련 수치 계산, 혜택 정보 제공 서비스
    - 고객 입력 정보 기반으로 상담 내용 정리하는 PDF 파일 생성
""")

st.markdown("---")

st.markdown("## 6. 결과 및 기대 효과")
st.write("""
### 프로젝트 최종 결과
- 기존 데이터의 불완전성을 해결하여 보다 정확한 차량 추천이 가능
- 머신러닝 모델 최적화를 통해 예측 성능을 향상시켰으며, 실시간 응답 속도를 개선
- 보안 강화 위해 `secrets.toml` 파일을 활용하여 API 키 관리
- Streamlit 기반으로 개발하여 웹과 모바일 환경에서도 쉽게 접근할 수 있도록 설계
""")

st.markdown("### 기대 효과")
st.table([
    ["고객 만족도 증가", "맞춤형 프로모션 정보 제공을 통해 사용자 경험 개선"],
    ["업무 자동화", "영업사원이 프로모션을 쉽게 조회하고 고객에게 제공 가능"],
    ["운영 비용 절감", "데이터 분석 및 머신러닝 활용으로 최적의 혜택 제공"],
    ["보안 강화", "환경 변수 관리 및 CI/CD 자동화를 통한 보안 유지"]
])

st.write("""
본 프로젝트를 통해 차량 추천 및 프로모션 관리를 자동화하여, 
고객과 영업사원이 더욱 효과적으로 차량을 선택하고 혜택을 누릴 수 있도록 개선함.
""")
