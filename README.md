# 🖼️ Image Conv & Edge Detection Sobel | 图像卷积与边缘检测（Sobel 算子）

> **From-scratch implementation of image convolution and Sobel edge detection. No OpenCV, pure NumPy. Vertical edge detection, Gaussian blur, gradient computation, and non-maximum suppression. Educational and production-ready.**
>
> 从零实现图像卷积和 Sobel 边缘检测。不使用 OpenCV，纯 NumPy。垂直边缘检测、高斯模糊、梯度计算和非极大值抑制。兼具教学和实用价值。

---

## 🌟 Features | 核心特性

- **Pure NumPy** — No OpenCV dependency
- **Convolution** — 2D convolution from scratch
- **Sobel Operator** — Horizontal and vertical gradients
- **Vertical Edge Detection** — Specialized for vertical edges
- **Gaussian Blur** — Pre-processing noise reduction
- **Gradient Magnitude** — Combined edge strength
- **Non-Maximum Suppression** — Thin edges
- **Comparison** — vs OpenCV results

---

## 🚀 Quick Start | 快速开始

```bash
pip install numpy matplotlib pillow opencv-python

# Run edge detection
python sobel_edge_detection.py --input image.jpg --output edges.jpg

# Vertical edges only
python sobel_vertical.py --input image.jpg
```

---

## 🔬 Sobel Kernels | Sobel 算子

```
Gx (horizontal):          Gy (vertical):
[-1  0  1]                [-1 -2 -1]
[-2  0  2]                [ 0  0  0]
[-1  0  1]                [ 1  2  1]
```

---

## 📄 License | 许可证

MIT License.

[GitHub](https://github.com/Windyhhh/Image-Conv-Edge-Detection-Sobel)
