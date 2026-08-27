# 🖼️ 图像卷积与边缘检测 | Image Convolution & Edge Detection

> **从零实现的图像卷积与 Sobel 边缘检测——卷积核、边界处理、梯度计算、可视化对比，深入理解图像处理原理。**
>
> *Image convolution and Sobel edge detection implemented from scratch — convolution kernels, boundary handling, gradient computation, visual comparison, deep understanding of image processing.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| 🔬 **从零实现** | From Scratch | 纯 NumPy 实现卷积，不依赖库 |
| 🧠 **卷积原理** | Convolution | 卷积核、步长、填充原理详解 |
| 🔍 **边缘检测** | Edge Detection | Sobel 算子垂直/水平边缘检测 |
| 🎨 **可视化** | Visualization | 原图、梯度图、边缘图对比展示 |
| 📚 **教学友好** | Teaching Friendly | 代码 + 原理 + 可视化完整配套 |

---

## 🏆 技术栈 | Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-1.21+-blue?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-red?logo=matplotlib)
![PIL](https://img.shields.io/badge/PIL-8.0+-orange?logo=python)

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/Image-Conv-Edge-Detection-Sobel.git
cd Image-Conv-Edge-Detection-Sobel

# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行边缘检测
python src/sobel_edge_detection.py --image data/input.jpg

# 3. 自定义卷积
python src/convolution.py --image data/input.jpg --kernel sobel_vertical

# 4. 批量处理
python src/batch_process.py --dir data/images/ --output result/

# 5. 可视化对比
python src/visualize.py --image data/input.jpg
```

---

## 📂 项目结构 | Project Structure

```
Image-Conv-Edge-Detection-Sobel/
├── src/                       # 核心代码
│   ├── convolution.py         # 卷积实现
│   ├── sobel_edge_detection.py # Sobel 边缘检测
│   ├── kernels.py             # 卷积核定义
│   ├── padding.py             # 边界填充
│   └── visualize.py           # 可视化
├── data/                      # 测试图片
├── result/                    # 处理结果
└── requirements.txt
```

---

## 🔬 核心实现 | Core Implementation

### 卷积与 Sobel 边缘检测 | Convolution & Sobel

```python
# 从零实现图像卷积
import numpy as np

def convolve2d(image, kernel, padding=1, stride=1):
    """二维卷积实现"""
    h, w = image.shape
    kh, kw = kernel.shape
    
    # 边界填充
    padded = np.pad(image, padding, mode='constant')
    out_h = (h + 2*padding - kh) // stride + 1
    out_w = (w + 2*padding - kw) // stride + 1
    
    output = np.zeros((out_h, out_w))
    for i in range(0, out_h):
        for j in range(0, out_w):
            region = padded[i*stride:i*stride+kh, j*stride:j*stride+kw]
            output[i, j] = np.sum(region * kernel)
    return output

# Sobel 垂直边缘检测
def sobel_vertical_edge(image):
    """Sobel 算子垂直边缘检测"""
    # 垂直边缘检测核 (检测水平方向的灰度变化)
    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    # 水平边缘检测核
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    # 转为灰度
    gray = np.mean(image, axis=2) if image.ndim == 3 else image
    
    # 应用 Sobel
    gx = convolve2d(gray, sobel_x)
    gy = convolve2d(gray, sobel_y)
    
    # 梯度幅值
    magnitude = np.sqrt(gx**2 + gy**2)
    # 梯度方向
    direction = np.arctan2(gy, gx)
    
    return magnitude, direction
```

---

## 📊 效果对比 | Result Comparison

```
原图                 灰度图               Sobel 边缘图
┌─────────┐        ┌─────────┐        ┌─────────┐
│  ██  ██  │        │  ██  ██  │        │  ╱╲  ╱╲  │
│ █  ██  █ │  →     │ █  ██  █ │  →     │ █  ██  █ │
│  ██  ██  │        │  ██  ██  │        │  ╲╱  ╲╱  │
└─────────┘        └─────────┘        └─────────┘
(彩色)              (灰度)             (边缘轮廓高亮)
```

---

## 🎯 应用场景 | Use Cases

- 🧠 **图像处理教学**：卷积神经网络基础
- 🔬 **CV 入门**：图像特征提取
- 🏭 **工业检测**：产品边缘缺陷检测
- 🎓 **算法实现**：从零实现图像处理算法

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **从零实现图像卷积与 Sobel 边缘检测，Star ⭐ 深入理解图像处理！**
