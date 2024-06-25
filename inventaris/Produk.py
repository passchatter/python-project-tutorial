class Produk:
    def __init__(self, name, hargajual, hargabeli, stok) -> None:
        self.name = name
        self.hargajual = hargajual
        self.hargabeli = hargabeli
        self.stok = stok

    def TambahStok(self, jumlah):
        self.stok += jumlah
    
    def KurangStok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False
    
    def update_produk(self, name=None, hargajual=None, hargabeli=None, stok=None ):
        if hargajual is not None:
            self.hargajual = hargajual
        if hargabeli is not None:
            self.hargabeli = hargabeli
        if name is not None:
            self.name = name
        if stok is not None:
            self.stok = stok