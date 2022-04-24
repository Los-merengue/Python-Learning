### Practicing using Functions and method in a string data types
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print("The length of the string of the variable verse is {}".format(len(verse)))
print("The index of the first 'and' can be found in the {}th position".format(verse.find("and")))
print("The index of the last 'and' can be found in the {}th position".format(verse.rfind("you")))

### Practicing Ordering and Indexing of Data Types
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month-1]
print(num_days) 


### Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
#Modify this line so it prints the last three elements of the list
eclipse_dates = eclipse_dates[-3:]
print(eclipse_dates)

### A Basic Split Method

new_str = "The cow jumped over the moon."
new_str.split(" ",3)