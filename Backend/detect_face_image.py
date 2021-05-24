import cv2
import pathlib
from AIProjektZaliczeniowy.settings import MEDIA_ROOT


def detect_image(x):
    tmp = pathlib.Path().absolute()
    face_cascade = cv2.CascadeClassifier(str(tmp)+'/Backend/'+'haarcascade_frontalface_default.xml')
    path = '{y}/{x}'.format(y = str(MEDIA_ROOT),x = x)
    print(path)
    img = cv2.imread(str(path), 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite(path, img)
    cv2.waitKey()

