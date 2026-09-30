## Take input in float
feet = float(input('Enter feet'))
inches = float(input('Enter inches'))

##convert everything into inches first

total_inches = ( feet * 12) + inches

#1 inch = 0.0254 meter

meter = total_inches * 0.0254

#1 inch = 2.54 centimeter

centimeter = total_inches * 2.54

print('meter =',meter)
print('centimeter =', centimeter)

#OUTPUT :
#Enter feet 5.8
#Enter inches 2.5
#meter = 1.83133999999997
#centimeter = 183.134