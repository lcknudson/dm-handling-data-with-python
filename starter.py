# PROBLEM 1
# Create a variable that holds the value of your first name.

name_first = "Lorin"



# PROBLEM 2
# Create a variable that holds the value of your favorite number.

num = 34

print(num)


# PROBLEM 3
# Create a variable that holds a boolean value representing if your hair is brown.

hair = "Brown"
hair2 = "Blue"

def is_hair_brown(color):
    if color == "Brown":
        print("True, hair is Brown")
    else:
        print("False, hair is not Brown")
    

is_hair_brown(hair)
is_hair_brown(hair2)



# PROBLEM 4
# Print your first name, by printing the variable created in problem 1.

print(name_first)


# PROBLEM 5
#  Create a variable called `loves_code` and set it equal to true. 
loves_code = True

#  Check to see if `loves_code` is equal to true or false. 
print(loves_code)

#  If it is true, print "I love to code!"

if loves_code == True:
    print("I love to code!")
else:
    print("Coding has it's challenges.")


#  If it is not, print "Coding has it's challenges."
loves_code = False

if loves_code != True:
    print("Coding has it's challenges.")
else:
    print("I love to code!")

# PROBLEM 6
# Create an array called `colors` and set it equal to a list of at least five colors.

colors = ["Blue", "Pink", "Purple", "Green", "Blue", "Yellow"]


# Problem 7
# Using bracket syntax, print out the last item in your colors array.

print(colors[-1])


# For problems 8-9, use the following line of code:
numbers = [1,2,3,4,5,6,7,8,9,10]

# Problem 8
# Use a for-in loop to iterate over the `numbers` array and print each number.

for num in numbers:
    print(num)



# Problem 9
# Create an empty array called `even_numbers`.
# Use a for-in loop to iterate over the `numbers` array, and if a number is even, add  it to the `even_numbers` array.

even_numbers = []

for num in numbers:
    if (num % 2) == 0:
        even_numbers.append(num)
        # print(even_numbers) #Extra line to check if it's working



# Problem 10
# Do not edit the code below.
score = 74
# Do not edit the code above.

# Determine if the letter grade of the given variable 'score'. If the variable is a 90 or above, console-log an 'A', between 80 and 89, console-log a 'B', between 70 and 79, 'C', between 60 and 69, 'D', and anything below 60 should console-log an 'F'.

if score >= 90:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
elif score < 60:
    print('F')
else:
    print("Invalid, Mr. Spock.")




# Problem 11
# Create a variable called 'changeMyMind' and set it equal to true. 
# Check to see if changeMyMind is set to true or false, if it is true, change the status to false, if it is false, change the status to true.

changeMyMind = True

if changeMyMind == True:
    # print("First Value:", changeMyMind)
    changeMyMind = False
    # print("Second Value:", changeMyMind)
elif changeMyMind == False: 
    # print("Third Value:", changeMyMind)
    changeMyMind = True
    # print("Fourth Value:", changeMyMind)
else:
    print("Wrong input again, Captain Kirk.")




# ADVANCED

# For problems 12-15, use the following line of code:
friends = ['Joe', 'Sally', 'Camilo', 'Perry', 'Susan']

# Problem 12
# Research to find the Python method that allows you to add an element to the end of the array (similar to push() in JavaScript), then add a name to the end of the `friends` array.

def add_friend(name):
    friends.append(name)
    # print(friends)

# add_friend('Emma') #This works


# Problem 13
# Print out the total amount of elements in the `friends` array. The Python method you are looking for is similar to the JavaScript property `.length`.

list_size = len(friends)
# friends_index = friends.index(e) # perhaps flesh this out later...
print("Length of friends list:", list_size)


# Problem 14
# Add a name into the third position in the array (index 2). Make sure you are not overwriting the value that is already there.

def insert_friend(name):
    friends.insert(2, name)

# insert_friend("Laila")


# Problem 15
# Remove the last item in the array (try to think about how you can do this dynamically, meaning, if the array contents were to change, your code would still work).

print("original friends list:", friends)

ele = friends.pop() #This is the code that removes the last item in the list (array)

print("New friends list", friends)

# Extra code
for name in friends:
    print(name)