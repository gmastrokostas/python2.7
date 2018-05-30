#The script asks for a directory from the user. It then will dive in all the subdirectories within that directory. Itwill list all subdirectories and their size. It does this by actually looking for files within the subdirectories and calculating the actual size (not block size) of all the files with in that subdirectory.
#!/usr/bin/python
import humanize
import os, sys
from os.path import join,getsize
import humanize
import pwd
 
def dir_list():
    list = []
    drct = raw_input(":Enter directory name. Use full path: ")
    for dirpath, dirnames, filenames in os.walk(drct, followlinks=False):
        for loop_dir in dirnames:
            path = os.path.join(dirpath, loop_dir) #Joins the names of directories with the actual path
            list.append(path) # Enters all the directories with the full path to a list
 
    return list  #Return the whole list so dir_size function can process it
 
def dir_size():
     
    returned_list = dir_list() #The list returned from the dir_list function
 
    for loop in returned_list: #Breaks down the list in strings in order for OS.WALK to be able to process it
        total = 0
        for dirpath, dirnames, filenames in os.walk(loop, followlinks= False): #grab the paths from the list. This is the same as asking a user to enter a path
 
            for f_name in filenames: #Dive into directories to view files
                path = os.path.join(dirpath, f_name) #Join path with filenames for the directory we are trying to find the size
                if os.path.islink(path): 
                    continue
                else:
                    total += os.path.getsize(path)  #Find size of actual files within the directory
                    human_size = humanize.naturalsize(total, gnu=True) 
        print "Size of directory  : ",loop, "is", human_size
        human_size = 0
 
dir_size()
