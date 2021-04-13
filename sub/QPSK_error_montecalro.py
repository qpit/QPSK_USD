import numpy as np
from sub import USD_alpha0
from sub import USD_alpha1
from sub import USD_alpha2
from sub import USD_alpha3

def errorM(M,eta,visibility,dark,trysim,meanphotonmax):
    Error=[]
    Success=[]
    meanphoton=[]
    # for m in np.arange(0.01, meanphotonmax, 0.01):
    for m in [0.10000000000000001, 0.20000000000000001,0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25]:
        n=m*eta
        mean0 = dark / M + 2 * n * (1 - visibility) / M
        mean1 = dark / M + 2 * n / M
        mean2 = dark / M + 2 * n * (1 + visibility) / M

        suc0, error0=USD_alpha0.alpha0_success_error(M, trysim, mean0, mean1, mean2)
        suc1, error1=USD_alpha1.alpha1_success_error(M, trysim, mean0, mean1, mean2)
        suc2, error2=USD_alpha2.alpha2_success_error(M, trysim, mean0, mean1, mean2)
        suc3, error3=USD_alpha3.alpha3_success_error(M, trysim, mean0, mean1, mean2)


        suc=(suc0/trysim+suc1/trysim+suc2/trysim+suc3/trysim)/float(4)
        print(suc0)
        Success+=[suc]
        error=(error0/trysim+error1/trysim+error2/trysim+error3/trysim)/float(4)
        if (error !=0 and suc !=0):
            error=error/float(error+suc)
        else:
            error=1

        Error+=[error]
        meanphoton+=[m]
    return meanphoton,Error,Success
