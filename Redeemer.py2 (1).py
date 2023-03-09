#!/usr/bin/env python
# coding: utf-8

# # Assignment on Numpy

# # Use the zeros and ones functions of numpy to form the table.

# In[7]:


import numpy as np


# In[8]:


table = np.ones((5,5),dtype=int)


# In[9]:


table[1:-1,1:-1]=np.zeros((3,3),dtype=int)


# In[10]:


table[2,2]=9


# In[11]:


print(table)


# In[ ]:




