##Take input for Quadratic eqn
##ax**2+bc+c==0

import math
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

##Discriminant nikalo
#formula D = b**2-4ac
#(-b + **D)/2a #(-b - **D)/2a
D = b**2 - 4*a*c

root1 = (b + math.sqrt(D))/(2*a)
root2 = (b - math.sqrt(D))/(2*a)

#display result 
print("root 1 =", root1)
print("root 2 =", root2)
