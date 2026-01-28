#imports all necessary modules
import random
import string
import time

def mem_pass(word_file, n, case_type): #defines a function that will generate a memorable password
    with open(word_file, 'r') as w: #opens file with available words
        words = [] #creates empty list to store available words
        for line in w: #iterates through word document
            words.append(line.strip()) #cleans each word and adds them to the list

    pass_parts = [] #makes list to store parts of the password
    for _ in range(n): #chooses n number of words
        word = random.choice(words) #chooses a random word
        if case_type == 1: #if user enters one, the word is lowercase
            word = word.lower()
        elif case_type == 2: #if user enters two, the word is all caps
            word = word.upper()
        elif case_type == 3: #if user enters 3, the word is capitalized
            word = word.capitalize()
        else:
            print('Please enter a digit 1-3')
            continue
        digit = random.randint(1, 9) #determines a random digit 1-9
        pass_parts.append(word + str(digit)) #concatenates word and digit and appends to the password parts list

    password = '-'.join(pass_parts) #joins all passwords in list with a -
    time_created = time.ctime()
    return password, time_created #returns final password and the time it was created

def rand_pass(n, punct, not_allowed): #creares a function to generate random passwords
    chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits) #identifies available characters for passwords
    if punct == 'yes': #if user wants punctuation, punctation is added to the list of available chars
        chars += list(string.punctuation)
    elif punct != 'no':
        print('Please enter a yes or no')

    chars = [c for c in chars if c not in not_allowed] #identifies all available chars as those that are not in the list not_allowed
    password = ''.join(random.choices(chars, k=n)) #joins n number of random characters from the chars list
    time_created = time.ctime() #identifies the time of generation
    return password, time_created #returns the password and time it was created

#begins program
all_mem_pass = open('Memorable_generated_passwords.txt', 'w') #creates/opens a file for all memorable passwords
all_mem_pass.write('MEMORABLE PASSWORDS\n')
all_mem_pass = all_mem_pass.close() #closes file for best practice
all_rand_pass = open('Random_generated_passwords.txt', 'w') #creates/opens a file for all random passwords
all_rand_pass.write('RANDOM PASSWORDS\n')
all_rand_pass = all_rand_pass.close() #closes file for best practice

while True: #creates loop for users to repeated generate passwords
    choice = input('Please enter if you want to generate (a) a memorable password or (b) a random password (type "done" when finished): ') #identifies the type of password user wants
    if choice == 'a': #identifies if user wants a memorable password
        try: #protects user from invalid input
            n = int(input('How many words do you want?\n')) #identifies n as user input and converts to an integer
            case_type = int(input('What case type do you want? Enter (1) for lower (2) for upper (3) for capitalization.\n')) #identifies user input as case type and converts to an integer
        except ValueError: #catches invalid input and notifies user
            print('Please enter a number.')
        password, time_created = mem_pass('word_file.txt', n, case_type) #identifies password and calls the mem_pass function
        all_mem_pass = open('Memorable_generated_passwords.txt', 'a') #opens memorable password file to append new password
        all_mem_pass.write(password + time_created + '\n') #writes new password and the time it was generated into the file
        all_mem_pass.close() #closes file for best practice
        print('Your Memorable Password:', password, 'Time Created:', time_created)#prints final output (the memorable password) as final output
        all_mem_pass = open('Memorable_generated_passwords.txt', 'r') #opens file to read
        for line in all_mem_pass.readlines(): #prints out all passwords and time of their generation nicely
            print(line)
        all_mem_pass.close()
#if user picks random password:
    elif choice == 'b': #identifies user input as b (random password)
            try: #protects user from invalid input
                n = int(input('How many characters do you want?\n')) #identifies n as the number of chars generated
            except ValueError: #excepts value error and notifies user to enter a valid input
                print('Please enter a number.')
                continue
            punct = input('Do you want punctuation? (yes/no)\n') #identifies if the user wants punctuation or not
            not_allowed = list(input('Do you have any characters not allowed? If so, please enter them here. If not, press enter.\n')) #identifies any characters user doesn't want to use as a list
            password, time_created = rand_pass(n, punct, not_allowed) #calls random password function and returns password and time created
            all_rand_pass = open('Random_generated_passwords.txt', 'a') #opens random password file in append mode
            all_rand_pass.write(password + time_created + '\n') #adds all random passwords and the time they were created to the file
            all_rand_pass.close() #closes file
            print('Your Random Password:', password, 'Time Created:', time_created) #prints out newly generated random passwords
            all_rand_pass = open('Random_generated_passwords.txt', 'r') #opens random password file
            for line in all_rand_pass.readlines(): #prints all random passwords and the time they were generated nicely
                print(line)
            all_rand_pass.close()

    elif choice == 'done': break #if user types done, the program ends
    else: #if user does not enter a valid input, a message appears
        print('Please enter a valid input.')

#tests by randomly generating 1000 passwords
while True: #loop for user to choose whether or not they want to test the password generators
    test = input('Do you want to test by generating 1000 random passwords? (yes/no)\n')
    if test == 'no': #if user doesn't want to test, loop breaks and program ends
        break
    elif test == 'yes': #test is ran if user types yes
        for i in range (1001): #iterates through test 1000 times
            pass_type = ['a', 'b'] #makes list for code to decide between random or memorable passwords
            pass_choice = random.choice(pass_type) #randomly chooses if password is random or memorable
            if pass_choice == 'a': #if a is chosen, a memorable password is generated
                password, time_created = mem_pass('word_file.txt', random.randint(1,3), random.randint(1,3)) #memorable password function runs with random amount of words (1-2) and a random case type
                all_mem_pass = open('Memorable_generated_passwords.txt', 'a') #opens memorable password file to append new password and the time it was created
                all_mem_pass.write(password + time_created + '\n')
                all_mem_pass.close() #closes file for best practice
            elif pass_choice == 'b': #if b is randomly selected, random passwords are generated
                punct = ['yes', 'no'] #creates list to randomly select if punctuation is present
                punct = random.choice(punct) #chooses if punctuation is present
                password, time_created = rand_pass(random.randint(1,4), punct, []) #calls random password function and returns the password and the time it is generated
                all_rand_pass = open('Random_generated_passwords.txt', 'a') #opens random password file
                all_rand_pass.write(password + time_created + '\n') #appends new password and the time it was created
                all_rand_pass.close() #closes file for best practice
    else: print('Please enter a valid input.')

#opens both memorable and random password files to print out nicely
        all_mem_pass = open('Memorable_generated_passwords.txt', 'r')
        all_rand_pass = open('Random_generated_passwords.txt', 'r')
        for line in all_mem_pass.readlines(): print(line)
        for line in all_rand_pass.readlines(): print(line)
        all_mem_pass.close()
        all_rand_pass.close()
        break #program ends