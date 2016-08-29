# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:00:37 2016

@author: Minhyun Yoo
"""

# fred example
# Treasury Constant Maturity rates

from fred import Fred
import pandas as pd
import matplotlib.pyplot as plt

# register api_key
fr = Fred(api_key='.......', 
          response_type='dict');       

# option
param = {
          "observation_start":"2005-01-01",
          "observation_end":"2016-08-29",
        };

# interest rates data set
data_set = ['DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', \
            'DGS3', 'DGS5', 'DGS7', 'DGS10', 'DGS20', 'DGS30'];

i = 0; # index
all_res = pd.DataFrame(); # init
for series_id in data_set:
    print 'iter : %s (%d/%d)' % (series_id, i+1, len(data_set));
    
    res = fr.series.observations(series_id, "dict", params=param);
    
    df_res = pd.DataFrame(res);
    
    if (i == 0):
        all_res['date'] = df_res['date'];
        
    all_res[series_id] = df_res['value'] / 100.0; # % -> rates
    
    i+=1;
        

# plot
plt.figure(1);
all_res.plot(all_res['date'])
plt.grid('on')

# note that the surface figure is too slow to show