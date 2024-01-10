# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 00:06:39 2024

@author: LENOVO
"""
"""
The data set is a set of salareies from European countries. Considering its contineous nature contineous plots are used for calculating mean and rest of values

"""

import pandas as pd  # Load Pandas
import seaborn as sns  # Load seaborn
import numpy as np  # Load Numpy
import matplotlib.pyplot as plt  # Load matplotlib for plotting
import matplotlib as mpl  # Specifically added to control font size relatively

# Use r so that the interpreter reads the following string as raw string
file_path = r'C:\Users\LENOVO\Desktop\University\Fundamnetals of Data science\Data2-1.csv'

"""
The following function provides a function to read the file using file path
provides an error message if it fails
"""
def read_data(file_path: str):
    try:
        return pd.read_csv(file_path, header=None)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


data = read_data(file_path) # Provide the file path
data.columns = ['Salary(€)'] # Assign Column name with Euro since salary form European countries


mpl.rcParams["font.size"] = 12 # Set the overall font size compatable with the plot

x, y = sns.kdeplot(data).get_lines()[0].get_data() # getting x,y values for calculation

ax = sns.kdeplot(data['Salary(€)'], color='lime') # kdeplot of data
ax1 = sns.distplot(x=data['Salary(€)'], hist=True)# histogram plot 
ax.legend().set_visible(False)# Legend visibility removed since we have only one column

kdeline = ax.lines[0] # Initialise kdeline

mean = round(x.mean(), 2)# Mean calculation
SD = round(x.std(), 2)#standard deviation
q = data['Salary(€)'].quantile(0.95)#95th percentile
print(" Mean is :", mean)# Print mean
print("Standard Deviation is:", SD)#Print Standard deviation
print("Value of X where 5% salary are above X is :", q) # The value of X such that 5% of people are above it.

xs = kdeline.get_xdata()
ys = kdeline.get_ydata()
height = np.interp(mean, xs, ys)
shade = q > x # shading area greater than X. that is area above 95th percentile
trans = ax.get_xaxis_transform()
x1, y1 = x[shade], y[shade]
ax.fill_between(x, y, color='Yellow')
ax.fill_between(x1, y1)
ax.fill_between(xs, 0, ys, alpha=0.2)
ax.axvline(mean, color='black', linestyle='solid',  ymax=0.8) # Setting up the axvline mean
ax.axvline(q, color='g', ls='--', ymax=0.8)# Setting up the axvline value above 95th percentile
ax.text(mean, 0.45, f'Mean Salary is €{mean}', color='magenta', ha='right', va='center', rotation=-65,
        transform=ax.get_xaxis_transform()) # Text for axv line
ax.text(q, 0.55,  f'5% have salary above €{q}', color='r', ha='left', va='center', rotation=45,
        transform=ax.get_xaxis_transform())# Text for axv line 

"""
Setting up the labels and ticks
"""
plt.xticks(rotation=45)
plt.yticks()
plt.title("Probability density curve of Salary  in %s" % (u"\N{euro sign}")) # Title
plt.gcf().set_tight_layout(True)  # Prevent x labels being cutoff
plt.show()

"""
End of program
"""
