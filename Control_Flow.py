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
    usernames.append(name.replace(" ", "_"))

print(usernames)

### Modify the Usernames with Ranges

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for name in usernames:
    usernames = name.lower().replace(" ", "_")

print(usernames)