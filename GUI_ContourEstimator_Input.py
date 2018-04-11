#!/bin/python

import wx


class GUI_ContourEstimator_Input(wx.Panel):
    def __init__(self, bb_parent):
        def explain():
            text = ("Fill in a chain code without spaces. only digits in the" +
                    " range 0-7 are allowed.")
            return text
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)

        # Input Parameters
        self.chain_code = wx.TextCtrl(self)

        # Buttons
        self.calc = wx.Button(self, label="Calculate")
        self.stop = wx.Button(self, label="Quit")
        
        # Placing of items in frame
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.StaticText(self, label=explain()), 1, wx.EXPAND | wx.ALL)
        box.Add(self.chain_code, 3, wx.EXPAND | wx.ALL)  
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.calc, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)


if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_ContourEstimator_Output"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(250, 250))
            panel = wx.Panel(self)
            panel1 = GUI_ContourEstimator_Input(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()