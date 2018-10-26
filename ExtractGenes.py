# Extracting genes from mousebrain.org

"""
Install loompy in anaconda command prompt, run:
    pip install -U loompy
"""
# Set the path
import os
os.chdir('C:/Users/tyler/Documents/Python')

# Load the library
import loompy

# connect to loompy data 
ds = loompy.connect("l5_all.agg.loom")

# Open list (format = Mus Ensemble GeneIDs)
list =open('tylerslist.txt','r')
lines = list.read().splitlines()
list.close()

exp_dat = [ds.ca.ClusterName]
errors = []

count=0
accsn = []
for i in lines:
    try:
        exp_dat.append(ds[ds.ra["Accession"] == i,:][0])
        accsn.append(i)
    except:
        errors.append(i)
    count += 1
    print(count)

# Save data to .csv    
import pandas as pd

df= pd.DataFrame(exp_dat,columns=exp_dat.pop(0))
df['gene'] = accsn

cols = list(df)
cols.insert(0, cols.pop(cols.index('gene')))
df = df.loc[:, cols]

df.to_csv('wbmatrix.csv', sep=',')