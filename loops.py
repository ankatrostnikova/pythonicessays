#!/usr/bin/python
# Name: Anna Trostnikova
# Section: 1
# Date:23/07/2013
# loops.py

# Transfer fractions like 1/n in range 1/2-1/10 to decimals. Print the result.
for n in  range(2,11):
   k = 1.0/n
   print k

#Prints a countdown from the given number to 0.
print "Countdown"
num = raw_input("Enter a non negative number:")
num = int(num)
while num < 0:
    print "This is not a valid input. Please try again"
    num = input("Enter a non negative number")

while num > 0:
  
   print num - 1
   num = num-1

# Calculate the exponent, using base and exponent value.
base = raw_input("Enter the exponent base, please: ")
base = int(base)
exp = raw_input("Enter the exponent, please: ")
exp = int(exp)
if exp<0:
   print "This is not a valid input"
else:  
   c= 1
   for x in range(0,exp):
      c = c*base

   print c


#Asks user to enter an even number, if an odd number is entered prints a witty message and makes user enter another number. Runs till the even number is entered#
num = raw_input("Enter a number, divisable by two ")
num = int(num)
while num%2!= 0:
   print "Learn your math! This is not a number, divisable by two."
   num = raw_input("Enter another number ")
   num = int(num)
print "You are clever. This is an even number. Congratulations"

