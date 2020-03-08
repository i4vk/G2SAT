import sys
from eval.conversion import sat_to_LCG
import community

if len(sys.argv) != 2:
    print("Error en el paso de parámetros")
    exit(-1)

archivo = sys.argv[1]

with open(archivo, 'r') as f:
    len_claus = 0
    for line in f:
        div = line.split(' ')
        if div[0] != 'c':
            if div[0] == 'p':
                num_var = int(div[2])
                num_claus = int(div[3])
            else:
                len_claus += len(div)-1

    LCG = sat_to_LCG(archivo)
    partition = community.best_partition(LCG)
    modularity = community.modularity(partition, LCG)
    num_communities = len(set(partition.values()))

                
                
media_len_claus = len_claus/num_claus
print(f'Num. var.: {num_var}')
print(f'Num. claus.: {num_claus}')
print(f"Longitud media de claus.: {media_len_claus}")
print(f'Num. communities.: {num_communities}')
print(f'Modularity: {modularity}')