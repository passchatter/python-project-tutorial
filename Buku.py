class Buku:
    def __init__(self, judul, penulis, tahun_terbit, jumlah_salinan):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.jumlah_salinan = jumlah_salinan
    
    def pinjam(self):
        if self.jumlah_salinan > 0:
            self.jumlah_salinan -= 1
            return True
        return False
    
    def kembali(self):
        self.jumlah_salinan += 1


class Anggota:
    def __init__(self, name, id_anggota):
        self.name = name
        self.id_anggota = id_anggota
        self.bukuDipinjam = []
    
    def PinjamBuku(self, buku):
        if buku.pinjam():
            self.bukuDipinjam.append(buku)
            return True
        return False
    
    def KembalikanBuku(self, buku):
        for b in self.bukuDipinjam:
            if b.judul == buku.judul and b.penulis == buku.penulis:
                b.kembali()
                self.bukuDipinjam.remove(b)
                return True
        return False

    def ListAnggotaBuku(self):
        for buku in self.bukuDipinjam:
            print(f"{buku.judul} oleh {buku.penulis} ({buku.tahun_terbit}) - {buku.jumlah_salinan} salinan tersedia")

class Perpustakaan:
    def __init__(self, name):
        self.name = name
        self.DaftarAnggota = []
        self.DaftarBuku = []
    
    def TambahBuku(self, buku):
        self.DaftarBuku.append(buku)
    
    def TambahAnggota(self,anggota):
        self.DaftarAnggota.append(anggota)

    def ListBuku(self):
        for buku in self.DaftarBuku:
            print(f"{buku.judul} oleh {buku.penulis} ({buku.tahun_terbit}) - {buku.jumlah_salinan} salinan tersedia")
    
    def ListAnggota(self):
        for anggota in self.DaftarAnggota:
            print(f"{anggota.name} (ID : {anggota.id_anggota})")
        
    def cariBuku(self, judul):
        hasil = []
        for buku in self.DaftarBuku:
            if judul.lower() in buku.judul.lower():
                hasil.append(buku)
        return hasil
    


def menu():
    perpustakaan = Perpustakaan("perpustakaan pusat")
    while True:
        print("\nmenu : ")
        print("1. tambah buku")
        print("2. tambah anggota")
        print("3. tampilkan buku tersedia")
        print("4. tampilkan daftar anggota")
        print("5. pinjam buku")
        print("6. kembalikan buku")
        print("7. list buku anggota")
        print("8. cari buku")
        print("9. keluar program")
        pilihan = input("masukkan menu pilihan : ")

        if pilihan == "1":
            judul = input("masukkan judul : ")
            penulis = input("masukkan penulis : ")
            tahun_terbit = int(input("masukkan tahun terbit : "))
            salinan = int(input("masukkan salinan : "))
            buku = Buku(judul,penulis,tahun_terbit,salinan)
            perpustakaan.TambahBuku(buku)
            print("Buku berhasil ditambahkan")
        elif pilihan == "2":
            name = input("masukkan nama : ")
            id_anggota = int(input("masukkan id anggota : "))
            anggota = Anggota(name, id_anggota)
            perpustakaan.TambahAnggota(anggota)
            print("anggota berhasil di tambah")
        elif pilihan == "3":
            print("\n========Buku Tersedia========")
            perpustakaan.ListBuku()
        elif pilihan == "4":
            print("=======Daftar Anggota======")
            perpustakaan.ListAnggota()
        elif pilihan == "5":
            id_anggota = int(input("masukkan id anda : "))
            judul_buku = input("masukkan judul buku : ")
            anggota = next((a for a in perpustakaan.DaftarAnggota if a.id_anggota == id_anggota), None)
            buku = next((b for b in perpustakaan.DaftarBuku if b.judul.lower() == judul_buku.lower()), None)
            if anggota and buku:
                if anggota.PinjamBuku(buku):
                    print("buku berhasil di pinjam")
                else:
                    print("strok buku habis")
            else:
                print("anggota dan buku tidak di temukan")
            
        elif pilihan == "6":
            id_anggota = int(input("masukkan id anggota : "))
            judul_buku = input("masukkan judul buku : ")
            anggota = next((a for a in perpustakaan.DaftarAnggota if a.id_anggota == id_anggota), None)
            buku = next((b for b in perpustakaan.DaftarBuku if b.judul.lower() == judul_buku.lower()), None)
            if anggota and buku:
                if anggota.KembalikanBuku(buku):
                    print("buku berhasil di kembalikan")
                else:
                    print("buku tidak ditemukan dari daftar pinjaman anggota")
            else:
                print("anggota dan judul buku tidak ditemukan")        

            
        elif pilihan == "7":
            id_anggota = int(input("input id anggota : "))
            anggota = next((a for a in perpustakaan.DaftarAnggota if a.id_anggota == id_anggota), None)
            if anggota:
                anggota.ListAnggotaBuku()
            else:
                print("id anggota tidak terdaftar")

        elif pilihan == "8":
            judul_buku = input("masukkan judul buku : ")
            hasil = perpustakaan.cariBuku(judul_buku)
            if hasil:
                print("=======Buku Ditemukan========")
                for buku in hasil:
                    print(f"{buku.judul}")
            else:
                print("buku tidak di temukan")

        

        elif pilihan == "9":
            print("terimakasi telah menggunakan perbustakaan")
            break
        else:
            print("masukkan menu yang sesuai")

menu()