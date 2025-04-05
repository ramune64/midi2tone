import cv2
import os
from main_code import getting_sound,make_list
cap_file = cv2.VideoCapture("videos\.mp4")
print(cap_file.isOpened())
print(cap_file.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap_file.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap_file.get(cv2.CAP_PROP_FPS))
print(cap_file.get(cv2.CAP_PROP_FRAME_COUNT))
print(cap_file.get(cv2.CAP_PROP_FRAME_COUNT)/cap_file.get(cv2.CAP_PROP_FPS))
aaa = cap_file.get(cv2.CAP_PROP_FRAME_COUNT)
#print(ret)
#cv2.imwrite("frame.jpg",frame)
#os.remove("sounds.txt")
aaaaa = open("sounds.txt","w")
aaaaa.close()
for ff in range(1):
    cap_file.set(cv2.CAP_PROP_POS_FRAMES, ff)
    ret, frame = cap_file.read()
    make_list(frame)
for f in range(int(aaa)):
#for f in range(2):
    #f += 1530
    #print(frame.shape)
    #hsv = cv2.resize(frame[f],(1920,1080))
    #cv2.imwrite("frame.jpg",hsv)
    cap_file.set(cv2.CAP_PROP_POS_FRAMES, f)
    ret, frame = cap_file.read()
    #if f == 188:cv2.imwrite("frame_188.jpg",frame)
    getting_sound(frame,f,0)
    #cv2.imshow("a",frame)