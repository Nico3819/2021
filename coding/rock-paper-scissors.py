import random
while True:
#  import random:
  item = raw_input ('Choose rock, paper or scissor:  ')
  if item == 'quit':
    break
  cpu_choice = ['rock', 'paper', 'scissor']
  cpu = random.choice(cpu_choice)
  if cpu == 'rock' and item == 'rock':
    print cpu
    print 'you tied'
  if cpu == 'rock' and item == 'paper':
    print cpu
    print 'you win'
  if cpu == 'rock' and item == 'scissor':
    print cpu
    print 'you lose'
  if cpu == 'paper' and item == 'rock':
    print cpu
    print 'you lose'
  if cpu == 'paper' and item == 'paper':
    print cpu
    print 'you tied'
  if cpu == 'paper' and item == 'scissor':
    print cpu
    print 'you win'
  if cpu == 'scissor' and item == 'rock':
    print cpu
    print 'you win'
  if cpu == 'scissor' and item == 'paper':
    print cpu
    print 'you lose'
  if cpu == 'scissor' and item == 'scissor':
    print cpu
    print 'you tied'
