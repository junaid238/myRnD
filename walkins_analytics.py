
# coding: utf-8

# In[39]:


import pandas as pd
# import fuzzywuzzy as fuzz 
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import seaborn as sns
import matplotlib as plt 


# In[40]:


data_file = '/home/khan/Desktop/walkins.xlsx'
dfs = pd.read_excel(data_file)


# In[42]:


dfs.head()
dfs.fillna('unknown')


# In[43]:


status=dfs['Status']


# In[44]:


tech=dfs['Technology']


# In[45]:


for i in dfs['Technology']:
    print str(i)
    print type(str(i))


# In[46]:


allTech = []
for i in range(0,len(tech)):
     allTech.append(str(tech[i]))
allTech


# In[47]:


dataHub = "Python data science PY+DS DS hadoop big data analytics django machine learning deep BD "
fullstack = "frontend backend mongodb html css js javascript angular node typescript full stack"
cloudops = "Devops AWS AZURE cloud "


# In[48]:


for items in allTech:
    score = fuzz.partial_ratio(items, dataHub)
#     print(score)
    if(score>55):
        print("%s ---> %d" %(items , score))



# In[49]:


ds_count = 0
fs_count = 0 
dv_count = 0
others = 0 

for items in allTech:
    if(fuzz.partial_ratio(items.lower(), dataHub.lower())>50):
#         print("%s --> DataHub " %(items))
        ds_count = ds_count + 1
    elif(fuzz.partial_ratio(items.lower(), fullstack.lower())>50):
#         print("%s --> Full stack" %(items))
        fs_count = fs_count + 1
    elif(fuzz.partial_ratio(items.lower(), cloudops.lower())>50):
#         print("%s --> cloud " %(items))
        dv_count = dv_count + 1
    else:
        print(items+ "--> others")
        others = others + 1


# In[50]:


def cat_return(items):
    global ds_count
    global fs_count
    global dv_count
    global others
    if(fuzz.partial_ratio(items.lower(), dataHub.lower())>50):
#         print("%s --> DataHub " %(items))
        ds_count = ds_count + 1
        cat = "data_item"
    elif(fuzz.partial_ratio(items.lower(), fullstack.lower())>50):
#         print("%s --> Full stack" %(items))
        fs_count = fs_count + 1
        cat = "fs_item"
    elif(fuzz.partial_ratio(items.lower(), cloudops.lower())>50):
#         print("%s --> cloud " %(items))
        dv_count = dv_count + 1
        cat = "cloud_item"
    else:
#         print(items+ "--> others")
        others = others + 1
        cat = "others"
    return cat
cat_return("Python")


# In[51]:


print((ds_count , fs_count , dv_count , others))


# In[52]:


# for i in dfs['Technology']:
#     dfs['Technology']
#     dfs['Technology'].replace(['i'],cat_return(str(i)) )
# dfs.head()
for i in range(0,len(dfs['Technology'])):
    dfs['Technology'][i] = cat_return(str(dfs['Technology'][i]))
#     dfs['Technology'].replace(['i'],cat_return(str(i)) )
dfs.head()


# In[37]:


len(dfs['Technology'])


# In[35]:


dfs.head()


# In[18]:


dfs['Notes'].replace(['offered project n placement. will come next week'], 'A')


# In[19]:


dfs.head()


# In[55]:


sns.set(style="whitegrid", color_codes=True)
sns.countplot(x="Technology", data=dfs, palette="Greens_d");

