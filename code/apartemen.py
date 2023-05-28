from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, harga, lokasi, foto):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, harga)
        self.nama_pemilik = nama_pemilik
        self.lokasi = lokasi
        self.foto = foto

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_lokasi(self):
        return self.lokasi
    
    def get_foto(self):
        return self.foto
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nHarga : " + str(self.harga) + "\nLokasi : " + self.lokasi + "\n"