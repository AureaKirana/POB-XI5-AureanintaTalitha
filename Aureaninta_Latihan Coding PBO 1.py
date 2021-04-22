#Aureaninta TNKP (XI MIPA 5/06)

class pelamar:
    #class variabel
    jumlah_calon = 0
    #konstruktor
    def __init__(self, nama, umur, lahir, asal, nilai):
        self.nama = nama
        self.umur = umur
        self.lahir = lahir
        self.asal = asal
        self.nilai = nilai
        pelamar.jumlah_pelamar =+ 1

    #methode
    def viewPelamar(self):
        print("________________________________________")
        print(" ")
        print("Data Pelamar Kerja")
        print("Nama : ", self.nama)
        print("Umur : ", self.umur)
        print("Tanggal Lahir : ", self.lahir)
        print("Negara Asal : ", self.asal)
        print("------------------------------")
    
    def viewNilai(self):
        print("Data Nilai")
        print("Nama : ", self.nama)
        for nilai in self.nilai:
            print("Nilai : ", nilai)
        print("------------------------------")
    
    def viewKeterangan(self):
        print("Keterangan")
        print("Nama : ", self.nama)
        print("Umur : ", self.umur)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata : ", rata)
        if rata >= 75:
            keterangan = "Lulus."
        else:
            keterangan = "Tidak lulus."
        print("Keterangan : ", keterangan)
        print("------------------------------")

#instansiasi objek
calon1 = pelamar("William Miller", "17 tahun", "25 Maret 2004", "Inggris", [78,97,100,90])
calon2 = pelamar("Nichol", "22 tahun", "15 Januari 1999", "Indonesia", [90,95,90,75])
calon3 = pelamar("Yadi Sarimin", "23 tahun", "27 Februari 1998", "Hawai", [94,83,60,70])
#pemanggilan objek siswa 1
calon1.viewPelamar()
calon1.viewNilai()
calon1.viewKeterangan()
print("Jumlah calon : ", pelamar.jumlah_pelamar)
#pemanggilan objek siswa 2
calon2.viewPelamar()
calon2.viewNilai()
calon2.viewKeterangan()
print("Jumlah calon : ", pelamar.jumlah_pelamar)
#pemanggilan objek siswa 3
calon3.viewPelamar()
calon3.viewNilai()
calon3.viewKeterangan()
print("Jumlah calon : ", pelamar.jumlah_pelamar)
