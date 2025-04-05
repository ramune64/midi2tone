path = "sounds.txt"

all_sounds = open(path,"r")
sounds_line = all_sounds.readlines()
all_sounds.close()

for i in range(len(sounds_line)):
    sounds_line[i] = sounds_line[i].replace("\n","")


if "*" in sounds_line[0]:
    last_sound = sounds_line[0].split("*")[0]
else:last_sound = sounds_line[0]
sound_only = ""
count = 0
to_txt = open("sound_and_length.txt","w")
to_txt.close()
to_txt = open("sound_and_length.txt","a")
for p in sounds_line:
    if "*" in p:
        sound_only = p.split("*")[0]
    else:sound_only = p
    if last_sound == sound_only:
        count += 1
        if "*" in p:
            to_txt.write(last_sound)
            to_txt.write(","+str(round(count/30*1000))+"\n")
            to_txt.write("delay")
            to_txt.write(","+str(round(p.count("*")/30*1000))+"\n")
            count = 0
    elif last_sound != sound_only:
        count += 1
        to_txt.write(last_sound)
        to_txt.write(","+str(round(count/30*1000))+"\n")
        count = 1
        if "*" in p:
            to_txt.write(sound_only)
            to_txt.write(","+str(count/30*1000)+"\n")
            to_txt.write("delay")
            to_txt.write(","+str(round(p.count("*")/30*1000))+"\n")
            count = 0
    last_sound = sound_only
to_txt.close()




#print(sounds_line)
