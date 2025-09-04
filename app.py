import streamlit as st
from datetime import datetime

st.set_page_config(page_title="나의 포트폴리오", page_icon="🌟", layout="wide")

st.title("🌟 나만의 Streamlit 포트폴리오")
st.caption("20회차 종합 프로젝트 — 멀티페이지 버전")

st.markdown("""
이 앱은 5개의 페이지로 구성되어 있습니다.

1) **자기소개**  
2) **취미 시각화**  
3) **날씨 API**  
4) **미디어**  
5) **할 일 관리**
""")

# 화면에 페이지 파일명 다시 보여주기
PAGE_FILES = [
    "pages/01_자기소개.py",
    "pages/02_취미시각화.py",
    "pages/03_날씨_API.py",
    "pages/04_미디어.py",
    "pages/05_할일관리.py",
]

with st.expander("📄 현재 포함된 페이지 파일명 보기", expanded=True):
    st.write(PAGE_FILES)
    st.code("\n".join(PAGE_FILES), language="text")

st.divider()
st.info("왼쪽 사이드바의 페이지 메뉴에서 이동하세요. (Streamlit 멀티페이지 기능)")
st.caption(f"빌드 시각: {datetime.now():%Y-%m-%d %H:%M}")
