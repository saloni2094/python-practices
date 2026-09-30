##Take a input hh, min, sec
hh = int(input('Enter hh:'))
min = int(input('Enter min:'))
sec = int(input('Enter sec:'))

##use formula
total_second = (hh * 3600) + (min * 60) + sec
print('total second =', total_second)

#Output: Enter hh: 6
#        Enter min: 50
#        Enter sec: 200
#total second + 24800