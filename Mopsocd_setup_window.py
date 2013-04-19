# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:52:27 2013

@author: Rowly
"""

import Tkinter as tk
import numpy as np
def cc():
    
    Nparticles = []
    archivesize = []
    maxgen = []
    kc_range = []
    ti_range = []
    td_range = []
    Xobjective = []
    Yobjective = []
    class Optimizer_setup(tk.Canvas):
        def __init__(self, master = None):
            tk.Canvas.__init__(self, master)
            self.grid(ipadx =70, ipady=100)
            self.Nparticles()
            self.Archivesize()
            self.Maxgen()
            self.Para_kc_range()
            self.Para_ti_range()
            self.Para_td_range()
            self.Drop()
            self.Drop2()
            self.Run()
            self.Close()
            self.create_text((40,68),activefill="red",text="Nparticles",fill="black")
            self.create_text((40,98),activefill="red",text="Archivesize",fill="black")
            self.create_text((40,128),activefill="red",text="Maxgen",fill="black")
            self.create_text((40,158),activefill="red",text="kc range",fill="black")
            self.create_text((40,188),activefill="red",text="ti range",fill="black")
            self.create_text((40,218),activefill="red",text="td range",fill="black")
            self.create_text((110,30),activefill="red",text="MOPSO-cd PARAMETERS",fill="black")
            self.create_text((400,30),activefill="red",text="OBJECTIVES",fill="black")
            self.create_text((300,98),activefill="red",text="X axis objective",fill="black")
            self.create_text((300,158),activefill="red",text="Y axis objective",fill="black")
            
        def Nparticles(self):
            self.Nentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.Nentry.place(x= 100, y = 60)
            self.Nentry.insert(0,"100")
            
        def Archivesize(self):
            self.Archentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.Archentry.place(x= 100, y = 90)
            self.Archentry.insert(0,"50")
            
        def Maxgen(self):
            self.Maxentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.Maxentry.place(x= 100, y = 120)
            self.Maxentry.insert(0,"100")
            
        def Para_kc_range(self):
            self.kcentry= tk.Entry(self,width = 10,justify = tk.CENTER)
            self.kcentry.place(x= 100, y = 150)
            self.kcentry.insert(0,"0.1,40")
            
        def Para_ti_range(self):
            self.tientry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tientry.place(x= 100, y = 180)
            self.tientry.insert(0,"0.1,80")
            
        def Para_td_range(self):
            self.tdentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tdentry.place(x= 100, y = 210)
            self.tdentry.insert(0,"0,10")
            
        def Get_entries(self):
            self.quit()
            Nparticles.append( eval(self.Nentry.get()))
            archivesize.append( eval(self.Archentry.get()))
            maxgen.append( eval(self.Maxentry.get()))
            kc_range.append( eval(self.kcentry.get()))
            ti_range.append( eval(self.tientry.get()))
            td_range.append( eval(self.tdentry.get()))
            Xobjective.append(self.varx.get())
            Yobjective.append(self.vary.get())
#            self.quit()
        def Drop(self):
            optionList = ('Risetime', 'Overshoot ratio', 'ISE', 'IAE', 'ITAE')
            self.varx = tk.StringVar()
            self.varx.set(optionList[0])
            self.Xobj = tk.OptionMenu(self,self.varx,*optionList)
            self.Xobj.place(x= 400, y = 85)
        def Drop2(self):
            optionList = ('Risetime', 'Overshoot ratio', 'ISE', 'IAE', 'ITAE')
            self.vary = tk.StringVar()
            self.vary.set(optionList[1])
            self.Yobj = tk.OptionMenu(self,self.vary,*optionList)
            self.Yobj.place(x= 400, y = 145)
        def Run(self):
            self.runb= tk.Button(self, width = 10,text ='Run', command = self.Get_entries)
            self.runb.place(x= 390, y = 250)
            
        def Close(self):
            self.quitb = tk.Button(self, width = 10,text ='Cancel', command = self.quit)
            self.quitb.place(x= 290, y = 250)    
            
                 
    window = Optimizer_setup()
    
    window.mainloop()     
    return   Nparticles, archivesize, maxgen, kc_range, ti_range, td_range ,Xobjective, Yobjective 