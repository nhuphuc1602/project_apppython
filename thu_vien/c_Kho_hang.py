from thu_vien.c_Database import *


class KhoHang(Database):
    def __init__(self, path_db):
        Database.__init__(self, path_db)

    def doc_danh_sach_kho(self):
        chuoi_sql = "SELECT * FROM KhoHang"
        noi_dung = Database.get_all(self, chuoi_sql)
        ds_kho_hang = []
        for dong in noi_dung:
            nhom = {"Ten": dong[0], "Dia_chi": dong[1]}
            ds_kho_hang.append(nhom)
        return ds_kho_hang

    def them_kho_hang(self, ten, dia_chi):
        chuoi_sql = "INSERT INTO KhoHang (Ten, Dia_chi) VALUES(?, ?)"
        kq = Database.execute(self, chuoi_sql, (ten, dia_chi))
        return kq

    