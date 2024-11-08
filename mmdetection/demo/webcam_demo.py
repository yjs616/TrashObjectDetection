# Copyright (c) OpenMMLab. All rights reserved.
#V3
import argparse

import cv2
import mmcv
import torch

from mmdet.apis import inference_detector, init_detector
from mmdet.registry import VISUALIZERS

import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(description='MMDetection webcam demo')
    parser.add_argument('config', help='test config file path')
    parser.add_argument('checkpoint', help='checkpoint file')
    parser.add_argument(
        '--device', type=str, default='cuda:0', help='CPU/CUDA device option')
    parser.add_argument(
        '--camera-id', type=int, default=0, help='camera device id')
    parser.add_argument(
        '--score-thr', type=float, default=0.5, help='bbox score threshold')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    # build the model from a config file and a checkpoint file
    device = torch.device(args.device)
    model = init_detector(args.config, args.checkpoint, device=device)

    # 체크포인트 로드 시 strict=False로 설정하여 가중치 불일치 무시
    #checkpoint = torch.load(args.checkpoint, map_location=args.device)

    # bbox_head.cls_header에서 90개의 클래스 가중치를 10개로 조정
    #checkpoint['state_dict']['bbox_head.cls_header.pointwise_conv.weight'] = checkpoint['state_dict']['bbox_head.cls_header.pointwise_conv.weight'][:10, :, :, :]
    #checkpoint['state_dict']['bbox_head.cls_header.pointwise_conv.bias'] = checkpoint['state_dict']['bbox_head.cls_header.pointwise_conv.bias'][:10]

    # 수정된 체크포인트를 다시 저장
    #torch.save(checkpoint, args.config)

    #model.load_state_dict(checkpoint['state_dict'], strict=False)

    # init visualizer
    visualizer = VISUALIZERS.build(model.cfg.visualizer)
    # the dataset_meta is loaded from the checkpoint and
    # then pass to the model in init_detector
    visualizer.dataset_meta = model.dataset_meta

    camera = cv2.VideoCapture('/data/ephemeral/home/mmdetection/f9b4ce3a68db4d8e916a6a36a81aa802.mp4') #args.camera_id

    print('Press "Esc", "q" or "Q" to exit.')
    while True:
        ret_val, img = camera.read()
        print('aaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhh :', img)
        print(type(img))
        result = inference_detector(model, img)

        img = mmcv.imconvert(img, 'bgr', 'rgb')
        visualizer.add_datasample(
            name='result',
            image=img,
            data_sample=result,
            draw_gt=False,
            pred_score_thr=args.score_thr,
            show=False)

        img = visualizer.get_image()
        img = mmcv.imconvert(img, 'bgr', 'rgb')
        #cv2.imshow('result', img)
        # 이미지 파일로 저장
        cv2.imwrite('result.jpg', img)

        #ch = cv2.waitKey(1)
        #if ch == 27 or ch == ord('q') or ch == ord('Q'):
        #    break
        # 수정된 코드 (waitKey 제거)
        ch = ord('q')  # 예: 항상 'q'로 종료하는 것처럼 설정


if __name__ == '__main__':
    main()
