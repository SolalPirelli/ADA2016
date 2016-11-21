# coding: utf-8
import pandas as pd
import numpy as np
import seaborn as sns
data = pd.read_csv('CrowdstormingDataJuly1st.csv')
data
del data['playerShort']
del data['player']
del data['birthday']
data
del data['height']
del data['weight']
data
del data['refNum']
del data['refCountry']
data
get_ipython().magic('save del_features.py 1-16')
