'''
Acetic acid, CH3CO2H, is a weak acid with pKa = 4.756. What is the pH of a 0.1
M solution of acetic acid in water?
'''
import math as m
# The pKa of acetic acid, log10 of the acid dissociation constant.
pka=4.756
ka=10**(-pka)
# "Standard" amount concentration , 1 M = 1 mol.dm-3.
c_std=1
# The concentration of the acid.
c=0.1
# The concentration of hydrogen ions at equilibrium.
x=m.sqrt(ka*c*c_std)

pH=-m.log10(x)
print("The pH of 0.1 M acetic acid is:",pH)
