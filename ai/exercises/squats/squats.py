import cv2
import mediapipe as mp
import numpy as np
import csv
import os

# Initialize mediapipe pose class.
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Initialize video capture.
cap = cv2.VideoCapture('squats_videos/squatscorrect2.MOV')

# Prepare CSV file to store landmarks.
csv_file = 'squatscorrect2.csv'
landmark_names = [f'x{i}' for i in range(33)] + [f'y{i}' for i in range(33)] + [f'z{i}' for i in range(33)] + [f'v{i}' for i in range(33)]
with open(csv_file, mode='w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['label'] + landmark_names)

# Initialize pose detection with mediapipe.
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, image = cap.read()

        if not ret:
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('Raw webcam feed', image)

        key = cv2.waitKey(10)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF in [ord('u'), ord('d'), ord('h'), ord('k')]:
            label = ''
            if key & 0xFF == ord('u'):
                label = 'up'
            elif key & 0xFF == ord('d'):
                label = 'down'
            elif key & 0xFF == ord('h'):
                label = 'half_reps'
            elif key & 0xFF == ord('k'):
                label = 'arched_back'

            if results.pose_landmarks:
                landmarks = [label] + [lm.x for lm in results.pose_landmarks.landmark] + \
                            [lm.y for lm in results.pose_landmarks.landmark] + \
                            [lm.z for lm in results.pose_landmarks.landmark] + \
                            [lm.visibility for lm in results.pose_landmarks.landmark]
                
                with open(csv_file, mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(landmarks)

cap.release()
cv2.destroyAllWindows()