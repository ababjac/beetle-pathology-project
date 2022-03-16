import pandas as pd
import numpy as np
import mantel

#initial test
#set1 = pd.read_csv('data/forAshley/GM16-path.txt', index_col=0).fillna(0)
#set2 = pd.read_csv('data/forAshley/GM16-tree.txt', index_col=0).fillna(0)
#print(set1.shape, set2.shape)
#print(mantel.test(set1.values, set2.values))

DIR = 'data/forAshley/'
OUT = open('data/mantel-results-fill0.txt', 'w')

for i in range(1, 56):
    if i in [8, 23, 24, 25, 31, 36, 41, 44, 45, 46, 47, 52]: #we are missing files apparently?
        continue

    if i < 10:
        count = '0'+str(i)
    else:
        count = str(i)

    filename = DIR+'GM'+count

    path = pd.read_csv(filename+'-path.txt', index_col=0).fillna(0)
    tree = pd.read_csv(filename+'-tree.txt', index_col=0).fillna(0)

    if path.shape != tree.shape:
        tree_array = np.array(tree, order='F')
        tree_array.resize(path.shape)

        tree = tree_array
        path = path.values

    print(path.shape, tree.shape)

    try:
        r, p, z = mantel.test(path, tree)
    except:
        continue

    OUT.write(filename+':\n')
    OUT.write('r: '+str(r)+', p-value: '+str(p)+', z-score: '+str(z)+'\n\n')
