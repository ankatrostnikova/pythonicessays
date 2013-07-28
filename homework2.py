#!/usr/bin/python
#Anna Trostnikova
# Section:2
# hw2.py
import math
import random
##### Template for Homework 2, exercises 2.0 - 2.5  ######


# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 
# Simulate Rock, paper, scissors game
# Input player 1 and player 2 choices in rock, paper, scissors.
#Output. Who wins the game.
##### YOUR CODE HERE ####
def rps_results(Player1, Player2):
    if Player1 == "rock" and Player2 =="rock":
        return "Tie."
    elif Player1 == "rock" and Player2 == "paper":
        return "Player2 wins!"
    elif Player1 == "rock" and  Player2 == "scissors":
       return "Player1 wins!"
    elif Player1 == "paper" and  Player2 == "paper":
      return "Tie."
    elif Player1 == "paper" and  Player2 == "rock":
       return "Player1 wins!"
    elif Player1 == "paper" and  Player2 == "scissors":
       return "Player2 wins!"
    elif Player1 == "scissors" and  Player2 == "scissors":
       return "Tie."
    elif Player1 == "scissors" and  Player2 == "paper":
       return "Player1 wins!"
    elif Player1 == "scissors" and  Player2 == "rock":
       return "Player2 wins!"
    else:
       return "This is not a valid choice. Please enter correct values."
# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####
print rps_results("rock","paper")
print rps_results("scissors","scissors")
print rps_results("scissors", "paper")
print rps_results("juk","fuk")
# ********** Exercise 2.2 ********** 
#
# is_divisible determine, whether one integer is divisible by another integer. Input: 2 integers.Output:shows divisibility.
##### YOUR CODE HERE #####
def is_divisible(m,n):
   if m%n == 0:
    return True
   else:
    return False


# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?



#not_equal compares two integers and returns True if they are not equal and False if they are equal. Input: 2 integers. Output: If not equal = True, if equal = False
##### YOUR CODE HERE #####
def not_equal(m,n):
    #  int(m)
     # int(n)
      if m == n:
        return False
      else:
        return True


# Test cases for not_equal
##### YOUR CODE HERE #####
#print not_equal(3,3)
print  not_equal(4.5,4.8)
print not_equal(3.0,3)
print not_equal(-2.78,-2.78)

#print not_equal("puk", "puk")
#print not_equal("puk", "hujuk") 
# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
   d = a*b+c
   return d
#print multadd(1,1,1)
#print multadd(3,0,3.5)
#print multadd (1,-1,-2)


   
## 2 - Equations
##### YOUR CODE HERE #####
#print math.sin (math.pi/4) 
#print multadd(1,math.sin(math.pi/4),math.cos(math.pi/4)/2)
# multadd(2,math.log(12,7), math.ceil(276/19))  
# Test Cases
angle_test =  multadd(1,math.sin(math.pi/4),math.cos(math.pi/4)/2)
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test =  multadd(2.0,math.log(12,7), math.ceil(276.0/19.0))  
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test
## 3 - yikes function
##### YOUR CODE HERE #####

def yikes(x) :
   t = math.e**(-x)
   put = math.sqrt(1-math.e**(-x))
   an = multadd(x,t,put)
   return an


# Test Cases
x = 5
print "yikes(5) =", yikes(x)
x = 100
print "yikes(100) =", yikes(x)
#x = -8
#print "yikes(-8) =", yikes(x)
# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
 t = random.randint(0,103)
 
 if t%3 == 0:
   return True
 else:
   return False
print rand_divis_3()



# Test Cases
##### YOUR CODE HERE #####
print rand_divis_3()
## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(sides,dices):
     n = dices
     while n > 0:   
       print  random.randint(1,sides)
       n = n-1
     return "That`s all!"    

  
# Test Cases
##### YOUR CODE HERE #####                            
print roll_dice(6,1)
print roll_dice(9,3)
print roll_dice(100,3)

# ********** Exercise 2.5 **********
def roots(a,b,c):
     x = None
     y = None
     if b**2 - 4*a*c < 0:
       print "Sorry, no real roots. Please come for complex roots later."
     elif b**2 - 4*a*c == 0:
       x = (-b)/2.0*a
       print "The equation has only one root."
     else:
      x = ((-b)+(math.sqrt(b**2 - 4*a*c)))/(2.0*a)
      y = ((-b)-(math.sqrt(b**2 - 4*a*c)))/(2.0*a)
     return x,y 


print roots(6,8,2)
print roots (1,12,36)
print roots(2,5,2)
print roots(14,1,28)
   
# code for roots function
##### YOUR CODE HERE #####   

### Test Cases###
##### YOUR CODE HERE #####   
