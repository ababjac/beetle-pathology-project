import pandas as pd
import numpy as np
from skbio.stats.distance import permanova, DistanceMatrix

def force_symmetric(matrix):
    for i in range(matrix.shape[0]):
        matrix[i][i] = 0.0
        for j in range(i, matrix.shape[1]):
            if matrix[i][j] != matrix[j][i]:
                matrix[j][i] = matrix[i][j]

    return matrix

def get_significance(matrix, labels):
    matrix = force_symmetric(matrix)
    dm = DistanceMatrix(matrix)
    print(dm)

    result = permanova(dm, labels)
    print(result)

# def make_matrix_and_labels(df, ext):
#     df.to_csv(ext+'-dist-noheaders.csv', header=False, index=False)
#
#     labels = df.columns.tolist()
#
#     states = []
#     for elem in labels:
#         state = elem.partition('_')[0]
#         states.append(state)
#
#     file = open(ext+'labels-noheaders.csv', 'w')
#     for state in states:
#         file.write(state+',')
#
#     file.close()


gm_df = np.loadtxt('data/gm-dist-noheaders.csv', delimiter=',')
wtb_df = np.loadtxt('data/wtb-dist-noheaders.csv', delimiter=',')

gm_labels = np.loadtxt('data/gm-labels-noheaders.csv', delimiter=',', dtype=str)
wtb_labels = np.loadtxt('data/wtb-labels-noheaders.csv', delimiter=',', dtype=str)

#print(gm_df.shape)
#print(wtb_df.shape)

#print(len(gm_labels))
#print(len(wtb_labels))

get_significance(gm_df, gm_labels)
get_significance(wtb_df, wtb_labels)
