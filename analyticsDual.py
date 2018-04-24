import pandas as pd
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import seaborn as sns
import matplotlib.pyplot as plt

data_file = '/home/khan/Desktop/walkins.xlsx'
dfs = pd.read_excel(data_file)
dfs.fillna('unknown')
status=dfs['Status']
tech=dfs['Technology']
# for i in dfs['Technology']:
#     print str(i)
#     print type(str(i))
allTech = []
for i in range(0,len(tech)):
     allTech.append(str(tech[i]))
allTech

dataHub = "Python data science PY+DS DS hadoop big data analytics django machine learning deep BD "
fullstack = "frontend backend mongodb html css js javascript angular node typescript full stack"
cloudops = "Devops AWS AZURE cloud "

for items in allTech:
    score = fuzz.partial_ratio(items, dataHub)
#     print(score)
    if(score>55):
        print("%s ---> %d" %(items , score))

ds_count = 0
fs_count = 0 
dv_count = 0
others = 0 
catlist = [] 

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
# cat_return("Python")

print((ds_count , fs_count , dv_count , others))

catlist= []
for i in range(0,len(dfs['Technology'])):
    cat_return(str(dfs['Technology'][i]))
    catlist.append(cat_return(str(dfs['Technology'][i])))

dfs.insert(5, "category", catlist)

sns.set(style="whitegrid", color_codes=True)
sns.countplot(x="category", data=dfs, palette="Greens_d");

visited = 0
joined = 0
call_back = 0
others_status = 0 
positive = "visited "
registered = "joined registered "
callBack = " will come later  call back tomorrow "
negative = "not interested  somewhere else"
def status_return(items):
    global visited
    global joined
    global call_back
    global others_status
    if(fuzz.partial_ratio(items.lower(), positive.lower())>50):
#         print("%s --> DataHub " %(items))
        visited = visited + 1
        cat = "visited"
    elif(fuzz.partial_ratio(items.lower(), callBack.lower())>50):
#         print("%s --> Full stack" %(items))
        call_back = call_back + 1
        cat = "call_back"
    elif(fuzz.partial_ratio(items.lower(), registered.lower())>50):
#         print("%s --> cloud " %(items))
        joined = joined + 1
        cat = "joined"
    else:
#         print(items+ "--> others")
        others_status = others_status + 1
        cat = "others"
    return cat

statlist= []
for i in range(0,len(dfs['Status'])):
    status_return(str(dfs['Status'][i]))
    statlist.append(status_return(str(dfs['Status'][i])))
# status_return("Python")
dfs.insert(8, "Status_cat", statlist)
dfs.head()
sns.countplot(x="Status_cat", data=dfs, palette="Greens_d");

dfs.head()

plt.show()