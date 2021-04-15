#Aureaninta Talitha NKP (XI MIPA 5/06)
class Cabang:
    '''Dasar kelas untuk semua cabang'''
    jumlah_cabang = 0

    def __init__(self, nama, head, karyawan, pemasukan):
        self.nama = nama
        self.head = head
        self.karyawan = karyawan
        self.pemasukan = pemasukan
        Cabang.jumlah_cabang += 1

    def tampilkan_jumlah(self):
        print("Total cabang: ", Cabang.jumlah_cabang)

    def tampilkan_profil(self):
        print("Nama Cabang : ", self.nama)
        print("Kepala Cabang : ", self.head)
        print("Jumlah Karyawan : ", self.karyawan)
        print("Pemasukan/hari : ", self.pemasukan)

cabang1 = Cabang("Hartono Mall", "Harto", 8, 5000000)
cabang2 = Cabang("Yadi Mall", "Jokok Suparyadi", 3, 2000000)
cabang3 = Cabang("Senayan City", "Pasha Buana", 10, 9000000)
cabang4 = Cabang("Grand Indonesia", "Kevin Arganta", 17, 12000000)

cabang1.tampilkan_profil()
cabang2.tampilkan_profil()
cabang3.tampilkan_profil()
cabang4.tampilkan_profil()
print("Total cabang : ", Cabang.jumlah_cabang)
