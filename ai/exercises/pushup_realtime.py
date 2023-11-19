import cv2
import mediapipe as mp
import pandas as pd
import pickle

# Load the trained model using pickle
with open('trained_pushup_model.pkl', 'rb') as file:
    best_clf = pickle.load(file)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
landmark_names = [f'x{i}' for i in range(33)] + [f'y{i}' for i in range(33)] + [f'z{i}' for i in range(33)] + [f'v{i}' for i in range(33)]

cap = cv2.VideoCapture('pushup_videos/archedback1.mp4')

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, image = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            landmarks = []
            for lm in results.pose_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z, lm.visibility])

            landmarks_df = pd.DataFrame([landmarks], columns=landmark_names)
            pose_label = best_clf.predict(landmarks_df)[0]

            # Text settings
            font_scale = 1.5  # Increase the font size
            font = cv2.FONT_HERSHEY_COMPLEX  # Change the font style
            text = pose_label
            text_size = cv2.getTextSize(text, font, font_scale, 2)[0]
            text_x = 10
            text_y = 50  # Adjust the y position to accommodate larger text
            text_w = text_size[0]
            text_h = text_size[1]

            # Draw rectangle background
            cv2.rectangle(image, (text_x, text_y + 5), (text_x + text_w, text_y - text_h - 5), (0, 0, 0), -1)
            
            # Put text on the image
            cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(image, 'No Pose Detected', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 2.0, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Raw webcam feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
