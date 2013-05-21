# -*- coding: utf-8 -*-
"""
Created on Sat Feb 09 11:56:47 2013

@author: Rowly
"""
#import Tkinter as tk
#import tkFont
import Tkinter as tk

#def sys_setup():
#    
#    wind = tk.Toplevel()
#    wind.title('new window')
#    
#    Gpn = tk.Entry(wind, width=20, justify=tk.CENTER)
#    Gpn.place(x=220, y=60)
#    Gpn.insert(0, "0.125")
#    
#    Gpd = tk.Entry(wind, width=20, justify=tk.CENTER)
#    Gpd.place(x=220, y=90)
#    Gpd.insert(0, "1 3 3 1")
#    
#    Tsim = tk.Entry(wind, width=10, justify=tk.CENTER)
#    Tsim.place(x=100, y=160)
#    Tsim.insert(0, "100")
#    
#
#    Tinc = tk.Entry(wind, width=10, justify=tk.CENTER)
#    Tinc.place(x=100, y=190)
#    Tinc.insert(0, "0.1")
#
#    dt = tk.Entry(wind, width=10, justify=tk.CENTER)
#    dt.place(x=100, y=220)
#    dt.insert(0, "0")
#
#
#    sp = tk.Entry(wind, width=10, justify=tk.CENTER)
#    sp.place(x=400, y=160)
#    sp.insert(0, "1")
#
#
#    st = tk.Entry(wind, width=10, justify=tk.CENTER)
#    st.place(x=400, y=190)
#    st.insert(0, "0")
#
#
#    rt = tk.Entry(wind, width=10, justify=tk.CENTER)
#    rt.place(x=400, y=220)
#    rt.insert(0, "10")
#    
#    optionList = ('Step', 'Ramp')
#    inputvar = tk.StringVar()
#    inputvar.set(optionList[0])
#    SPinput = tk.OptionMenu(wind, inputvar, *optionList)
#    SPinput.place(x=400, y=260)
#    
#    def Get_entries():
#        global GPn, Gpd, tfinal, dt, DT, SP, step_time, ramp_time, SP_input
#        wind.quit()
#        GPn = [float(s) for s in Gpn.get().split()]
#        
#        Gpd = [float(s) for s in Gpd.get().split()]
#        print Gpd
#        tfinal = [float(s) for s in Tsim.get().split()][0]
#        dt = [float(s) for s in Tinc.get().split()][0]
#        DT = [float(s) for s in dt.get().split()][0]
#        SP = [float(s) for s in sp.get().split()][0]
#        step_time = [float(s) for s in st.get().split()][0]
#        ramp_time = [float(s) for s in rt.get().split()][0]
#        SP_input = inputvar.get()
#
#    def Get_entries2():
#        global GPn, Gpd, tfinal, dt, DT, SP, step_time, ramp_time, SP_input
#        GPn = (eval(Gpn.get()))
#        Gpd = (eval(self.Gpd.get()))
#        tfinal = (eval(self.Tsim.get()))
#        dt = (eval(self.Tinc.get()))
#        DT = (eval(self.dt.get()))
#        SP = (eval(self.sp.get()))
#        step_time = (self.st.get())
#        ramp_time = (self.rt.get())
#        SP_input = (self.inputvar.get())
#        self.quit()
#
#
#
#
#    okb = tk.Button(
#        wind, width=10, text='Ok', command= Get_entries)
#    okb.place(x=390, y=350)
#
#
#    appyb = tk.Button(
#        wind, width=10, text='Apply', command= Get_entries2)
#    appyb.place(x=290, y=350)
#
#    wind.mainloop(n = 0)
#    wind.mainloop.quit()
    
class System_setup(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid(ipadx=280 , ipady=190)
        self.TFnum()
        self.TFden()
        self.Simtime()
        self.Timeinc()
        self.Deadtime()
        self.Setpoint()
        self.Steptime()
        self.Ramptime()
        self.Input()
        self.Ok()
        self.Apply()
        self.tfinal = 0  
#            self.create_text(
#                (180, 68), activefill="red", text="Gp(s) num", fill="black")
#            self.create_text(
#                (180, 98), activefill="red", text="Gp(s) den", fill="black")
#            self.create_text(
#                (280, 138), activefill="red", text="Simulation Parameters",
#                font=tkFont.Font(weight='bold'))
#            self.create_text((
#                40, 168), activefill="red", text="Sim time(s)", fill="black")
#            self.create_text((40, 198), activefill="red",
#                             text="Time inc.(s)", fill="black")
#            self.create_text((40, 228), activefill="red",
#                             text="Dead time(s)", fill="black")
#            self.create_text(
#                (280, 30), activefill="red", text="Process Tranfser function",
#                font=tkFont.Font(weight='bold'))
#            self.create_text(
#                (350, 168), activefill="red", text="Set Point", fill="black")
#            self.create_text((350, 198), activefill="red",
#                             text="Step time(s)", fill="black")
#            self.create_text((350, 228), activefill="red",
#                             text="Ramp time(s)", fill="black")
#            self.create_text((350, 275), activefill="red",
#                             text="SP input type", fill="black")
#
    def TFnum(self):
        self.Gpn = tk.Entry(self, width=20, justify=tk.CENTER)
        self.Gpn.place(x=220, y=60)
        self.Gpn.insert(0, "0.125")

    def TFden(self):
        self.Gpd = tk.Entry(self, width=20, justify=tk.CENTER)
        self.Gpd.place(x=220, y=90)
        self.Gpd.insert(0, "1 3 3 1")

    def Simtime(self):
        self.Tsim = tk.Entry(self, width=10, justify=tk.CENTER)
        self.Tsim.place(x=100, y=160)
        self.Tsim.insert(0, "100")

    def Timeinc(self):
        self.Tinc = tk.Entry(self, width=10, justify=tk.CENTER)
        self.Tinc.place(x=100, y=190)
        self.Tinc.insert(0, "0.1")

    def Deadtime(self):
        self. dt = tk.Entry(self, width=10, justify=tk.CENTER)
        self.dt.place(x=100, y=220)
        self.dt.insert(0, "0")

    def Setpoint(self):
        self.sp = tk.Entry(self, width=10, justify=tk.CENTER)
        self.sp.place(x=400, y=160)
        self.sp.insert(0, "1")

    def Steptime(self):
        self.st = tk.Entry(self, width=10, justify=tk.CENTER)
        self.st.place(x=400, y=190)
        self.st.insert(0, "0")

    def Ramptime(self):
        self.rt = tk.Entry(self, width=10, justify=tk.CENTER)
        self.rt.place(x=400, y=220)
        self.rt.insert(0, "10")

    def Get_entries(self):
        self.quit()
        GPn = [float(s) for s in self.Gpn.get().split()]
        
        Gpd = [float(s) for s in self.Gpd.get().split()]
        self.tfinal = [float(s) for s in self.Tsim.get().split()][0]
        dt = [float(s) for s in self.Tinc.get().split()][0]
        DT = [float(s) for s in self.dt.get().split()][0]
        SP = [float(s) for s in self.sp.get().split()][0]
        step_time = [float(s) for s in self.st.get().split()][0]
        ramp_time = [float(s) for s in self.rt.get().split()][0]
        SP_input = self.inputvar.get()
        print 'im leaving'
        return

    def Get_entries2(self):

        GPn = (eval(self.Gpn.get()))
        Gpd = (eval(self.Gpd.get()))
        tfinal = (eval(self.Tsim.get()))
        dt = (eval(self.Tinc.get()))
        DT = (eval(self.dt.get()))
        SP = (eval(self.sp.get()))
        step_time = (self.st.get())
        ramp_time = (self.rt.get())
        SP_input = (self.inputvar.get())
        self.quit()

    def Input(self):
        optionList = ('Step', 'Ramp')
        self.inputvar = tk.StringVar()
        self.inputvar.set(optionList[0])
        self.SPinput = tk.OptionMenu(self, self.inputvar, *optionList)
        self.SPinput.place(x=400, y=260)

    def Ok(self):
        self.okb = tk.Button(
            self, width=10, text='Ok', command=self.Get_entries)
        self.okb.place(x=390, y=350)

    def Apply(self):
        self.appyb = tk.Button(
            self, width=10, text='Apply', command=self.Get_entries2)
        self.appyb.place(x=290, y=350)
##
#    wind = System_setup()
#    wind.mainloop()
##    wind.master.title('System Specification')
##    mainloop()

#    return GPn, Gpd, tfinal, dt, DT, SP, step_time, ramp_time, SP_input
