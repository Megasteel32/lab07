# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Group 8: Anthony Matl, Landon Matak, Luca Maddaleni, Nathaniel Michaud
# Group:       8
# Section:     273
# Assignment:  Lab #7 Activity 5
# Date:        7 October 2020

TOL = 10**-6
value_x = float(input('Enter a value on the interval -1 < x < 1: '))
while value_x >= 1.0 or -1.0 >= value_x:
    value_x = float(input('Invalid value. Enter one between -1 and 1: '))
n = 0
valv = 1
approx = 0
while abs(valv) > TOL:
    valv = value_x**n
    approx += valv
    n += 1
print('The approximation for 1/(1-x) is ', approx)

