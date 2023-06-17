#!/usr/bin/env python
# coding: utf-8

# In[1]:


def extract_fields(data):
    records = []
    for item in data:
        record = {
            'country': item['address']['country'],
            'name': item['first_name'],
            'surname': item['last_name'],
            'gender': item['gender']
        }
        records.append(record)
    return records


# In[ ]:




