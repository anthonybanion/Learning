# -*- coding: utf-8 -*-
"""computer_vision - Windows Compatible Version"""

import cv2
import os

# ----------------------------
# IMAGE FACE DETECTION
# ----------------------------


image_path = r"C:\github\computer vision application\cv_application\sample_data\dhoni and tendulkar.jpg"


if not os.path.exists(image_path):
    print("Image not found:", image_path)
else:
    image = cv2.imread(image_path)

    
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)

    # Convert to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", image_gray)
    cv2.waitKey(0)

    # Load Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    detections = face_cascade.detectMultiScale(image_gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around faces
    for (x, y, w, h) in detections:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display result
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)

    # Save result
    result_image_path = r"C:\github\computer vision application\cv_application\outputs\result.jpg"
    if not os.path.exists(os.path.dirname(result_image_path)):
        os.makedirs(os.path.dirname(result_image_path))
    cv2.imwrite(result_image_path, image)
    print(f"Image processed and saved at: {result_image_path}")

cv2.destroyAllWindows()

# ----------------------------
# VIDEO FACE DETECTION
# ----------------------------

video_path = r"C:\github\computer vision application\cv_application\sample_data\3249935-sd_426_240_25fps.mp4"

if not os.path.exists(video_path):
    print("Video not found:", video_path)
else:
    if not os.path.exists(r"C:\github\computer vision application\cv_application\outputs"):
        os.makedirs(r"C:\github\computer vision application\cv_application\outputs")

    cap = cv2.VideoCapture(video_path)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        r"C:\github\computer vision application\cv_application\outputs\result.mp4",
        fourcc, 20.0,
        (int(cap.get(3)), int(cap.get(4)))
    )

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Optional: show video frame
        cv2.imshow("Video Processing", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit early
            break

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Processing complete. Video saved in 'outputs/result.mp4'")
