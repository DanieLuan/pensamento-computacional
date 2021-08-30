import math as mt

x = float(input('x? '))
y = float(input('y? '))
z = float(input('z? '))

exp1 = ((x**2) + (y**2) + (z**2))**(1/3)
print('('+str(x)+'^2 + '+str(y)+'^2 + '+str(z)+'^2)^(1/3) = '+str(exp1))

exp2 = x**y + y**z
print(str(x)+'^'+str(y)+' + '+str(y)+'^'+str(z) +' = '+str(exp2))

exp3 = mt.sin(x**2 + y**2) + mt.cos(y**2 + z**2)
print('sin('+ str(x)+'^2 + '+str(y)+'^2) + cos('+str(y)+'^2 + '+str(z)+'^2) = '+str(exp3))

exp4 = (mt.log(x)+mt.log(y)+mt.log(z))**(x+y+z)
print('log '+str(x)+' + log '+str(y)+' + log '+str(z)+')^('+str(x)+' + '+str(y)+' + '+str(z)+') = '+str(exp4))