import sys
from eval.conversion import sat_to_VIG
import community

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Error en el paso de parámetros")
    exit(-1)

archivo = sys.argv[1]

with open(archivo, 'r') as f:
    len_claus = 0
    min_len = float('Inf')
    for line in f:
        div = line.split(' ')
        if div[0] != 'c':
            if div[0] == 'p':
                num_var = int(div[2])
                num_claus = int(div[3])
            else:
                len_claus += len(div)-1
                if (len(div)-1) < min_len:
                    min_len = len(div)-1

    VIG = sat_to_VIG(archivo)
    partition = community.best_partition(VIG)
    modularity = community.modularity(partition, VIG)
    num_communities = len(set(partition.values()))                
                
media_len_claus = len_claus/num_claus

if len(sys.argv) == 3:
    if sys.argv[2] == 'csv':
        print(f'{num_var},{num_claus},{media_len_claus},{min_len},{num_communities},{modularity}')
else: 
    print(f'Num. var.: {num_var}')
    print(f'Num. claus.: {num_claus}')
    print(f"Longitud media de claus.: {media_len_claus}")
    print(f"Long. clausula más corta: {min_len}")
    print(f'Num. communities.: {num_communities}')
    print(f'Modularity: {modularity}')