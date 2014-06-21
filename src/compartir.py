#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

from preferencias import FramePreferencias


class FramePrincipal(wx.Frame):
    def __init__(self):
        super(FramePrincipal, self).__init__(
            parent=None,
            id=-1,
            title=u'Compartir',
            pos=(0, 0)
        )

        panel = wx.Panel(self)
        status_bar = self.CreateStatusBar()
        menu_bar = wx.MenuBar()

        menu1 = wx.Menu()
        menu1.Append(wx.ID_EXIT, u'&Salir')
        menu_bar.Append(menu1, u'&Archivo')

        menu2 = wx.Menu()
        menu2.Append(wx.ID_PREFERENCES, u'&Preferencias')
        menu_bar.Append(menu2, u'&Editar')

        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.OnCloseMe, id=wx.ID_EXIT)
        self.Bind(wx.EVT_CLOSE, self.OnCloseMe, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnPreferencias, id=wx.ID_PREFERENCES)

        self.preferencias = None

    def OnCloseMe(self, event):
        print "Me cierran"
        self.Close(True)

    def OnPreferencias(self, event):
        if not self.preferencias:
            print 'Creando ventana'
            self.preferencias = FramePreferencias(parent=self)
            self.preferencias.Show()
        else:
            print 'Mostrando ventana'
            self.preferencias.Raise()

        print self.preferencias.GetBestSize()


class Compartir(wx.App):
    def __init__(self):
        super(Compartir, self).__init__(redirect=False)

    def OnInit(self):
        self.frame = FramePrincipal()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = Compartir()
    app.MainLoop()

if __name__ == '__main__':
    main()
