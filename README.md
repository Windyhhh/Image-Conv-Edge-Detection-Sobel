<div align="center">

# 🖼️ Image-Conv-Edge-Detection-Sobel

### Sobel vertical edge detection from scratch.

A clean, tested image-convolution + Sobel edge-detection implementation in pure Python.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21-013243?logo=numpy&logoColor=white)](https://numpy.org/)

</div>

---

**Image-Conv-Edge-Detection-Sobel** implements image convolution and **Sobel** edge detection from scratch, with unit tests and experiment scripts.

> [!NOTE]
> 中文项目：图像卷积与边缘检测——Sobel 算子垂直边缘检测，从零实现。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Image-Conv-Edge-Detection-Sobel.git
cd Image-Conv-Edge-Detection-Sobel

pip install -r requirements.txt

# Run the experiment on a sample image
python src/experiments/run_experiment.py

# Run tests
python -m pytest src/tests/test_validation.py
```

---

## Features

- **From-scratch convolution** — `image_convolution.py`.
- **Sobel detection** — vertical edge detection.
- **Tested** — validation suite + experiment runner.

---

## Project Structure

```
Image-Conv-Edge-Detection-Sobel/
├── src/
│   ├── core/image_convolution.py
│   ├── experiments/run_experiment.py
│   └── tests/test_validation.py
├── data/input/             # sample images
├── data/output/            # results
└── requirements.txt
```

---

## License

MIT — free to use, modify and distribute.
