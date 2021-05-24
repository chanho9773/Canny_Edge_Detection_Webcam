import cv2

def canny_video():

    cap = cv2.VideoCapture('KHU.mp4')

    while True:
        ret, frame = cap.read()

        frame = frame[600:900, 400:1500]

        cv2.imshow('Canny Edge', frame)

        if cv2.waitKey(20) == ord('q'):
            break

canny_video()
