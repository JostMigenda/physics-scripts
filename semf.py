# semf.py - Calculate the binding energy for a nucleus with given A and Z using the Semi-Empirical Mass Formula
# Note that there are various different numerical fits to the available data. If you prefer to use a different one, edit the fit parameters `a_*` below.

import argparse

p = argparse.ArgumentParser()
p.add_argument('A', type=int, help='atomic mass number')
p.add_argument('Z', type=int, help='number of protons')
args = p.parse_args()
A, Z = args.A, args.Z

if A < Z:
    A, Z = Z, A

# Volume term
a_V = 15.56
volume = a_V * A

# Surface term
a_S = 17.23
surface = a_S * A**(2/3)

# Coulomb term
a_C = 0.697
coulomb = a_C * Z * (Z-1) / A**(1/3)

# Asymmetry term
a_A = 23.28
asymmetry = a_A * (A - 2*Z)**2 / A

# Pairing term
a_P = 12.0
if A%2 == 1:
    pairing = 0
elif Z%2 == 0:
    pairing = a_P / A**(1/2)
else:
    pairing = - a_P / A**(1/2)

bindingEnergy = volume - surface - coulomb - asymmetry + pairing
print(f'B(A={A}, Z={Z}) = {bindingEnergy} MeV')
