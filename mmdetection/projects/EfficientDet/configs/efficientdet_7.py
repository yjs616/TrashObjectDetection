_base_ = [
    'mmdet::_base_/datasets/coco_detection.py',
    'mmdet::_base_/schedules/schedule_1x.py',
    'mmdet::_base_/default_runtime.py'
]
custom_imports = dict(
    imports=['projects.EfficientDet.efficientdet'], allow_failed_imports=False)

image_size = 768  # EfficientDet-B7은 더 큰 입력 이미지 크기를 사용합니다.
batch_augments = [
    dict(type='BatchFixedSizePad', size=(image_size, image_size))
]
dataset_type = 'CocoDataset'
evalute_type = 'CocoMetric'
norm_cfg = dict(type='SyncBN', requires_grad=True, eps=1e-3, momentum=0.01)
#checkpoint = 'https://download.openmmlab.com/mmclassification/v0/efficientnet/efficientnet-b8_3rdparty_8xb32-aa-advprop_in1k_20220119-297ce1b7.pth'  # EfficientNet-B7에 대한 사전학습된 체크포인트 URL
checkpoint = 'https://download.openmmlab.com/mmclassification/v0/efficientnet/efficientnet-b7_3rdparty_8xb32-aa-advprop_in1k_20220119-c6dbff10.pth'

metainfo = {
    'classes': ("General trash", "Paper", "Paper pack", "Metal", "Glass", "Plastic", 
                "Styrofoam", "Plastic bag", "Battery", "Clothing")
}

model = dict(
    type='EfficientDet',
    data_preprocessor=dict(
        type='DetDataPreprocessor',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        bgr_to_rgb=True,
        pad_size_divisor=image_size,
        batch_augments=batch_augments),
    backbone=dict(
        type='EfficientNet',
        arch='b7',  # EfficientNet-B7로 변경
        drop_path_rate=0.2,
        out_indices=(3, 4, 5),
        frozen_stages= 0,
        conv_cfg=dict(type='Conv2dSamePadding'),
        norm_cfg=norm_cfg,
        norm_eval=False,
        init_cfg=dict(
            type='Pretrained', prefix='backbone', checkpoint=checkpoint)),
    neck=dict(
        type='BiFPN',
        num_stages=8,
        in_channels=[80, 224, 640],  # EfficientNet-B7의 출력 채널에 맞게 조정
        out_channels=384,  # 더 큰 BiFPN 출력 채널
        start_level=0,
        norm_cfg=norm_cfg),
    bbox_head=dict(
        type='EfficientDetSepBNHead',
        num_classes=10,
        num_ins=5,
        in_channels=384,  # BiFPN 출력 채널에 맞게 조정
        feat_channels=384,
        stacked_convs=4,
        norm_cfg=norm_cfg,
        anchor_generator=dict(
            type='AnchorGenerator',
            octave_base_scale=4,
            scales_per_octave=3,
            ratios=[0.5, 1.0, 2.0],
            strides=[8, 16, 32, 64, 128],
            center_offset=0.5),
        bbox_coder=dict(
            type='DeltaXYWHBBoxCoder',
            target_means=[.0, .0, .0, .0],
            target_stds=[1.0, 1.0, 1.0, 1.0]),
        loss_cls=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=1.5,
            alpha=0.25,
            loss_weight=1.0),
        loss_bbox=dict(type='HuberLoss', beta=0.1, loss_weight=50)),
    # training and testing settings
    train_cfg=dict(
        assigner=dict(
            type='MaxIoUAssigner',
            pos_iou_thr=0.5,
            neg_iou_thr=0.5,
            min_pos_iou=0,
            ignore_iof_thr=-1),
        sampler=dict(
            type='PseudoSampler'),  # Focal loss should use PseudoSampler
        allowed_border=-1,
        pos_weight=-1,
        debug=False),
    test_cfg=dict(
        nms_pre=1000,
        min_bbox_size=0,
        score_thr=0.0, #0.05이하는 지워짐 -> 0, 0.05
        nms=dict(
            type='soft_nms',
            iou_threshold=0.3,
            sigma=0.5,
            min_score=1e-3,
            method='gaussian'),
        max_per_img=100))

# dataset settings
train_pipeline = [
    dict(type='LoadImageFromFile', backend_args={{_base_.backend_args}}),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='RandomResize',
        scale=(image_size, image_size),
        ratio_range=(0.1, 2.0),
        keep_ratio=True),
    dict(type='RandomCrop', crop_size=(image_size, image_size)),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]

#기본 test_pipeline
test_pipeline = [
    dict(type='LoadImageFromFile', backend_args={{_base_.backend_args}}),
    dict(type='Resize', scale=(320, 320), keep_ratio=True), #scale=(image_size, image_size)
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]
#test_pipeline = [
#    dict(type='LoadImageFromFile', backend_args={{_base_.backend_args}}),
#    dict(
#        type='MultiScaleFlipAug',  # TTA 적용
#        img_scale=[(1333, 800), (768, 768), (1024, 1024)],  # 다양한 크기 설정
#        flip=True,  # 좌우 반전 적용
#        flip_direction=['horizontal'],  # 수평 반전 추가
#        transforms=[
#            dict(type='Resize', scale=(image_size, image_size), keep_ratio=True),
#            dict(type='RandomFlip'),
#            dict(type='Normalize', mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True),
#            dict(type='Pad', size_divisor=32),
#            dict(type='PackDetInputs',
#                meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
#                           'scale_factor', 'flip', 'flip_direction'))
#        ])
#]


train_dataloader = dict(
    batch_size= 16, #16
    num_workers=8,
    dataset=dict(type=dataset_type, pipeline=train_pipeline, metainfo=metainfo), 
    )
val_dataloader = dict(dataset=dict(type=dataset_type, pipeline=test_pipeline, metainfo=metainfo)
                      )
test_dataloader = val_dataloader

val_evaluator = dict(type=evalute_type)
test_evaluator = val_evaluator

#optimizer
optim_wrapper = dict(
    #optimizer=dict(type='AdamW', lr=0.0005, weight_decay=1e-4, betas=(0.9, 0.999)), #초기 0.001
    _delete_=True,
    type='OptimWrapper',
    optimizer=dict(type='AdamW', lr=0.0005, weight_decay=1e-4, betas=(0.9, 0.999)),
    paramwise_cfg=dict(norm_decay_mult=0, bias_decay_mult=0, bypass_duplicate=True), #여러 레이어에서 참조하는 경우, 그 파라미터에 대해 중복하여 decay를 적용하지 않도록
    clip_grad=dict(max_norm=10, norm_type=2))# accum_iters=4

# 잠재적인 'momentum' 파라미터 제거
#if 'momentum' in optim_wrapper['optimizer']:
#    del optim_wrapper['optimizer']['momentum']

# learning policy
#max_epochs = 300
max_epochs = 60
param_scheduler = [
    dict(type='LinearLR', start_factor=0.1, by_epoch=False, begin=0, end=1000),
    dict(
        type='CosineAnnealingLR',
        eta_min= 0.00001,  # 최저 학습률을 너무 낮지 않게 설정하여 학습이 멈추지 않도록 함
        begin=1,
        T_max=60, #max_epoch -1 299, # 60 에포크 동안 CosineAnnealing 적용
        end=60,   #max_epoch 300
        by_epoch=True,
        convert_to_iter_based=True)
]
train_cfg = dict(max_epochs=max_epochs, val_interval=2)  #매 에포크마다 검증(validation)을 수행

vis_backends = [
    dict(type='LocalVisBackend'),
    dict(type='TensorboardVisBackend')
]
visualizer = dict(
    type='DetLocalVisualizer', vis_backends=vis_backends, name='visualizer')

default_hooks = dict(checkpoint=dict(type='CheckpointHook', interval=4)) # 4 에포크마다 체크포인트를 저장
custom_hooks = [
    dict(
        type='EMAHook',
        ema_type='ExpMomentumEMA',
        momentum=0.0002,
        update_buffers=True,
        priority=49)
]
# cudnn_benchmark=True can accelerate fix-size training
env_cfg = dict(cudnn_benchmark=True)

# NOTE: `auto_scale_lr` is for automatically scaling LR,
# USER SHOULD NOT CHANGE ITS VALUES.
# base_batch_size = (8 GPUs) x (16 samples per GPU)
auto_scale_lr = dict(base_batch_size=128)