from ultralytics import YOLO
import torch
import os

# Force CPU usage to avoid CUDA compatibility issues
torch.cuda.is_available = lambda: False

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

model = YOLO(os.path.join(script_dir, "../../yolov8n.pt")).to("cpu")

# Save results in the script's directory
results = model(os.path.join(script_dir, "images/school_bus.jpg"), 
                show=True, 
                save=True, 
                project=os.path.join(script_dir, "runs"))

