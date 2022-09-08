name = input ("enter your name : ")
print("hello",name,"welcome to the quiz world")
playing = input ("do you want to play? ") .lower() .strip()

if playing != "yes": 
  quit ()


print ("okay! Let's play! :)")
  
score = 0 

# QUESTION 1 
answer1 = input("what is the capital of Queensland? \na. Townsville \nb. Brisbane \nc. Noosa \nAnswer: ") .lower() .strip()
if answer1 == "b" or answer1 == "brisbane": 
  score  += 1 
  print("correct!")
  print("score: ", score)
  print("\n")
else:
  print("incorrect ! The answer is Brisbane. ")
  print("score: ", score)
  print("\n")


# QUESTION 2 
answer2 = input("In which state is Briyedsville found? \na. New South Wales \nb. South Australia  \nc. Queensland \nAnswer: ") .lower() .strip()  
if answer2 == "c" or answer2 == "Queensland": 
  score  += 1 
  print("correct!")
  print("score: ", score)
  print("\n")
else:
  print("incorrect ! The answer is Queensland. ")
  print("score: ", score)
  print("\n")


# QUESTION 2 
answer1 = input("what is the capital city of Australia? \na. Canberra \nb. Sydney \nc. Noosa \nAnswer: ") .lower() .strip()
if answer1 == "b" or answer1 == "brisbane": 
  score  += 1 
  print("correct!")
  print("score: ", score)
  print("\n")
else:
  print("incorrect ! The answer is Brisbane. ")
  print("score: ", score)
  print("\n")






