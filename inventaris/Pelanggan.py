from Penjualan import Penjualan

class Pelanggan:
    def __init__(self, name, id_pelanggan, toko):
        self.name = name
        self.id_pelanggan = id_pelanggan
        self.keranjang = {}
        self.toko = toko
    
    def TambahKeranjang(self, produk, jumlah):
        if produk.KurangStok(jumlah):
            if produk in self.keranjang:
                self.keranjang[produk] += jumlah
            else:
                self.keranjang[produk] = jumlah
            return True
        return False
    
    def HapusKeranjang(self, produk, jumlah):
        if produk in self.keranjang and self.keranjang[produk] >= jumlah:
            self.keranjang[produk] -= jumlah
            if self.keranjang[produk] == 0:
                del self.keranjang[produk]
            produk.TambahStok(jumlah)
            return True
        return False
    
    def TampilkanKeranjang(self):
        if not self.keranjang.items():
            print("keranjang kosong")
        else:
            print(f"keranjang dari {self.name}")
            for produk,jumlah in self.keranjang.items():
               print(f"{produk.name} => {jumlah}")
    
    def Checkout(self):
        total = sum(produk.hargajual * jumlah for produk, jumlah in self.keranjang.items())
        for produk, jumlah in self.keranjang.items():
            transaksi = Penjualan(produk, jumlah)
            self.toko.TambahTransaksi(transaksi)
        self.keranjang.clear()
        print("=========Chekut Berhasil=========")
        print(f"total pembelian = {total}")
        print("")