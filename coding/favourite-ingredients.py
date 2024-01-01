ingridients = ['fries', 'burgers', 'pizza', 'chips']
number = 0
while number < 5:
  number = number + 1
  for x in ingridients:
    print(number, x)
    number = number + 1
  # if x == 'chips':
    #  break
