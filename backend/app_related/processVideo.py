import sys
from flask import make_response
import time
import requests
import cv2
import mediapipe as mp
import pandas as pd
from joblib import load

def handleProcessVideo(route,exercise):
    with open('trained_pushup_model.pkl', 'rb') as file:
        best_clf = load(file)

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    landmark_names = [f'x{i}' for i in range(33)] + [f'y{i}' for i in range(33)] + [f'z{i}' for i in range(33)] + [f'v{i}' for i in range(33)]

    cap = cv2.VideoCapture(route)

    # Get video properties for the output file
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

    # Initialize video writer
    out = cv2.VideoWriter('tmp/processed_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))

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
                font_scale = 1.5
                font = cv2.FONT_HERSHEY_COMPLEX
                text = pose_label
                text_size = cv2.getTextSize(text, font, font_scale, 2)[0]
                text_x = 10
                text_y = 50
                text_w = text_size[0]
                text_h = text_size[1]

                # Draw rectangle background
                cv2.rectangle(image, (text_x, text_y + 5), (text_x + text_w, text_y - text_h - 5), (0, 0, 0), -1)
                
                # Put text on the image
                cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 255, 0), 2, cv2.LINE_AA)
            else:
                cv2.putText(image, 'No Pose Detected', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 2.0, (0, 0, 255), 2, cv2.LINE_AA)

            # Write the processed frame to the video
            out.write(image)

        cap.release()
        out.release()  # Release the video writer
        cv2.destroyAllWindows()


def processVideo_api(args,storage):
    current_time_string = str(int(time.time()))
    exercise = args.get("exercise")
    local_file_path = f"tmp/test.mov"
    
    response = requests.get(args.get("downloadUrl"))
    print(response)
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
    
    print(response)
    
    handleProcessVideo(local_file_path,exercise)
    
    print(local_file_path)
    
    local_file_path = f"tmp/processed_video.mp4"
    destination_blob_name = f"files/processed_{current_time_string}.mov"
    
    bucket = storage.bucket()  
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)
    blob.make_public()
    download_url = blob.public_url
    
    
    return make_response({"message":download_url})