from ultralytics import YOLO

# Create a new YOLO model from scratch
# model = YOLO("yolo11plane.yaml")

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11n.pt")

if __name__ == '__main__':
    # Train the model using the plane dataset
    results = model.train(data="HRPlanesv2.yaml", epochs=10, imgsz=640)

    # Evaluate the model's performance on the validation set
    results = model.val()

    # # Perform object detection on an image using the model
    # results = model("https://ultralytics.com/images/bus.jpg")

    # Export the model to ONNX format
    success = model.export(format="onnx")