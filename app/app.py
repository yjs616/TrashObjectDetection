import sys
import os
import streamlit as st
from PIL import Image


# 상위 디렉토리로 경로 추가 (pages 등 프로젝트 내 모듈 불러오기용)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# mmdetection 폴더를 경로에 추가 (streamlit_demo_mp4_3 모듈 불러오기용)
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'mmdetection'))

from pages import start, second, info, help
#from mmdetection.demo.streamlit_demo_mp4_3 import show_real_time_detection
from mmdetection.demo.streamlit_demo_webcam import show_real_time_detection  # 웹캠 사용 시

def main():
    # 페이지 전환 상태 관리
    if 'page' not in st.session_state:
        st.session_state.page = 'intro'

    # 페이지 상태에 따른 화면 전환
    if st.session_state.page == 'intro':
        start.show_intro()
    elif st.session_state.page == 'next':
        second.load_second_page()

    elif st.session_state.page == 'camera_info':
        config_path = './mmdetection/configs/swin/faster_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco.py'
        checkpoint_path = 'https://github.com/yjs616/TrashObjectDetection/releases/download/v1.0/epoch_36.pth' #./mmdetection/work_dirs/epoch_36.pth
        video_path = './assets/test.mp4'

        show_real_time_detection(config_path, checkpoint_path, show_info=True)
    elif st.session_state.page == 'camera_action':
        config_path = './mmdetection/configs/swin/faster_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco.py'
        checkpoint_path = 'https://github.com/yjs616/TrashObjectDetection/releases/download/v1.0/epoch_36.pth'
        video_path = './assets/test.mp4'

        show_real_time_detection(config_path, checkpoint_path, show_info=False)
    elif st.session_state.page == 'help':
        help.show_help()
        

if __name__ == "__main__":
    main()
