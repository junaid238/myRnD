
import pandas as pd
# import fuzzywuzzy as fuzz 
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import seaborn as sns
import matplotlib as plt 


# In[11]:


data_file = '/home/khan/srn_data.xlsx'
dfs = pd.read_excel(data_file)


# In[12]:


dfs.head()
len(dfs)


# In[13]:


new_df = dfs.dropna(axis=0, how='all')


# In[16]:


len(new_df)


# In[17]:


new_df.head()


# In[21]:

plt.pyplot.title('Monthly analysis at SRN')

ss = sns.countplot(new_df['Month'])
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
plt.pyplot.tight_layout()
plt.pyplot.show()



# In[25]:

plt.pyplot.title('DataHub students status at SRN')

ss = sns.countplot(new_df['Student Status'])
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right") 
plt.pyplot.tight_layout()
plt.pyplot.show()


# In[26]:

plt.pyplot.title('Courses of students at SRN')

ss = sns.countplot(new_df['Course Opted'])
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
plt.pyplot.tight_layout()
plt.pyplot.show()


# In[66]:


# new_df['Course Opted']
python = "Python  PY"
datascience = "DS PY+DS data science"
Python = 0
DataScience = 0 
Others = 0
techlist= []
for techs in new_df['Course Opted']:
    if(fuzz.partial_ratio(str(techs), python)>=50):
#         print(techs+"-->",fuzz.partial_ratio(str(techs), python))
        Python +=1
        techlist.append(str("Python"))
    elif(fuzz.partial_ratio(str(techs), datascience) >= 50):
#         print(techs+"-->",fuzz.partial_ratio(str(techs), datascience))
        DataScience += 1
        techlist.append(str("DataScience"))

    else:
        Others += 1
        techlist.append(str("others"))
#         print(str(techs))
# print(Python)
# print(DataScience)
# print(Others)
# print(techlist)
# new_df.groupby('Course Opted').count()


# In[67]:


new_df.head()


# In[69]:


new_df.insert(7, "category", techlist)


# In[70]:


new_df.head()

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('srndataPython.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
new_df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
# In[71]:


plt.pyplot.title('DataHub students at SRN')

ss = sns.countplot(new_df['category'])
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
plt.pyplot.tight_layout()
plt.pyplot.show()

print("Python students : " , Python)
print("DataScience students : ",DataScience)
print("Other students :" ,Others)