'''
Under the temperature T, the ionized level of hydrogen in thermal equilibrium.
This can be calculated by "Saha Equation"
n_+ : ionized hydrogen(proton)
n_0 : neutral hydrogen
n_e : density of electrons
g_+ : statistical weight of proton in the ground state
g_0 : statistical weight of neutral hydrogen in the ground state
m_e : 9.109e-31 [kg] , mass of electron
X_I : 13.6 [eV] , Ionized potential of hydrogen
h   : 6.626e-34 [Js]
k_B : 1.381e-23 [J/K]
(n_+ * n_e)/n_0 = (2*g_+/g_0)*((2*pi*m_e*K_b*T)/(h^2))^(3/2)*exp(-X_I/(K_b*T))
'''
import numpy as np
'''
Total Density: n_H = n_0 + n_+ = 1.e+4 [cm^-3]
Calculation of T required for 50% ionization of hydrogen
'''
m_e = 9.109e-31
X_I = 13.6
h = 6.626e-34
k_B = 1.381e-23


