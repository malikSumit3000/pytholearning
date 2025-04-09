import glob
import os
import cv2
import time
from emailing import sending_email
from threading import Thread

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
image = 1


def clean_folder():
    images = glob.glob("images/*.png")
    for item in images:
        os.remove(item)


while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    threshold_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(threshold_frame, None, iterations=7)
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{image}.png", frame)
            image = image + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]
    print(status_list)
    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=sending_email, args=(image_with_object, ))
        email_thread.start()
        print("email sent")

    cv2.putText(img=frame, text=time.strftime("%Y-%m-%d %H:%M:%S"), org=(25, 25),
                fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(20, 100, 200),
                thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow("video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
clean_thread = Thread(target=clean_folder)
clean_thread.start()
