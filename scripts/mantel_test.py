import pandas as pd
import numpy as np
import mantel
from scipy.spatial.distance import squareform

#initial test
#set1 = pd.read_csv('data/forAshley/GM16-path.txt', index_col=0).fillna(0)
#set2 = pd.read_csv('data/forAshley/GM16-tree.txt', index_col=0).fillna(0)
#print(set1.shape, set2.shape)
#print(mantel.test(set1.values, set2.values))

DIR = 'data/imputed/'
OUT = open('data/mantel-results-fillKNN.txt', 'w')

for i in range(1, 56):
    if i in [8, 19, 23, 24, 25, 31, 36, 41, 44, 45, 46, 47, 52]: #we are missing files apparently?
        continue

    if i < 10:
        count = '0'+str(i)
    else:
        count = str(i)

    filename = DIR+'GM'+count

    path = pd.read_csv(filename+'-path.txt', index_col=0).fillna(0)
    tree = pd.read_csv(filename+'-tree.txt', index_col=0).fillna(0)
    #print(path.shape, tree.shape)

    if path.shape != tree.shape:
        path = path.values
        tree = tree.values

        #print(path.shape, tree.shape)
        if tree.shape > path.shape:
            if path.shape[1] < path.shape[0]:
                new_size = path.shape[1]
            else:
                new_size = path.shape[0]

            tree_array = []
            for i in range(new_size):
                tmp = [tree[i][j] for j in range(new_size)]
                tree_array.append(tmp)

            tree = np.array(tree_array)

        else:
            if tree.shape[1] < tree.shape[0]:
                new_size = tree.shape[1]
            else:
                new_size = tree.shape[0]

            path_array = []
            for i in range(new_size):
                tmp = [path[i][j] for j in range(new_size)]
                path_array.append(tmp)

            path = np.array(path_array)

    try:
        r, p, z = mantel.test(squareform(path, checks=False), squareform(tree, checks=False))
    except:
        continue

    OUT.write('GM'+count+':\n')
    OUT.write('r: '+str(r)+', p-value: '+str(p)+', z-score: '+str(z)+'\n\n')
