#!/bin/python

import math
import sys
import re

import wx

from ESC_ContourEstimator import ESC_ContourEstimator
from GUI_ContourEstimator_Input import GUI_ContourEstimator_Input
from GUI_ContourEstimator_Output import GUI_ContourEstimator_Output

class ContourEstimator(wx.Frame):
    def __init__(self, s_parent, s_title="ContourEstimator"):
        wx.Frame.__init__(self, s_parent, title=s_title, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self)
        box = wx.BoxSizer()
        self.frames()
        self.hiding()
        self.panel.SetSizer(self.box2)
        self.dic['A'].Show()
        self.binder()
        self.Show(True)
        self.Centre()
        self.SetSize((250, 250))
        box.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)

    def frames(self):
        def dic_make():
            self.dic = {}
            self.dic['A'] = self.contourinput
            self.dic['B'] = self.contouroutput

        self.contourinput = GUI_ContourEstimator_Input(self.panel)
        self.contouroutput = GUI_ContourEstimator_Output(self.panel)
        dic_make()
        self.box2 = wx.BoxSizer()
        for x in self.dic:
            self.box2.Add(self.dic[x], 1, wx.ALL | wx.EXPAND)

    def hiding(self):
        for x in self.dic:
            self.dic[x].Hide()

    def binder(self):
        def stop_buttons():
            for x in self.dic:
                self.dic[x].stop.Bind(wx.EVT_BUTTON, self.quitting)

        def other_buttons():
            self.contourinput.calc.Bind(wx.EVT_BUTTON, self.next_frame)
            self.contouroutput.prev.Bind(wx.EVT_BUTTON, self.prev_frame)

        stop_buttons()
        other_buttons()

    def quitting(self, event):
        sys.exit()

    def next_frame(self, event):
        def set_values(chain):
            est = ESC_ContourEstimator(chain)
            self.contouroutput.simple.SetLabel(str(est.get_simple()))
            self.contouroutput.freeman.SetLabel(str(est.get_freeman()))
            self.contouroutput.groen_verbeek.SetLabel(str(est.get_groen_verbeek()))
            self.contouroutput.profitt_rosen.SetLabel(str(est.get_profitt_rosen()))
            self.contouroutput.vossepoel_smeulders.SetLabel(str(est.get_vossepoel_smeulders()))
        
        chain = self.contourinput.chain_code.GetValue()
        chain = chain.replace("\n", "").replace(" ", "").replace("\t", "")
        if bool(re.match('^[0-7]+$', chain)):
            set_values(chain)
            self.hiding()
            self.dic['B'].Show()
            self.Layout()
            self.Centre()
    
    def prev_frame(self, event):
        self.hiding()
        self.dic['A'].Show()
        self.Layout()
        self.Centre()


# Is called when this script is used as the MAIN.
if __name__ == "__main__":
    class MyApp(wx.App):
        def OnInit(self):
            frame = ContourEstimator(None)
            frame.Show(True)
            frame.Centre()
            self.SetTopWindow(frame)
            return True

    # The application-loop
    app = MyApp(0)
    app.MainLoop()
