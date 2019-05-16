#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
os.chdir('C:\\Analytics\\MachineLearning\\Recomendation system')


# In[2]:


movie = pd.read_csv('movie.csv')
movie.columns


# In[3]:


movie.head()


# In[4]:


## We need movie id and title
movie = movie.loc[:,['movieId','title']]
movie.head(5)


# In[5]:


rating = pd.read_csv('rating.csv')
rating.head(5)


# In[6]:


## we need userid,movieid and rating
rating = rating.loc[:,['userId','movieId','rating']]
rating.head(5)


# In[7]:


# now merge movie and rating
data = pd.merge(movie,rating)
data.head(5)


# Will use item based recommendation system

# In[8]:


data.shape


# In[10]:


# using 1 million sample data
data = data.iloc[:1000000,:]


# In[12]:


#using pivot table to make rows are users and columns are movies. Values are ratings
pivot_table = data.pivot_table(index=['userId'],columns=['title'],values='rating')
pivot_table.head(10)


# In[ ]:





# In[14]:


# we have movie Bad Boys(1995) which is watched by people. Question is which
# movie do we recommend who watched the above movie. To answer this we need
# to find the simililarities between Bad Boys and other movies

movie_watched = pivot_table["Bad Boys (1995)"]
similarity_with_other_movies = pivot_table.corrwith(movie_watched)
similarity_with_other_movies = similarity_with_other_movies.sort_values(ascending=False)
similarity_with_other_movies.head()


# It is concluded that we need to remommend Headless Body in Topless Bar (1995)
# who watchd Bad Boys(1995)

# In[ ]:




