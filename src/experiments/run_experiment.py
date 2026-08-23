"""
图像卷积实验运行脚本
简化版本，便于快速测试
"""

from ..core.image_convolution import ImageConvolution
import numpy as np
import cv2

def quick_test():
    """快速测试函数"""
    print("开始图像卷积实验...")
    
    # 创建处理器
    processor = ImageConvolution()
    
    # 显示模板
    print("\n使用的模板：")
    print(processor.template)
    
    # 处理图像
    original, conv_result, normalized = processor.process_image()
    
    if original is not None:
        print(f"\n原始图像尺寸: {original.shape}")
        print(f"卷积结果范围: [{np.min(conv_result):.2f}, {np.max(conv_result):.2f}]")
        print(f"归一化结果范围: [{np.min(normalized)}, {np.max(normalized)}]")
        
        # 保存关键结果
        cv2.imwrite('../data/input/test_original.png', original)
        cv2.imwrite('../data/output/test_result.png', normalized)
        
        print("\n文件已保存:")
        print("- test_original.png: 原始测试图像")
        print("- test_result.png: 卷积处理结果")
        
        return True
    else:
        print("处理失败！")
        return False

if __name__ == "__main__":
    success = quick_test()
    if success:
        print("\n实验完成！请查看生成的图像文件。")
    else:
        print("\n实验失败，请检查代码。")
