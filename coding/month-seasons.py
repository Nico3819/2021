fall = ['september', 'october', 'november']
winter = ['january', 'febuary','december']
spring = ['march','april','may']
summer = ['june','july','august']
month = raw_input ('enter a month:  ')
if (month in fall):
	print ('this month is in fall')
	exit()
if (month in winter):
        print ('this month is in winter')
	exit()
if (month in spring):
        print ('this month is in spring')
	exit()
if (month in summer):
        print ('this month is in summer')
	exit()
else:
        print ('this is not a month')
