from ultralytics import YOLO
import torch

# Force CPU usage to avoid CUDA compatibility issues
torch.cuda.is_available = lambda: False

model = YOLO("yolov8n.pt").to("cpu")

results = model("object_detection/running_yolo/images/school_bus.jpg", show=True, save=True)