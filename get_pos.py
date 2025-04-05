import cv2

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

img = cv2.imread('midi2tone/hsv_lined3.jpg')
cv2.imshow('sample', img)
cv2.setMouseCallback('sample', onMouse)
cv2.waitKey(0)