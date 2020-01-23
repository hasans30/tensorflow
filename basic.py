import pandas as pd 

df = pd.DataFrame({'name':['A','B','C','A','B','C','A','B','C'],'Year':[2003,2002,2001,2003,2002,2001,2003,2002,2001]})
for each in df.groupby(["Year"]): 
    print(each)