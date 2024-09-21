#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kendalltau

# Load the datasets
url_health = 'https://raw.githubusercontent.com/mokar2001/Statistics-Cheat-Sheet/main/9.%20CoVariance%20&%20Correlation/Notebook/Health.txt'
url_happy = 'https://raw.githubusercontent.com/mokar2001/Statistics-Cheat-Sheet/main/9.%20CoVariance%20&%20Correlation/Notebook/Happy.txt'

data_health = pd.read_csv(url_health, header=None, names=['Health'])
data_happy = pd.read_csv(url_happy, header=None, names=['Happy'])

# Calculate covariance
covariance = np.cov(data_health['Health'], data_happy['Happy'])[0, 1]

# Calculate correlations
pearson_corr, _ = pearsonr(data_health['Health'], data_happy['Happy'])
spearman_corr, _ = spearmanr(data_health['Health'], data_happy['Happy'])
kendall_corr, _ = kendalltau(data_health['Health'], data_happy['Happy'])

# Show the results
covariance, pearson_corr, spearman_corr, kendall_corr


# In[ ]:




