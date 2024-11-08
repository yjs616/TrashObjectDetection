import streamlit as st

def show_info(detected_class):
    st.title("객체 정보 화면")
    st.write(f"검출된 객체는 {detected_class} 입니다.")
    # 여기서 해당 객체에 대한 추가 정보를 제공할 수 있음
    # 예: 해당 객체의 재활용 방법, 분류 방법 등
