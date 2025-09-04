import streamlit as st

st.set_page_config(page_title="할 일 관리", page_icon="✅")

st.header("✅ 할 일 관리")

if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "done" not in st.session_state:
    st.session_state.done = []

with st.sidebar:
    st.subheader("할 일 추가")
    new_task = st.text_input("할 일을 입력하세요")
    if st.button("추가") and new_task:
        st.session_state.tasks.append(new_task)
        st.success("추가되었습니다.")

st.subheader("할 일 목록")
for i, task in enumerate(list(st.session_state.tasks)):
    cols = st.columns([6, 1])
    cols[0].write(f"- {task}")
    if cols[1].button("완료", key=f"done_{i}"):
        st.session_state.done.append(task)
        st.session_state.tasks.remove(task)
        st.rerun()

st.subheader("완료된 일")
if st.session_state.done:
    st.write(st.session_state.done)
else:
    st.caption("아직 완료 항목이 없습니다.")
