# This program says hello and asks for myname.

print ('Hello world!')
print ('What is your name ?') # Ask for their name.

myName = input()

print ('It is good to meet you ,' + myName)
print ('The length of your name is :')

print (len(myName))

print ('What is your age ?') # Ask for their age

myAge = input()

print ('You will be ' + str(int(myAge) + 1) + 'in a year')