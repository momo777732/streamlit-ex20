import streamlit as st
from pathlib import Path

st.set_page_config(page_title="미디어", page_icon="🎨")

st.header("🎨 미디어 소개")
st.caption("assets 폴더에 파일을 두고 상대경로로 불러옵니다.")

img_path = Path("assets/profile.jpg")
audio_path = Path("assets/sample.mp3")
video_path = Path("assets/sample.mp4")

if img_path.exists():
    st.image(str(img_path), caption="나의 프로필 사진", width=250)
else:
    st.warning("assets/profile.jpg 파일이 없습니다.")

st.divider()

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.info("assets/sample.mp3 파일이 없어서 오디오를 표시하지 않습니다.")

if video_path.exists():
    st.video(str(video_path))
else:
    st.info("assets/sample.mp4 파일이 없어서 비디오를 표시하지 않습니다.")
