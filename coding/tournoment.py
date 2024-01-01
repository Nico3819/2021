player1 = raw_input ('what is the name of player 1:  ')
player2 = raw_input ('what is the name of player 2:  ')
player3 = raw_input ('what is the name of player 3:  ')
player4 = raw_input ('what is the name of player 4:  ')
player5 = raw_input ('what is the name of player 5:  ')
sub1 = raw_input ('what is the name of sub 1:  ')
sub2 = raw_input ('what is the name of sub 2:  ')
team = [player1, player2, player3, player4, player5]
subs = [sub1, sub2]
print ('team = %s' % team)
print ('subs = %s' % subs)
full = [team, subs]
#print full
player6 = raw_input ('what is the name of player 6:  ')
team.append(player6)
print full
