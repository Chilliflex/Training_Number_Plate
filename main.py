from ultralytics import YOLO


# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data="data.yaml", epochs=120, imgsz=640, project='runs', name='license_plate_model', patience=10)

# Save the trained model
model.save('./license_plate_detector.pt')