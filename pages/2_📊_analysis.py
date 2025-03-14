import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 고객 분석 대시보드")

st.write("이 페이지에서는 고객 데이터를 분석하고 인사이트를 제공합니다.")

# 샘플 데이터 (향후 실제 데이터와 연결)
df = pd.DataFrame({
    "연령대": ["20대", "30대", "40대", "50대"],
    "고객 수": [50, 100, 80, 40]
})

# 간단한 바 그래프 예제
fig, ax = plt.subplots()
df.plot(kind="bar", x="연령대", y="고객 수", ax=ax)
st.pyplot(fig)
