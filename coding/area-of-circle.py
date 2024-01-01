calculator = raw_input ("what would you like to calculate: ")
if calculator == 'c':
  radius = input ("what is the radius of the circle:  ")

  radius = radius * radius

  answer = 3.14 * radius

  print answer
if calculator == 'r':
  length = input ("what is the length of your rectangle:  ")
  width = input ("what is the width of your rectangle:  ")
  answer = length * width
  print answer

if calculator == 's':
  side = input ("what is one side of the square:  ")
  answer = side * side
  print answer
