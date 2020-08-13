# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


from thu_vien.c_Kho_hang import *
from thu_vien.c_San_pham import *
from thu_vien.XL_Chung import *
###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Thêm Kho hàng", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        self.m_staticText29.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer3.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gbSizer11 = wx.GridBagSizer( 0, 0 )
        gbSizer11.SetFlexibleDirection( wx.BOTH )
        gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Tên Kho hàng", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )

        gbSizer11.Add( self.m_staticText30, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_tenkhohang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer11.Add( self.txt_tenkhohang, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        gbSizer11.Add( self.m_staticText31, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_diachi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer11.Add( self.txt_diachi, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.them_khohang = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer11.Add( self.them_khohang, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer3.Add( gbSizer11, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        # Connect Events
        self.them_khohang.Bind( wx.EVT_BUTTON, self.them_khohang_click )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def them_khohang_click( self, event ):
        xl_khohang = KhoHang(duong_dan_san_pham)

        # Gán biến
        ten = self.txt_tenkhohang.GetValue()
        dia_chi = self.txt_diachi.GetValue()
        

        kq = xl_khohang.them_kho_hang(ten, dia_chi)
        if kq != 0:
            self.txt_tenkhohang.SetValue("")
            self.txt_diachi.SetValue("")
            wx.MessageBox("Thêm dữ liệu thành công.", "Thông báo", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Thêm dữ liệu thất bại.", "Thông báo", wx.OK | wx.ICON_ERROR)


