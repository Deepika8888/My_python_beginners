print(" Welcome to my computer quiz")

playing= input (" Do you want to play the game? ")

if playing!= "Yes":
    quit()

print("Okay!, lets play :)")
score=0

answer= input(" What does CPU stands for? ")
if answer.lower()=="central processing unit":
   print("Correct!")
   score+=1
else:
    print("Wrong!, what a dumb idiot ;( ")

answer_1= input(" What does RAM stands for? ")
if answer_1.lower()=="random access memory":
   print("Correct!")
   score+=1
else:
    print("Wrong!, what a dumb idiot ;( ")

answer_2= input(" What is the capital city of USA?  ")
if answer_2.lower()=="washing ton dc":
   print("Correct!")
   score+=1
else:
    print("Wrong!, what a dumb idiot ;( ")

answer_3= input(" What does ALU stands for? ")
if answer_3.lower()=="arithmetic logic unit":
   print("Correct!")
   score+=1
else:
    print("Wrong!, what a dumb idiot ;( ")     

print("Well good job for getting here :)")
print("You got "+ str(score) + "correct questions!")
print("Thank you for playing")




