#The script searches in a specific location for files and it gets in POSIX the time of modification of all files. It also creates a temp file (and write text in it) within the same directory (which gets deleted once the script exits). This temp file is used to get today’s modification date. Then all POSIX dates are converted into human readable format and a comparison is done between the temp file and the files we are examining. If the files we are examining are three months or older, then …. you can enter what ever custom action you want
#!/usr/bin/python
#The script searches in a specific location for files and it gets in POSIX the time of modification of all files.
#It also creates a temp file (and write text in it)  within the same directory (which gets deleted once the script exits)
#This temp file is used to get today's modification date. Then all POSIX dates are converted into human readable format
#and a comparison is done between the temp file and the files we are examining. If the files we are examining are
#three months or older, then .... you can enter what ever custom action you want.
 
import os.path
import tempfile
import datetime
import dateutil.relativedelta
import dateutil
 
#Path of where we are looking for the files
drc = '/root/Music'
 
#We create a temp file so we can get today's date. File is deleted after script is done executing
tempF = tempfile.NamedTemporaryFile(dir=drc)#, delete=False)
tempF.write('something')#We put in some text in so we are sure to get a time modified.
fileT =  os.stat(tempF.name)[8] #We are getting the mtime aka time of modification
fileT_human = datetime.datetime.fromtimestamp(fileT)#We are converting it to human readeable
 
for dirpath, dirname, filename in os.walk(drc):  #we are going huntinf for...
        for fname in filename:                   #...files
                path = os.path.join(dirpath, fname) #full path of files
                mtime = os.stat(path)[8] #We are getting time of modification of all the files
                mtime_human  = datetime.datetime.fromtimestamp(mtime) #We humanize the date
 
                #We are comparing each file with the fileT_human in order to get the difference in date when it comes to modification time
                diff = dateutil.relativedelta.relativedelta (fileT_human, mtime_human)
 
                #Just a sample output. You can use years, months, days to do the comparison between files.
                #print "%d years, %d months, %d days, %d hours, %d minutes and %d seconds" % (diff.years, diff.months, diff.days, diff.hours, diff.minutes, diff.seconds)
                months = diff.months
                if  months > 3:
                        print "Deleting file ", path
                        #Put whatever action you want here.
                        os.remove(path) #it will delete files only
                else:
                        exit;
