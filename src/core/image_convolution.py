"""
图像模板运算（卷积）实现
作者：学生姓名
日期：2025年10月14日

本程序实现了使用指定模板对灰度图像进行卷积运算的功能。
模板：[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

class ImageConvolution:
    """图像卷积处理类"""
    
    def __init__(self):
        """初始化卷积处理器"""
        # 定义指定的模板（Sobel垂直边缘检测算子）
        self.template = np.array([[-1, 0, 1],
                                 [-2, 0, 2],
                                 [-1, 0, 1]], dtype=np.float32)
        
    def load_image(self, image_path):
        """
        加载图像并转换为灰度图像
        
        Args:
            image_path (str): 图像文件路径
            
        Returns:
            numpy.ndarray: 灰度图像数组
        """
        try:
            # 读取图像
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"无法读取图像文件: {image_path}")
            
            # 转换为灰度图像
            if len(image.shape) == 3:
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray_image = image
                
            print(f"成功加载图像，尺寸: {gray_image.shape}")
            return gray_image
            
        except Exception as e:
            print(f"加载图像时出错: {e}")
            return None
    
    def create_sample_image(self):
        """
        创建一个示例图像用于演示
        
        Returns:
            numpy.ndarray: 示例灰度图像
        """
        # 创建一个包含不同特征的示例图像
        image = np.zeros((200, 200), dtype=np.uint8)
        
        # 添加一些几何形状
        # 矩形
        cv2.rectangle(image, (50, 50), (100, 100), 255, -1)
        
        # 圆形
        cv2.circle(image, (150, 150), 30, 128, -1)
        
        # 线条
        cv2.line(image, (20, 150), (180, 150), 200, 3)
        cv2.line(image, (100, 20), (100, 180), 200, 3)
        
        print("创建示例图像成功")
        return image
    
    def manual_convolution(self, image, kernel):
        """
        手动实现卷积运算（与OpenCV保持一致的边界处理）

        Args:
            image (numpy.ndarray): 输入图像
            kernel (numpy.ndarray): 卷积核

        Returns:
            numpy.ndarray: 卷积结果
        """
        # 获取图像和卷积核的尺寸
        img_height, img_width = image.shape
        kernel_height, kernel_width = kernel.shape

        # 计算填充大小
        pad_h = kernel_height // 2
        pad_w = kernel_width // 2

        # 对图像进行反射填充（与OpenCV的BORDER_REFLECT_101类似）
        padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)),
                             mode='reflect')

        # 初始化输出图像
        output = np.zeros((img_height, img_width), dtype=np.float32)

        # 执行卷积运算
        for i in range(img_height):
            for j in range(img_width):
                # 提取当前窗口
                window = padded_image[i:i+kernel_height, j:j+kernel_width]
                # 计算卷积
                output[i, j] = np.sum(window * kernel)

        return output
    
    def opencv_convolution(self, image, kernel):
        """
        使用OpenCV实现卷积运算
        
        Args:
            image (numpy.ndarray): 输入图像
            kernel (numpy.ndarray): 卷积核
            
        Returns:
            numpy.ndarray: 卷积结果
        """
        # 使用cv2.filter2D进行卷积
        result = cv2.filter2D(image, cv2.CV_32F, kernel)
        return result
    
    def normalize_result(self, result):
        """
        将卷积结果归一化到0-255范围
        
        Args:
            result (numpy.ndarray): 卷积结果
            
        Returns:
            numpy.ndarray: 归一化后的结果
        """
        # 获取结果的最小值和最大值
        min_val = np.min(result)
        max_val = np.max(result)
        
        # 归一化到0-255范围
        if max_val - min_val != 0:
            normalized = ((result - min_val) / (max_val - min_val) * 255).astype(np.uint8)
        else:
            normalized = np.zeros_like(result, dtype=np.uint8)
            
        return normalized
    
    def process_image(self, image_path=None, use_sample=True, method='opencv'):
        """
        处理图像的主函数
        
        Args:
            image_path (str): 图像文件路径
            use_sample (bool): 是否使用示例图像
            method (str): 卷积方法 ('manual' 或 'opencv')
            
        Returns:
            tuple: (原图像, 卷积结果, 归一化结果)
        """
        # 加载或创建图像
        if use_sample or image_path is None:
            original_image = self.create_sample_image()
        else:
            original_image = self.load_image(image_path)
            if original_image is None:
                return None, None, None
        
        # 执行卷积运算
        print(f"使用{method}方法进行卷积运算...")
        if method == 'manual':
            conv_result = self.manual_convolution(original_image, self.template)
        else:
            conv_result = self.opencv_convolution(original_image, self.template)
        
        # 归一化结果
        normalized_result = self.normalize_result(conv_result)
        
        print("卷积运算完成")
        return original_image, conv_result, normalized_result
    
    def analyze_template(self):
        """
        分析模板的作用
        
        Returns:
            str: 分析结果
        """
        analysis = """
        模板分析：[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        
        1. 模板类型：这是Sobel垂直边缘检测算子
        
        2. 作用机制：
           - 左列系数为负值(-1, -2, -1)：对左侧像素进行负权重处理
           - 中列系数为零(0, 0, 0)：忽略中间像素
           - 右列系数为正值(1, 2, 1)：对右侧像素进行正权重处理
        
        3. 检测效果：
           - 主要检测垂直方向的边缘（从左到右的亮度变化）
           - 当图像从左侧暗区域过渡到右侧亮区域时，产生正响应
           - 当图像从左侧亮区域过渡到右侧暗区域时，产生负响应
           - 对水平边缘响应较弱
        
        4. 数学原理：
           - 计算水平方向的梯度（一阶导数近似）
           - 中间行权重最大(-2, 0, 2)，增强边缘检测效果
           - 上下行权重较小(-1, 0, 1)，提供平滑效果
        
        5. 应用场景：
           - 边缘检测
           - 特征提取
           - 图像预处理
           - 计算机视觉中的特征检测
        """
        return analysis
    
    def visualize_results(self, original, conv_result, normalized, save_path=None):
        """
        可视化结果
        
        Args:
            original (numpy.ndarray): 原始图像
            conv_result (numpy.ndarray): 卷积结果
            normalized (numpy.ndarray): 归一化结果
            save_path (str): 保存路径
        """
        # 创建子图
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('图像模板运算（卷积）结果', fontsize=16, fontweight='bold')
        
        # 原始图像
        axes[0, 0].imshow(original, cmap='gray')
        axes[0, 0].set_title('原始灰度图像')
        axes[0, 0].axis('off')
        
        # 卷积结果（原始值）
        im1 = axes[0, 1].imshow(conv_result, cmap='gray')
        axes[0, 1].set_title('卷积结果（原始值）')
        axes[0, 1].axis('off')
        plt.colorbar(im1, ax=axes[0, 1])
        
        # 归一化结果
        axes[1, 0].imshow(normalized, cmap='gray')
        axes[1, 0].set_title('归一化结果（0-255）')
        axes[1, 0].axis('off')
        
        # 模板可视化
        im2 = axes[1, 1].imshow(self.template, cmap='RdBu_r')
        axes[1, 1].set_title('使用的模板')
        axes[1, 1].axis('off')
        plt.colorbar(im2, ax=axes[1, 1])
        
        # 在模板图上添加数值标注
        for i in range(self.template.shape[0]):
            for j in range(self.template.shape[1]):
                axes[1, 1].text(j, i, f'{self.template[i, j]:.0f}', 
                               ha='center', va='center', fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        
        # 保存图像
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"结果图像已保存到: {save_path}")
        
        plt.show()

def main():
    """主函数"""
    print("=" * 60)
    print("图像模板运算（卷积）演示程序")
    print("=" * 60)
    
    # 创建卷积处理器
    processor = ImageConvolution()
    
    # 显示模板分析
    print("\n模板分析：")
    print(processor.analyze_template())
    
    # 处理图像
    print("\n" + "=" * 40)
    print("开始图像处理...")
    
    # 使用示例图像进行演示
    original, conv_result, normalized = processor.process_image(
        use_sample=True, method='opencv'
    )
    
    if original is not None:
        # 保存结果
        cv2.imwrite('original_image.png', original)
        cv2.imwrite('convolution_result.png', normalized)
        
        # 可视化结果
        processor.visualize_results(original, conv_result, normalized, 
                                  'convolution_analysis.png')
        
        print("\n处理完成！")
        print("生成的文件：")
        print("- original_image.png: 原始图像")
        print("- convolution_result.png: 卷积结果")
        print("- convolution_analysis.png: 完整分析图")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
