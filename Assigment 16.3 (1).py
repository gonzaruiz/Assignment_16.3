
# coding: utf-8

# In[2]:


import numpy as np



# In[3]:


x = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3)


# In[4]:


np.mean(x)


# In[7]:


np.var(x)


# In[8]:


np.std(x)


# In[15]:


get_ipython().run_line_magic('pylab', 'inline')


# In[19]:



failed = array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3])
plot(failed)
plot(failed,'*')


# In[20]:


import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


plt.hist(failed) #histogram
plt.show()


# In[22]:


plt.figure(figsize=(18,5))
for i in range(2):
    plt.plot(failed)


# In[23]:


# histogram of different columns on one graph from a single dataset
kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=100)
plt.figure(figsize=(18,6))
plt.hist(failed, **kwargs)

