# TrashObjectDetection
Object Detection 프로젝트 진행 후 만든 데모입니다 🌏 🗑️


## ObjectDetection Projects
[💻More Information](https://github.com/boostcampaitech7/level2-objectdetection-cv-07)


## Demo
### 1. 실시간 웹캠 객체 탐지
```plaintext
mmdetection/demo/streamlit_demo_webcam.py
```
[<img src="https://github.com/user-attachments/assets/08c83020-4e2e-4e25-b785-8be7164f4d16" width="800"/>](https://github.com/user-attachments/assets/4c7aceaa-c14a-4f63-b839-7bd55f4614f5)

### 2. 실시간 비디오 객체 탐지
```plaintext
mmdetection/demo/streamlit_demo_mp4_3.py
```
[<img src="https://github.com/user-attachments/assets/31697004-9a6e-4a41-87a9-8efb08c39f03" width="800"/>](https://github.com/user-attachments/assets/31697004-9a6e-4a41-87a9-8efb08c39f03)


## Demo pages
![스크린샷 2024-11-08 오후 2 01 35](https://github.com/user-attachments/assets/1bda3ff5-209f-421c-9ac1-1caa2f5b3d38)
![스크린샷 2024-11-08 오후 2 01 49](https://github.com/user-attachments/assets/0e893219-42c5-4d91-99bc-3145cd97f454)
![스크린샷 2024-11-08 오후 2 02 04](https://github.com/user-attachments/assets/b274e25a-5fe6-40d9-97c9-129aaab9e198)
![스크린샷 2024-11-08 오후 2 02 24](https://github.com/user-attachments/assets/71f2c31e-2d32-465e-9a42-66660c59d886)
![스크린샷 2024-11-08 오후 2 02 46](https://github.com/user-attachments/assets/e58565e1-e98c-4ff8-81b5-0758063a1bcd)

## class characters
![스크린샷 2024-11-09 오후 11 35 36](https://github.com/user-attachments/assets/8749eb67-63bd-42ba-ac57-806396ba10f3)

출처-GPT

## 실행
```plaintext
streamlit run {디렉터리경로/}app.py
```

## requirements
```plaintext
pip install -r requirements.txt
```
```plaintext
numpy==1.26.4
opencv-python==4.10.0.84
torch==2.5.0
mmcv==2.1.0
mmdet==3.3.0
streamlit==1.36.0
mmengine==0.10.5
```



## Tree
```plaintext
TrashObjectDetection/
├── .git/
├── app/
│   ├── app.py
│   └── app.txt
├── assets/
│   ├── assets.txt
│   ├── character.png
│   ├── sample.mp4
│   ├── speechbubble.png
│   └── test.mp4
├── mmdetection/
└── pages/
    ├── camera.py
    ├── help.py
    ├── info.py
    ├── second.py
    ├── start.py
    └── class_info.json
├── README.md
├── requirement.txt
├── packages.txt
└── tree.txt
```
