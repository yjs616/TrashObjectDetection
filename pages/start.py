import streamlit as st
from PIL import Image

# 초기 세션 상태 설정
if 'page' not in st.session_state:
    st.session_state.page = 'intro'  # 시작 페이지는 'intro'

def show_intro():
    # 첫 번째 화면
    if st.session_state.page == 'intro':
        # 이미지 URL (블로그 이미지 URL 사용)
        bubble_image_url = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F4hYIE%2FbtsKg71BxMn%2FgrVjzMfHWWH6CM485cvw41%2Fimg.png"
        character_image_url = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcZuvHa%2FbtsKhbph2q2%2FDoGEiL2BYX0K1QZCyKCHIK%2Fimg.png"

        # CSS 스타일 추가
        st.markdown(
            f"""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

            /* 전체 페이지 스타일 */
            .stApp {{
                background-color: #d7f5d5;
            }}

            /* 말풍선 이미지 배경 스타일 */
            .speech-bubble {{
                width: 300px;
                height: 200px;
                position : absolute;
                top : 200px;
                left: 30%;
                transform: translateX(-50%);
                background-image: url({bubble_image_url});
                background-size: 100% 100%;
                background-repeat: no-repeat;
                background-position: center;
                padding: 20px;       
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            /* 캐릭터 이미지 위치 및 비율 유지 */
            .character {{
                position: absolute;
                top: 300px;      /* 상단에서부터 300px 아래로 이동 */
                left: 50%;     /* 왼쪽에서부터 100px 오른쪽으로 이동 */
                width: 50%;      /* 너비를 %로 지정하면 반응형 크기 조정 가능 */
                height: auto;    /* 비율을 유지하면서 높이를 자동으로 설정 */
            
            }}

            /*폰트*/
            .speech-bubble-text {{
                font-family: 'Gowun Dodum', sans-serif;
                font-size: 30px;    /* 텍스트 크기 증가 */
                color: #333333;     /* 텍스트 색상 */
            }}

            /*버튼*/
            div.stButton > button:first-child{{   
                width : 600px;
                position : relative;
                top : 750px; 
                left : 50%;
                transform: translateX(-50%);
                background-color : #92BA83;
                border : none; 
                padding : 20px 0px;
                font-family: 'Gowun Dodum', sans-serif;
                font-size: 24px;    /* 텍스트 크기 증가 */
                color: #333333;     /* 텍스트 색상 */
                border-radius : 20px;
                cursor : pointer;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            }}

            /*버튼 클릭할 때*/
            div.stButton > button:first-child:active{{
                background-color : #F3FFE7;
                color: #333333;     /* 텍스트 색상 */
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            }}
            .custom-button:focus {{
                outline: none;
            }}


            /* 반응형 미디어 쿼리 (화면 너비 768px 이하) */
            @media (max-width: 768px) {{
                .speech-bubble {{
                    width: 200px;  /* 말풍선 크기 조정 */
                    height: 100px;
                    top: 180px;    /* 말풍선 위치 조정 */
                }}

                .speech-bubble-text {{
                    font-size: 16px;  /* 텍스트 크기 조정 */
                }}

                .character {{
                    width: 150px;  /* 캐릭터 크기 조정 */
                    top: 250px;    /* 캐릭터 위치 조정 */
                }}

                div.stButton > button:first-child {{
                    width : 350px;
                    padding : 10px;
                    font-size: 18px;     /* 버튼 텍스트 크기 조정 */
                    top: 550px;        /* 하단에서 더 위로 */
                }}

            }}
        
            </style>
            """,
            unsafe_allow_html=True
        )

        # 말풍선 텍스트 추가
        st.markdown(
            """
            <div class="speech-bubble">
                <span class="speech-bubble-text"> 같이...<br>분리수거 할래?</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 캐릭터 이미지 추가 (HTML과 CSS로 위치 조정)
        st.markdown(
            f"""
            <img src="{character_image_url}" class="character">
            """,
            unsafe_allow_html=True
        )

        #st.markdown(
        #    """
        #    <button class="custom-button">시작!</button>
        #    """,
        #    unsafe_allow_html=True
        #)


        #st.button에 커스텀 버튼 적용
        if st.button("시작!"):
            st.session_state.page='next' #페이지 상태 변경
            st.rerun() 

        if st.button("도움말💡"):
            st.session_state.page='help'
            st.rerun()

#def show_next_page():
#    import second
#    #st.experimental_rerun()  # 페이지 즉시 새로고침
#    second.load_second_page()

#def show_camera_action():
#    import camera
#    camera.show_camera_action() 

#if st.session_state.page=='intro':
#    show_intro()
#elif st.session_state.page == 'next':
#    show_next_page()
#elif st.session_state.page=='camera_action':
#    show_camera_action()

