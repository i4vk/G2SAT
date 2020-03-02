import os
import shutil

path = "dataset/train_formulas/"
archivos = os.listdir(path)

num_claus = []

for archivo in archivos:
    if os.path.isfile(path+archivo):
        f = open(path+archivo)
        line = f.readline()[:-1].split(" ")
        num_claus.append((archivo,int(line[2])+int(line[3])))

num_claus_ord = sorted(num_claus, key=lambda x: x[1])

if not os.path.isdir(path+"utiles"):
    os.mkdir(path+"utiles")

for f,_ in num_claus_ord[:10]:
    shutil.copy(path+f, path+"utiles")
