# bending of a beam with given properties
# using the finite element method

import numpy as np
from dolfin import *
import matplotlib.pyplot as plt

# Create mesh and define function space
mesh = UnitSquareMesh(8, 8)
V = FunctionSpace(mesh, 'Lagrange', 1)

# Define boundary conditions
tol = 1E-14
def left(x, on_boundary):
    return on_boundary and abs(x[0]) < tol

def right(x, on_boundary):
    return on_boundary and abs(x[0] - 1) < tol

bc_left = DirichletBC(V, Constant(0), left)
bc_right = DirichletBC(V, Constant(0), right)
bcs = [bc_left, bc_right]

# Define functions
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(0)

# Define strain and stress
def epsilon(u):
    return 0.5*(grad(u) + grad(u).T)

def sigma(u):
    return 2*epsilon(u)

# Define variational problem
a = inner(sigma(u), epsilon(v))*dx
L = inner(f, v)*dx

# Compute solution
u = Function(V)
solve(a == L, u, bcs)

# Plot and compare with analytical solution
plt.figure()
plot(u, title='Solution')
plt.show()

# Compute error in L2 norm
error_L2 = errornorm(u, u_exact, 'L2')
print('Error in L2 norm:', error_L2)

# Compute error in H1 norm
error_H1 = errornorm(u, u_exact, 'H1')
print('Error in H1 norm:', error_H1)

# Compute error in H1 semi-norm
error_H1s = errornorm(u, u_exact, 'H1s')
print('Error in H1 semi-norm:', error_H1s)