import streamlit as st

# 화면 전환을 처리하는 함수
def show_help():
    # 이미지 URL
    bubble_image_url = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F4hYIE%2FbtsKg71BxMn%2FgrVjzMfHWWH6CM485cvw41%2Fimg.png"  # 말풍선 이미지 링크
    character_image_url = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcZuvHa%2FbtsKhbph2q2%2FDoGEiL2BYX0K1QZCyKCHIK%2Fimg.png"  # 캐릭터 이미지 링크

    # CSS 스타일 추가
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

        .stApp {{
            background-color: #d7f5d5;
        }}

        /* 말풍선 이미지 배경 스타일 */
        .speech-bubble {{
            width: 300px;
            height: 200px;
            position : absolute;
            top : 100px;
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
            top: 200px;      /* 상단에서부터 300px 아래로 이동 */
            left: 50%;     /* 왼쪽에서부터 100px 오른쪽으로 이동 */
            width: 40%;      /* 너비를 %로 지정하면 반응형 크기 조정 가능 */
            height: auto;    /* 비율을 유지하면서 높이를 자동으로 설정 */
            
        }}

        /* 말풍선 텍스트 */
        .speech-bubble-text {{
            font-family: 'Gowun Dodum', sans-serif;
            font-size: 24px;
            color: #333333;
            text-align: center;
        }}

        .rules {{
            margin-top: 450px;
            margin-left: 70px;
        }}

        /* 분리수거 4원칙 텍스트 */
        .rules p{{ 
            font-family: 'Gowun Dodum', sans-serif;
            font-size: 30px;
            color: #333333;
            text-align: left;
            margin-top: 10px;
        }}

        /* 분리수거 4원칙 텍스트 */
        .rules li {{ 
            font-family: 'Gowun Dodum', sans-serif;
            font-size: 30px;
            color: #333333;
            text-align: left;
            margin-top: 10px;
        }}

        /* 시작 버튼 스타일 */
        div.stButton > button:first-child {{
            width: 600px;
            height: 65px;
            font-family: 'Gowun Dodum', sans-serif;
            font-size: 36px;
            color: #333333;
            background-color: #92BA83;
            border: none;
            border-radius: 20px;
            position: absolute;
            cursor : pointer;
            top: 100px;
            left: 50%;                      /* 부모 컨테이너의 50% 지점으로 이동 */
            transform: translateX(-50%);    /* 요소의 크기만큼 왼쪽으로 이동해 완벽히 중앙 정렬 */
        }}

        /* 반응형 미디어 쿼리 */
        @media (max-width: 768px) {{
            .speech-bubble {{
                width: 200px;
                height: 100px;
            }}

            .speech-bubble-text {{
                font-size: 14px;
            }}

            .character {{
                width: 120px;
            }}

            .rules {{
                font-size: 16px;
            }}

            div.stButton > button:first-child {{
                width: 200px;
                height: 40px;
                font-size: 16px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 말풍선과 캐릭터 표시
    st.markdown(
        """
        <div class="speech-bubble">
            <span class="speech-bubble-text">자, 안녕!<br>내가 분리수거 </br>4원칙을 알려줄게! </br>꼭 기억하길!😉</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <img src="{character_image_url}" class="character">
        """,
        unsafe_allow_html=True
    )

    # 분리수거 4원칙 텍스트
    st.markdown(
        """
        <div class="rules">
            <p>분리수거 4원칙:</p>
            <ol>
                <li>내용물을 비우고</li>
                <li>이물질을 헹구고 🚰</li>
                <li>라벨 등을 분리하고 🏷️</li>
                <li>다른 재질과 섞이지 않게 하기 🗑️</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 시작 버튼
    if st.button("시작!!!!"):
        st.session_state.page = 'next'  # 페이지 전환
        st.rerun()

