import random
number = random.randint(1, 20)
x = 0
while 4 > x:  
  guess = input ("guess a number 1 through 20:  ")
  if guess == number:
    print ('that is the correct number you win')
    exit()
  if guess > number:
    print ('choose a lower number')
  if guess < number:
    print ('choose a higher number')
  x = x + 1
