"""
Name:           ode_solver2.py
Description:    A program that solves a second order ODE
"""
from sympy import dsolve, Eq, exp, Function, symbols
t = symbols('t')
y = symbols('y', cls=Function)

deqn2 = Eq(y(t).diff(t,t) + y(t).diff(t) + y(t), exp(t))
sol2 = dsolve(deqn2, y(t))
print(sol2)