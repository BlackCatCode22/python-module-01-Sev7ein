
# Chapter 1 testing

#This is grabbing input from use to determine file name
# name = input('Enter file:')
# handle = open(name, 'r')

# defining variable then a for loop to count how many words
#counts = dict()
#for line in handle:
    #words = line.split()
    #for word in words:
        #counts[word] = counts.get(word, 0) + 1

#bigcount = None
#bigword = None
#for word, count in counts.items():
    #if bigcount is None or count > bigcount:
        #bigcount = count
        #bigword = word


year = input('Enter year:')

print(year)

print('I’m gonna make him an offer he can’t refuse.')
print('“I’ll be back.”')

# Chapter 1 Exercises
# Exercise Answers 1-10
# Q1 = C
# Q2: A program is a set of instructions written in language that tells the computer what to do
# Q3: A Complier translates an entire program into machine code before it runs. An interpreter translates and runs code as you go
# Q4 = A
# Q5: The print is misspelled. it should be "print" not "primt" and it requires parenthesis
# Q6 = B
# Q7 = B
# Q8 CPU would be the brain, RAM would be short term memory as Secondary Memory would be Long-term Memory.The input device would be the senses and the output device would be speaking or moving around.


# Chapter 2 testing
x = 10
y = input('Enter Number: ')

a = x * y
print(f'A is: {a}')

type('Hello, World!')

# Chapter 2 Exercise

# Exercise 2
name = input('Enter Your Name: ')
print(f'Hello, {name}')

# Exercise 3
width = 17
height = 12.0

answer1 = width // 2
answer2 = width / 2.0
answer3 = height / 3
answer4 = 1 + 2 * 5
print(f'Width: {answer1}')
print(f'Width: {answer2}')
print(f'Height: {answer3}')
print(f'Answer: {answer4}')

# Chapter 3

# Examples
year = input('Enter Year: ')
if year <= '2007':
    print('You are over the legal age')
else:
    print('You are under legal age')


inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

# Exercise 1
#hoursWorked = input('Enter Hours: ')
#payRate = input('Enter Rate: ')

#try:
    # convert inputs
    #h = float(hoursWorked)
    #p = float(payRate)

    # fun condition check
    #if h <= 4:
        #print('You Barely worked today')
    #else:
        #print('Good Job')

    # pay calculation with overtime
    #if h > 40:
        # normal 40 hours pay + overtime pay
        #w = (40 * p) + ((h - 40) * p * 1.5)
    #else:
        # regular pay
        #w = h * p

    #print("Pay:", w)

#except (ValueError, NameError):
    #print('Please enter required numbers')

#finally:
    #print('scope ended')

# Exercise 2

# wage calculator / e
hoursWorked = input('Enter Hours Worked: ')
payRate = input('Enter Payment Rate: ')

# code that needs to be run goes in try
try:
    # wage calculator with graceful exit.
    h = float(hoursWorked)
    p = float(payRate)

    # if/else condition just for fun
    if h <= 4:
        print('You Barely worked today')
    else:
        print('Good Job')

    # calculation
    w = float((h * p))
    print(w)

    # if any errors occur from these two selected, the code runs without leaving a traceback
except (ValueError, NameError):
    print('Please enter required numbers')
    # no matter good or bad code is ran, the "finally" will run no matter what
finally:
    print('scope ended')

score = input('Enter Score (0.0 - 1.0): ')
try:
    s = float(score)
    if s > 1.0 or s < 0.0:
        print('Score not valid')
    elif s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    else:
        print('F')
except (ValueError, NameError):
    print('Please enter required numbers')
