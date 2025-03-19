import streamlit as st
import pandas as pd

st.set_page_config(page_title="프로젝트 정보", layout="wide")

st.title("자동화된 차량 추천 및 프로모션 관리 시스템")

st.markdown("## 1. 프로젝트 개요")
st.write("""
본 프로젝트는 데이터 전처리, 인공지능 학습, Streamlit 기반 대시보드 개발, GitHub 자동 배포, 보안 강화를 포함한 
**자동화된 차량 추천 및 프로모션 관리 시스템**을 구축하는 것을 목표로 합니다. 
이를 위해 Jupyter Notebook을 활용한 **데이터 전처리 및 머신러닝 모델 학습**, 
**Streamlit을 통한 웹 애플리케이션 구축**, 그리고 **GitHub Actions 기반의 자동화된 배포 시스템**을 구현하였습니다.
""")

st.markdown("---")

st.markdown("## 2. 데이터 전처리 및 가공")
st.write("""
### 데이터 전처리 주요 내용
- 기존 원본 데이터에는 불완전한 정보가 포함되어 있으며, 결측치 및 이상치가 존재함.
- 데이터 정제 및 변환을 위해 **Pandas, NumPy, Scikit-learn**을 활용하여 **정규화, 스케일링, 이상치 제거** 등의 전처리 작업을 수행함.
- 전처리된 데이터를 CSV 및 Pickle 파일로 저장하여 학습 및 예측 모델에서 활용함.
""")

st.markdown("### 주요 전처리 작업")
st.table([
    ["결측치 처리", "평균 대체 (Mean Imputation), KNN Imputer 적용"],
    ["이상치 제거", "IQR(사분위 범위) 기반 이상치 필터링"],
    ["데이터 정규화", "Min-Max Scaling 및 Standard Scaling 적용"],
    ["특성 엔지니어링", "PCA(주성분 분석) 활용 차원 축소"]
])

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
        - 변환 방법 : get_dummies() -> One-Hot Encoding
- 인코딩 완료한 데이터를 기반으로, 특정 연료 구분(예 : 디젤)에 해당하는 데이터 추출하여 학습 진행
    - 각 연료 구분에 대하여 9가지의 인공지능 모델을 활용
        - LogisticRegression, SVC, Decision Tree Classifier, Random Forest Classifier, Gradient Boosting Classifier, Gaussian Naive Bayes, K-Neighbors Classifier, Light GBM Classifier, Cat Boost Classifier
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
data = {
    "디젤 모델": ["91.7%", "91.7%", "100%", "100%", "100%", "91.7%", "91.7%", "91.7%", "100%"],
    "전기 모델": ["100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%"],
    "휘발유 모델": ["27.3%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%"]
}

df = pd.DataFrame(data, index=["Logistic Regression", "SVC", "Decision Tree Classifier", "Random Forest Classifier",
                               "Gradient Boosting Classifier", "Gaussian Naive Bayes", "K-Neighbors Classifier", "Light GBM Classifier",
                               "Cat Boost Classifier"])

def highlight_rows(row):
    highlight_color = "background-color: lightyellow"

    highlight_rows_list = ["Decision Tree Classifier", "Random Forest Classifier",
                           "Gradient Boosting Classifier", "Light GBM Classifier"]

    if row.name in highlight_rows_list:
        return [highlight_color] * len(row)
    else:
        return [""] * len(row)

styled_df = df.style.apply(highlight_rows, axis=1)

col1, col2 = st.columns(2)
with col1:
    st.dataframe(styled_df)

st.markdown("### 최종 모델 선정")
st.write("""
- 전반적으로 높은 정확도를 기록하였으나, 모든 모델을 사용하기에 처리 부하가 커질 우려가 있었음
    - 따라서, **Decision Tree**, **Random Forest**, **Gradient Boosting**, **Light GBM** 모델을 사용하기로 결정함
    - 총 모델의 개수는 **4종류(모델 유형)** X **3종류(연료 유형)** = 12개
- 12개 모델을 '.pkl' 파일로 저장하여 프로젝트에서 활용이 가능하도록 함
""")

st.markdown("---")

st.markdown("## 5. Streamlit 기반 웹 애플리케이션 구축")
st.write("""
### Streamlit 활용
- 고객이 원하는 차량을 추천하고, 프로모션 정보를 제공하는 대시보드를 Streamlit으로 구축함.
- 직관적인 UI/UX를 설계하여 사용자가 쉽게 차량을 선택하고 혜택을 비교할 수 있도록 함.
- Progressive Web App(PWA) 형태로 개발하여 모바일과 PC에서 모두 원활하게 동작하도록 구현함.
""")

st.markdown("### 주요 기능")
st.table([
    ["차량 추천 시스템", "인공지능 모델을 활용한 맞춤형 차량 추천"],
    ["할부 계산기", "고객이 할부 조건을 선택하면 실시간 월 납입금 계산"],
    ["프로모션 비교", "두 개의 차량을 선택하여 할인 및 혜택 비교"],
    ["고객 전용 화면", "고객이 새로운 창에서 맞춤형 프로모션 정보 확인"]
])

st.markdown("---")

st.markdown("## 6. 결과 및 기대 효과")
st.write("""
### 프로젝트 최종 결과
- 기존 데이터의 불완전성을 해결하여 보다 정확한 차량 추천이 가능해짐.
- 머신러닝 모델 최적화를 통해 예측 성능을 향상시켰으며, 실시간 응답 속도를 개선함.
- 보안 강화를 위해 환경 변수를 `secrets.toml` 파일을 활용하여 관리함.
- Streamlit 기반으로 개발하여 웹과 모바일 환경에서도 쉽게 접근할 수 있도록 설계함.
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
