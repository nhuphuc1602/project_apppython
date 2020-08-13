from giao_dien.gd_them import*
from thu_vien.c_Kho_hang import *
from thu_vien.XL_Chung import *

# Khởi tạo 
xl_kho_hang = KhoHang(duong_dan_san_pham)
ds_kho_hang = xl_kho_hang.doc_danh_sach_kho()

# Lấy ds tên nhóm để hiển thị lên choice
ds_ten_kho_hang = []
for kho_hang in ds_kho_hang:
    ds_ten_kho_hang.append(kho_hang['Ten'])

# Giao diện
app = wx.App()
frame = wx.Frame(None, title="Thêm Sản Phẩm", size=(520, 280))

panel = MyPanel2(frame)
panel.choice_tenkho.Append(ds_ten_kho_hang)

frame.Show(True)
app.MainLoop()
