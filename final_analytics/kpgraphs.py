import pandas as pd
# import fuzzywuzzy as fuzz 
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import seaborn as sns
import matplotlib as plt 

data_file = '/home/khan/kp_analytics.xlsx'
dfs = pd.read_excel(data_file)

new_df = dfs.dropna(axis=0, how='all')

len(new_df)
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

print("Python students : " , Python)
print("DataScience students : ",DataScience)
print("Other students :" ,Others)

fig, ((ax1, ax2), (ax3, ax4)) =plt.pyplot.subplots(nrows=2, ncols=2)
plt.pyplot.title('Monthly analysis at KP')
ss = sns.countplot(new_df['Month'], ax=ax1)
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
plt.pyplot.tight_layout()
ss.set_title('Monthly analysis at KP')

# plt.pyplot.show()
plt.pyplot.title('DataHub students Status at KP')
ss = sns.countplot(new_df['Student Status'], ax=ax2)
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right") 
plt.pyplot.tight_layout()
ss.set_title('DataHub students Status at KP')

plt.pyplot.title('Courses of students at KP')
ss = sns.countplot(new_df['Course Opted'], ax=ax3)
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
plt.pyplot.tight_layout()
ss.set_title('Courses of students at KP')

new_df.insert(7, "category", techlist)
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('kpdataPython.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
new_df.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
# plt.pyplot.title('DataHub students at KP')

ss = sns.countplot(new_df['category'], ax=ax4)
ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
plt.pyplot.tight_layout()
ss.set_title('DataHub students at KP')

manager = plt.pyplot.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
plt.pyplot.show()