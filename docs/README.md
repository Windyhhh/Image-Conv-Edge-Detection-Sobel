# 图像模板运算（卷积）实验

## 项目简介

本项目实现了使用指定模板 `[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]` 对灰度图像进行卷积运算的完整解决方案。

## 文件结构

```
├── image_convolution.py      # 主程序文件
├── run_experiment.py         # 快速测试脚本
├── requirements.txt          # 依赖包列表
├── 说明文档.md              # 详细实验报告
├── README.md                # 项目说明
└── 生成的结果文件/
    ├── original_image.png           # 原始测试图像
    ├── convolution_result.png       # 卷积结果图像
    ├── convolution_analysis.png     # 完整分析图表
    ├── test_original.png           # 快速测试原图
    └── test_result.png             # 快速测试结果
```

## 环境要求

- Python 3.7+
- numpy >= 1.21.0
- opencv-python >= 4.5.0
- matplotlib >= 3.5.0

## 安装和运行

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行完整程序
```bash
python image_convolution.py
```

### 3. 快速测试
```bash
python run_experiment.py
```

## 功能特性

### 核心功能
- ✅ 实现指定模板的卷积运算
- ✅ 支持手动卷积和OpenCV卷积两种方法
- ✅ 自动生成测试图像
- ✅ 结果可视化和保存
- ✅ 详细的模板作用分析

### 模板分析
使用的模板：
```
[[-1,  0,  1],
 [-2,  0,  2],
 [-1,  0,  1]]
```

**作用**: Sobel垂直边缘检测算子
- 检测垂直方向的边缘
- 计算水平方向的梯度
- 对左右亮度变化敏感

## 输出结果

程序运行后会生成以下文件：

1. **original_image.png**: 原始灰度测试图像
2. **convolution_result.png**: 卷积运算结果
3. **convolution_analysis.png**: 包含四个子图的完整分析：
   - 原始图像
   - 卷积结果（原始数值）
   - 归一化结果
   - 使用的模板可视化

## 实验结果说明

### 边缘检测效果
- ✅ 垂直边缘被清晰检测出来
- ✅ 矩形的左右边界产生强烈响应
- ✅ 圆形的左右弧线被突出显示
- ✅ 垂直线条产生最强响应

### 数值特性
- 原始卷积结果范围：约 [-800, 1020]
- 归一化后范围：[0, 255]
- 正值表示从左暗到右亮的边缘
- 负值表示从左亮到右暗的边缘

## 代码结构

### 主要类和方法

```python
class ImageConvolution:
    def __init__(self)                    # 初始化，定义模板
    def load_image(self, path)            # 加载外部图像
    def create_sample_image(self)         # 创建测试图像
    def manual_convolution(self, img, kernel)  # 手动卷积实现
    def opencv_convolution(self, img, kernel)  # OpenCV卷积实现
    def normalize_result(self, result)    # 结果归一化
    def process_image(self, ...)          # 主处理函数
    def analyze_template(self)            # 模板分析
    def visualize_results(self, ...)      # 结果可视化
```

## 扩展使用

### 使用自己的图像
```python
processor = ImageConvolution()
original, conv_result, normalized = processor.process_image(
    image_path="your_image.jpg", 
    use_sample=False
)
```

### 使用手动卷积方法
```python
original, conv_result, normalized = processor.process_image(
    method='manual'
)
```

## 学习要点

1. **卷积运算原理**: 理解模板与图像的数学运算过程
2. **边缘检测**: 掌握Sobel算子的工作机制
3. **图像处理**: 学习Python图像处理的基本方法
4. **结果分析**: 理解卷积结果的物理意义

## 作业提交

本项目包含完整的作业材料：
- ✅ **代码**: `image_convolution.py` (主程序)
- ✅ **说明文档**: `说明文档.md` (详细实验报告)
- ✅ **运行结果**: 生成的图像文件
- ✅ **测试脚本**: `run_experiment.py` (便于验证)

## 技术特点

- 🔧 **双重实现**: 提供手动和OpenCV两种卷积实现
- 📊 **完整可视化**: 四合一分析图表
- 📝 **详细注释**: 代码注释详细，便于理解
- 🎯 **教学导向**: 专为学习目的设计
- ✅ **即开即用**: 无需额外配置，直接运行

## 常见问题

**Q: 为什么卷积结果有负值？**
A: 卷积运算的数学特性决定了结果可能为负值，这表示边缘的方向性。

**Q: 归一化的作用是什么？**
A: 将卷积结果映射到0-255范围，便于图像显示和保存。

**Q: 为什么只检测垂直边缘？**
A: 使用的模板是垂直Sobel算子，专门用于检测垂直方向的边缘。

## 联系方式

如有问题，请检查：
1. Python环境是否正确安装
2. 依赖包是否完整安装
3. 运行目录是否正确
