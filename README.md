## 结构说明
```
├── TensoRF/                       
│   ├── configs/                   
│   │   └── your_own_data.txt      
│   ├── renderer.py                
│   └── train.py                
│
├── gaussian-splatting/            
│   ├── render.py                
│   └── train.py                    
│
├── nerf-pytorch/                 
│   ├── configs/                   
│   │   └── cat_llff.txt          
│   └── run_nerf.py               
│
├── extract_frames.py        #将视频分为图片     
└── README.md                     
```              

## NeRF(torch版本)
#### 训练数据
使用的llff格式文件（网盘链接里面的```.npy```文件）和原始图片
#### 环境配置
```torch==2.0.1```，其他环境和官方框架一致
#### 训练渲染方式
和官方框架一致

训练```python run_nerf.py --config configs/cat_llff.txt```

渲染```python run_nerf.py --config configs/cat_llff.txt --render_only```

未做更改的代码没有上传，请参考官方文件
## TensoRF
#### 训练数据
使用的json格式文件（网盘链接里面的```.json```文件）和原始图片
#### 环境配置，
```torch==1.10.1```，其他环境和官方框架一致
#### 训练渲染方式
和官方框架一致

训练```python train.py --config configs/your_own_data.txt```

渲染```python train.py --config configs/your_own_data.txt --ckpt path/to/your/checkpoint --render_only 1 --render_test 1 ```

未做更改的代码没有上传，请参考官方文件
## 3D Gaussian Splatting
#### 训练数据
使用的colmap生成的```.bin```文件和原始图片
#### 环境配置
和官方框架略有差异（```cuda12.2 pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1```）
#### 训练渲染方式
和官方框架一致

训练```python train.py -s <path to COLMAP or NeRF Synthetic dataset> --eval```

渲染```python render.py -m <path to trained model>```

未做更改的代码没有上传，请参考官方文件


