musicname = input("musicname:")
fff = open("music\{}.ino".format(musicname),"w")
fff.close()
base = 3
kenban = ["do","re","mi","fa","so","ra","si"]
kokken = ["do#","re#","fa#","so#","ra#"]
all_kenban = ["do","do#","re","re#","mi","fa","fa#","so","so#","ra","ra#","si"]
b_freq_0 = ["139","156","185","208","233"]
b_freq_1 = ["277","311","370","415","466"]
b_freq_2 = ["554","622","740","831","932"]
b_freq_3 = ["1109","1245","1480","1661","1865"]
b_freq_4 = ["2217","2489","2960","3322","3729"]
b_freqs = [b_freq_0,b_freq_1,b_freq_2,b_freq_3,b_freq_4]
w_freq_0 = ["131","147","165","175","196","220","247"]
w_freq_1 = ["262","294","330","349","392","440","494"]
w_freq_2 = ["523","587","659","698","784","880","988"]
w_freq_3 = ["1047","1175","1319","1397","1568","1760","1976"]
w_freq_4 = ["2093","2349","2637","2749","3136","3520","3951"]
w_freqs = [w_freq_0,w_freq_1,w_freq_2,w_freq_3,w_freq_4]
path = "sound_and_length.txt"
r_txt = open(path)
sounds_line = r_txt.readlines()
for i in range(len(sounds_line)):
    sounds_line[i] = sounds_line[i].replace("\n","")


music = open("music\{}.ino".format(musicname),"a")
music.write("void {}()".format(musicname)+"{"+"\n")
for p in sounds_line:
    only_sound = p.split(",")[0]
    time = p.split(",")[-1]
    if "+" in only_sound:
        waon = only_sound.split("+")
        key_w = []
        sound_w = []
        for q in waon:
            key_w.append(only_sound.split("/")[0])
            sound_w.append(only_sound.split("/")[-1])
        key_w_s = sorted(key_w)
        for e in range(len(sound_w)):
            sound_w[e] = all_kenban.index(sound_w[e])
        sound_w_s = sorted(sound_w)
        if key_w_s[0] == key_w_s[-1]:
            sound = all_kenban[sound_w_s[0]]
            key = key_w_s[0]
            if "#" in sound:
                music.write("tone(pin,{},{});\n".format(b_freqs[int(key)-base][kokken.index(sound)],time))
                music.write("delay({});\n".format(time))
            else:
                music.write("tone(pin,{},{});\n".format(w_freqs[int(key)-base][kenban.index(sound)],time))
                music.write("delay({});\n".format(time))

        else:
            key_w_r = [t for t in key_w if t==key_w_s[0]]
            key = key_w_r[0]
            sound = sound_w[key_w.index(key)]
            if "#" in sound:
                music.write("tone(pin,{},{});\n".format(b_freqs[int(key)-base][kokken[sound]],time))
                music.write("delay({});\n".format(time))
            else:
                music.write("tone(pin,{},{});\n".format(w_freqs[int(key)-base][kenban[sound]],time))
                music.write("delay({});\n".format(time))

            
                

    elif only_sound == "delay":
        music.write("delay({});\n".format(time))
    elif "#" in only_sound:
        key,sound = only_sound.split("/")
        music.write("tone(pin,{},{});\n".format(b_freqs[int(key)-base][kokken.index(sound)],time))
        music.write("delay({});\n".format(time))
    else:
        key,sound = only_sound.split("/")
        music.write("tone(pin,{},{});\n".format(w_freqs[int(key)-base][kenban.index(sound)],time))
        music.write("delay({});\n".format(time))


music.write("}")
music.close()