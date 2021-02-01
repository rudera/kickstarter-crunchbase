import numpy as np
import pandas as pd
from glob import glob
import json

kickstarter_files = sorted(glob('eship_data_share/kickstarter/csv/*.csv'))
ks_df = pd.concat((pd.read_csv(file) for file in kickstarter_files), ignore_index = True)
print(ks_df)
for index, row in ks_df.iterrows():
    if ks_df.at[index, 'twitter'] != '[]':
        ks_df.at[index, 'twitter'] = eval(ks_df.at[index,'twitter'])[0].split('//')[1]