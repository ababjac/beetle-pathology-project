import pandas as pd
import numpy as np
import statistics
import math
from sklearn import linear_model
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
import random
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as col
import seaborn as sns
import plotly.figure_factory as ff
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster,set_link_color_palette, cut_tree
from scipy.spatial.distance import squareform
from scipy_cut_tree_balanced import cut_tree_balanced
from sklearn import metrics

print('Reading data...')
data = pd.read_csv('data/distance_matrix_wtb_male_female.csv', index_col=0)
data = data.fillna(0)
labels = data.columns.tolist()

print('Condensing matrix...')
matrix = data.values.tolist()
n = len(matrix)

#same format as returned by scipy pdist()
condensed_matrix = [0]*round(n*(n-1) / 2)
for j in range(0, n):
    for i in range(0, j):
        condensed_matrix[n * i + j - ((i + 2) * (i + 1)) // 2] = matrix[j][i]

#print(condensed_matrix)

print('Computing Linkages...')
Z = linkage(condensed_matrix, method='single')
#print(Z)

# print('Creating Clustermap...')
# sns.clustermap(data, row_linkage=Z, col_linkage=Z,  cmap='YlGnBu')
# plt.savefig('images/clustermaps/ward.png')
# plt.close()

#print('Creating clusters using cut_tree...')
#clusters = cut_tree(Z, n_clusters=4)
print('Creating clusters using fcluster...')
clusters = fcluster(Z, 4, criterion='distance')
print(clusters)
#clusters_flattened = [elem[0] for elem in clusters]
#print(clusters_flattened)

df = pd.DataFrame()
df['labels'] = labels
df['cluster_id'] = clusters

states = []
for elem in labels:
    state = elem.partition('_')[0]

    if state == 'CA':
        states.append(0)
    elif state == 'AZ':
        states.append(1)
    elif state == 'NM':
        states.append(2)
    elif state == 'UT':
        states.append(3)

print(states)
df['state_id'] = states
