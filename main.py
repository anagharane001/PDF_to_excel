from tkinter import *
#import PyPDF2
import tabula
#import pandas as pd
from tkinter import filedialog as fd
import json

import string
window = Tk()
Label(window, text="").grid(row=0, column=1)
Label(window, text="").grid(row=6, column=1)
Label(window, text="").grid(row=8, column=0)

# return name
def pdf2excel():
    name = fd.askopenfilenames(parent = window,title='choose the file')
    newvar = str(name)
    Label(window, text="Your all file is converted from pdf to Excel ! ").grid(row=7, column=0)
    # Label(window,text = "new file name is " + str(newvar)).grid(row=6,column=1)
    for i in range(len(name)):
     dfs = tabula.read_pdf(name[i], pages='5',encoding=('ISO-8859-1'))
    print(dfs)
    for j in range(len(name)):
        #{dfs[i].to_csv(f"table{i}.csv")}
        {dfs[j].to_csv(f"table{j}.csv")}
        #fd.convert_into('dfs',)
        #tabula.convert_into('dfs[j]',"new.csv",output_format="csv",pages='5')
    # Label(window,text="file is converted into the excel").grid(row=6,column=1)


# x = tabula.convert_into('C:/Users/chand/OneDrive/Documents/Internship/file.pdf',"newfill1910.csv",output_format="csv",pages='5',lattice = False,silent = True)
#b1 = Button(window,text="Browse The file ",command = browse_file,bg = "green",fg="white")
#b1.grid(row=2,column=1)
b2 = Button(window, text="convert to Excel", command=pdf2excel, bg="blue", fg="white")
b2.grid(row=4, column=0,columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
mainloop()