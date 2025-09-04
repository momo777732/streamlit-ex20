import streamlit as st

st.set_page_config(page_title="자기소개", page_icon="👋")

st.header("👋 자기소개")

name = "홍길동"
job = "데이터 분석가 지망생"
hobby = ["독서", "헬스", "여행"]

st.write(f"안녕하세요, 저는 **{name}** 입니다.")
st.write(f"현재는 {job} 준비 중이며, 관심 분야는 **데이터 시각화**와 **머신러닝**입니다.")

st.subheader("좋아하는 음식")
foods = ["떡볶이", "김밥", "치킨"]
st.markdown("- " + "\n- ".join(foods))

st.subheader("취미")
for h in hobby:
    st.text(f"✅ {h}")

st.caption("이 앱은 20회차 종합 프로젝트의 일부입니다.")
