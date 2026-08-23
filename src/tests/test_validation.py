"""
验证测试脚本
比较手动卷积和OpenCV卷积的结果一致性
"""

import numpy as np
from ..core.image_convolution import ImageConvolution
import matplotlib.pyplot as plt

def validate_convolution_methods():
    """验证两种卷积方法的一致性"""
    print("开始验证卷积方法的一致性...")
    
    # 创建处理器
    processor = ImageConvolution()
    
    # 创建简单的测试图像
    test_image = np.array([
        [0, 0, 255, 255, 0],
        [0, 0, 255, 255, 0],
        [0, 0, 255, 255, 0],
        [0, 0, 255, 255, 0],
        [0, 0, 255, 255, 0]
    ], dtype=np.uint8)
    
    print("测试图像:")
    print(test_image)
    
    # 手动卷积
    manual_result = processor.manual_convolution(test_image, processor.template)
    
    # OpenCV卷积
    opencv_result = processor.opencv_convolution(test_image, processor.template)
    
    # 比较结果
    difference = np.abs(manual_result - opencv_result)
    max_diff = np.max(difference)
    mean_diff = np.mean(difference)
    
    print(f"\n手动卷积结果:")
    print(manual_result)
    print(f"\nOpenCV卷积结果:")
    print(opencv_result)
    print(f"\n差异统计:")
    print(f"最大差异: {max_diff:.6f}")
    print(f"平均差异: {mean_diff:.6f}")
    
    # 判断是否一致
    tolerance = 1e-5
    if max_diff < tolerance:
        print(f"\n✅ 验证通过！两种方法结果一致（差异 < {tolerance}）")
        return True
    else:
        print(f"\n❌ 验证失败！两种方法结果不一致（差异 = {max_diff}）")
        return False

def test_edge_detection_properties():
    """测试边缘检测的特性"""
    print("\n" + "="*50)
    print("测试边缘检测特性...")
    
    processor = ImageConvolution()
    
    # 创建包含不同边缘类型的测试图像
    test_cases = {
        "垂直边缘": np.array([
            [0, 0, 255, 255],
            [0, 0, 255, 255],
            [0, 0, 255, 255],
            [0, 0, 255, 255]
        ], dtype=np.uint8),
        
        "水平边缘": np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [255, 255, 255, 255],
            [255, 255, 255, 255]
        ], dtype=np.uint8),
        
        "均匀区域": np.array([
            [128, 128, 128, 128],
            [128, 128, 128, 128],
            [128, 128, 128, 128],
            [128, 128, 128, 128]
        ], dtype=np.uint8)
    }
    
    for name, image in test_cases.items():
        result = processor.opencv_convolution(image, processor.template)
        max_response = np.max(np.abs(result))
        
        print(f"\n{name}:")
        print(f"输入图像:\n{image}")
        print(f"卷积结果:\n{result}")
        print(f"最大响应强度: {max_response:.2f}")
        
        # 分析结果
        if name == "垂直边缘":
            if max_response > 100:
                print("✅ 垂直边缘检测正常")
            else:
                print("❌ 垂直边缘检测异常")
        elif name == "水平边缘":
            if max_response < 50:
                print("✅ 对水平边缘响应较弱（符合预期）")
            else:
                print("❌ 对水平边缘响应过强")
        elif name == "均匀区域":
            if max_response < 10:
                print("✅ 对均匀区域响应很弱（符合预期）")
            else:
                print("❌ 对均匀区域响应异常")

def performance_comparison():
    """性能比较测试"""
    print("\n" + "="*50)
    print("性能比较测试...")
    
    import time
    
    processor = ImageConvolution()
    
    # 创建较大的测试图像
    large_image = processor.create_sample_image()
    
    # 测试手动卷积性能
    start_time = time.time()
    manual_result = processor.manual_convolution(large_image, processor.template)
    manual_time = time.time() - start_time
    
    # 测试OpenCV卷积性能
    start_time = time.time()
    opencv_result = processor.opencv_convolution(large_image, processor.template)
    opencv_time = time.time() - start_time
    
    print(f"图像尺寸: {large_image.shape}")
    print(f"手动卷积耗时: {manual_time:.4f} 秒")
    print(f"OpenCV卷积耗时: {opencv_time:.4f} 秒")
    if opencv_time > 0:
        print(f"性能提升: {manual_time/opencv_time:.1f}x")
    else:
        print("OpenCV卷积速度极快，无法准确测量时间差异")
    
    # 验证结果一致性
    difference = np.max(np.abs(manual_result - opencv_result))
    print(f"结果差异: {difference:.6f}")

def main():
    """主测试函数"""
    print("图像卷积验证测试")
    print("="*60)
    
    # 1. 验证方法一致性
    validation_passed = validate_convolution_methods()
    
    # 2. 测试边缘检测特性
    test_edge_detection_properties()
    
    # 3. 性能比较
    performance_comparison()
    
    print("\n" + "="*60)
    if validation_passed:
        print("✅ 所有验证测试通过！代码实现正确。")
    else:
        print("❌ 验证测试失败，请检查代码实现。")
    print("="*60)

if __name__ == "__main__":
    main()
