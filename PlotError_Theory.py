import numpy as np
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

from sub import QPSK_USDopt as QUOP
from sub import QPSK_error_montecalro as QUM

from collections import OrderedDict
linestyles = OrderedDict(
    [('solid',               (0, ())),
     ('loosely dotted',      (0, (1, 10))),
     ('dotted',              (0, (1, 5))),
     ('densely dotted',      (0, (1, 1))),

     ('loosely dashed',      (0, (5, 10))),
     ('dashed',              (0, (5, 5))),
     ('densely dashed',      (0, (5, 1))),

     ('loosely dashdotted',  (0, (3, 10, 1, 10))),
     ('dashdotted',          (0, (3, 5, 1, 5))),
     ('densely dashdotted',  (0, (3, 1, 1, 1))),

     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))])


plt.close('all')
##############################################################################################################################################################################################################
##############################################################################################################################################################################################################
dark=0.001 # dark counts per signal state
eta=1  # detection efficiency of photon counter
meanphotonmax=7.25 # plot range -> 0 - meanphotonmax, 0.01 step
visibility=0.994 # visibility of displacement
trysim=10**4 # number of simulation cycles

M=4 # number of stages
successerrortheoryM4=QUM.errorM(M,eta,visibility,dark,trysim,meanphotonmax)
meanphoton=successerrortheoryM4[0]
successM4=successerrortheoryM4[1]
errorM4=successerrortheoryM4[2]
M=10 # number of stages
successerrortheoryM10=QUM.errorM(M,eta,visibility,dark,trysim,meanphotonmax)
meanphoton=successerrortheoryM10[0]
successM10=successerrortheoryM10[1]
errorM10=successerrortheoryM10[2]

# ##############################################################################################################################################################################################################
# ##############################################################################################################################################################################################################
meanphotonmax=10.5
Photon = []
Helstrombox = []
USD_simple = []
USD_Enk = []

for m in np.arange(0, meanphotonmax, 0.1):
    Helstrombox += [QUOP.USDopt(m)]
    USD_simple += [1-QUOP.USD_simple(m)]
    USD_Enk += [QUOP.USD_Enk(m)]
    Photon += [m]

######################################################################################################
#
#######################################################################################################
mm = 1/25.4
# ---------------------------------------------------------------------------
fig, axK = plt.subplots(1, 1, figsize=(86*mm, 62.5*mm), dpi=150)
fontsize=8
# ---------------------------------------------------------------------------
fig.patch.set_facecolor('white')
axK.patch.set_facecolor('grey')
axK.patch.set_alpha(0.1)

axK.text(0.2, 0.88, "Optimal USD", size = fontsize, color = "black",rotation=0)
axK.text(3.0, 0.4, "M=10", size = fontsize, color = "black",rotation=0)
axK.text(4.3, 0.58, "M=4", size = fontsize, color = "black",rotation=0)
axK.annotate(s='',xy=(2.1,0.78),xytext=(1.4, 0.85),xycoords='data',
            arrowprops=dict( arrowstyle='->', facecolor='black'))
axK.annotate(s='',xy=(1.65,0.451),xytext=(2.5, 0.34),xycoords='data',
            arrowprops=dict( arrowstyle='->', facecolor='black'))
axK.annotate(s='',xy=(3.95, 0.72),xytext=(4.6, 0.63),xycoords='data',
            arrowprops=dict( arrowstyle='->', facecolor='black'))
axK.annotate(s='',xy=(2.3, 0.58),xytext=(3.3, 0.45),xycoords='data',
            arrowprops=dict( arrowstyle='->', facecolor='black'))


axK.set_ylabel("Probabiliity of conclusive results", size = fontsize, color = "black")
axK.set_xlabel("Mean photon number $|\\alpha|^2$", size = fontsize, color = "black")

axK.tick_params(axis="x", labelsize=fontsize)
axK.tick_params(axis="y", labelsize=fontsize)

axK.plot(Photon, Helstrombox, color='black',  linestyle='solid', linewidth=1)
axK.plot(Photon, USD_simple, color='green', linewidth=1)
axK.plot(meanphoton, successM10, color='salmon', linestyle=linestyles['densely dashed'], linewidth=1)
axK.plot(meanphoton, successM4, color='green', linestyle=linestyles['densely dashed'], linewidth=1)

axK.grid(color='black',linestyle='-', linewidth=0.2)
axK.set_xlim([0,7.25])
axK.set_ylim([0,1])





fig, axK2 = plt.subplots(1, 1, figsize=(86*mm, 62.5*mm), dpi=150)
# ---------------------------------------------------------------------------
fig.patch.set_facecolor('white')
axK2.patch.set_facecolor('grey')
axK2.patch.set_alpha(0.1)

axK2.set_ylabel("Error probability", size = fontsize, color = "black")
axK2.set_xlabel("Mean photon number $|\\alpha|^2$", size = fontsize, color = "black")

axK2.tick_params(axis="x", labelsize=fontsize)
axK2.tick_params(axis="y", labelsize=fontsize)

axK2.plot(meanphoton, errorM10, color='salmon',  linestyle=linestyles['solid'], linewidth=1)
axK2.plot(meanphoton, errorM4, color='green',  linestyle=linestyles['solid'], linewidth=1)
axK2.set_ylim([0.00005,0.05])
axK2.set_yscale('log')

axK2.grid(color='black',linestyle='-', linewidth=0.2)
axK2.set_xlim([0,7.25])
# axK2.set_ylim([-1,2])



plt.show()

