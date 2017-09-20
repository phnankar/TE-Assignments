import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly as pl

df = pd.read_csv("assign_3_data.csv")
sgpa_df = df.iloc[:,-4]
sgpa_list = list(sgpa_df)
sgpa_f = []
for i in sgpa_list:
    sgpa_f.append(i.strip(','))
sgpa_f = [i.replace('--','00') for i in sgpa_f]

sgpa = np.array(sgpa_f,dtype = np.float)
dist = np.where(np.logical_and(sgpa <= 10.00 , sgpa >= 7.75))
first = np.where(np.logical_and(sgpa <=7,75 , sgpa >=7))
second =np.where(np.logical_and(sgpa <=7.00 , sgpa >=6.00))
fail = np.where(sgpa == 00)

lenz = len(sgpa[:])
d_len = len(sgpa[dist])
f_len = len(sgpa[first])
s_len = len(sgpa[second])
fa_len =len(sgpa[fail])

labels = ['Distinction','First','Second','Fail']
sizes  = [d_len,f_len,s_len,fa_len]
colors = ['gold', 'yellowgreen', 'lightskyblue','red']

explode = (0.03,0.03,0.03,0.03)
plt.pie(sizes,explode = explode,labels = labels, colors = colors,startangle = 90,shadow = True,autopct = '%1.1f%%')
plt.show()