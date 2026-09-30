## calculate compound intreset  P T R
p = float(input('Enter p value'))
t = float(input('Enter t value'))
r = float(input('Enter r value'))

## use formula compound intreset FV=PV(1+r)n**
Amount = p  * ( 1+ r/100)**t

CI = Amount - p
## Display result
print('Compound intreset =', CI)
print('Amount =', Amount )


