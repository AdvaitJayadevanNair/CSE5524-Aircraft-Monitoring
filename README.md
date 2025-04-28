# Satellite Imagery Aircraft Detection

---

## 1. Installation Instructions

Create a virtual environment:

```bash
python -m venv aircraft-detection-env
source aircraft-detection-env/bin/activate    # Linux/Mac
.\aircraft-detection-env\Scripts\activate     # Windows
```

Install pytorch:
https://pytorch.org/get-started/locally/

Install required Python packages:

```bash
pip install ultrultralytics
```

---

## 2. Advanced Algorithm

This project uses an **advanced object detection model** based on **YOLO11 Large (YOLO11l)** architecture.  
YOLO11l introduces enhanced feature fusion and attention mechanisms for better detection of **small**, **rotated**, and **densely clustered** aircraft in high-resolution satellite imagery.

- **Training** was performed on the **HRPlanesv2** dataset for **100 epochs**.
- Model achieves **98.9% mAP@50** and **80.5% mAP@50-95** on validation data.

🔗 **Download the pretrained YOLO11l and YOLOv8l ONNX model here:**

> [Pretrained YOLO11l Model (One Drive link)](https://buckeyemailosu-my.sharepoint.com/:u:/g/personal/jayadevannair_1_buckeyemail_osu_edu/EXRPcTx9oZlIvfdp2bzQ2_UB07_RRYUogDPdpuNJpGvKTA?e=PXgFqA)

---

## 3. Test / Validation Examples

Sample validation images from HRPlanesv2 are provided for testing the model.

🔗 **Download test/validation images here:**

> [Validation/Test Images (One Drive link)](https://buckeyemailosu-my.sharepoint.com/:u:/g/personal/jayadevannair_1_buckeyemail_osu_edu/EcZsd8SiPwNPk4_X1g_MxOgBC-kiLiySh4gu1r0SvoO3cQ?e=7gcFku)

Test images are organized as:

```
datasets/HRPlanesv2/
  ├── HRPlanesv2.yaml
  ├── images/
  │   └── test/
  └── labels/
      └── test/
```

---

## 4. Commands to Run on Test Images

After downloading the pretrained model and test images your folder should look like:

```
datasets/HRPlanesv2/
  ├── HRPlanesv2.yaml
  ├── images/
  │   └── test/
  └── labels/
      └── test/
yolov8l-best.pt
yolo11l-best.pt
```

you can run inference using the following command:

YOLOv8l:

```bash
yolo val model=yolov8l-best.pt data=datasets/HRPlanesv2/HRPlanesv2test.yaml
```

YOLO11l:

```bash
yolo val model=yolo11l-best.pt data=datasets/HRPlanesv2/HRPlanesv2test.yaml
```

This will:

- Load the YOLO11l model
- Perform detection on the provided test images
- Output detected aircraft with bounding boxes and confidence scores
- Reuslts can be seen in runs folder
