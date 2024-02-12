import pandas as pd
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#Getting File Path
filename_only = os.path.basename(filename)
filename_wo_extension = os.path.splitext(os.path.basename(filename))


# Read CSV
file_csv = filename  # put file name in this line
df = pd.read_csv(file_csv, sep=';')



# Split fist column using '#'
df[['date', 'Hour']] = df['Time'].str.split('#', expand=True)
df[['Hour','Min','Secs']] = df['Time'].str.split(':', expand=True)
#df['Hour'] = pd.to_datetime(df['Hour'], format='%H:%M:%S.%f').dt.strftime('%S.%f') #%M:

column_order = ['date', 'Hour','Min','Secs'] + [col for col in df.columns if col not in ['date', 'Hour','Min','Secs']]
df = df[column_order]


# Enum the col Secs satrting in 1 ()to remove if we want to keep the real value 
df['Secs'] = df.index*0.02 #(20 ms increments


# Delte Time Colums
df = df.drop(columns=['Time'])
df = df.drop(columns=['date'])
df = df.drop(columns=['Hour'])
df = df.drop(columns=['Min']) #To remove if we want to keep Min


# Delete Status Columns
cols = df.columns[df.iloc[1].str.strip().eq('OK')]
df = df.drop(columns=cols)


# save the new DataFrame in Excel File
excel_out = filename_wo_extension[0] + '_treated' + '.xlsx'
df.to_excel(excel_out, index=False, engine='openpyxl')

print(f'Modified Table saved in {excel_out}')


