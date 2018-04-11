#!/bin/python

import wx


class GUI_ContourEstimator_Output(wx.Panel):
    def __init__(self, bb_parent):
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)

        # Output Parameters
        self.simple = wx.StaticText(self, label="")
        self.freeman = wx.StaticText(self, label="")
        self.groen_verbeek = wx.StaticText(self, label="")
        self.profitt_rosen = wx.StaticText(self, label="")
        self.vossepoel_smeulders = wx.StaticText(self, label="")

        # Buttons
        self.prev = wx.Button(self, label="Back")
        self.stop = wx.Button(self, label="Quit")
        
        # Placing of items in frame
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.StaticText(self, label="Simple:"), 1, wx.EXPAND | wx.ALL)
        hbox1.Add(self.simple, 2, wx.EXPAND | wx.ALL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(wx.StaticText(self, label="Freeman:"), 1, wx.EXPAND | wx.ALL)
        hbox2.Add(self.freeman, 2, wx.EXPAND | wx.ALL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(wx.StaticText(self, label="Groen & Verbeek:"), 1,
                  wx.EXPAND | wx.ALL)
        hbox3.Add(self.groen_verbeek, 2, wx.EXPAND | wx.ALL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(wx.StaticText(self, label="Profitt & Rosen:"), 1,
                  wx.EXPAND | wx.ALL)
        hbox4.Add(self.profitt_rosen, 2, wx.EXPAND | wx.ALL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5.Add(wx.StaticText(self, label="Vossepoel & Smeulders:"), 1,
                  wx.EXPAND | wx.ALL)
        hbox5.Add(self.vossepoel_smeulders, 2, wx.EXPAND | wx.ALL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6.Add(self.prev, 1, wx.EXPAND | wx.ALL)
        hbox6.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(hbox1, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox2, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox3, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox4, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox5, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox6, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)


if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_ContourEstimator_Output"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(250, 250))
            panel = wx.Panel(self)
            panel1 = GUI_ContourEstimator_Output(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()