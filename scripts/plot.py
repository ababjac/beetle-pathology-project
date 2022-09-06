import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

gm_df = pd.read_csv('data/gm_dist_matrix_filled_na_KNN_new.csv', index_col=0)
wtb_df = pd.read_csv('data/wtb_dist_matrix_filled_na_KNN_new.csv', index_col=0)

sns.set(rc={"figure.figsize":(8, 8)})

sns.heatmap(gm_df, cmap='RdBu')
plt.title('GM Distance')
#plt.savefig('images/heatmaps/gm_heatmap_new.pdf')
plt.show()

sns.heatmap(wtb_df, cmap='RdBu')
plt.title('WTB Distance')
#plt.savefig('images/heatmaps/wtb_heatmap_new.pdf')
plt.show()
