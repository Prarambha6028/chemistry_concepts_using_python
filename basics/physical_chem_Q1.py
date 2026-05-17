'''How many molecules of water are there in a 250 mL glass of water?
Take the density, ρ(H2O(l))=1 g cm−3 and the molar mass, M(H2O)=18 g mol−1'''
#Avogardo Constant
#The volume of the water being considered , in cm3
V=250
# The density of water, in g.cm-3.
rho=1
# The molar mass of H2O, in g.mol-1.
M_H20=18
#The mass of water, in g.
m=rho*V
#The amount of water, in mol.
n=m/M_H20
#The number of water molecules is then
N=n*N_A
print("Number of molecules in 250 ml glass of water is:",N)
