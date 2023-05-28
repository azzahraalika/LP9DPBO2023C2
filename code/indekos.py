from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, harga, lokasi, foto):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga = harga
        self.lokasi = lokasi
        self.foto = foto

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_harga(self):
        return self.harga
    
    def get_lokasi(self):
        return self.lokasi

    def get_foto(self):
        return self.foto

    def get_summary(self):
        return "Hunian Indekos Bujang Berbakat."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nNama Penghuni : " + self.nama_penghuni + "\nHarga : " + self.harga + "\nLokasi : " + self.lokasi + "\n"
    

