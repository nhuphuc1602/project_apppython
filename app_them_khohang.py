from giao_dien.gd_them_khohang import*
from thu_vien.c_Kho_hang import *
from thu_vien.XL_Chung import *


# Giao diện
app = wx.App()
frame = wx.Frame(None, title="Thêm Sản Phẩm", size=(520, 280))

panel = MyPanel3(frame)

frame.Show(True)
app.MainLoop()
