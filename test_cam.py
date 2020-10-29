import cv2
import os
from time import sleep


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = cam.read()
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #     count += 1
    #     Сохраняем лицо
    #     cv2.imwrite('face/user.' + str(face_id) + '.' + str(count) + '.jpg', gray[y:y + h, x:x + w])
    cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff  # 'ESC'
    if k == 27:
        break
    # elif count >= 30:  # Если сохранили 30 изображений выход.
    #     break
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
