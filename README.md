# 🖐️ Hand Gesture Volume Control using OpenCV, MediaPipe & Pycaw

This project allows you to control your system's volume using hand gestures via your webcam. It uses **OpenCV** for capturing video, **MediaPipe** for hand tracking, and **pycaw** to control system audio.

---

## 📦 Requirements

Make sure you have the following libraries installed:

```bash
pip install opencv-python mediapipe pycaw comtypes numpy
```

Also, create a module file named `hands_tracking_project_module.py` which contains the `HandDetector` class (you can use MediaPipe to implement it).

---

## 🧠 How It Works

- The webcam captures the video in real-time.
- MediaPipe detects your hand and identifies key landmarks.
- The distance between **thumb tip (id 4)** and **index finger tip (id 8)** is measured.
- Based on the distance, system volume is adjusted using pycaw.
- A visual volume bar is drawn on the video.

---

## 📂 Project Structure

```
.
├── main.py                          # Main script
├── hands_tracking_project_module.py # Contains HandDetector class using MediaPipe
└── README.md
```

---

## ▶️ How to Run

```bash
python main.py
```

> Press `Q` to quit the webcam window.

---

## 📸 Features

- Real-time hand detection and tracking.
- Control system volume using finger distance.
- Visual feedback via volume bar.
- Uses smooth interpolation for realistic volume control.

---

## 💡 Controls

- 👌 **Pinch thumb and index finger** → Minimum volume.
- ✌️ **Spread thumb and index finger** → Maximum volume.

---

## ⚠️ Notes

- Works **only on Windows**, as `pycaw` relies on Windows Core Audio.
- Make sure your webcam is connected and not being used by other apps.
- Install compatible fonts and ensure the webcam resolution is set to `640x480` for best results.

---

## ✍️ Author

Developed by **[Your Name]**  
For improvements, suggestions, or bugs, feel free to contribute or raise issues.

