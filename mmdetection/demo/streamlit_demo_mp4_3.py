# Copyright (c) OpenMMLab. All rights reserved.
#동영상에 있는 객체 실시간으로 탐지하는 코드 

import streamlit as st
import cv2
import torch
import json
from mmdet.apis import inference_detector, init_detector
from mmdet.registry import VISUALIZERS
from mmengine import Config
from PIL import Image
import numpy as np  # numpy 모듈 추가

#target_width = 640

# JSON 파일에서 클래스 정보를 불러오는 함수
def load_class_info(file_path="class_info.json"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

#"/data/ephemeral/home/class_info.json"
# JSON 파일에서 정보를 불러오기
class_info = load_class_info()

# CSS 스타일을 설정하는 함수
def apply_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
        
        .stApp {
            background-color: #d7f5d5;
        }
        * {
            font-family: 'Gowun Dodum', sans-serif;
            color: #333333;
        }
        .title-text {
            font-size: 36px;
            color: #333333;
            font-family: 'Gowun Dodum', sans-serif;
            margin-bottom: 30px;
        }
        .detected-object-text {
            font-size: 36px;
            color: #333333;
            font-family: 'Gowun Dodum', sans-serif;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton {
            display: flex;
            justify-content: center;
        }
        div.stButton > button:first-child {
            display: inline-block;
            width: 700px;
            margin: 0 auto;
            padding: 15px 0;
            background-color: #92BA83;
            border: none;
            border-radius: 20px;
            font-size: 24px;
            color: #333333;
            cursor: pointer;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            position: relative;
        }
        </style>
    """, unsafe_allow_html=True)

def display_class_info(detected_class, info_area):
    info = class_info.get(detected_class)
    if info:
        # 이미지와 텍스트를 함께 표시할 HTML 템플릿을 생성
        content = f"""
        <div style="text-align: center;">
            <img src="{info['image_path']}" width="200" style="margin-bottom: 20px;">
            <h3 class='detected-object-text'>나야, {info['name']}</h3>
            <p>{info['description']}</p>
        </div>
        """

        # info_area에 한 번에 콘텐츠를 업데이트
        info_area.markdown(content, unsafe_allow_html=True)
    else:
        info_area.markdown("알 수 없는 객체입니다.")


# 실시간 객체 감지 함수
def show_real_time_detection(config_path, checkpoint_path, video_path, show_info=True):
    apply_css()
    st.markdown("<h1 class='title-text'>지구 지키는 중 🌏</h1>", unsafe_allow_html=True)

    # 모델 초기화
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    cfg = Config.fromfile(config_path)
    if 'roi_head' in cfg.model:
        cfg.model.roi_head.mask_head = None
        cfg.model.roi_head.bbox_head.num_classes = 10

    # 클래스 정보 설정
    metainfo = {
        'classes': ("General trash", "Paper", "Paper pack", "Metal", "Glass", "Plastic", 
                    "Styrofoam", "Plastic bag", "Battery", "Clothing")
    }

    model = init_detector(cfg, checkpoint_path, device=device)
    visualizer = VISUALIZERS.build(model.cfg.visualizer)
    visualizer.dataset_meta = metainfo

    # 클래스 ID와 한국어 이름 매핑
    class_name_mapping = {
        "General trash": "일반쓰레기 🗑️",
        "Paper": "종이 📃",
        "Paper pack": "종이팩 🧃",
        "Metal": "금속🥫",
        "Glass": "유리🍸",
        "Plastic": "플라스틱 🗑️",
        "Styrofoam": "스티로폼 🗑️",
        "Plastic bag": "비닐봉지 🗑️",
        "Battery": "배터리 🔋",
        "Clothing": "의류 👕"
    }

    # 비디오 파일 열기
    cap = cv2.VideoCapture(video_path)


    stframe = st.empty()  # Streamlit 프레임 생성
    detected_text = st.empty()  # 객체 이름을 표시할 텍스트 공간
    info_area = st.empty()  # 객체 정보를 표시할 고정 공간

    if st.button("뒤로가기 🔙", key="back_button"):
        st.session_state.page = 'next'
        st.rerun()
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.warning("비디오 프레임을 가져올 수 없습니다. 비디오 경로나 파일을 확인하세요.")
            break

        # frame이 numpy 배열인지 확인
        if not isinstance(frame, np.ndarray):
            st.error("프레임 데이터가 올바르지 않습니다.")
            break

        result = inference_detector(model, frame)
        detected_objects = [obj for obj in result.pred_instances if obj.scores > 0.5]
        
        if len(detected_objects) == 1:
            class_id = int(detected_objects[0].labels)
            class_name = visualizer.dataset_meta['classes'][class_id]
            korean_name = class_name_mapping.get(class_name, "알 수 없는 객체")
            detected_text.markdown(f"<h2 class='detected-object-text'>{korean_name}</h2>", unsafe_allow_html=True)
            if show_info:
                display_class_info(class_name, info_area)  # 객체 정보 업데이트

        elif len(detected_objects) > 1:
            detected_text.markdown("<h2 class='detected-object-text'>한 개만 보여주세요!</h2>", unsafe_allow_html=True)
            info_area.empty()  # 중복 탐지 시 정보 창 비우기
        else:
            detected_text.markdown("<h2 class='detected-object-text'></h2>", unsafe_allow_html=True)
            info_area.empty()  # 탐지된 객체가 없으면 정보 창 비우기

        visualizer.add_datasample(
            name='result', image=frame, data_sample=result,
            draw_gt=False, pred_score_thr=0.5, show=False
        )

        display_img = visualizer.get_image()
        display_img = cv2.cvtColor(display_img, cv2.COLOR_BGR2RGB)
        
        stframe.image(display_img, channels="RGB", use_column_width=True) #True

    cap.release()

