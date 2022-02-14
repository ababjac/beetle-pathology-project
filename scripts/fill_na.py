import pandas as pd
import numpy as np
from impyute.imputation.cs import fast_knn, mice
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster,set_link_color_palette, cut_tree
from scipy.stats import chi2_contingency
import sys


def test_w_clustering(data, link, path):
    labels = data.columns.tolist()

    print('Condensing matrix...')
    matrix = data.values.tolist()
    n = len(matrix)

    #same format as returned by scipy pdist()
    condensed_matrix = [0]*round(n*(n-1) / 2)
    for j in range(0, n):
        for i in range(0, j):
            condensed_matrix[n * i + j - ((i + 2) * (i + 1)) // 2] = matrix[j][i]

    print('Computing Linkages...')
    Z = linkage(condensed_matrix, method=link)

    print('Creating clusters with cut_tree...')
    clusters = cut_tree(Z, n_clusters=4)
    #print(clusters)
    clusters_flattened = [elem[0] for elem in clusters]
    #print(clusters_flattened)

    df = pd.DataFrame()
    df['labels'] = labels
    df['cluster_id'] = clusters_flattened

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

    #print(states)
    df['state_id'] = states

    print('Creating Clustermap...')
    sns.clustermap(data, row_linkage=Z, col_linkage=Z,  cmap='YlGnBu')
    plt.savefig('images/clustermaps/'+path)
    plt.close()

    print('Calculating Chi-Squared Correlation...')
    comp = pandas.crosstab(df['state_id'], df['cluster_id'])
    stat, p, dof = chi2_contingency([comp[0].values, comp[1].values])
    print('Statistic: ', stat, ', P-value: ', p, ', Degrees of Freedom: ', dof, sep='')

print('Reading data...')
data = pd.read_csv('data/distance_matrix_wtb_male_female.csv', index_col=0)
#print(data)
#print(data.isnull().sum(axis=1).tolist()) # a LOT of missing values

LINKAGE = 'single'

print('Filling NAs with fast_knn...')
#TRYING fast_knn
sys.setrecursionlimit(50000)
imputed_training = fast_knn(data.values, k=10)
test_w_clustering(imputed_training, LINKAGE, 'fill_knn/'+LINKAGE+'.png')

print('Filling NAs with mice...')
#TRYING mice
imputed_training = mice(data.values)
test_w_clustering(imputed_training, LINKAGE, 'fill_mice/'+LINKAGE+'.png')
