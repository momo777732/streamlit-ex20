import streamlit as st
import requests

st.set_page_config(page_title="날씨 API", page_icon="☀️")

st.header("☀️ 실시간 날씨 확인 (OpenWeather)")

# API 키는 반드시 secrets로 관리!
API_KEY = st.secrets.get("OPENWEATHER_API_KEY", None)

city = st.text_input("도시 이름을 입력하세요:", "Seoul")

btn = st.button("날씨 가져오기")

if btn:
    if not API_KEY:
        st.error("API 키가 설정되지 않았습니다. 관리자에게 문의하세요.")
    else:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric&lang=kr"
        )
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                data = res.json()
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]
                st.success(f"{city}의 현재 기온은 **{temp}°C**, 날씨는 **{weather}** 입니다.")
                with st.expander("원본 응답 보기"):
                    st.json(data)
            else:
                st.error(f"요청 실패 (status: {res.status_code}) — 도시명을 확인하세요.")
        except requests.exceptions.RequestException as e:
            st.error(f"요청 중 오류: {e}")
