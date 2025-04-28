# Satellite Imagery Analysis for Aircraft Monitoring

Official Repository for  
**Satellite Imagery Analysis for Aircraft Monitoring**  
(NeurIPS 2025 Project)

---

## Overview

Accurate detection of aircraft in satellite imagery has major applications in defense, surveillance, and emergency response.  
In this project, we develop an automated deep learning system for aircraft detection:

- **Baseline**: YOLOv8 Large (YOLOv8l)
- **Advanced**: YOLO11 Large (YOLO11l) with enhanced feature fusion and attention
- **Deployment**: Real-time web application using ONNX and WebAssembly
- **Dataset**: HRPlanesv2 high-resolution satellite images

We achieve strong mAP scores even under cluttered, challenging conditions, with practical real-time deployment.

---

## Requirements

![](https://img.shields.io/badge/python-3.10-green.svg)
![](https://img.shields.io/badge/torch-2.0.1-blue.svg)

Create a virtual environment:

```bash
python -m venv aircraft-detection-env
source aircraft-detection-env/bin/activate  # or .\aircraft-detection-env\Scripts\activate on Windows
```

Install the Python requirements:

```bash
pip install ultralytics
```

Install pytorch:
https://pytorch.org/get-started/locally/

Install the web app dependencies:

```bash
cd demo
npm install
```

---

## Dataset

### HRPlanesv2

- **Download**:  
  Download the HRPlanesv2 dataset manually from [Zenodo (HRPlanesv2)](https://zenodo.org/records/7331974#.Y4rPp3ZBwdV).

- **Preparation**:
  After downloading:

  1. **Manually split** the dataset into `train`, `val`, and `test` sets under `images/` and `labels/` directories:

  ```
  datasets/HRPlanesv2/
  ├── HRPlanesv2.yaml
  ├── HRPlanesv2test.yaml
  ├── images/
  │   ├── train/
  │   ├── val/
  │   └── test/
  └── labels/
      ├── train/
      ├── val/
      └── test/
  ```

  2. Use the provided **HRPlanesv2.yaml** file to configure dataset paths for training and testing.

- **About the dataset**:
  - 2,120 high-resolution aerial and satellite images
  - 14,335 annotated aircraft instances
  - Wide variety of aircraft types, rotations, densities, and backgrounds
  - Designed for small object detection challenges in cluttered scenes

---

## Models

| Model   | mAP@50 | mAP@50-95 |
| ------- | ------ | --------- |
| YOLOv8l | 98.9%  | 79.6%     |
| YOLO11l | 98.9%  | 80.5%     |

- Trained for **100 epochs** each
- Data augmentation: random flips, scaling
- Advanced model improves detection on dense clusters and overlapping aircraft

Exported models (ONNX format):

```
demo/static/models/
├── yolov8l-best.onnx
├── yolo11l-best.onnx
├── yolo11m-best.onnx
├── yolo11n-best.onnx
```

---

## Usage

### Train a model

In the train.py file change the pretained model(yolov8l.pt, yolo11n.pt, etc) to which ever one you want to use. CHange epochs in the same file as needed.

```bash
python train.py
```

### Predict using a model

Place the model in the

### Test mAP evaluation

```bash
yolo val model=trainedModels\yolov8l-best.pt data=datasets/HRPlanesv2/HRPlanesv2test.yaml
```

### Test CUDA support

```bash
python testCuda.py
```

---

## Web Deployment

After exporting trained models to ONNX, you can deploy the web-based app:

### Start the local server

```bash
cd demo
npm run dev
```

Then open your browser at [http://localhost:3000](http://localhost:3000).

- Detect aircraft in uploaded images
- Detect aircraft directly from Google Maps satellite views
- Output precise latitude and longitude of detected aircraft

Supported models selectable via dropdown.

---

## Repository Structure

```
.
├── README.md                # Project overview
├── datasets/HRPlanesv2/      # Dataset (images, labels, yaml configs)
├── trainedModels/            # Trained YOLO .pt models
├── demo/                     # Web app (SvelteKit + ONNX.js frontend)
│   ├── static/               # ONNX models, favicon, ONNX runtime wasm files
│   ├── src/                  # Web frontend code (components, routes, types)
│   ├── package.json          # Node.js dependencies
│   └── vite.config.ts        # Build config
├── predict.py                # Single/batch image prediction script
├── train.py                  # Model training script
├── testCuda.py               # CUDA test script
└── requirements.txt          # Python libraries
```

---

## Results

Training and validation curves:

- YOLOv8l: ![](results-8l.png)
- YOLO11l: ![](results-11l.png)

Example aircraft detection output:  
![](results.jpg)

---

## Citation

If you use this project or ideas from it, please cite:

```
@misc{jayadevan2025aircraft,
  title={Satellite Imagery Analysis for Aircraft Monitoring},
  author={Advait Jayadevan Nair, Jay Chawla, Puvvanrao Rhamarao},
  year={2025},
  note={NeurIPS 2025 Project}
}
```

---

## Contact & Contributions

- **Advait Jayadevan Nair** ([jayadevannair.1@osu.edu](mailto:jayadevannair.1@osu.edu))
- **Jay Chawla** ([chawla.113@osu.edu](mailto:chawla.113@osu.edu))
- **Puvvanrao Rhamarao** ([rhamarao.1@osu.edu](mailto:rhamarao.1@osu.edu))

We welcome feedback, issues, and contributions! Feel free to open a pull request.

---

## Acknowledgments

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [HRPlanesv2 Dataset (Zenodo)](https://zenodo.org/records/7331974#.Y4rPp3ZBwdV)
- [ONNX.js](https://github.com/microsoft/onnxruntime)

---

## Notes

- YOLO11l offered **qualitative improvements** in small, dense aircraft detection.
- **Real-time inference** achieved through WebAssembly SIMD optimization.
- Future work can explore rotation-invariant detection and lightweight deployment optimizations.
