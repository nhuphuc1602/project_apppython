# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

from thu_vien.c_Kho_hang import *
from thu_vien.c_San_pham import *
from thu_vien.XL_Chung import *

from giao_dien.gd_them import *
from giao_dien.gd_them_khohang import *
from giao_dien.gd_xuat import *
###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.MDIParentFrame ):

    def __init__( self, parent ):
        wx.MDIParentFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Quản lý Sản phẩm", pos = wx.DefaultPosition, size = wx.Size( 1200,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arimo" ) )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.menu_xem = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Xem Sản phẩm", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_xem )

        self.menu_them_sanpham = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Thêm Sản phẩm", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_them_sanpham )

        self.menu_them_khohang = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Thêm Kho hàng", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_them_khohang )

        self.menu_quit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Thoát", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_quit )

        self.m_menubar1.Append( self.m_menu1, u"Chỉnh sửa" )

        self.menu_help = wx.Menu()
        self.menu_about = wx.MenuItem( self.menu_help, wx.ID_ANY, u"Về", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_help.Append( self.menu_about )

        self.m_menubar1.Append( self.menu_help, u"Giúp đỡ" )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.menu_xem_click, id = self.menu_xem.GetId() )
        self.Bind( wx.EVT_MENU, self.menu_them_sanpham_click, id = self.menu_them_sanpham.GetId() )
        self.Bind( wx.EVT_MENU, self.menu_them_khohang_click, id = self.menu_them_khohang.GetId() )
        self.Bind( wx.EVT_MENU, self.menu_quit_click, id = self.menu_quit.GetId() )
        self.Bind( wx.EVT_MENU, self.menu_about_click, id = self.menu_about.GetId() )

    def __del__( self ):
        pass


    # Mục xem, tìm kiếm và sửa tất cả sản phẩm
    def menu_xem_click( self, event ):
        tieu_de = "Chỉnh sửa sản phẩm"

        ds_Children = self.GetChildren()
        for children in ds_Children:
            if children.GetTitle() == tieu_de:
                children.Activate()
                return
        xl_san_pham = SanPham(duong_dan_san_pham)
        ds_san_pham = xl_san_pham.doc_danh_sach_sanpham()
        app = wx.App()
        frame = wx.MDIChildFrame(self, title=tieu_de, size=(900, 500))
        panel = MyPanel1(frame)
        panel.grid_data.SetCellValue(0,0, "Tên")
        panel.grid_data.SetCellValue(0,1, "Mã số")
        panel.grid_data.SetCellValue(0,2, "Hãng")
        panel.grid_data.SetCellValue(0,3, "Giá nhập")
        panel.grid_data.SetCellValue(0,4, "Giá bán")
        panel.grid_data.SetCellValue(0,5, "Kho hàng")
        panel.grid_data.SetCellValue(0,6, "Tồn kho")
        i = 1
        while i <= len(ds_san_pham):
            for san_pham in ds_san_pham:
                panel.grid_data.SetCellValue(i,0, san_pham['Ten'])
                panel.grid_data.SetCellValue(i,1, san_pham['Ma_so'])
                panel.grid_data.SetCellValue(i,2, san_pham['Hang'])
                panel.grid_data.SetCellValue(i,3, str(san_pham['Gia_nhap']))
                panel.grid_data.SetCellValue(i,4, str(san_pham['Gia_ban']))
                panel.grid_data.SetCellValue(i,5, str(san_pham['Ten_kho']))
                panel.grid_data.SetCellValue(i,6, str(san_pham['Ton_kho']))
                i+=1
        frame.Show(True)
        app.MainLoop()
    # Mục thêm sản phẩm mới
    def menu_them_sanpham_click( self, event ):
        tieu_de = "Thêm sản phẩm"

        ds_Children = self.GetChildren()
        for children in ds_Children:
            if children.GetTitle() == tieu_de:
                children.Activate()
                return
        xl_kho_hang = KhoHang(duong_dan_san_pham)
        ds_kho_hang = xl_kho_hang.doc_danh_sach_kho()

        # Lấy ds để hiển thị lên choice
        ds_ten_kho_hang = []
        for kho_hang in ds_kho_hang:
            ds_ten_kho_hang.append(kho_hang['Ten'])


        app = wx.App()
        frame = wx.MDIChildFrame(self, title=tieu_de, size=(600, 350))
        panel = MyPanel2(frame)
        panel.choice_tenkho.Append(ds_ten_kho_hang)

        frame.Show(True)
        app.MainLoop()

        xl_kho_hang.disconnect()

    #Mục thêm kho hàng mới
    def menu_them_khohang_click( self, event ):
        tieu_de = "Thêm kho hàng"

        ds_Children = self.GetChildren()
        for children in ds_Children:
            if children.GetTitle() == tieu_de:
                children.Activate()
                return
        
        

        app = wx.App()
        frame = wx.MDIChildFrame(self, title=tieu_de, size=(500, 200))

        panel = MyPanel3(frame)
        

        frame.Show(True)
        app.MainLoop()

        
    #Click thoát
    def menu_quit_click( self, event ):
        self.Close()

    #Mục thông tin app
    def menu_about_click( self, event ):
        info = wx.adv.AboutDialogInfo()
        info.SetName("Bài Tập Cuối Kỳ")
        info.SetVersion("1.0")
        info.SetDescription("Môn học Python Nâng Cao \nTrung Tâm Tin Học Khoa Học Tự Nhiên \nThis software is developed by Vo Nhu Phuc")

        wx.adv.AboutBox(info)


