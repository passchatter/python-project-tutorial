class Produk:
    def __init__(self, name, harga, stok):
        self.name = name
        self.harga = harga
        self.stok = stok
    
    def tambah_stok(self, jumlah):
        self.stok += jumlah
    
    def kurang_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False

class Pelanggan:
    def __init__(self, name, id_pelanggan):
        self.name = name
        self.id_pelanggan = id_pelanggan
        self.keranjang = {}
    
    def tambah_keranjang(self, produk, jumlah):
        if produk.kurang_stok(jumlah):
            if produk in self.keranjang:
                self.keranjang[produk] += jumlah
            else:
                self.keranjang[produk] = jumlah
            return True
        return False
    
    def hapus_keranjang(self, produk, jumlah):
        if produk in self.keranjang and self.keranjang[produk] >= jumlah:
            self.keranjang[produk] -= jumlah
            if self.keranjang[produk] <= 0:
                del self.keranjang[produk]
            produk.tambah_stok(jumlah)
            return True
        return False

    def TampilkanKeranjang(self):
        if not self.keranjang.items():
            print("keranjang kosong silahkan pilih produk")
        else:
            print(f"isi keranjang {self.name} (ID : {self.id_pelanggan})")
            for produk, jumlah in self.keranjang.items():
                print(f"{produk.name}, => {jumlah}")

    def checkout(self):
        total = sum(produk.harga * jumlah for produk, jumlah in self.keranjang.items())
        self.keranjang.clear()
        print(f"terimakasih telah berbelanjan total = {total}")

class Toko:
    def __init__(self, name):
        self.name = name
        self.DaftarProduk = []
        self.DaftarPelanggan = []
    
    def TambahProduk(self, produk):
        self.DaftarProduk.append(produk)
    
    def TambahPelanggan(self, pelanggan):
        self.DaftarPelanggan.append(pelanggan)
    
    def ListProduk(self):
        for produk in self.DaftarProduk:
            print(f"{produk.name}, => Rp. {produk.harga} = {produk.stok}")
    
    def ListPelanggan(self):
        for pelanggan in self.DaftarPelanggan:
            print(f"{pelanggan.name} (ID : {pelanggan.id_pelanggan})")


def main():
   toko = Toko("nadi mark")
   while True:
        print("1. tambah produk")
        print("2. tambah pelanggan")
        print("3. tampilkan produk")
        print("4. tampilkan pealanggan")#
        print("5. tambah keranjang")
        print("6. hapus keranjang")
        print("7. tampilkan keranjang")
        print("8. checkout")
        print("0. close program")
        pilihan = input("masukkan nomor menu : ")

        if pilihan == "1":
            name = input("masukkan nama produk : ")
            harga = int(input("masukkan harga produk : "))
            stok = int(input("masukkan jumlah stol : "))
            produk = Produk(name, harga, stok)
            toko.TambahProduk(produk)
        elif pilihan == "2":
            name = input("masukkan nama pelanggan : ")
            id_pelanggan = int(input("masukkan id pelanggan : "))
            pelanggan = Pelanggan(name, id_pelanggan)
            toko.TambahPelanggan(pelanggan)
        elif pilihan == "3":
            print("\n======Daftar Produk======")
            toko.ListProduk()
            print("")
        elif pilihan == "4":
            print("\n======Daftar Pelanggan======")
            toko.ListPelanggan()
            print("")
        elif pilihan == "5":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            nama_produk = input("masukkan nama produk : ")
            julmah = int(input("masukkan jumlah : "))
            pelanggan = next((pl for pl in toko.DaftarPelanggan if pl.id_pelanggan == id_pelanggan), None)
            produk = next((p for p in toko.DaftarProduk if p.name.lower() == nama_produk.lower()), None)
            if produk and pelanggan:
                if pelanggan.tambah_keranjang(produk, julmah):
                    print("produk berhasil di tambahkan ke keranjang")
                else:
                    print("stok produk habis")
            else:
                print("produk dan pelanggan tidak di temukan")
        
        elif pilihan == "6":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            nama_produk = input("masukkan nama produk : ")
            jumlah = int(input("masukkan jumlah stok : "))
            pelanggan = next((pl for pl in toko.DaftarPelanggan if pl.id_pelanggan == id_pelanggan), None)
            produk = next((p for p in toko.DaftarProduk if p.name.lower() == nama_produk.lower()), None)
            if produk and pelanggan:
                if pelanggan.hapus_keranjang(produk, jumlah):
                    print("produk berhasil di rubah")
                else:
                    print("produk tidak di temukan")
            else:
                print("produk dan pelanggan tidak di temukan")

        elif pilihan == "7":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            pelanggan = next((pl for pl in toko.DaftarPelanggan if pl.id_pelanggan == id_pelanggan), None)
            if pelanggan:
                pelanggan.TampilkanKeranjang()
            else:
                print("pelanggan tidak di temukan")
        elif pilihan == "8":
            id_pelanggan = int(input("masukkan id pelanggan : "))
            pelanggan = next((pl for pl in toko.DaftarPelanggan if pl.id_pelanggan == id_pelanggan), None)
            if pelanggan:
                pelanggan.checkout()
            else:
                print("pelanggan tidak di temukan")

        elif pilihan == "0":
            print("terimakasih telah mengunjungi toko kami")
            break
        else:
            print("masukkan nomor menu yang sesuai")
    
main()