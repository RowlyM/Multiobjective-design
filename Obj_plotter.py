# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 01:59:46 2013

@author: Rowly
"""
import matplotlib.pyplot as plt 

def obj_redrawer(fig,ppor, ptr, pise, piae, pitae, xobj, yobj, Mop_points,por, tr, ISE, IAE, ITAE):
    
    
###################################Risetime as Y objective #############################################     
    if (xobj == 'RT') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(tr, tr, 'wo',picker = 5,)
        ax3.plot(Mop_points[1],Mop_points[1],'ro')
        ax3.plot(ptr, ptr, 'bo-')
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'RT'):
        
        ax3= fig.add_subplot(233)
        pline = ax3.plot(por, tr, 'wo',picker = 5,)
        ax3.plot(Mop_points[0],Mop_points[1],'ro')
        ax3.plot(ppor, ptr, 'bo-')
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ISE, tr, 'wo',picker = 5,)
        ax3.plot(Mop_points[2],Mop_points[1],'ro')
        ax3.plot(pise, ptr, 'bo-')
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(IAE, tr, 'wo',picker = 5,)
        ax3.plot(Mop_points[3],Mop_points[1],'ro')
        ax3.plot(piae, ptr, 'bo-')
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'RT'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ITAE, tr, 'wo',picker = 5,)
        ax3.plot(Mop_points[4],Mop_points[1],'ro')
        ax3.plot(pitae, ptr, 'bo-')
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')
        
###################################Overshoot ratio as Y objective ############################################# 
      
    elif (xobj == 'RT') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(tr, por, 'wo',picker = 5,)
        ax3.plot(Mop_points[1],Mop_points[0],'ro')
        ax3.plot(ptr, ppor, 'bo-')
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'OSR'):
        
        ax3= fig.add_subplot(233)
        pline = ax3.plot(por, por, 'wo',picker = 5,)
        ax3.plot(Mop_points[0],Mop_points[0],'ro')
        ax3.plot(ppor, ppor, 'bo-')
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ISE, por, 'wo',picker = 5,)
        ax3.plot(Mop_points[2],Mop_points[0],'ro')
        ax3.plot(pise, ppor, 'bo-')
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(IAE, por, 'wo',picker = 5,)
        ax3.plot(Mop_points[3],Mop_points[0],'ro')
        ax3.plot(piae, ppor, 'bo-')
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'OSR'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ITAE, por, 'wo',picker = 5,)
        ax3.plot(Mop_points[4],Mop_points[0],'ro')
        ax3.plot(pitae,ppor, 'bo-')
        plt.ylabel('overshoot ratio',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')  
        
        
################################### ISE as Y objective ############################################# 
      
    elif (xobj == 'RT') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(tr, ISE, 'wo',picker = 5,)
        ax3.plot(Mop_points[1],Mop_points[2],'ro')
        ax3.plot(ptr, pise, 'bo-')
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'ISE'):
        
        ax3= fig.add_subplot(233)
        pline = ax3.plot(por, ISE, 'wo',picker = 5,)
        ax3.plot(Mop_points[0],Mop_points[2],'ro')
        ax3.plot(ppor, pise, 'bo-')
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ISE, ISE, 'wo',picker = 5,)
        ax3.plot(Mop_points[2],Mop_points[2],'ro')
        ax3.plot(pise, pise, 'bo-')
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(IAE, ISE, 'wo',picker = 5,)
        ax3.plot(Mop_points[3],Mop_points[2],'ro')
        ax3.plot(piae, pise, 'bo-')
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'ISE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ITAE, ISE, 'wo',picker = 5,)
        ax3.plot(Mop_points[4],Mop_points[2],'ro')
        ax3.plot(pitae, pise, 'bo-')
        plt.ylabel('ISE',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')   
        
 ################################### IAE as Y objective ############################################# 
      
    elif (xobj == 'RT') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(tr, IAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[1],Mop_points[3],'ro')
        ax3.plot(ptr, piae, 'bo-')
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'IAE'):
        
        ax3= fig.add_subplot(233)
        pline = ax3.plot(por, IAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[0],Mop_points[3],'ro')
        ax3.plot(ppor, piae, 'bo-')
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ISE, IAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[2],Mop_points[3],'ro')
        ax3.plot(pise, piae, 'bo-')
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(IAE, IAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[3],Mop_points[3],'ro')
        ax3.plot(piae, piae, 'bo-')
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'IAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ITAE, IAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[4],Mop_points[3],'ro')
        ax3.plot(pitae, piae, 'bo-')
        plt.ylabel('IAE',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')   
        
 ################################### ITAE as Y objective ############################################# 
      
    elif (xobj == 'RT') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(tr, ITAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[1],Mop_points[4],'ro')
        ax3.plot(ptr, pitae, 'bo-')
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('risetime (s)',fontsize = 'large')
    
    elif (xobj == 'OSR') & (yobj == 'ITAE'):
        
        ax3= fig.add_subplot(233)
        pline = ax3.plot(por, ITAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[0],Mop_points[4],'ro')
        ax3.plot(ppor, pitae, 'bo-')
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        
    elif (xobj == 'ISE') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ISE, ITAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[2],Mop_points[4],'ro')
        ax3.plot(pise, pitae, 'bo-')
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('ISE',fontsize = 'large')
        
    elif (xobj == 'IAE') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(IAE, ITAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[3],Mop_points[4],'ro')
        ax3.plot(piae, pitae, 'bo-')
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('IAE',fontsize = 'large')    
        
    elif (xobj == 'ITAE') & (yobj == 'ITAE'):
        ax3= fig.add_subplot(233)
        pline = ax3.plot(ITAE, ITAE, 'wo',picker = 5,)
        ax3.plot(Mop_points[4],Mop_points[4],'ro')
        ax3.plot(pitae, pitae, 'bo-')
        plt.ylabel('ITAE',fontsize = 'large')
        plt.xlabel('ITAE',fontsize = 'large')           