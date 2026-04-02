import cv2
from ultralytics import YOLO
import time

# Try sound (optional)
try:
    from playsound import playsound
    sound_available = True
except:
    sound_available = False

# Load YOLOv8 model (auto downloads first time)
model = YOLO("yolov8n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

# Alert control
last_alert_time = 0
cooldown = 5  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    # Run detection
    results = model(frame)

    intrusion_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            # Class 0 = person
            if cls == 0:
                intrusion_detected = True

                # Draw box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, "INTRUSION!", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Alert system
    current_time = time.time()
    if intrusion_detected and (current_time - last_alert_time > cooldown):
        print("🚨 Intrusion Detected!")
        
        if sound_available:
            try:
                playsound("alarm.wav")  # optional
            except:
                pass

        last_alert_time = current_time

    # Show output
    cv2.imshow("Intrusion Detection", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()