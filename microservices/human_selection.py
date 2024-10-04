import cv2
import numpy as np

def select_human(frame):
    r = cv2.selectROI("Select Human", frame, fromCenter=False, showCrosshair=True)
    if r != (0, 0, 0, 0):
        x, y, w, h = r
        frame = frame[y:y+h, x:x+w]
    cv2.destroyWindow("Select Human")
    return frame

def receive_video_frames(frames):
    selected_frames = []
    for frame in frames:
        selected_frame = select_human(frame)
        selected_frames.append(selected_frame)
    return selected_frames
