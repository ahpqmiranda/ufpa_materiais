from math import sqrt, pi,cos,sin,tan,atan,degrees
from anastruct import SystemElements

ss = SystemElements(EA=15000, EI=5000)

#parameters
h_1 = 0.454 #m
h_2 = 4.811 #m
b_1 = 3.898 #m
b_2 = 5.265 #m
l = 10 #m

ldo =sqrt((h_2+h_1)**2+b_2**2)
ldw =sqrt(h_2**2+b_1**2)
print("Daklengte west = ",ldw,", daklengte oost = ",ldo)
beta = atan((h_2+h_1)/b_2)
alfa = atan(h_2/b_1)
print("west hoek = ",degrees(alfa),"oosthoek = ",degrees(beta))
m_sneeuw = 1000 #N/m^2
M_dak =600+480/3,14+m_sneeuw#N/m^2

W_do = 920 #N/m
W_dw = 920 #N/m

F_dak = 1000 #N/m
F_sneeuw = 280 #N/m
F_last = 000 #N

F_ds = F_dak+F_sneeuw

# Add beams to the system.
ss.add_element(location=[[0, h_1], [b_1, (h_1+h_2)]],spring={2:0})
ss.add_element(location=[[b_1, (h_1+h_2)], [(b_1+b_2), 0]])

# Add a fixed support at node 1.
ss.add_support_hinged(node_id=1)
ss.add_support_hinged(node_id=3)

#windbelasting
ss.q_load(q=-W_dw, element_id=1)
ss.q_load(q=-W_do, element_id=2)

#sneeuwbelasting/eigen gewicht
ss.q_load(q=-F_ds, element_id=1,direction = "y")
ss.q_load(q=-F_ds, element_id=2,direction = "y")

# Solve
ss.solve()

# Get visual results.
ss.show_structure(scale=0.6)
ss.show_reaction_force(scale=0.8)
ss.show_axial_force(scale=0.6)
ss.show_shear_force(scale=0.6)
ss.show_bending_moment(scale=0.6)
ss.show_displacement(scale=0.6)