from moviepy.editor import *

### File names
num = ["01_Hans Muggesen","02_Pixabay","03_Magda Ehlers","04_LOUANN DAVIS","05_Deeana Creates","06_Phillip Dillow","07_Artyom Saqib","08_Mary Grace Monera","09_Kelly Lacy","10_ROMAN ODINTSOV","11_cottonbro","12_J D","13_Wady Mee-asa","14_THAI NHAN","15_How TO","16_ROMAN ODINTSOV","17_cottonbro","18_ROMAN ODINTSOV","19_Damian Scarlassa","20_Nando Lee","21_GRace Wu","22_cottonbro","23_Videas Cl","24_cottonbro","25_ROMAN ODINTSOV","26_ilimdar avgezer","27_Resty Jabines","28_KoolShooters","29_KoolShooters","30_Slobodan Potic","31_Altaf Shah"]

for k in range(0, len(num)) :

    file = "mov/"+num[k]+".mp4"
    block_size = 216
    x_block = 5
    y_block = 5
    count=1

    cwidth = {}
    cheight = {}

    clip = (VideoFileClip(file)
            #!.subclip((0, 11, 30), (0, 11, 40))
            .resize(1))

    for i in range(0, y_block) :
        cheight[i] = (clip.h / 2 - (block_size * 2.5)) + block_size * i
        for j in range(0, x_block) :
            cwidth[j] = (clip.w/2-(block_size * 2.5)) + block_size * j
            cropped_clip = clip.crop(x1=cwidth[j], x2=cwidth[j]+block_size, y1=cheight[i], y2=cheight[i]+block_size)
            cropped_clip.write_gif('mov/'+num[k]+'/'+str(count)+'.gif')
            count += 1
