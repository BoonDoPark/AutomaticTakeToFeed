import cv2
import numpy as np
import time
import os

def getCameraStream():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("웹캠을 열 수 없습니다. 프로그램을 종료합니다.")
        exit()

    ret, prev_frame = cam.read()
    if not ret:
        print("초기 프레임을 캡처할 수 없습니다. 프로그램을 종료합니다.")
        exit()

    image_save_dir = "image/"
    image_filename = None
    image_save_interval = 60

    while True:
        val, frame = cam.read()

        if not ret:
            break
        
        frame_diff = cv2.absdiff(prev_frame, frame)
        diff_percentage = np.count_nonzero(frame_diff) / frame_diff.size

        if diff_percentage > 0.4:
            image_filename = f"capture_image_{int(time.time())}.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"이미지를 저장했습니다 : {image_filename}")

        if image_filename and (time.time() - os.path.getmtime(image_filename)) > image_save_interval:
            image_filename = f"capture_image_{int(time.time())}.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"60초마다 이미지를 저장했습니다 : {image_filename}")

        prev_frame = frame

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & OxFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()