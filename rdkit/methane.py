from rdkit import Chem

methane=Chem.MolFromSmiles("C")

Num_methane=methane.GetNumAtoms()
print(f"The number of atoms in methane is {Num_methane}") #By default, RDKit only counts “heavy atoms”. This means that hydrogen isn’t included

Num_methane_h=methane.GetNumAtoms(onlyExplicit=False)
print(f"The number of atoms in methane including hydrogens is {Num_methane_h}")
