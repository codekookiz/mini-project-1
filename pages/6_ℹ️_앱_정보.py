import streamlit as st

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
- 환경 변수 및 API 키를 보호하기 위해 `.env` 파일을 사용하려 했으나, Streamlit과 호환되지 않아 `secrets.toml` 파일을 활용하는 방식으로 변경함.
- GitHub Actions를 활용하여 코드 변경 시 자동으로 애플리케이션을 배포하도록 설정함.
- Streamlit Cloud 또는 AWS EC2 환경에서 자동화된 CI/CD 파이프라인을 구축함.
""")

st.markdown("### GitHub 자동 배포 흐름")
st.markdown("""
1. 로컬 개발 환경에서 코드 변경
2. GitHub Repository에 코드 푸시
3. GitHub Actions 실행 (CI/CD 파이프라인)
4. 자동 배포 (Streamlit Cloud 또는 AWS)
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
    - 
""")

st.markdown("### 테스트된 머신러닝 모델 목록")
st.table([
    ["Decision Tree", "82.1%", "단순한 트리 기반 학습"],
    ["Random Forest", "89.3%", "다중 트리를 활용한 앙상블 학습"],
    ["LightGBM", "92.0%", "빠른 연산 속도, 대용량 데이터 적합"],
    ["Gradient Boosting", "91.5%", "단계적 학습으로 성능 향상"]
])

st.markdown("### 최종 모델 선정")
st.write("""
- **LightGBM**이 가장 높은 성능(92.0%)을 기록하였으며, 학습 속도가 빠르고 실시간 예측이 가능하여 최종 선택됨.
- 최적화된 LightGBM 모델을 `.pkl` 파일로 저장하여 Streamlit 애플리케이션에서 활용하도록 설계함.
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
