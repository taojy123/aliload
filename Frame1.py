#coding=gbk
#Boa:Frame:Frame1

import wx
import Dialog1
import urllib2
import os
import zipfile

global mself
global HOST
HOST = "http://107.160.0.142"
global PATH
PATH = "D:\\data\\"

if not os.path.exists(PATH):
    os.makedirs(PATH)


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1LOGIN_TEXT, 
 wxID_FRAME1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(468, 234), size=wx.Size(562, 323),
              style=wx.DEFAULT_FRAME_STYLE,
              title='\xb0\xa2\xc0\xef\xbf\xec\xb5\xdd\xb5\xa5 \xca\xfd\xbe\xdd\xd6\xfa\xca\xd6')
        self.SetClientSize(wx.Size(546, 285))
        self.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.SetBackgroundColour(wx.Colour(253, 226, 181))
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='\xb0\xa2\xc0\xef\xbf\xec\xb5\xdd\xb5\xa5 \xca\xfd\xbe\xdd\xd6\xfa\xca\xd6',
              name='staticText1', parent=self, pos=wx.Point(112, 32),
              size=wx.Size(326, 42), style=0)
        self.staticText1.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.login_text = wx.StaticText(id=wxID_FRAME1LOGIN_TEXT, label='-',
              name='login_text', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(4, 14), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label='\xb5\xbc\xb3\xf6\xca\xfd\xbe\xdd', name='button1',
              parent=self, pos=wx.Point(112, 152), size=wx.Size(136, 56),
              style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label='\xb5\xbc\xb3\xf6\xcd\xbc\xc6\xac', name='button2',
              parent=self, pos=wx.Point(296, 152), size=wx.Size(136, 56),
              style=0)
        self.button2.SetToolTipString('')
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

    def __init__(self, parent):
        global mself
        mself = self
        self._init_ctrls(parent)

    def OnFrame1Close(self, event):
        self.Destroy()
        event.Skip()

    def OnButton1Button(self, event):
        try:
            if self.login_text.GetLabelText() == "-":
                Dialog1.create(None).Show()
            else:
                user_id = self.login_text.GetLabelText()
                url = HOST + "/output/?user_id=" + user_id
                r = urllib2.urlopen(url)
                code = r.read()
                if "alert" in code:
                    wx.MessageBox("暂时没有未导出的记录")
                else:
                    filename = PATH + r.url.split("/")[-1]
                    open(filename, "wb").write(code)
                    wx.MessageBox("已成功导出至 " + filename)
                    os.popen("explorer d:\\data")
        except:
            wx.MessageBox("请检查网络连接是否正常")
        event.Skip()

    def OnButton2Button(self, event):
        try:
            if self.login_text.GetLabelText() == "-":
                Dialog1.create(None).Show()
            else:
                user_id = self.login_text.GetLabelText()
                url = HOST + "/output_img/?user_id=" + user_id
                r = urllib2.urlopen(url)
                code = r.read()
                if "alert" in code:
                    wx.MessageBox("暂时没有未导出的图片")
                else:
                    filename = PATH + r.url.split("/")[-1]
                    open(filename, "wb").write(code)
                    f = zipfile.ZipFile(filename, 'r')
                    for file in f.namelist():
                        f.extract(file, PATH)
                    f.close()
                    wx.MessageBox("已将图片成功导出至 " + PATH)
                    os.popen("explorer d:\\data")
                    os.remove(filename)
        except:
            wx.MessageBox("请检查网络连接是否正常")
        event.Skip()
        
        
