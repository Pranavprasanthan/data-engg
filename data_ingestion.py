#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

def fetch_data():
    url = 'https://random-data-api.com/api/v2/users?size=100'
    response = requests.get(url)
    data = response.json()
    return data


# In[ ]:




