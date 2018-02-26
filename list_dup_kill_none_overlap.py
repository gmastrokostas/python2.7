#!/usr/bin/python
#Merge two lists, eliminate duplicates, detect items that do not overlap between lists


f_master_list    = open('master-list','r')
f_second_list  = open('my_list','r')

master_list  = []
second_list = []

for line in f_master_list:
    master_list.append(line.strip())

for line in f_second_list:
    second_list.append(line.strip())

#print master_list
#print second_list_list
print ""
print "-----------------------------------------------"
print "Below items are unique to each list."
print "-----------------------------------------------"
print  set(master_list).symmetric_difference(second_list)
print ""
print ""
print "---------------------------------------------------------------"
print "Merging both lists and removing duplicates"
print "---------------------------------------------------------------"
results = list(set(master_list+second_list))

results.sort()
master_list.sort()
second_list.sort()


print "master_list has   ",   len(master_list), "elements"
print "second_list has ",     len(second_list), "elements"
print "The updated list has", len(results), "elements"
print results

for items in results:
    print items
