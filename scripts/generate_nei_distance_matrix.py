import pandas as pd
import numpy as np
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
#import os
#import rpy2.situation


#os.environ['PATH'] = '/home/ababjac/R/x86_64-pc-linux-gnu-library/4.1' + os.pathsep + os.environ.get('PATH', '')
#for row in rpy2.situation.iter_info():print(row)

pandas2ri.activate()

poppr = importr('poppr')

data = pd.read_csv('data/Co-evolution_Data_Nov2021/Datasets_Codes_distantace_matrices/genalex_wtb_male_female.csv')
#print(data)

#deleted the rest until can get r environment path configured with Python to call poppr.nei.dist()
