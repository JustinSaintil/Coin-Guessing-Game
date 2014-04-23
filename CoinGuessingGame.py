import random

f = open ("CoinFLIP.py", "r+")
highscore = f.read()
highscore = int(highscore)


score = 0
correct = True



#_____________________________________________________________________

print "This is called THE Guessing Game.", "\nFor this Game the All Time Highscore is:", highscore, "\nCan You beat it?"


while correct:
    gop = raw_input("Predict Heads or Tails: ")
    guess = random.randint(1,2)
    if guess ==1:
        guess = "Heads"
    else:
        guess = "Tails"
    if guess == gop:
        print "The Right answer was:", guess, "\nYour answer was:", gop, "\nWho was right:You were"
        score = 0
        score = score +1
        print "Your current score is:", score
    else:
        print "The Right answer was:", guess, "\nYour answer was:", gop, "\nWho was right:You Weren't"
        correct = False
        print "You are a Failure.", "\nYour Score is:", score, ".", "The Highscore still is:", highscore


highscore = int(highscore)

if score > highscore:
    f.seek(0)
    f.write(str(score))