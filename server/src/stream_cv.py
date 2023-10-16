import cv2

def getCameraStream():
    cam = cv2.VideoCapture(0)

    while True:
        val, mat = cam.read()
        if not val:
            break

        val, jpgImg = cv2.imencode('.jpg', mat)
        jpgBin = bytearray(jpgImg.tobytes())

        yield (b'--PNPframe\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            jpgBin + b'\r\n')