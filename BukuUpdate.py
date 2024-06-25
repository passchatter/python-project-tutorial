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

    def kembalikan(self):
        self.jumlah_salinan += 1

    def __str__(self):
        return f"{self.judul} oleh {self.penulis} ({self.tahun_terbit}) - {self.jumlah_salinan} salinan tersedia"

class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.buku_dipinjam.append(buku)
            return True
        return False

    def kembalikan_buku(self, buku):
        for b in self.buku_dipinjam:
            if b.judul == buku.judul and b.penulis == buku.penulis:
                b.kembalikan()
                self.buku_dipinjam.remove(b)
                return True
        return False

    def __str__(self):
        return f"{self.nama} (ID: {self.id_anggota})"

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.anggota_terdaftar = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def daftar_buku_tersedia(self):
        for buku in self.daftar_buku:
            print(buku)

    def tambah_anggota(self, anggota):
        self.anggota_terdaftar.append(anggota)

    def tampilkan_daftar_anggota(self):
        for anggota in self.anggota_terdaftar:
            print(anggota)

    def cari_buku(self, judul=None, penulis=None):
        hasil = []
        for buku in self.daftar_buku:
            if (judul and judul.lower() in buku.judul.lower()) or (penulis and penulis.lower() in buku.penulis.lower()):
                hasil.append(buku)
        return hasil

# Fungsi untuk interaksi dengan pengguna
def menu():
    perpustakaan = Perpustakaan("Perpustakaan Pusat")

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Tambah Anggota")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Tampilkan Buku Tersedia")
        print("6. Tampilkan Daftar Anggota")
        print("7. Cari Buku")
        print("8. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan penulis buku: ")
            tahun = int(input("Masukkan tahun terbit: "))
            salinan = int(input("Masukkan jumlah salinan: "))
            buku = Buku(judul, penulis, tahun, salinan)
            perpustakaan.tambah_buku(buku)
            print("Buku berhasil ditambahkan!")

        elif pilihan == "2":
            nama = input("Masukkan nama anggota: ")
            id_anggota = int(input("Masukkan ID anggota: "))
            anggota = Anggota(nama, id_anggota)
            perpustakaan.tambah_anggota(anggota)
            print("Anggota berhasil ditambahkan!")

        elif pilihan == "3":
            id_anggota = int(input("Masukkan ID anggota: "))
            judul_buku = input("Masukkan judul buku yang ingin dipinjam: ")
            anggota = next((a for a in perpustakaan.anggota_terdaftar if a.id_anggota == id_anggota), None)
            buku = next((b for b in perpustakaan.daftar_buku if b.judul.lower() == judul_buku.lower()), None)
            if anggota and buku:
                if anggota.pinjam_buku(buku):
                    print("Buku berhasil dipinjam!")
                else:
                    print("Stok buku tidak mencukupi!")
            else:
                print("Anggota atau buku tidak ditemukan!")

        elif pilihan == "4":
            id_anggota = int(input("Masukkan ID anggota: "))
            judul_buku = input("Masukkan judul buku yang ingin dikembalikan: ")
            anggota = next((a for a in perpustakaan.anggota_terdaftar if a.id_anggota == id_anggota), None)
            buku = next((b for b in perpustakaan.daftar_buku if b.judul.lower() == judul_buku.lower()), None)
            if anggota and buku:
                if anggota.kembalikan_buku(buku):
                    print("Buku berhasil dikembalikan!")
                else:
                    print("Buku tidak ditemukan dalam daftar pinjaman anggota!")
            else:
                print("Anggota atau buku tidak ditemukan!")

        elif pilihan == "5":
            print("\nBuku yang tersedia:")
            perpustakaan.daftar_buku_tersedia()

        elif pilihan == "6":
            print("\nDaftar Anggota Perpustakaan:")
            perpustakaan.tampilkan_daftar_anggota()

        elif pilihan == "7":
            judul = input("Masukkan judul buku (kosongkan jika tidak mencari berdasarkan judul): ")
            penulis = input("Masukkan penulis buku (kosongkan jika tidak mencari berdasarkan penulis): ")
            hasil = perpustakaan.cari_buku(judul if judul else None, penulis if penulis else None)
            if hasil:
                print("\nBuku yang ditemukan:")
                for buku in hasil:
                    print(buku)
            else:
                print("Buku tidak ditemukan!")

        elif pilihan == "8":
            print("Terima kasih telah menggunakan sistem perpustakaan!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan fungsi menu untuk interaksi dengan pengguna
menu()
