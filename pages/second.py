import streamlit as st

def load_second_page():
    st.title("다음 화면입니다!")
    st.write("분리수거 교육을 시작합니다.")
    
    # 다시 첫 화면으로 돌아가는 버튼
    if st.button("처음으로 돌아가기"):
        st.session_state.page = 'intro'
        st.experimental_rerun()

# second.py의 페이지 함수 실행
#load_second_page()
