# Face Detection with OpenCV

A simple Python project for real-time face detection using your webcam and OpenCV.

## Features

- Detects faces in real-time from your webcam
- Draws a rectangle around each detected face
- Press `q` or `Esc` to close the webcam window

## Requirements

- Python 3.x
- opencv-python
- numpy

## How it Works


1. The program opens your webcam and reads video frames.
2. Each frame is converted to grayscale for faster and more accurate face detection.
3. The Haar Cascade model detects faces in the frame.
4. A green rectangle is drawn around each detected face.
5. The video window closes when you press q or Esc.

## How to Run

```bash
python Project8-Face Detection with OpenCV.py

