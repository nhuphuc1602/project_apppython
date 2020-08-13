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
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"THÊM SẢN PHẨM", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "@Arial Unicode MS" ) )

        bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gbSizer2.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_ten, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        gbSizer2.Add( self.m_staticText5, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_maso = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_maso, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Hãng", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_hang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_hang, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá bán", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gbSizer2.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_giaban = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_giaban, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gbSizer2.Add( self.m_staticText8, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_gianhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_gianhap, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Tồn kho", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        gbSizer2.Add( self.m_staticText9, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_tonkho = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_tonkho, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Kho", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        gbSizer2.Add( self.m_staticText10, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.bnt_them = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.bnt_them, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        choice_tenkhoChoices = []
        self.choice_tenkho = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_tenkhoChoices, 0 )
        self.choice_tenkho.SetSelection( 0 )
        gbSizer2.Add( self.choice_tenkho, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        # Connect Events
        self.bnt_them.Bind( wx.EVT_BUTTON, self.bnt_them_click )
        self.choice_tenkho.Bind( wx.EVT_CHOICE, self.choice_tenkho_click )

    def __del__( self ):
        pass


    def bnt_them_click( self, event ):
        # Khởi tạo Sản phẩm
        xl_sanpham = SanPham(duong_dan_san_pham)

        # Gán biến
        ten = self.txt_ten.GetValue()
        ma_so = self.txt_maso.GetValue()
        hang = self.txt_hang.GetValue()
        don_gia_ban = self.txt_giaban.GetValue()
        don_gia_nhap = self.txt_gianhap.GetValue()
        so_luong_ton = self.txt_tonkho.GetValue()
        ten_kho = self.choice_tenkho_click(self)

        kq = xl_sanpham.them_sanpham(ten, ma_so, hang, don_gia_ban, don_gia_nhap, ten_kho, so_luong_ton )
        if kq != 0:
            self.txt_ten.SetValue("")
            self.txt_maso.SetValue("")
            self.txt_hang.SetValue("")
            self.txt_giaban.SetValue("")
            self.txt_gianhap.SetValue("")
            self.txt_tonkho.SetValue("")
            wx.MessageBox("Thêm dữ liệu thành công.", "Thông báo", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Thêm dữ liệu thất bại.", "Thông báo", wx.OK | wx.ICON_ERROR)

    def choice_tenkho_click( self, event ):
        # Khởi tạo
        xl_kho_hang = KhoHang(duong_dan_san_pham)

        # Gán biến
        ten_kho = self.choice_tenkho.GetStringSelection()

    
        return ten_kho

