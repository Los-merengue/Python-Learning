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

'''
Using a Break Statement when you are running a code for Cargo ships
the loading of the goods in the ship
'''
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

'''
Write a loop with a break statement to create a string, news_ticker, 
that is exactly 140 characters long.
'''

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

'''
In the following coding environment, write code to check if the 
numbers provided in the list check_prime are prime numbers.
'''

check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 
# 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a \
                factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible 
# factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))

'''
Using Zip and Enumerate to run your code
'''
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

'''
Zip List to Dictionary
'''
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

'''
Unzip Turples
'''
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)

'''
Transpose with Zip
'''
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

'''
Extract the First name in the list of names
'''
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names] # write your list comprehension here
print(first_names)

'''
Multiple of Three using List Comprehension
'''
# write your list comprehension here
multiples_3 =[ 3*x for x in range(1,200) if x <= 20] 

print(multiples_3)

'''
Using List Comprehension to filter name by scores
'''
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score > 65] # write your list comprehension here
print(passed)

'''
The following questions are based on data on Oscar Award 
Nominations for Best Director between the years 1931 to 
2010. To start you off, we've provided a dictionary called 
"nominated" with the year (as key) and list of directors who 
were nominated in that year (as value). We've provided you 
with a different dictionary called "winners" with the year 
(as key) and list of directors who won the award in that year 
(as value).
'''

'''
Question 1.
A. Create a dictionary that includes the count of Oscar nominations
 for each director in the nominations list.

B. Provide a dictionary with the count of Oscar wins for each 
director in the winners list.
'''
nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 
'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 
1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 
1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: 
['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: 
['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 
1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 
'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey',  
'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 
'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 
'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: 
['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 
'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler',
'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 
'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 
 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz',  
 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 
 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: 
['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock',
'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

# The Code for Question 1A
nom_count_dict = {}
for year, list_dir in nominated.items():
    for director in list_dir:
        if director not in nom_count_dict:
            nom_count_dict[director] = 1
        else:
            nom_count_dict[director] += 1

# The Code for Question 1B
win_count_dict = {}
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
    
'''
Question 2
Provide a list with the name(s) of the director(s) with the most 
Oscar wins.
'''
#FIRST PART OF SOLUTION
win_count_dict = {}
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1

#SECOND PART OF SOLUTION
highest_count = 0
most_win_director = []

for key, value in win_count_dict.items():
    if value > highest_count:
        highest_count = value
        most_win_director.clear()
        most_win_director.append(key)
    elif value == highest_count:
        most_win_director.append(key)
    else:
        continue