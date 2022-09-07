import pandas as pd
import numpy as np
from skbio.stats.distance import permanova

def get_significance(df):
    pass
    #dm = DistanceMatrix(df)
    #print(dm)


gm_df = pd.read_csv('data/gm_dist_matrix_filled_na_KNN_new.csv', index_col=0)
wtb_df = pd.read_csv('data/wtb_dist_matrix_filled_na_KNN_new.csv', index_col=0)

#get_significance(gm_df)
