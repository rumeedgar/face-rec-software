import face_recognition
import cv2
import os
import glob
import numpy as np


class RecEngine:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25