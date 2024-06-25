from datetime import datetime
class Penjualan:
    def __init__(self, produk, jumlah) -> None:
        self.produk = produk
        self.jumlah = jumlah
        self.tanggal = datetime
    
    def total_harga(self):
        return self.produk.hargajual * self.jumlah
    
    def total_laba(self):
        return (self.hargajual - self.hargabeli) * self.jumlah