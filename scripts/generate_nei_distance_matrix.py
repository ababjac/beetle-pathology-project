import pandas as pd
import numpy as np
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

pandas2ri.activate()

poppr = importr('poppr')

data = pd.read_csv('data/Co-evolution_Data_Nov2021/Datasets_Codes_distantace_matrices/genalex_wtb_male_female.csv')
