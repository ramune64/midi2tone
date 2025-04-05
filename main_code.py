import cv2
import numpy as np
from collections import deque

mid_h = 54
mid_s = 151
mid_v = 229
mid = np.array([54, 151, 229])
lower_color = np.array([0, 125, 0])
upper_color = np.array([106, 255, 255])





kenban = ["do","re","mi","fa","so","ra","si"]
kokken = ["do#","re#","fa#","so#","ra#"]
left = "so"
right = "mi"
key = 5
edge = 0
kenbans = deque(kenban)
kokkens = deque(kokken)
left_key = kenban.index(left)
if left == "re":kokkens.rotate(-1)
elif left == "mi" or left == "fa":kokkens.rotate(-2)
elif left == "so":kokkens.rotate(-3)
elif left == "ra":kokkens.rotate(-4)

kenbans.rotate(left_key*-1)
#print(kenbans)
right_key = kenbans.index(right)
num_key = 7*(key-1) + right_key + 1
#print(num_key)
#print(num_key)
global interval
interval = round(1920/(num_key)) + 1
print("interval")
print(interval)
global differ
differ = interval - edge
#print(interval)
#print(kenbans)
black = 11*interval//23 + 5

global all_white
all_white = [0]
global all_black
all_black = []
def make_list(hsv):
    interval = round(1920/(num_key))
    o_int = interval
    aaa = 0
    hsv = cv2.resize(hsv,(1920,1080))
    hsv = hsv[790 : 1080, 0: 1920]
    c = 0
    for i in range(num_key+1):
        c += 1
        if aaa != 0:
            #print(i)
            #print("waaa")
            interval = o_int
            if c%2==0 and c != 1:
                interval = int(interval + 2)
                print(2)
            elif c%2!=0 and c != 1:
                interval = int(interval - 1)
                print(1)
        #print(i)
        cv2.line(hsv, (interval*(i+2)-differ,0), ((interval*(i+2)-differ,280)), (255,0,0), thickness=1, lineType=cv2.LINE_8, shift=0)
        all_white.append(interval*(i+2))
        if kenbans[i%7] == "ra":
            cv2.line(hsv, (int(interval*(i+2)+((interval*2)//23)*-1)-differ,0), (int(interval*(i+2)+((interval*2)//23)*-1)-differ,280), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            cv2.line(hsv, (int(interval*(i+2)+((interval*2)//23)*-1)+black-differ,0), (int(interval*(i+2)+((interval*2)//23)*-1)+black-differ,280), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            all_black.append(int(interval*(i+2)+((interval*2)//23)*-1)-differ)
        elif kenbans[i%7] == "so":
            #print((interval*(i+1)+((interval*3.5)//23+5)*-1+5,0))
            cv2.line(hsv, (int(interval*(i+2)+((interval*3.5)//23)*-1)-differ-5,0), ((int(interval*(i+2)+((interval*3.5)//23)*-1)-differ-5,280)), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            cv2.line(hsv, (int(interval*(i+2)+((interval*3.5)//23)*-1)+black-differ-5,0), ((int(interval*(i+2)+((interval*3.5)//23)*-1)+black-differ-5,280)), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            all_black.append(int(interval*(i+2)+((interval*3.5)//23)*-1)-differ-5)
            #((interval*2)//23)*-1
        elif kenbans[i%7] == "fa":
            #print((interval*(i+1)+((interval*3.5)//23+5)*-1+5,0))
            cv2.line(hsv, (int(interval*(i+2)+((interval*9)//23)*-1)-differ,0), ((int(interval*(i+2)+((interval*9)//23)*-1)-differ,280)), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            cv2.line(hsv, (int(interval*(i+2)+((interval*9)//23)*-1)+black-differ,0), ((int(interval*(i+2)+((interval*9)//23)*-1)+black-differ,280)), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            all_black.append(int(interval*(i+2)+((interval*9)//23)*-1)-differ)
        elif kenbans[i%7] == "re":
            #print((interval*(i+1)+((interval*3.5)//23+5)*-1+5,0))
            cv2.line(hsv, (int(interval*(i+2)+((interval*2.6)//23)*-1)-differ,0), ((int(interval*(i+2)+((interval*2.6)//23)*-1)-differ,280)), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            cv2.line(hsv, (int(interval*(i+2)+((interval*2.6)//23)*-1)+black-differ,0), ((int(interval*(i+2)+((interval*2.6)//23)*-1)-differ+black,280)), (100,100,0), thickness=1, lineType=cv2.LINE_8, shift=0)
            all_black.append(int(interval*(i+2)+((interval*2.6)//23)*-1)-differ)
        elif kenbans[i%7] == "do":
            #print((interval*(i+1)+((interval*3.5)//23+5)*-1+5,0))
            cv2.line(hsv, (int(interval*(i+2)+((interval*8.4)//23)*-1)-differ,0), ((int(interval*(i+2)+((interval*8.4)//23)*-1)-differ,280)), (0,0,100), thickness=1, lineType=cv2.LINE_8, shift=0)
            cv2.line(hsv, (int(interval*(i+2)+((interval*8.4)//23)*-1)+black-differ,0), ((int(interval*(i+2)+((interval*8.4)//23)*-1)+black-differ,280)), (0,0,100), thickness=1, lineType=cv2.LINE_8, shift=0)
            all_black.append(int(interval*(i+2)+((interval*8.4)//23)*-1)-differ)
    all_black.append(1920)
    cv2.imwrite("lined.jpg", hsv)




def getting_sound(hsv,fra,debug):
    sounds = []
    #hsv = cv2.imread(hsv)
    # img[top : bottom, left : right]
    # サンプル1の切り出し、保存
    hsv = cv2.resize(hsv,(1920,1080))
    hsv = hsv[790 : 1080, 0: 1920]
    mask = cv2.inRange(hsv, lower_color, upper_color)
    #output = cv2.bitwise_and(hsv, hsv, mask = mask)
    if debug == 1:
        cv2.imwrite("zmask_img3.jpg", mask)
    #cv2.imshow("preview",mask)
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)
    if debug == 1:
        print(stats)

    #if debug == 1:
        
    #print(kenbans[i%7])
    #print(len(all_white))
    #print(len(all_black))
    #print(kokkens)
        
    def get_sound(n):
        if stats[n][3] <= 180:
            key_pos = stats[n][0] + stats[n][2]/2
            a = [q for q in all_black if q>=key_pos]
            try :
                now_key = all_black.index(a[0]) -1
            except:
                cv2.imwrite("error_pic.jpg",hsv)
                print(key_pos)
                print(all_black[-1])
                print(stats)
                print(fra)
            sounds.append(str(now_key//5+1) + "/" + str(kokkens[now_key%5]))
        else:
            key_pos = stats[n][0] + stats[n][2]
            #print(key_pos)
            #a = [all_white >= key_pos]
            #all_white[a]
            a = [q for q in all_white if q>=key_pos]
            now_key = all_white.index(a[0]) -1
            #print(now_key)
            sounds.append(str(now_key//7+1) + "/" +str(kenbans[now_key%7]))
            #print(kenbans[now_key%7])

    w = open("sounds.txt","a")
    if len(stats) >= 2:
        if stats[1][4] >= 3000:
            get_sound(1)
        else:pass#print("none")
        if len(stats) >= 3:
            if stats[2][4] >= 3000:
                get_sound(2)
        if len(stats) >= 4:
            if stats[3][4] >= 3000:
                get_sound(3)
    elif len(stats) <= 1:pass#print("none")
    if len(sounds) == 1:
        w.write("\n"+str(sounds[0]))
    elif len(sounds) == 2:
        w.write("\n"+str(sounds[0]) + "+" + str(sounds[1]))
        #if (str(sounds[0]) + "+" + str(sounds[1])) == "do#+re#":
            #cv2.imwrite("mask_waon.jpg", mask)
            #print(stats)
    elif len(sounds) == 1:
        w.write("\n"+str(sounds[0]) + "+" + str(sounds[1]) + "+" + str(sounds[2]))
    elif len(sounds) == 0:
        w.write("*none")
    w.close()
    
#getting_sound(cv2.imread("nya.png"))


