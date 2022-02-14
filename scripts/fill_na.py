import pandas as pd
import numpy as np
from impyute.imputation.cs import fast_knn, mice
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster,set_link_color_palette, cut_tree
from scipy.stats import chi2_contingency
import sys


def test_w_clustering(matrix, labels, link, path):

    print('Condensing matrix...')
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
    sns.clustermap(matrix, row_linkage=Z, col_linkage=Z,  cmap='YlGnBu')
    plt.savefig('images/clustermaps/'+path)
    plt.close()

    print('Calculating Chi-Squared Correlation...')
    comp = pd.crosstab(df['state_id'], df['cluster_id'])
    stat, p, dof, _ = chi2_contingency(comp)
    print('Statistic: ', stat, ', P-value: ', p, ', Degrees of Freedom: ', dof, sep='')

print('Reading data...')
df = pd.read_csv('data/distance_matrix_wtb_male_female.csv', index_col=0)
data = df.fillna(0)
labels = data.columns.tolist()
#print(data)
#print(data.isnull().sum(axis=1).tolist()) # a LOT of missing values

#baseline comparison
print('Testing baseline...')
for l in ['single', 'weighted', 'ward', 'average', 'complete']:
    test_w_clustering(data.values.tolist(), labels, l, 'fill_0/'+l+'.png')

print('Filling NAs with fast_knn...')
#TRYING fast_knn
sys.setrecursionlimit(50000)
imputed_training = fast_knn(df.values, k=10)

for l in ['single', 'weighted', 'ward', 'average', 'complete']:
    test_w_clustering(imputed_training, labels, l, 'fill_knn/'+l+'.png')

###Throwing error: "numpy.linalg.LinAlgError: SVD did not converge in Linear Least Squares"
# print('Filling NAs with mice...')
# #TRYING mice
# imputed_training = mice(df.values)
# for l in ['single', 'weighted', 'ward', 'average', 'complete']:
#     test_w_clustering(imputed_training, l, 'fill_mice/'+l+'.png')
