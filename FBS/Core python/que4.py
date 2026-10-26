height = float(input('Enter wall height:'))
width = float(input('Enter wall width:'))
rate = float(input('Enter painting rate per sq.m:'))

area = height * width * 4
cost = area * rate

print('total area:', area)
print('total painting cost:',cost)
