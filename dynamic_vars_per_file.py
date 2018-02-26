#!/usr/bin/python
files_list = []  #Putting all files in a list
for files in glob.glob("*"):
     files_list.append(files)
 
vars_dict = {} #creating variables for each file dynamically with a dictionary
for elem_files in range(len(files_list)):
    vars_dict[elem_files] = files_list[elem_files]
