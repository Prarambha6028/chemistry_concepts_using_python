from rdkit import Chem

methane=Chem.MolFromSmiles("C")

ethanol=Chem.MolFromSmiles("CCO")

for atoms in methane.GetAtoms():
    print(atoms.GetSymbol(), atoms.GetMass())

for atom in ethanol.GetAtoms():
    print(atom.GetSymbol(),atom.GetMass())
