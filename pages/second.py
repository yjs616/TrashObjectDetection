import streamlit as st
#from pages import camera

# Google Fonts의 Material Icons 사용
st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)

def load_second_page():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

        /*전체 페이지*/
        .stApp {{
            background-color: #d7f5d5;
            
        }}

        /*왼쪽 상단 back*/
        .back-icon{{     
            font-size:36px;
            color: #333333;  /* 검정색 */
            cursor: pointer;     
            transition: color 0.3s ease;  /* 부드러운 효과 */
            position: relative;
            left: -50px; /* 현재 위치에서 20px 오른쪽으로 이동 */
            top: 10px;  /* 현재 위치에서 10px 아래로 이동 */    
        }}

        /* 텍스트 스타일 */
        .text {{
            font-family: 'Gowun Dodum', sans-serif;
            font-size: 24px;
            color: #333333;
            margin-top: 120px;  /* 텍스트와 아이콘 사이 간격 조정 */
            margin-bottom: 40px;  /* 텍스트와 첫 번째 버튼 사이 간격 조정 */
            position: relative;
            left : 20px;
        }}

        /* 투명 버튼 스타일 (좀 더 수정해서 back 아이콘으로 적용해보자)*/
        div.stButton > button:first-child {{
            display: inline-block;  /* 나란히 배치 */
            width: 600px;  /* 버튼 크기 조정 */
            margin: 0px 20px;  /* 버튼 간격 좁게 */
            padding: 15px 0;
            background-color: transparent; /* 투명한 배경 */
            border: 2px solid #333333; /* 검정색 테두리 */
            border: none;
            border-radius: 20px;
            font-family: 'Gowun Dodum', sans-serif;
            font-size: 24px;
            color: #333333;
            cursor: pointer;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            position: relative;
        }}

        /* 버튼 스타일 */
        div.stButton > button:first-child {{
            display: inline-block;  /* 나란히 배치 */
            width: 600px;  /* 버튼 크기 조정 */
            margin: 0px 20px;  /* 버튼 간격 좁게 */
            padding: 15px 0;
            background-color: #92BA83;
            border: none;
            border-radius: 20px;
            font-family: 'Gowun Dodum', sans-serif;
            font-size: 24px;
            color: #333333;
            cursor: pointer;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            position: relative;
        }}

        div.stButton > button:first-child:active {{
            background-color: #F3FFE7;
            color: #333333;
        }}

        /* 기본 focus 스타일을 제거 */
        div.stButton > button:first-child:focus {{
            outline: none;
        }}
        /* 마우스 오버 시 버튼 색상 약간 변경 */
        div.stButton > button:first-child:hover {{
            background-color: #86a973;
        }}


        /* 반응형 미디어 쿼리 (화면 너비 768px 이하) */
        @media (max-width: 768px) {{
            .back-icon {{
                font-size: 28px;  /* 아이콘 크기 줄이기 */
                top: -30px;    /* 모바일에서 아이콘을 더 위쪽으로 */
                left: -30px;   /* 모바일에서 아이콘을 더 왼쪽으로 */
                
            }}

            .text {{
                font-size: 28px;  /* 텍스트 크기 줄이기 */
                margin-top: 100px;
                margin-bottom: 30px;  /* 모바일 텍스트와 버튼 사이 간격 */
                
                
            }}

            div.stButton > button:first-child {{
                width: 350px;     /* 버튼 크기 줄이기 */
                font-size: 18px;  /* 버튼 텍스트 크기 줄이기 */
                margin: 8px auto;  /* 모바일에서 버튼 간격 */
                top: 150px;        /* 하단에서 더 위로 */
            }}
        }}

        </style>
        """, unsafe_allow_html=True
    )

    #back button
    #if st.markdown(
    #    """
    #    <span class="material-icons back-icon" onclick="window.history.back()">arrow_back</span>
    #    """,
    #    unsafe_allow_html=True
    #):
    #    st.session_state.page == 'intro'
    #    #st.rerun()

    #main 텍스트
    st.markdown(
        """
        <div class="text">
            지구를 지키러 가보자!<br>하핫🚀
        </div>
        """,
        unsafe_allow_html=True
    )
    # back-icon을 눌렀을 때 start.py로 돌아가기
    if st.button("뒤로가기 🔙"):
        st.session_state.page = 'intro'
        st.rerun()
    # 버튼들 (컨테이너로 중앙 정렬)
    if st.button("알려줘!📝"):
        st.session_state.page = 'camera_info'  # 알려줘! 버튼 클릭 시
        #camera.show_camera_info()
        st.rerun()

    if st.button("실전으로!🌍"):
        st.session_state.page = 'camera_action'  # 실전으로! 버튼 클릭 시
        #camera.show_camera_action()
        st.rerun()


# second.py의 페이지 함수 실행
#load_second_page()
