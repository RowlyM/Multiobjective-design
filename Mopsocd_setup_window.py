# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:52:27 2013

@author: Rowly Mudzhiba
"""

import Tkinter as tk
import numpy as np
import tkFont
import platform

def cc():
    
    class Optimizer_setup_windows(tk.Canvas):
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
            self.create_text((40,68),text="Nparticles",fill="black")
            self.create_text((40,98),text="Archivesize",fill="black")
            self.create_text((40,128),text="Maxgen",fill="black")
            self.create_text((350,68),text="kc min.",fill="black")
            self.create_text((350,98),text="kc max.",fill="black")
            self.create_text((350,128),text="ti min.",fill="black")
            self.create_text((350,158),text="ti max.",fill="black")
            self.create_text((350,188),text="td min.",fill="black")
            self.create_text((350,218),text="td max.",fill="black")
            self.create_text((40,158),text="pMut",fill="black")
            self.create_text((40,188),text="printinterval",fill="black")
            self.create_text((42,218),text="rememberevals",fill="black")
            self.create_text((110,30),text="MOPSO-cd Parameters",font =tkFont.Font(weight = 'bold') )
            self.create_text((400,30),text="Controller Para. range",font =tkFont.Font(weight = 'bold') )
    
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
            self.kcHentry.insert(0,"60")
            
        def Para_ti_Lrange(self):
            self.tiLentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tiLentry.place(x= 400, y = 120)
            self.tiLentry.insert(0,"0.1")
            
        def Para_ti_Hrange(self):
            self.tiHentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tiHentry.place(x= 400, y = 150)
            self.tiHentry.insert(0,"60")
            
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
    
        def Run(self):
            self.runb= tk.Button(self, width = 10,text ='Run', command = self.Get_entries)
            self.runb.place(x= 390, y = 290)
            
        def Close(self):
            self.quitb = tk.Button(self, width = 10,text ='Cancel', command = self.quit)
            self.quitb.place(x= 290, y = 290)    
            

    class Optimizer_setup_Linux(tk.Toplevel):
        def __init__(self, master = None):
            tk.Toplevel.__init__(self, master, height = 330, width = 500)

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
            
            self.text = tk.Label(self, text="MOPSO-cd Parameters",font =tkFont.Font(weight = 'bold'))
            self.text.place(x=10, y=30)
            
            self.text = tk.Label(self, text="Controller Para. range",font=tkFont.Font(weight='bold'))
            self.text.place(x=300, y=30)
            
            self.text = tk.Label(self, text="Nparticles")
            self.text.place(x=10, y=60)
            
            self.text = tk.Label(self, text="Archivesize")
            self.text.place(x=10, y=90)
            
            self.text = tk.Label(self, text="Maxgen")
            self.text.place(x=10, y=120)
            
            self.text = tk.Label(self, text="pMut")
            self.text.place(x=10, y=150)
            
            self.text = tk.Label(self, text="printinterval")
            self.text.place(x= 10, y = 180)
            
            self.text = tk.Label(self,text="rememberevals")
            self.text.place(x=10, y=225)
            
            self.text = tk.Label(self, text="kc min.")
            self.text.place(x=330, y=60)
            
            self.text = tk.Label(self, text="kc max.")
            self.text.place(x=330, y=90)

            self.text = tk.Label(self, text="ti min.")
            self.text.place(x=330, y=120)
            
            self.text = tk.Label(self, text="ti max.")
            self.text.place(x=330, y=150)
            
            self.text = tk.Label(self, text="td min.")
            self.text.place(x=330, y=180)
            
            self.text = tk.Label(self, text="td max.")
            self.text.place(x=330, y=210)              
    
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
            self.kcHentry.insert(0,"60")
            
        def Para_ti_Lrange(self):
            self.tiLentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tiLentry.place(x= 400, y = 120)
            self.tiLentry.insert(0,"0.1")
            
        def Para_ti_Hrange(self):
            self.tiHentry = tk.Entry(self,width = 10,justify = tk.CENTER)
            self.tiHentry.place(x= 400, y = 150)
            self.tiHentry.insert(0,"60")
            
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
    
        def Run(self):
            self.runb= tk.Button(self, width = 10,text ='Run', command = self.Get_entries)
            self.runb.place(x= 390, y = 290)
            
        def Close(self):
            self.quitb = tk.Button(self, width = 10,text ='Cancel', command = self.quit)
            self.quitb.place(x= 290, y = 290)    
        
    OS = platform.system()
    if OS == "Windows":
        window = Optimizer_setup_windows()
    else:
        window = Optimizer_setup_Linux()
        
    window.master.title('Mopso-cd setup')
    window.mainloop()    
    return   Nparticles, archivesize, maxgen, pMut, rememberevals, printinterval, kc_range, ti_range, td_range 