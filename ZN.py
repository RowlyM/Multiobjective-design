# -*- coding: utf-8 -*-
def ZN(A,B,C,kp):
    def ZNsettings(w):
        out = [-(w[0]**2) + B, (-A*(w[0]**2) + C +(kp*w[1]))]
        return out

    from scipy.optimize import fsolve
    tr = fsolve(ZNsettings,[1,10])
    Pu = 2*3.141/tr[0]
    kczn =tr[1]/2.2
    tizn = Pu/1.2
    return kczn,tizn

    
    
    

