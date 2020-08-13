# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

from thu_vien.c_Kho_hang import *
from thu_vien.c_San_pham import *
from thu_vien.XL_Chung import *

###########################################################################
## Class MyPanel1
###########################################################################
class MyPanel1 ( wx.Panel ):
    
    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 704,496 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        #Lấy danh sách sản phẩm để lấy số lượng sản phẩm tạo size cho Grid
        xl_sanpham = SanPham(duong_dan_san_pham)
        ds_san_pham = xl_sanpham.doc_danh_sach_sanpham()
        
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"QUẢN LÝ KHO", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.grid_data = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        # Tạo Grid từ len danh sách sản phẩm 
        self.grid_data.CreateGrid( len(ds_san_pham)+3, 7 )
        self.grid_data.EnableEditing( True )
        self.grid_data.EnableGridLines( True )
        self.grid_data.EnableDragGridSize( False )
        self.grid_data.SetMargins( 0, 0 )

        # Columns
        self.grid_data.EnableDragColMove( False )
        self.grid_data.EnableDragColSize( True )
        self.grid_data.SetColLabelSize( 30 )
        self.grid_data.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.grid_data.EnableDragRowSize( True )
        self.grid_data.SetRowLabelSize( 80 )
        self.grid_data.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.grid_data.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        gbSizer3.Add( self.grid_data, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer1.Add( gbSizer3, 1, wx.EXPAND, 5 )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.bnt_find = wx.Button( self, wx.ID_ANY, u"Tìm kiếm", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.bnt_find, 0, wx.ALL, 5 )

        self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl9.SetMaxSize( wx.Size( 400,-1 ) )

        fgSizer3.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

        self.bnt_luu = wx.Button( self, wx.ID_ANY, u"Chỉnh sửa", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.bnt_luu, 0, wx.ALL, 5 )

        self.bnt_reset = wx.Button( self, wx.ID_ANY, u"Hiển thị lại", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.bnt_reset, 0, wx.ALL, 5 )


        bSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        # Connect Events
        self.bnt_find.Bind( wx.EVT_BUTTON, self.bnt_find_click )
        self.bnt_luu.Bind( wx.EVT_BUTTON, self.bnt_luu_click )
        self.bnt_reset.Bind( wx.EVT_BUTTON, self.bnt_reset_click )

    def __del__( self ):
        pass


    # Nút tìm kiếm

    def bnt_find_click( self, event ):
        key = self.m_textCtrl9.GetValue()
        xl_sanpham = SanPham(duong_dan_san_pham)
        # Tìm sản phẩm từ key nhập vào
        ds_san_pham = xl_sanpham.tim_kiem_sanpham(key)
        self.grid_data.ClearGrid()
        self.grid_data.SetCellValue(0,0, "Tên")
        self.grid_data.SetCellValue(0,1, "Mã số")
        self.grid_data.SetCellValue(0,2, "Hãng")
        self.grid_data.SetCellValue(0,3, "Giá nhập")
        self.grid_data.SetCellValue(0,4, "Giá bán")
        self.grid_data.SetCellValue(0,5, "Kho hàng")
        self.grid_data.SetCellValue(0,6, "Tồn kho")
        # Set giá trị vào Grid
        i = 1
        while i <= len(ds_san_pham):
            for san_pham in ds_san_pham:
                self.grid_data.SetCellValue(i,0, san_pham['Ten'])
                self.grid_data.SetCellValue(i,1, san_pham['Ma_so'])
                self.grid_data.SetCellValue(i,2, san_pham['Hang'])
                self.grid_data.SetCellValue(i,3, str(san_pham['Gia_nhap']))
                self.grid_data.SetCellValue(i,4, str(san_pham['Gia_ban']))
                self.grid_data.SetCellValue(i,5, str(san_pham['Ten_kho']))
                self.grid_data.SetCellValue(i,6, str(san_pham['Ton_kho']))
                i+=1

    def bnt_luu_click( self, event ):
        xl_sanpham = SanPham(duong_dan_san_pham)
        ds_san_pham = xl_sanpham.doc_danh_sach_sanpham()
        ds_maso_sanpham = []
        for san_pham in ds_san_pham:
            ds_maso_sanpham.append(san_pham['Ma_so'])
        # Xử lý trường hợp người dùng sửa mã số sản phẩm, mã số là primary key không thể chỉnh sửa
        u = 1
        kt = 0 
        while u <= len(ds_maso_sanpham):
            if ds_maso_sanpham[u-1] != self.grid_data.GetCellValue(u,1):
                kt += 1
                wx.MessageBox("Không thể chỉnh sửa mã sản phẩm !", "Thông báo", wx.OK | wx.ICON_INFORMATION)
                self.grid_data.SetCellValue(0,0, "Tên")
                self.grid_data.SetCellValue(0,1, "Mã số")
                self.grid_data.SetCellValue(0,2, "Hãng")
                self.grid_data.SetCellValue(0,3, "Giá nhập")
                self.grid_data.SetCellValue(0,4, "Giá bán")
                self.grid_data.SetCellValue(0,5, "Kho hàng")
                self.grid_data.SetCellValue(0,6, "Tồn kho")
                i = 1
                while i <= len(ds_san_pham):
                    for san_pham in ds_san_pham:
                        self.grid_data.SetCellValue(i,0, san_pham['Ten'])
                        self.grid_data.SetCellValue(i,1, san_pham['Ma_so'])
                        self.grid_data.SetCellValue(i,2, san_pham['Hang'])
                        self.grid_data.SetCellValue(i,3, str(san_pham['Gia_nhap']))
                        self.grid_data.SetCellValue(i,4, str(san_pham['Gia_ban']))
                        self.grid_data.SetCellValue(i,5, str(san_pham['Ten_kho']))
                        self.grid_data.SetCellValue(i,6, str(san_pham['Ton_kho']))
                        i+=1
                break
            u+=1
        # Nếu mã số sản phẩm không bị chỉnh sửa, cập nhập các giá trị bị chỉnh sửa khác
        if kt == 0:   
            i = 1
            while i <= len(ds_san_pham):
                ten = self.grid_data.GetCellValue(i,0)
                ma_so = self.grid_data.GetCellValue(i,1)
                hang = self.grid_data.GetCellValue(i,2)
                gia_ban = self.grid_data.GetCellValue(i,3)
                gia_nhap = self.grid_data.GetCellValue(i,4)
                ten_kho = self.grid_data.GetCellValue(i,5)
                so_luong_ton = self.grid_data.GetCellValue(i,6)
                xl_sanpham.cap_nhat_sanpham(ten,ma_so,hang,gia_ban,gia_nhap,ten_kho,so_luong_ton)
                i+=1
            wx.MessageBox("Sửa dữ liệu thành công.", "Thông báo", wx.OK | wx.ICON_INFORMATION)
            

    def bnt_reset_click( self, event ):
        #Tải lại Grid với tất cả sản phẩm
        xl_san_pham = SanPham(duong_dan_san_pham)
        ds_san_pham = xl_san_pham.doc_danh_sach_sanpham()
        self.grid_data.SetCellValue(0,0, "Tên")
        self.grid_data.SetCellValue(0,1, "Mã số")
        self.grid_data.SetCellValue(0,2, "Hãng")
        self.grid_data.SetCellValue(0,3, "Giá nhập")
        self.grid_data.SetCellValue(0,4, "Giá bán")
        self.grid_data.SetCellValue(0,5, "Kho hàng")
        self.grid_data.SetCellValue(0,6, "Tồn kho")
        i = 1
        while i <= len(ds_san_pham):
            for san_pham in ds_san_pham:
                self.grid_data.SetCellValue(i,0, san_pham['Ten'])
                self.grid_data.SetCellValue(i,1, san_pham['Ma_so'])
                self.grid_data.SetCellValue(i,2, san_pham['Hang'])
                self.grid_data.SetCellValue(i,3, str(san_pham['Gia_nhap']))
                self.grid_data.SetCellValue(i,4, str(san_pham['Gia_ban']))
                self.grid_data.SetCellValue(i,5, str(san_pham['Ten_kho']))
                self.grid_data.SetCellValue(i,6, str(san_pham['Ton_kho']))
                i+=1
  



