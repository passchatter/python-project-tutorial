from Penjualan import Penjualan
from datetime import datetime

class Toko:
    def __init__(self):
        self.DaftarProduk = []
        self.DaftarPelanggan = []
        self.DaftarTransaksi = []
    
    def TambahProduk(self, produk):
        self.DaftarProduk.append(produk)
    
    def HapusProduk(self, produk):
        self.DaftarProduk.remove(produk)

    def DaftarPelangganClass(self):
        return self.DaftarPelanggan

    def DaftarProdukClass(self):
        return self.DaftarProduk

    def ListProduk(self):
        for produk in self.DaftarProduk:
            print(f"{produk.name} - harga jual: Rp.{produk.hargajual} stok = {produk.stok}")

    def TambahPelanggan(self, pelanggan):
        self.DaftarPelanggan.append(pelanggan)
    
    def listPelanggan(self):
        for pelanggan in self.DaftarPelanggan:
            print(f"{pelanggan.name} (ID : {pelanggan.id_pelanggan})")

    def TambahTransaksi(self, transaksi):
        self.DaftarTransaksi.append(transaksi)
    
    def ListTransaksi(self):
        for transaksi in self.DaftarTransaksi:
            print(f"{transaksi.produk.name}=>{transaksi.jumlah}")
    

    