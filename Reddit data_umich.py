# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# load libraries
import pandas as pd
import datetime as dt
from psaw import PushshiftAPI
import os

# working directory
os.chdir('C:/Users/赵晨笛/Desktop')


# set API
api = PushshiftAPI()

# Set beging and end date of period interested in
start_epoch_2020=int(dt.datetime(2020, 3, 1).timestamp())
end_epoch_2020=int(dt.datetime(2020, 10, 31).timestamp())


# Create empty lists
subm_list_umich = []


# Fill lists with data from API
# Here: search submissions made to subreddit democrats which contain kavanaugh
subm_list_umich = list(api.search_submissions(
                            before=end_epoch_2020,
                            after=start_epoch_2020,               
                            subreddit='uofm'))



# Save as .csv
pd.DataFrame([s.d_ for s in subm_list_umich]).to_csv('subm_list_umich.csv', index=False)



    
