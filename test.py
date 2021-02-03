import numpy as np
import pandas as pd
from glob import glob
import json
'''
kickstarter_files = sorted(glob('eship_data_share/kickstarter/csv/*.csv'))
ks_df = pd.concat((pd.read_csv(file) for file in kickstarter_files), ignore_index = True)
print(ks_df)
for index, row in ks_df.iterrows():
    if ks_df.at[index, 'twitter'] != '[]':
        ks_df.at[index, 'twitter'] = eval(ks_df.at[index,'twitter'])[0].split('//')[1]
'''
cb_df = pd.read_csv('eship_data_share/crunchbase/selectorg_11132020.csv', low_memory=False)
print(cb_df)
for index, row in cb_df.iterrows():
    if pd.isna(cb_df.at[index, 'twitter']):
        continue
    else:
    	print(index)
    	cb_df.at[index, 'twitter'] = cb_df.at[index, 'twitter'].split('.com/')[1]
print(cb_df)