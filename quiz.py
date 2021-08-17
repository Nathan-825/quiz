score = 0

def check_guess(guess,answer):
    global score
    if guess.lower() == answer.lower():
        print('You are correct!')
        score = score + 1
    else:
        print('You have a mistake!')

print("Hello")

guess = input("1+1=?")
check_guess(guess,"2")

guess = input("80-13=?")
check_guess(guess,"67")

guess = input("99999+99999=?")
check_guess(guess,"199998")


print("Your score is",score)

if score == 3:
  print("Congratulations!You got all correct!")
else:
  print("Maybe next time!")

while True:
  from time import sleep
  sleep(1)
