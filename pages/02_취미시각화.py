import streamlit as st
import pandas as pd

st.set_page_config(page_title="취미 시각화", page_icon="📊")

st.header("📊 나의 취미 활동 빈도")

data = {
    "취미": ["독서", "헬스", "여행", "게임", "요리"],
    "주간 횟수": [4, 3, 1, 2, 1],
}
df = pd.DataFrame(data)

left, right = st.columns([1, 2])
with left:
    st.subheader("표")
    st.table(df)

with right:
    st.subheader("바 차트")
    st.bar_chart(df.set_index("취미"))

max_hobby = df.loc[df["주간 횟수"].idxmax(), "취미"]
st.success(f"가장 많이 하는 취미는 **{max_hobby}** 입니다!")
