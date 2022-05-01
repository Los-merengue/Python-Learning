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

book_title =  ['Great', 'expectations','the', 'adventures', 'of', \
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
