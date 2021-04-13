import numpy as np
import scipy as sp
import scipy.optimize
import math
from math import erfc
from math import erf
import sympy as sym
from sympy.solvers import solve
from sympy import Symbol
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
from matplotlib import ticker


def USDopt(n):
    lam0=2*np.exp(-n)*(np.cosh(n)+np.cos(n))
    lam1=2*np.exp(-n)*(np.sinh(n)+np.sin(n))
    lam2=2*np.exp(-n)*(np.cosh(n)-np.cos(n))
    lam3=2*np.exp(-n)*(np.sinh(n)-np.sin(n))
    return np.min([lam0,lam1,lam2,lam3])


def USD_simple(n):
    return 1-(1-np.exp(-n))*(1-np.exp(-n/2))*(1-np.exp(-n/2))

def USD_Enk(n):
    return 1+3*np.exp(-2*n)+2*n*np.exp(-2*n)-4*np.exp(-n)

def psuccess (n,x):
    return (erfc(x-np.sqrt(n/2))+erfc(x+np.sqrt(n/2)))**2/4

def USD_Heterodyne (n,success):
    mineq=100
    xmin=0
    # try:
    for x in np.arange(0, 10, 0.01):
        eq=abs(psuccess(n,x)-success)
        if eq<mineq:
            mineq=eq
            xmin=x
    PeHetero=erfc(xmin+np.sqrt(n/2))*(erfc(xmin+np.sqrt(n/2))+2*erfc(xmin-np.sqrt(n/2)))/(4*psuccess(n,xmin))
    return PeHetero


def Heterodyne_success (n, ptharray, delta, step):
    success=0
    i=0
    for m in np.arange(step):
        success =success + erfc(ptharray[i] + np.sqrt(n) / np.sqrt(2)) *erfc(ptharray[i]-np.sqrt(n)/np.sqrt(2))* (erf(np.sqrt(n)/np.sqrt(2)-m*delta)-erf(np.sqrt(n)/np.sqrt(2)+m*delta)+erf(np.sqrt(n)/np.sqrt(2)+(m+1)*delta)-erf(np.sqrt(n)/np.sqrt(2)-(m+1)*delta))/4
        i=i+1
    return success

def Heterodyne_error (n, ptharray, delta, step):
    i=0
    for m in np.arange(step):
        error=Heterodyne_success(n, m, delta, ptharray[i]) - (erf(np.sqrt(n)/np.sqrt(2)-m*delta)- erf(np.sqrt(n)/np.sqrt(2)-(m+1)*delta))*erfc(ptharray[i] + np.sqrt(n) / np.sqrt(2))/4
        i=i+1
    return error
#
#
n=1
step=10
success=0.09428125

# # def USD_Heterodyne_opt (n,success,step):
# xmax=n*20
# xmin=0
# delta=(xmax-xmin)/step
# mineq=0.001
# mineqarray=[]
# ptharraymin=[]
# for pth0 in np.arange(0,10,0.1)[::-1]:
#     for pth1 in np.arange(0,pth0,0.1)[::-1]:
#         for pth2 in np.arange(0,pth1,0.1)[::-1]:
#             for pth3 in np.arange(0,pth2,0.1)[::-1]:
#                 for pth4 in np.arange(0,pth3,0.1)[::-1]:
#                     for pth5 in np.arange(0,pth4,0.1)[::-1]:
#                         for pth6 in np.arange(0,pth5,0.1)[::-1]:
#                             for pth7 in np.arange(0,pth6,0.1)[::-1]:
#                                 for pth8 in np.arange(0,pth7,0.1)[::-1]:
#                                     for pth9 in np.arange(0,pth8,0.1)[::-1]:
#                                         ptharray=[pth0,pth1,pth2,pth3,pth4,pth5,pth6,pth7,pth8,pth9]
#                                         eq=abs(Heterodyne_success(n, ptharray, delta, step)-success)
#                                         if eq<mineq:
#                                             mineqarray+=[eq]
#                                             ptharraymin+=[ptharray]
#
# # PeHetero=Heterodyne_error (n, ptharraymin, delta, step)
# # return mineqarray,ptharraymin
#
# print(mineqarray)
# print(ptharray)