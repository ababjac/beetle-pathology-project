import pandas as pd
import numpy as np
#from skbio.stats.distance import permanova

def get_significance(df):
    pass
    #dm = DistanceMatrix(df)
    #print(dm)

def make_matrix_and_labels(df, ext):
    df.to_csv(ext+'-dist-noheaders.csv', header=False, index=False)

    labels = df.columns.tolist()

    states = []
    for elem in labels:
        state = elem.partition('_')[0]
        states.append(state)

    file = open(ext+'labels-noheaders.csv', 'w')
    for state in states:
        file.write(state+',')

    file.close()


gm_df = pd.read_csv('data/gm_dist_matrix_filled_na_KNN_new.csv', index_col=0)
wtb_df = pd.read_csv('data/wtb_dist_matrix_filled_na_KNN_new.csv', index_col=0)

make_matrix_and_labels(gm_df, 'gm')
make_matrix_and_labels(wtb_df, 'wtb')
#get_significance(gm_df)
