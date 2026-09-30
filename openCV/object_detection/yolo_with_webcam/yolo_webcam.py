from ultralytics import YOLO
import os
from pathlib import Path
import cv2
import cvzone
import math

script_dir = Path(__file__).parent

# Loading model
model = YOLO(os.path.join(script_dir.parent, "yolo_weights/yolov8n.pt")).to("cpu")

className = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
             "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
             "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
             "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
             "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork",
             "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza",
             "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
             "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock",
             "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

cap = cv2.VideoCapture(0)
cap.set(3, 640) # Width
cap.set(4, 480) # Height

while True:
    succ, img = cap.read()
    result = model(img, stream=True)
    for r in result:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # print(x1, y1, x2, y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            conf = math.ceil(box.conf[0] * 100) / 100
            if conf > 0.8:
                cls = int(box.cls[0])
                cvzone.cornerRect(img, (x1, y1, x2 - x1, y2 - y1))
                cvzone.putTextRect(img, f'{className[cls]}    {conf}', (max(0, x1), max(35, y1)))
                print(f'Class: {className[cls]}, Confidence: {conf}')

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()