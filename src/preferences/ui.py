# -*- coding: utf-8 -*-

import wx

class NotebookPreferencias(wx.Notebook):
    def __init__(self, parent):
        super(NotebookPreferencias, self).__init__(parent=parent)

        self.pnl_compartir = wx.Panel(self)

        ttl_general = wx.StaticText(self.pnl_compartir, label=u'General')
        ttl_general.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        chk_iniciar = wx.CheckBox(self.pnl_compartir, label=u'Iniciar Compartir automáticamente')

        sizer = wx.BoxSizer(wx.VERTICAL)
        szr_ttl = wx.BoxSizer(wx.HORIZONTAL)
        szr_chk = wx.BoxSizer(wx.HORIZONTAL)

        szr_ttl.Add(ttl_general, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=10)
        szr_chk.Add(chk_iniciar, flag=wx.LEFT, border=15)

        sizer.Add(szr_ttl)
        sizer.Add(szr_chk)

        self.pnl_compartir.SetSizer(sizer)
        sizer.Fit(self)
        self.AddPage(self.pnl_compartir, u'Compartir')


        self.pnl_mi_perfil = wx.Panel(self)

        lbl_nombre = wx.StaticText(self.pnl_mi_perfil, label=u'Tu nombre:')
        input_nombre= wx.TextCtrl(self.pnl_mi_perfil)

        sizer = wx.BoxSizer(wx.VERTICAL)
        szr_titulo = wx.BoxSizer(wx.HORIZONTAL)
        szr_nombre = wx.BoxSizer(wx.HORIZONTAL)

        szr_nombre.Add(lbl_nombre, flag=wx.ALL, border=5)
        szr_nombre.Add(input_nombre, flag=wx.ALL, border=5)

        sizer.Add(szr_titulo, flag=wx.ALL|wx.EXPAND, border=5)
        sizer.Add(szr_nombre, flag=wx.ALL|wx.EXPAND, border=5)

        self.pnl_mi_perfil.SetSizer(sizer)
        sizer.Fit(self)
        self.AddPage(self.pnl_mi_perfil, u'Perfil')


class FramePreferencias(wx.Frame):
    def __init__(self, parent):
        super(FramePreferencias, self).__init__(
            parent=parent,
            id=-1,
            title=u'Preferencias de Compartir',
            style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        )

        self.def_flags = wx.LEFT|wx.TOP|wx.RIGHT|wx.EXPAND

        panel = wx.Panel(self)

        titulo = wx.StaticText(panel, label=u'Preferencias')
        titulo.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        tabs = NotebookPreferencias(panel)
        btn_guardar = wx.Button(panel, wx.ID_SAVE)

        self.Bind(wx.EVT_BUTTON, self.OnSave, btn_guardar)

        sizer = wx.BoxSizer(wx.VERTICAL)
        szr_titulo = wx.BoxSizer(wx.HORIZONTAL)
        szr_tabs = wx.BoxSizer(wx.HORIZONTAL)
        szr_botones = wx.BoxSizer(wx.HORIZONTAL)

        szr_titulo.Add(titulo, flag=self.def_flags, border=10)
        szr_tabs.Add(tabs, flag=self.def_flags, border=10)
        szr_botones.Add(btn_guardar, flag=self.def_flags, border=10)

        sizer.Add(szr_titulo, flag=wx.ALL|wx.EXPAND)
        sizer.Add(szr_tabs, flag=wx.ALL|wx.EXPAND)
        sizer.Add(szr_botones, flag=wx.BOTTOM|wx.ALIGN_RIGHT, border=10)

        panel.SetSizer(sizer)
        panel.Layout()
        sizer.Fit(self)

    def OnSave(self, event):
        self.Close()
