# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:52:27 2013

@author: Rowly
"""

import Tkinter as tk
import numpy as np
import tkFont
def cc():
    
    class Optimizer_setup(tk.Canvas):
        def __init__(self, master = None):
            tk.Canvas.__init__(self, master)
            self.grid(ipadx =70, ipady=30)
            self.Nparticles()
            self.Archivesize()
            self.Maxgen()
            self.pMut()
            self.printinter()
            self.Para_kc_Lrange()
            self.Para_ti_Lrange()
            self.Para_td_Lrange()
            self.Para_kc_Hrange()
            self.Para_ti_Hrange()
            self.Para_td_Hrange()
            self.Drop()
            self.Run()
            self.Close()
            self.create_text((40,68),activefill="red",text="Nparticles",fill="black")
            self.create_text((40,98),activefill="red",text="Archivesize",fill="black")
            self.create_text((40,128),activefill="red",text="Maxgen",fill="black")
            self.create_text((350,68),activefill="red",text="kc min.",fill="black")
            self.create_text((350,98),activefill="red",text="kc max.",fill="black")
            self.create_text((350,128),activefill="red",text="ti min.",fill="black")
            self.create_text((350,158),activefill="red",text="ti max.",fill="black")
            self.create_text((350,188),activefill="red",text="td min.",fill="black")
            self.create_text((350,218),activefill="red",text="td max.",fill="black")
            self.create_text((40,158),activefill="red",text="pMut",fill="black")
            self.create_text((40,188),activefill="red",text="printinterval",fill="black")
            self.create_text((42,218),activefill="red",text="rememberevals",fill="black")
            self.create_text((110,30),activefill="red",text="MOPSO-cd PARAMETERS",font =tkFont.Font(weight = 'bold') )
    #            self.create_text((400,30),activefill="red",text="OBJECTIVES",font =tkFont.Font(weight = 'bold') )
            self.create_text((400,30),activefill="red",text="Controller Para. range",font =tkFont.Font(weight = 'bold') )
    #        self.create_text((300,98),activefill="red",text="X axis objective",fill="black")
    #        self.create_text((300,158),activefill="red",text="Y axis objective",fill="black")
    ######################## MOPSO-cd Parameters ############################################            
        def Nparticles(self):
            self.Nentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.Nentry.place(x= 100, y = 60)
            self.Nentry.insert(0,"50")
            
        def Archivesize(self):
            self.Archentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.Archentry.place(x= 100, y = 90)
            self.Archentry.insert(0,"50")
            
        def Maxgen(self):
            self.Maxentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.Maxentry.place(x= 100, y = 120)
            self.Maxentry.insert(0,"50")
            
        def pMut(self):
            self.pMutentry= tk.Entry(self,width = 10,justify = tk.CENTER)
            self.pMutentry.place(x= 100, y = 150)
            self.pMutentry.insert(0,"0.01")
            
        def printinter(self):
            self.printinter_entry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.printinter_entry.place(x= 100, y = 180)
            self.printinter_entry.insert(0,"1")
            
        def Drop(self):
            optionList = ('True', 'False')
            self.varx = tk.StringVar()
            self.varx.set(optionList[0])
            self.Xobj = tk.OptionMenu(self,self.varx,*optionList)
            self.Xobj.place(x= 100, y = 210)
            
    ######################## Controller parameter range #####################################            
        def Para_kc_Lrange(self):
            self.kcLentry= tk.Entry(self,width = 10,justify = tk.CENTER)
            self.kcLentry.place(x= 400, y = 60)
            self.kcLentry.insert(0,"0.1")
            
        def Para_kc_Hrange(self):
            self.kcHentry= tk.Entry(self,width = 10,justify = tk.CENTER)
            self.kcHentry.place(x= 400, y = 90)
            self.kcHentry.insert(0,"40")
            
        def Para_ti_Lrange(self):
            self.tiLentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tiLentry.place(x= 400, y = 120)
            self.tiLentry.insert(0,"0.1")
            
        def Para_ti_Hrange(self):
            self.tiHentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tiHentry.place(x= 400, y = 150)
            self.tiHentry.insert(0,"80")
            
        def Para_td_Lrange(self):
            self.tdLentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tdLentry.place(x= 400, y = 180)
            self.tdLentry.insert(0,"0")
            
        def Para_td_Hrange(self):
            self.tdHentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tdHentry.place(x= 400, y = 210)
            self.tdHentry.insert(0,"10")    
            
        def Get_entries(self):
            self.quit()
            global Nparticles, archivesize, maxgen, pMut, rememberevals, printinterval
            global kc_range, ti_range, td_range
            Nparticles =  eval(self.Nentry.get())
            archivesize =  eval(self.Archentry.get())
            maxgen = eval(self.Maxentry.get())
            pMut = eval(self.pMutentry.get())
            rememberevals =  self.varx.get()
            printinterval = eval(self.printinter_entry.get())
            kc_range =  [eval(self.kcLentry.get()), eval(self.kcHentry.get())] 
            ti_range = [eval(self.tiLentry.get()),eval(self.tiHentry.get())]
            td_range =  [eval(self.tdLentry.get()), eval(self.tdHentry.get())]
#            print Nparticles, archivesize, maxgen, pMut, rememberevals, printinterval, kc_range, ti_range, td_range
    #        def Drop(self):
    #            optionList = ('Risetime', 'Overshoot ratio', 'ISE', 'IAE', 'ITAE')
    #            self.varx = tk.StringVar()
    #            self.varx.set(optionList[0])
    #            self.Xobj = tk.OptionMenu(self,self.varx,*optionList)
    #            self.Xobj.place(x= 360, y = 85)
    #        def Drop2(self):
    #            optionList = ('Risetime', 'Overshoot ratio', 'ISE', 'IAE', 'ITAE')
    #            self.vary = tk.StringVar()
    #            self.vary.set(optionList[1])
    #            self.Yobj = tk.OptionMenu(self,self.vary,*optionList)
    #            self.Yobj.place(x= 360, y = 145)
        def Run(self):
            self.runb= tk.Button(self, width = 10,text ='Run', command = self.Get_entries)
            self.runb.place(x= 390, y = 290)
            
        def Close(self):
            self.quitb = tk.Button(self, width = 10,text ='Cancel', command = self.quit)
            self.quitb.place(x= 290, y = 290)    
        
             
    window = Optimizer_setup()
    window.master.title('Mopso-cd setup')
    window.mainloop()    
    return   Nparticles, archivesize, maxgen, pMut, rememberevals, printinterval, kc_range, ti_range, td_range 