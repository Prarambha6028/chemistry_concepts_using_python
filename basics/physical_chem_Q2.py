'''
The speed of sound in a gas of molar mass M at temperature T is
c =
sqrt(γ*R*T/M),
where R is the gas constant and for air the adiabatic index, γ = 7/5 .
Estimate the speed of sound in air at (a) 25 ◦C and (b) −20 ◦C. Take M =
29 g mol−1.
'''
import math as m
#The gas constant (J.K-1.mol-1)
R= 8.314
# Ratio of the heat capacities C_p / C_V (adiabatic index) for a diatomic gas
gamma=7/5
#Mean Molar mass of the gas, in kg mol-1.
M_gas=29/1000
#At temperature 25◦C
T1=25
#converting the celsius to kelvin
T1=T1+273

f=m.sqrt(gamma*R/M_gas)

#The Speed of sound in a gas:
C=f*m.sqrt(T1)
print("The speed of sound in air at 25 ◦C:",C)

T2=-20
# Convert the second temperature from degC to K
T2=T2+273

C=f*m.sqrt(T2)
print("the speed of sound in air at -20 ◦C:",C)
