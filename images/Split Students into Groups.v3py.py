import random
print "Welcome to Student Pair Generator"
print "\n"
print "Enter the names of 6 students." 
"""If user would like to enter more names, 
change the number in line 4 and in line 8.  
Number needs to be even. """

print "Press return after each name to generate your list of students."
print "You will then see a list of pairs."
mylist=[] #store names in list
for i in xrange(6): #executes your loop contents 6 times
    names = raw_input() #allows user to enter names
    mylist.append(names) # adds each name to the list until loop is completed 6 times

print mylist# at this point list contains the 6 things entered by user

random.shuffle(mylist) #this randomly shuffles the students in the list so that pairs can be randomly generated
print "\n"
print "Here are the groups:"
while len(mylist)>0:
    """repeats the step of pairing until all names are paired off.  
    This only works for even number of names.  
    It will run an error if the number of students is odd. """
    
    print mylist.pop(),"and", mylist.pop()#adding .pop to the list takes the name off the list.  
    


