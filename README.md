
# Hand_Recoginiton_using_gestures
# Hand Volume Control using MediaPipe and PyAutoGUI

## Overview

This project utilizes the MediaPipe library for hand tracking and PyAutoGUI for controlling system volume and other actions based on hand gestures. The application captures hand landmarks through a webcam feed and interprets specific gestures to trigger corresponding actions.

## Prerequisites

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

Install the required libraries using the following:

```bash
pip install opencv-python mediapipe pyautogui
```
## Hand Gestures

- **Thumb and Forefinger Pinch (Distance > 150):** Switch to the next tab (`Ctrl + Tab`).
- **Thumb and Forefinger Spread (40 < Distance < 100):** Decrease system volume (`Volume Down`).
- **Thumb and Forefinger Spread (Distance > 100):** Increase system volume (`Volume Up`).
- **Thumb and Pinky Spread (Distance > 200):** Open a new tab (`Ctrl + T`).

## Dependencies

- [OpenCV](https://github.com/opencv/opencv)
- [MediaPipe](https://github.com/google/mediapipe)
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
