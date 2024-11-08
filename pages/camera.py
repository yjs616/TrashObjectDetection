# camera.py

import sys
import os

# 정확한 경로를 추가합니다.
sys.path.append('/data/ephemeral/home/mmdetection/demo')

from streamlit_demo_mp4_3 import show_real_time_detection

def show_camera_action():
    config_path = '/data/ephemeral/home/mmdetection/configs/swin/faster_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco.py'
    checkpoint_path = '/data/ephemeral/home/mmdetection/work_dirs/epoch_36.pth'
    video_path = '/data/ephemeral/home/mmdetection/demo/IMG_04982.mp4'

    show_real_time_detection(config_path, checkpoint_path, video_path)
