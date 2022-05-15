### Conditional Flow Control

points = 174  # use this input to make your submission
prize =  ("wooden rabbit", "no prize", "wafer-thin mint", "penguin")
# write your if statement here
if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"
    
print(result)

### Practise question 2

# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 234 #provide answer
guess = 23 #provide guess

if guess < answer: #provide conditional
    result = "Oops!  Your guess was too low."
elif guess > answer: #provide conditional
    result = "Oops!  Your guess was too high."
elif guess == answer: #provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)

### For Loop Practise 
# Printing each words in a list
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)

# Multiple of 5

for i in range(5, 35, 5):
    print(i)


### For Loop Quiz using it to rewrite the structure of a dictionary

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

### Modify the Usernames with Ranges

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for name in range(len(usernames)):
    usernames[name] = usernames[name].lower().replace(" ", "_")

print(usernames)

### Tag Counter Scripts

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if ("<" in token) & (">" in token):
        count+=1
print("The Number of the Elements of the list are {} and the number of XML tag is {}".format(len(tokens),count))
print(count)

### Create an HTML List

items = ['first string', 'second string', 'third tag', 'fourth tag']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    dem = "<li>{}</li>\n".format(item)
    html_str += dem
html_str += "</ul>"
print(html_str)

### Printing the Color List in lower case

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    #finish this part
    lower_colors.append(color.lower())
print(lower_colors)

print("The lowercase of the string is gien as {}".format(lower_colors))

### Building Dictionaries

book_title =  ['great', 'expectations','the', 'adventures', 'of', \
    'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)


### Adding a Word Counter using the 'get' method
book_title =  ['great', 'expectations','the', 'adventures', 'of', \
     'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

words_counter = {}
for word in book_title:
    words_counter[word] = words_counter.get(word, 0) + 1

print(words_counter)

#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, values in basket_items.items():
    if key in fruits:
        result += int(values)

print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, values in basket_items.items():
    if key in fruits:
        result += int(values)

print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, values in basket_items.items():
    if key in fruits:
        result += int(values)

print(result)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for keys, values in basket_items.items():
#if the key is in the list of fruits, add to fruit_count.
    if keys in fruits:
        fruit_count += values
#if the key is not in the list, then add to the not_fruit_count
    if keys not in fruits:
        not_fruit_count += values

print("The number of fruits is {}.  There are {} objects \
     that are not fruits.".format(fruit_count, not_fruit_count))


# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= 6:
    
    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)

### Factorial Question Using For Loop

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for num in range(2, number + 1):
    product *= num


# print the factorial of number
print(product)

## Count By Quiz

start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

### Count By Check Quiz

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

### Nearest Square Quiz 

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)


### Odd Number Count using While Loop
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, \
    17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, \
        59, 84, 69, 113, 166]

count_odd = 4
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))

