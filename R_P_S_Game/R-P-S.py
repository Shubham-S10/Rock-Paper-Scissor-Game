                     #Rock_Paper_Scissor_Game

import random
print("                                    Rock_Paper_Scissor GAME ")                     
user = input("Enter Your Name .... ")
print("Welcome " + user )
go = ['r','p','s']
op = input("Press 1 !!\n{1}-> V/S Computer ........ ")                     #options of game types to user
print("""                                                                       Winning Rules as follows :

                                                                        Rock vs paper-> paper wins
                                                                        Rock vs scissor-> Rock wins
                                                                        paper vs scissor-> scissor wins
                                                                        if player and computer choose the same then its a TIE.""")

won = False

while not won:
  if(op=="1"):
    t = input(" Type #{rock} , #{paper} ,or #{scissor} .......    ")             #taking input from the user (t)
    i = random.choice(go)                                                       #random input from computer (i)
    if (t=="rock"):
      if (i=="r"):
        print("*********   You Chose rock. \n ********* Computer Chose Rock.   \n ************************************You TIED. ")
      elif(i=="p"):
        print("*********   You Chose rock. \n ********* Computer Chose Paper.   \n ************************************You LOSE. ")
      elif(i=="s"):
        print("*********   You Chose rock. \n ********* Computer Chose Scissor.   \n *******       ******      || YOU WON ||        *******      ********")
      
    elif(t=="paper"):
      if(i=="r"):
        print("*********   You Chose paper. \n ********* Computer Chose Rock.   \n *******       ******      || YOU WON ||        *******      ********")
      elif(i=="p"):
        print("*********   You Chose paper. \n ********* Computer Chose Paper.   \n ************************************You TIED. ")
      elif(i=="s"):
        print("*********   You Chose paper. \n ********* Computer Chose Scissor.   \n ************************************You LOSE. ")

    elif(t=="scissor"):
      if(i=="r"):
        print("*********   You Chose scissor. \n ********* Computer Chose Rock.   \n ************************************You LOSE. ")
      elif(i=="p"):
        print("*********   You Chose scissor. \n ********* Computer Chose paper.   \n *******       ******      || YOU WON ||        *******      ********")
      elif(i=="s"):
        print("*********   You Chose scissor. \n ********* Computer Chose Scissor.   \n ************************************You TIED. ")
    else:
      print("Invalid Input")
  else:
    print("Entered the wrong value")
      



