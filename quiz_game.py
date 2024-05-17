print("Welcome to my computer quiz!")

playing = input("Do you want to play?: ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0

answer = input("Who is Michael's Fiance? ")
if answer == "Symantha":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")  

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")
  
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the founder of ZAOGA FIF Ministries?: ")
if answer == "Ezekiel Handinawangu Guti":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")