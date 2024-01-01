name = raw_input ('what is your name:  ')
age = input ('whta is your age:  ')

if age < 18 and age > 5:
  league = age + 1
  print('you will play in u%s'% (league))
if age <= 5:
  print ('leagues start at 6 years or higher')
if age >= 18:
  print ('you are in the first team')
