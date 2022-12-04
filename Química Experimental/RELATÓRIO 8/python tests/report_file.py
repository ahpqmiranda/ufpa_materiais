class chemical:
    def __init__(self, name, molar_mass, density, mols, enthalpy=None, heat_capacity=None, initial_temperature=None, final_temperature=None):
        self.name = name
        self.molar_mass = molar_mass
        self.density = density
        self.mols = mols
        self.enthalpy = enthalpy
        self.heat_capacity = heat_capacity
        self.initial_temperature = initial_temperature
        self.final_temperature = final_temperature
        self.m = mols * molar_mass
        self.mol = mols
        self.vol = mols * molar_mass / density
        self.mol_vol = self.mol / self.vol
        self.mol_vol = round(self.mol_vol, 3)




    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name