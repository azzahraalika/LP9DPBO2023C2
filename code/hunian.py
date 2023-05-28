class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, harga = 0, lokasi = '', foto = ''):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.harga = harga
        self.lokasi = lokasi
        self.foto = foto

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_harga(self):
        return self.harga

    def get_lokasi(self):
        return self.lokasi

    def get_foto(self):
        return self.foto

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."