from Produk import Produk
from Toko import Toko
from Pelanggan import Pelanggan    

def templateMenu():
    print("1. tambah produk")
    print("2. tampilkan produk")
    print("3. update produk")
    print("4. hapus produk")
    print("5. tambah pelanggan")
    print("6. tampilkan pelanggan")
    print("7. tambah keranjang")
    print("8. hapus keranjang")
    print("9. list produk keranjang")
    print("10. checkout")
    print("11. tampilkan transaksi")
    
def main():
    toko = Toko()
    while True:
        templateMenu()
        pilihan = input("pilih nomor menu : ")

        if pilihan == "1":
            name = input("masukkan nama produk : ")
            hargajual = int(input("harga jual : "))
            hargabeli = int(input("harga beli : "))
            stok = int(input("stok : "))
            produk = Produk(name,hargajual,hargabeli,stok)
            toko.TambahProduk(produk)
            print("produk berhasil di tambahkan\n")
        elif pilihan == "2":
            print("\n======Daftar Produk======")    
            toko.ListProduk()
            print("")
        elif pilihan == "3":
            name_produk = input("masukkan nama produk : ")
            produk = next((p for p in toko.DaftarProduk if p.name.lower() == name_produk.lower()), None)
            if produk:
                print("===enter untuk skip===")
                name = input("ubah nama  : ")
                hargajual = input("ubah harga jual : ")
                hargabeli = input("ubah harga beli : ")
                stok = input("ubah stok : ")
                produk.update_produk(
                    name if name else None,
                    hargajual if hargajual else None,
                    hargabeli if hargabeli else None,
                    stok if stok else None
                )
                print("produk berhasil di rubah")
            else:
                print("produk tidak ditemukan")
        elif pilihan == "4":
            name_produk = input("masukkan nama produk : ")
            produk = next((p for p in toko.DaftarProduk if p.name.lower() == name_produk.lower()),None)
            if produk:
                toko.HapusProduk(produk)
                print("produk berhasil dihapus")
            else:
                print("produk tidak ditemukan")
        
        elif pilihan == "5":
            name = input("masukkan nama pelanggan : ")
            id_pelanggan = int(input("masukkan id pelanggan : "))
            while any(pelanggan.id_pelanggan == id_pelanggan for pelanggan in toko.DaftarPelangganClass()):
                    print("id pelanggan sudah ada")
                    id_pelanggan = int(input("masukkan id pelanggan : "))
                
            pelanggan = Pelanggan(name, id_pelanggan, toko)
            toko.TambahPelanggan(pelanggan)
            print("pelangan berhasi di buat\n")

        elif pilihan == "6":
            print("\n======Daftar Pelanggan=====")
            toko.listPelanggan()
            print("\n")
        
        elif pilihan == "7":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            nama_produk = input("masukkan nama produk : ")
            jumlah = int(input("masukkan jumlah produk : "))
            pelanggan = next((pl for pl in toko.DaftarPelangganClass() if pl.id_pelanggan == id_pelanggan),None)
            produk = next((p for p in toko.DaftarProdukClass() if p.name.lower() == nama_produk.lower()), None)
            if pelanggan and produk:
                if pelanggan.TambahKeranjang(produk, jumlah):
                    print("produk berhasil di tambah ke keranjang")
                else:
                    print("jumlah stok produk kurang")

            else:
                print("produk dan pelanggan tidak di temukan")
        
        elif pilihan == "8":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            nama_produk = input("masukkan nama produk : ")
            jumlah = int(input("masukkan jumlah produk : "))
            pelanggan = next((pl for pl in toko.DaftarPelangganClass() if pl.id_pelanggan == id_pelanggan), None)
            produk = next((p for p in toko.DaftarProdukClass() if p.name.lower() == nama_produk.lower()), None)

            if pelanggan and produk:
                if pelanggan.HapusKeranjang(produk, jumlah):
                    print("produk berhasil di rubah di keranjang")
                else:
                    print("jumlah tidak memenuhi")
            else:
                print("produk tidak di temukan")
        elif pilihan == "9":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            pelanggan = next((pl for pl in toko.DaftarPelangganClass() if pl.id_pelanggan == id_pelanggan), None)
            if pelanggan:
                pelanggan.TampilkanKeranjang()
            else:
                print("pelanggan tidak di temukan")

        elif pilihan == "10":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            pelanggan = next((pl for pl in toko.DaftarPelangganClass() if pl.id_pelanggan == id_pelanggan), None)
            if pelanggan:
                pelanggan.Checkout()
            else:
                print("pelanggan tidak di temukan")
            
        elif pilihan == "11":
            print("\n======Daftar Transaksi=====")
            toko.ListTransaksi()
            print("")

if __name__ == "__main__":
    main()