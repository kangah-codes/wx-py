import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 500))

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("TestApp")

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add((0, 0), 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()


class MyApp(wx.App):
    def OnInit(self):
        self.TestApp = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.TestApp)
        self.TestApp.Show()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
