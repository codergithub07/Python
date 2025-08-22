from ultralytics import YOLO

model = YOLO("yolov8n.pt").to("cpu")

results = model("object_detection/running_yolo/images/school_bus.jpg", show=True, save=True)