'''Birthday Problem
June 1, 2018'''

import random

#number of people in the room
NUM_PEOPLE = 60

#one trial
def trial():
    '''Returns True if birthday is repeated'''
    #empty list for birthday numbers 1 - 365
    birthday_list = []

    #add a random number 1-365 to birthday list
    # NUM_PEOPLE times

    for i in range(NUM_PEOPLE):
        birthday_list.append(random.randint(1,365))

    #print(birthday_list)

    #check for repeated number
    #if one number is repeated, return True (success!)
    for n in birthday_list:
        countN = birthday_list.count(n)
        if countN > 1:
            #print(n, countN)
            return True
    return False

successes = 0 #successful trials
trials = 60000 #number of trial

for i in range(trials):
#execute the trial function
    if trial() == True:
        successes += 1

print(successes / trials) #percent success
