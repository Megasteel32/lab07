# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Group 8: Anthony Matl, Landon Matak, Luca Maddaleni, Nathaniel Michaud
# Group:       8
# Section:     273
# Assignment:  Lab 7 Activity 1-4
# Date:        7 October 2020

f = 0
list = ['arroyo', 'elephantine', 'a', 'shines']
#printing string if character count is more than 2 and first and last characters are the same
for i in list:
    j = len(i) - 1
    if j > 2 and i[j] == i[0]:
        f+= 1
        print(i)

#printing all elements with values less than a user inputed number
list2 = []       #the list that gets check. I make it by default a list from 0 to 10000
for i in range(10001):
    list2.append(i)
value = int(input('Input number: '))
for i in list2:
    if i < value:
        print(i)
#getting sentence and letter to be checked
sentence = input('Enter a sentence: ')
checkLet = input('What letter do you want to check? ')
num_count = 0
#looping over string in order to determine the amount of times the letter was used

for i in sentence:
    if checkLet == i:
        num_count += 1
#print the amount of times it was used
print(checkLet, 'was used', num_count, 'times')

#function solver
from math import *
min = float(input('Enter minimum value: '))
max = float(input('Enter maximum value: '))
current_val = min
list_values = []
#getting the increments that will be plugged into y(x)
increments = (max-min) / 100
for i in range(101):
    current_val += min
    x = current_val
    y = sin(x) / (sin(x/10) + x/10)
    list_values.append(y)

print(list_values)
