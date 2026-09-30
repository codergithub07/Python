from ultralytics import YOLO
import torch
import os
from pathlib import Path

# Force CPU usage to avoid CUDA compatibility issues
# torch.cuda.is_available = lambda: False

# Get the script's directory
# script_dir = os.path.dirname(os.path.abspath(__file__))

# print(os.getcwd())

# script_dir = Path(__file__).resolve().parent # Absolute path to the script's directory
script_dir = Path(__file__).parent  # May return a relative path
# print(script_dir)

model = YOLO(os.path.join(script_dir.parent, "yolo_weights/yolov8l.pt")).to("cpu")

# Save results in the script's directory
results = model(os.path.join(script_dir, "images/school_bus.jpg"), 
                show=True, 
                save=True, 
                project=os.path.join(script_dir, "predictions"))
