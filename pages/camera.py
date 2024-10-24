import streamlit as st

# 카메라 기능을 처리하는 함수들
def show_camera_info():
    st.title("카메라 정보 화면")
    st.write("알려줘! 기능에서 카메라를 호출하고 있습니다.")
    # 여기서 카메라 사용 관련 기능을 추가하면 됩니다.
    st.camera_input("카메라로 사진을 찍어보세요:")

def show_camera_action():
    st.title("카메라 실전 화면")
    st.write("실전으로! 기능에서 카메라를 호출하고 있습니다.")
    # 여기서 카메라 사용 관련 기능을 추가하면 됩니다.
    st.camera_input("실전 카메라 기능을 시작합니다:")

# 페이지에 따라 다른 카메라 기능을 실행
if 'page' in st.session_state:
    if st.session_state.page == 'camera_info':
        show_camera_info()
    elif st.session_state.page == 'camera_action':
        show_camera_action()
