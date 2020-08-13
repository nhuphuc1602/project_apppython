from giao_dien.gd_xuat import*
from thu_vien.c_San_pham import *
from thu_vien.XL_Chung import *

# Khởi tạo NhomTivi
xl_san_pham = SanPham(duong_dan_san_pham)
ds_san_pham = xl_san_pham.doc_danh_sach_sanpham()
print(ds_san_pham)

# Lấy ds tên nhóm để hiển thị lên choice
#ds_ten_kho_hang = []


# Giao diện
app = wx.App()
frame = wx.Frame(None, title="Quản lý kho hàng", size=(900, 500))

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
