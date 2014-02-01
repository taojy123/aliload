#coding=gbk
#Boa:Dialog:Dialog1

import wx
import urllib2
import Frame1

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1STATICTEXT2, 
 wxID_DIALOG1STATICTEXT3, wxID_DIALOG1TEXTCTRL1, wxID_DIALOG1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(493, 276), size=wx.Size(419, 178),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='\xc7\xeb\xcf\xc8\xb5\xc7\xc2\xbc')
        self.SetClientSize(wx.Size(403, 140))
        self.SetToolTipString('')
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(152, 24), size=wx.Size(168, 22),
              style=0, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(152, 56), size=wx.Size(168, 22),
              style=wx.TE_PASSWORD, value='')

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='\xd3\xc3\xbb\xa7\xc3\xfb', name='staticText2', parent=self,
              pos=wx.Point(104, 24), size=wx.Size(36, 14), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3,
              label='\xc3\xdc\xc2\xeb', name='staticText3', parent=self,
              pos=wx.Point(112, 56), size=wx.Size(24, 14), style=0)

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1,
              label='\xc1\xa2\xbc\xb4\xb5\xc7\xc2\xbc', name='button1',
              parent=self, pos=wx.Point(168, 96), size=wx.Size(75, 24),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnDialog1Close(self, event):
        self.Destroy()
        event.Skip()

    def OnButton1Button(self, event):
        try:
            username = self.textCtrl1.GetValue()
            password = self.textCtrl2.GetValue()
            url = Frame1.HOST + "/login?username=%s&password=%s"%(username, password)
            user_id = urllib2.urlopen(url).read()
        
            if int(user_id) > -1:
                Frame1.mself.login_text.SetLabel(user_id)
                self.Destroy()
            else:
                raise
        except:
            wx.MessageBox("请检查网络连接是否正常并输入正确密码")
        event.Skip()
