##convert days into year weeks days 
##Take input total days

days = int(input('Enter total days'))
# first years nikalo
years = days // 365
## remainingdays nikalo years ke days remove karo pahile
remaining_days = days % 365
##weeks nikalo 1 week = 7 days
weeks = remaining_days // 7
## bache hue days 
days = remaining_days % 7
##Display resultt
print('years = ', years)
print(' weeks =', weeks)
print(' days =', days)   

## output Enter total days 400
#years // 365 = 1 years
#400 % 365 = 35 days
#35 // 7 = 5 weeks
#35 % 7 = 0 days

