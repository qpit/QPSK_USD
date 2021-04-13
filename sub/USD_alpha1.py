import numpy as np

def alpha1_success_error (M, trysim, mean0, mean1, mean2):
    suc1 = 0
    error1 = 0
    for trial in np.arange(trysim):
        a = 0
        m0 = 0
        m1 = 0
        m2 = 0
        m3 = 0

        photon = np.random.poisson(mean1, 1)
        if (photon != 0):
            m0 = 1
            a = 2
        photon = np.random.poisson(mean1, 1)
        if (photon != 0):
            m2 = 1
            if (a == 2):
                a = 1
        photon = np.random.poisson(mean0, 1)
        if (photon != 0):
            m1 = 1
            if (a == 1):
                a = 3
        photon = np.random.poisson(mean2, 1)
        if (photon != 0):
            m3 = 1
        # M-4 stages
        for stage in np.arange(M - 4):
            if (m0 == 0 and m1 == 0 and m2 == 0 and m3 == 0):
                if (a == 0):
                    photon = np.random.poisson(mean1, 1)
                    a = 2
                    if (photon != 0):
                        m0 = 1
                elif (a == 2):
                    photon = np.random.poisson(mean1, 1)
                    a = 1
                    if (photon != 0):
                        m2 = 1
                elif (a == 1):
                    photon = np.random.poisson(mean0, 1)
                    a = 3
                    if (photon != 0):
                        m1 = 1
                elif (a == 3):
                    photon = np.random.poisson(mean2, 1)
                    a = 0
                    if (photon != 0):
                        m3 = 1

            elif (m0 == 0 and m1 == 0 and m2 == 0 and m3 == 1):
                if (a == 0):
                    photon = np.random.poisson(mean1, 1)
                    a = 2
                    if (photon != 0):
                        m0 = 1
                elif (a == 2):
                    photon = np.random.poisson(mean1, 1)
                    a = 1
                    if (photon != 0):
                        m2 = 1
                elif (a == 1):
                    photon = np.random.poisson(mean0, 1)
                    a = 0
                    if (photon != 0):
                        m1 = 1

            elif (m0 == 0 and m1 == 0 and m2 == 1 and m3 == 0):
                if (a == 0):
                    photon = np.random.poisson(mean1, 1)
                    a = 1
                    if (photon != 0):
                        m0 = 1
                elif (a == 1):
                    photon = np.random.poisson(mean0, 1)
                    a = 3
                    if (photon != 0):
                        m1 = 1
                elif (a == 3):
                    photon = np.random.poisson(mean2, 1)
                    a = 0
                    if (photon != 0):
                        m3 = 1

            elif (m0 == 0 and m1 == 1 and m2 == 0 and m3 == 0):
                if (a == 0):
                    photon = np.random.poisson(mean1, 1)
                    a = 2
                    if (photon != 0):
                        m0 = 1
                elif (a == 2):
                    photon = np.random.poisson(mean1, 1)
                    a = 3
                    if (photon != 0):
                        m2 = 1
                elif (a == 3):
                    photon = np.random.poisson(mean2, 1)
                    a = 0
                    if (photon != 0):
                        m3 = 1

            elif (m0 == 1 and m1 == 0 and m2 == 0 and m3 == 0):
                if (a == 2):
                    photon = np.random.poisson(mean1, 1)
                    a = 1
                    if (photon != 0):
                        m2 = 1
                elif (a == 1):
                    photon = np.random.poisson(mean0, 1)
                    a = 3
                    if (photon != 0):
                        m1 = 1
                elif (a == 3):
                    photon = np.random.poisson(mean2, 1)
                    a = 2
                    if (photon != 0):
                        m3 = 1

            elif (m0 == 0 and m1 == 1 and m2 == 0 and m3 == 1):
                if (a == 0):
                    photon = np.random.poisson(mean1, 1)
                    a = 2
                    if (photon != 0):
                        m0 = 1
                elif (a == 2):
                    photon = np.random.poisson(mean1, 1)
                    a = 0
                    if (photon != 0):
                        m2 = 1

            elif (m0 == 0 and m1 == 0 and m2 == 1 and m3 == 1):
                if (a == 0):
                    photon = np.random.poisson(mean1, 1)
                    a = 1
                    if (photon != 0):
                        m0 = 1
                elif (a == 1):
                    photon = np.random.poisson(mean0, 1)
                    a = 0
                    if (photon != 0):
                        m1 = 1

            elif (m0 == 1 and m1 == 0 and m2 == 0 and m3 == 1):
                if (a == 2):
                    photon = np.random.poisson(mean1, 1)
                    a = 1
                    if (photon != 0):
                        m2 = 1
                elif (a == 1):
                    photon = np.random.poisson(mean0, 1)
                    a = 2
                    if (photon != 0):
                        m1 = 1

            elif (m0 == 0 and m1 == 1 and m2 == 1 and m3 == 0):
                if (a == 0):
                    photon = np.random.poisson(mean1, 1)
                    a = 3
                    if (photon != 0):
                        m0 = 1
                elif (a == 3):
                    photon = np.random.poisson(mean2, 1)
                    a = 0
                    if (photon != 0):
                        m3 = 1

            elif (m0 == 1 and m1 == 0 and m2 == 1 and m3 == 0):
                if (a == 1):
                    photon = np.random.poisson(mean0, 1)
                    a = 3
                    if (photon != 0):
                        m1 = 1
                elif (a == 3):
                    photon = np.random.poisson(mean2, 1)
                    a = 1
                    if (photon != 0):
                        m3 = 1

            elif (m0 == 1 and m1 == 1 and m2 == 0 and m3 == 0):
                if (a == 2):
                    photon = np.random.poisson(mean1, 1)
                    a = 3
                    if (photon != 0):
                        m2 = 1
                elif (a == 3):
                    photon = np.random.poisson(mean2, 1)
                    a = 2
                    if (photon != 0):
                        m3 = 1

            elif (m0 == 0 and m1 == 1 and m2 == 1 and m3 == 1):
                photon = np.random.poisson(mean1, 1)
                if (photon != 0):
                    m0 = 1
            elif (m0 == 1 and m1 == 0 and m2 == 1 and m3 == 1):
                photon = np.random.poisson(mean0, 1)
                if (photon != 0):
                    m1 = 1
            elif (m0 == 1 and m1 == 1 and m2 == 0 and m3 == 1):
                photon = np.random.poisson(mean1, 1)
                if (photon != 0):
                    m2 = 1
            elif (m0 == 1 and m1 == 1 and m2 == 1 and m3 == 0):
                photon = np.random.poisson(mean2, 1)
                if (photon != 0):
                    m3 = 1

        if (m0 == 0 and m1 == 1 and m2 == 1 and m3 == 1):
            error1 = error1 + 1
        elif (m0 == 1 and m1 == 0 and m2 == 1 and m3 == 1):
            suc1 = suc1 + 1
        elif (m0 == 1 and m1 == 1 and m2 == 0 and m3 == 1):
            error1 = error1 + 1
        elif (m0 == 1 and m1 == 1 and m2 == 1 and m3 == 0):
            error1 = error1 + 1

    return suc1, error1

