import os
import shutil
import eval.conversion as conv

source_path = "dataset/train_formulas/"
num_claus = []

for filename in os.listdir(source_path):
    assert(filename[-4:] == ".cnf")
    lcg_filename = filename.split(".")[0] + "_lcg_edge_list"
    LCG = conv.sat_to_LCG(source_path + "/" + filename)
    num_claus.append((filename, len(LCG)))

num_claus_ord = sorted(num_claus, key=lambda x: x[1])

if not os.path.isdir(source_path+"utiles"):
    os.mkdir(source_path+"utiles")

for f,_ in num_claus_ord[:10]:
    shutil.copy(source_path+f, source_path+"utiles")