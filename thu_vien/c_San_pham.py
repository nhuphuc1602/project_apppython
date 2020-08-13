from thu_vien.c_Database import *

class SanPham(Database):
    def __init__(self, path_db):
        Database.__init__(self, path_db)

    def them_sanpham(self, ten, ma_so, hang, gia_ban, gia_nhap, ten_kho, so_luong_ton):
        chuoi_sql = "INSERT INTO DienThoai VALUES (?, ?, ?, ?, ?, ?, ?)"
        kq = Database.execute(self, chuoi_sql, (ten, ma_so, hang, gia_ban, gia_nhap, ten_kho, so_luong_ton ))
        return kq

    def doc_danh_sach_sanpham(self):
        chuoi_sql = "SELECT * FROM DienThoai"
        noi_dung = Database.get_all(self, chuoi_sql)
        ds_san_pham = []
        for dong in noi_dung:
            nhom = {"Ten": dong[0], "Ma_so": dong[1], "Hang": dong[2], "Gia_nhap": dong[3],"Gia_ban": dong[4],"Ten_kho": dong[5],"Ton_kho": dong[6]}
            ds_san_pham.append(nhom)
        return ds_san_pham

    def cap_nhat_sanpham(self, ten, ma_so, hang, gia_ban, gia_nhap, ten_kho, so_luong_ton):
        chuoi_sql = "UPDATE DienThoai SET  Ten=?, Hang=?, Gia_nhap=?, Gia_ban=?, Ten_kho=?, Ton_kho=? WHERE Ma_so = ?"
        kq = Database.execute(self, chuoi_sql, ( ten, hang, gia_ban, gia_nhap, ten_kho, so_luong_ton, ma_so))
        return kq

    def tim_kiem_sanpham(self, key):
        chuoi_sql = "SELECT * FROM DienThoai WHERE Ten LIKE ?"
        key1 = "%" + str(key) + "%"
        noi_dung = Database.get_all(self, chuoi_sql, ( key1, ))
        ds_san_pham = []
        for dong in noi_dung:
            nhom = {"Ten": dong[0], "Ma_so": dong[1], "Hang": dong[2], "Gia_nhap": dong[3],"Gia_ban": dong[4],"Ten_kho": dong[5],"Ton_kho": dong[6]}
            ds_san_pham.append(nhom)
        return ds_san_pham