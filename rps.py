 #!/usr/bin/python
# Name: Anna Trostnikova
# Section: 2
# Date:12/07/2013
#Rock, paper, scissors game.

Player1  = raw_input("Player1?")

Player2 = raw_input('Player2 ?')

#Player1.lower()
#Player2.lower()

if Player1 == "rock" and Player2 =="rock":
   print "Tie."
elif Player1 == "rock" and Player2 == "paper":
    print "Player2 wins!"
elif Player1 == "rock" and  Player2 == "scissors":
     print "Player1 wins!"
elif Player1 == "paper" and  Player2 == "paper":
   print "Tie." 
elif Player1 == "paper" and  Player2 == "rock":
   print "Player1 wins!"
elif Player1 == "paper" and  Player2 == "scissors":
   print "Player2 wins!"
elif Player1 == "scissors" and  Player2 == "scissors":
   print "Tie."  
elif Player1 == "scissors" and  Player2 == "paper":
   print "Player1 wins!"
elif Player1 == "scissors" and  Player2 == "rock":
   print "Player2 wins!"
else: 
   print "This is not a valid choice. Please enter rock, paper or scissors."

