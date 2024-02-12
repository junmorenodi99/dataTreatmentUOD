import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import numpy as np
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os


# read table from excel file Excel

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
excel_file = filename
#excel_file = 'output.xlsx'  #Namefile by default
df = pd.read_excel(excel_file)

# Define the 'Secs' col as index
df.set_index('Secs', inplace=True)

# Plot al, the columns regarding (secs)
# fig = plt.figure(figsize=(12, 6))

fig, ax = plt.subplots(figsize=(14, 8))


axplot_list = list()
for columna in df.columns:
   axplot, =  ax.plot(df.index, df[columna], label=columna)
   axplot_list.append(axplot)
   



# Develope fo Pick legend signal 
# all the legends are casted to objects and are saved into a list

legend = plt.legend()

legend_list = legend.get_lines()


# Set pick aviability for each legend object. 
for i in range(len(legend_list)):
    temp_element = legend_list[i]
    temp_element.set_picker(True)
    temp_element.set_pickradius(10)



# Dictionary creation 
graphs = {}
#print(type(graphs))

#assign the legend objet to dictonary graph{}

counter = 0 

for columna in df.columns:
    tt = axplot_list[counter]
    tempvar = legend_list[counter]
    #print(tempvar)
    #print(tt)
    #graphs[tempvar] =  plt.plot(df.index, df[columna])  
    graphs[tempvar] =  tt
    #print(graphs[tempvar])    
    counter = counter + 1
  


def on_pick(event):
    legend = event.artist
    #print(legend) # Test
    
    isVisible = legend.get_visible()    
    #print(isVisible)
    
    graphs[legend].set_visible(not isVisible)
    #print(graphs[legend])
    
    legend.set_visible(not isVisible)

    fig.canvas.draw()
    


plt.connect('pick_event', on_pick)
plt.xlabel('Time (secs)')
plt.ylabel('Value')
plt.title('Values Plot in Time')
plt.grid(True)
plt.show()
