# 🚨 Smart Intrusion Detection System

---

## 📌 Description

This project is a real-time intrusion detection system built using Computer Vision and Deep Learning. It detects human presence through a webcam using the YOLOv8 model and triggers an alert when intrusion is detected.

The system automates surveillance and reduces the need for constant human monitoring, making it efficient and reliable for security applications.

---

## 🎯 Features

- Real-time human detection
- Uses YOLOv8 deep learning model
- Intrusion alert system
- Bounding box visualization
- Easy to run and implement

---

## 🛠️ Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- Playsound

---

## 📂 Project Structure
intrusion-detection/
│── main.py
│── requirements.txt
│── README.md
│── alarm.wav (optional)
│── screenshot.png (optional)


---

## ⚙️ Installation

### 1. Clone the repository
git clone  https://github.com/deen-cyber/intrusion-detection.git
cd intrusion-detection


### 2. Create virtual environment
python -m venv .venv

### 3. Activate virtual environment
**Mac/Linux:**
source .venv/bin/activate

**Windows:**
.venv\Scripts\activate


### 4. Install dependencies
pip install -r requirements.txt


Make sure all dependencies are installed properly before running the project.

---

## ▶️ Usage

Run the following command:
python main.py


Press **ESC key** to exit the program.

---

## 📸 Output

- Opens live webcam feed  
- Detects human presence in real-time  
- Draws bounding box around detected person  
- Displays **"INTRUSION!"** label  
- Generates alert message in console  

---

## 📸 Output Screenshot

