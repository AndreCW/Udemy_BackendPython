# Raizes de equacao de segundo grau
import math

def delta(a, b, c):
    return b**2 - 4*a*c

print("\nConsidere a seguinte equacao:")
print("\na*x^2 + b*x + c = 0")
print("\nInforme o valor dos coeficientes a, b e c:")

coef = []

for i in range(3):
    coef.append(float(input()))
    
d = delta(coef[0], coef[1], coef[2])

if d < 0:
    print("\nNao ha raizes para esta equacao")
elif d == 0:
    x = -coef[1]/(2*coef[0])
    print(x)
else:
    x1 = (-coef[1] + math.sqrt(d))/(2*coef[0])
    x2 = (-coef[1] - math.sqrt(d))/(2*coef[0])
    print(f"\nAs raizes da equacao sao {x1} e {x2}")