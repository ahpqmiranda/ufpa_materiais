import numpy as np
import matplotlib as plt
import fenics as fe

if True:
    n_elements = 32
    mesh = fe.UnitIntervalMesh(n_elements)

    lagrange_poly_fist_order = fe.FunctionSpace(
        mesh,
        "Lagrange",
        1
    )