import cv2
import os
import sys
import time
asciiList = 'Ñ@#W$9876543210?!abc;:+=-,._     '[::-1]

def getAscii(grayscale_value):
    char_len = len(asciiList)
    corr_char_value = int(grayscale_value/255 * char_len - 1)
    return asciiList[corr_char_value]


cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()
    scale_percent = 10

    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent * 0.75 / 100)
    dim = (width, height)

    new_frame = cv2.resize(frame, dim)
    # print(new_frame.shape)
    grayscale = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
    # img = np.zeros(new_frame.shape, np.uint8)
    os.system('clear')
    for i in range(height):
        for j in range(width):
            sys.stdout.write(getAscii(grayscale[i][j]))
        sys.stdout.write('\n')
    time.sleep(0.05)
    cv2.imshow("frame", grayscale)
    # cv2.imshow("frame2", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
