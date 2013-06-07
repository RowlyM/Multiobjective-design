# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 01:59:46 2013

@author: Rowly Mudzhiba
"""
import matplotlib.pyplot as plt 

def obj_redrawer(fig,ppor, ptr, pise, piae, pitae, xobj, yobj, Mop_points,por, tr, ISE, IAE, ITAE,gen_ppor, gen_ptr, gen_pise, gen_piae, gen_pitae, gen_por, gen_tr, gen_ise, gen_iae, gen_itae):
    
    
################## Risetime as Y objective #####################     
    if (xobj == 'RT') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        line11, = ax3.plot(Mop_points[1],Mop_points[1],'ro')
        ax3.plot(ptr, ptr, 'bo-')
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'RT'):

        ax3= fig.add_subplot(233)
        ax3.cla()
        line11,= ax3.plot(Mop_points[0],Mop_points[1],'ro', label = "MOPSO-cd", picker=5)
        line12,= ax3.plot(ppor, ptr, 'go', label = "User", picker=5)
        line13,= ax3.plot(gen_ppor, gen_ptr, 'bo', label = "Brute Force", picker=5)
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
        
    elif (xobj == 'ISE') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        ax3.cla()
        line11,= ax3.plot(Mop_points[2],Mop_points[1],'ro', label = "MOPSO-cd")
        line12,= ax3.plot(gen_pise, gen_ptr, 'bo', label = "User")
        line13,= ax3.plot(pise, ptr, 'go', label = "Brute Force")
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        line11,= ax3.plot(Mop_points[3],Mop_points[1],'ro', label = "MOPSO-cd")
        line12,= ax3.plot(gen_piae, gen_ptr, 'bo', label = "User")
        line13,= ax3.plot(piae, ptr, 'go')
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[4],Mop_points[1],'ro', label = "MOPSO-cd")
        ax3.plot(gen_pitae, gen_ptr, 'bo', label = "User")
        ax3.plot(pitae, ptr, 'go', label = "Brute Force")
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')
        
###############Overshoot ratio as Y objective ################## 
      
    elif (xobj == 'RT') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[1],Mop_points[0],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ptr, gen_ppor, 'bo', label = "Brute Force")
        ax3.plot(ptr, ppor, 'go', label = "User")
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'OSR'):
        
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[0],Mop_points[0],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ppor, gen_ppor, 'bo', label = "Brute Force")
        ax3.plot(ppor, ppor, 'go', label = "User")
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[2],Mop_points[0],'ro', label = "MOPSO-cd")
        ax3.plot(gen_pise, gen_ppor, 'bo', label = "Brute Force")
        ax3.plot(pise, ppor, 'go', label = "User")
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[3],Mop_points[0],'ro', label = "MOPSO-cd")
        ax3.plot(gen_piae, gen_ppor, 'bo', label = "Brute Force")
        ax3.plot(piae, ppor, 'go', label = "User")
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[4],Mop_points[0],'ro', label = "MOPSO-cd")
        ax3.plot(gen_piae, gen_ppor, 'bo', label = "Brute Force")
        ax3.plot(pitae,ppor, 'go', label = "User")
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')  
        
        
############## ISE as Y objective ##################### 
      
    elif (xobj == 'RT') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[1],Mop_points[2],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ptr, gen_pise, 'bo', label = "Brute Force")
        ax3.plot(ptr, pise, 'go', label = "User")
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'ISE'):
        
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[0],Mop_points[2],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ppor, gen_pise, 'bo', label = "Brute Force")
        ax3.plot(ppor, pise, 'go', label = "User")
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[2],Mop_points[2],'ro', label = "MOPSO-cd")
        ax3.plot(gen_pise, gen_pise, 'bo', label = "Brute Force")
        ax3.plot(pise, pise, 'go', label = "User")
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[3],Mop_points[2],'ro', label = "MOPSO-cd")
        ax3.plot(gen_piae, gen_pise, 'bo', label = "Brute Force")
        ax3.plot(piae, pise, 'go', label = "User")
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[4],Mop_points[2],'ro', label = "MOPSO-cd")
        ax3.plot(gen_piae, gen_pise, 'bo', label = "Brute Force")
        ax3.plot(pitae, pise, 'go', label = "User")
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')   
        
 ################### IAE as Y objective ##################### 
      
    elif (xobj == 'RT') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[1],Mop_points[3],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ptr, gen_piae, 'bo', label = "Brute Force")
        ax3.plot(ptr, piae, 'go', label = "User")
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'IAE'):
        
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[0],Mop_points[3],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ppor, gen_piae, 'bo', label = "Brute Force")
        ax3.plot(ppor, piae, 'go', label = "User")
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[2],Mop_points[3],'ro', label = "MOPSO-cd")
        ax3.plot(gen_pise, gen_piae, 'bo', label = "Brute Force")
        ax3.plot(pise, piae, 'go', label = "User")
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[3],Mop_points[3],'ro', label = "MOPSO-cd")
        ax3.plot(gen_piae, gen_piae, 'bo', label = "Brute Force")
        ax3.plot(piae, piae, 'go', label = "User")
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[4],Mop_points[3],'ro', label = "MOPSO-cd")
        ax3.plot(gen_pitae, gen_piae, 'bo', label = "Brute Force")
        ax3.plot(pitae, piae, 'go', label = "User")
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')   
        
 ################## ITAE as Y objective ########################### 
      
    elif (xobj == 'RT') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[1],Mop_points[4],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ptr, gen_pitae, 'bo', label = "Brute Force")
        ax3.plot(ptr, pitae, 'go', label = "User")
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'ITAE'):
        
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[0],Mop_points[4],'ro', label = "MOPSO-cd")
        ax3.plot(gen_ppor, gen_pitae, 'bo', label = "Brute Force")
        ax3.plot(ppor, pitae, 'go', label = "User")
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[2],Mop_points[4],'ro', label = "MOPSO-cd")
        ax3.plot(gen_pise, gen_pitae, 'bo', label = "Brute Force")
        ax3.plot(pise, pitae, 'go', label = "User")
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[3],Mop_points[4],'ro', label = "MOPSO-cd")
        ax3.plot(gen_piae, gen_pitae, 'bo', label = "Brute Force")
        ax3.plot(piae, pitae, 'go', label = "User")
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        ax3.cla()

        ax3.plot(Mop_points[4],Mop_points[4],'ro', label = "MOPSO-cd")
        ax3.plot(gen_pitae, gen_pitae, 'bo', label = "Brute Force")
        ax3.plot(pitae, pitae, 'go', label = "User")
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')   
        
    plt.legend( loc = 1) 
    return line11, line12, line13
