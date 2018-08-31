'''The Birthday Problem
August 31, 2018'''

import random

number_of_people = 23 #people in room

#define the match function
def match():
    '''Generate birthday list and
    return True if there's a repeated
    number'''
    birthdays = [random.randint(1,365) for i in range(number_of_people)]
    #print(birthdays)
    #check for a match by counting each item in the list
    for day in birthdays: #loop through every item
        if birthdays.count(day) > 1: #if any are repeated
            return True
    return False
            

successes = 0
trials = 10000
for i in range(trials):
    if match():
        successes += 1

print("Probability:",successes / trials)
        
#print(match())
