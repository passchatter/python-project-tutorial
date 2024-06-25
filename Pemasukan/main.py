from datetime import datetime
from collections import defaultdict

class Transaksi:
    def __init__(self, tanggal, jumlah, keterangan, tipe):
        self.tanggal = tanggal
        self.jumlah = jumlah
        self.keterangan = keterangan
        self.tipe = tipe  # 'pemasukan' atau 'pengeluaran'

class Anggaran:
    def __init__(self, total_anggaran):
        self.total_anggaran = total_anggaran
        self.pengeluaran = 0

    def tambah_pengeluaran(self, jumlah):
        self.pengeluaran += jumlah

    def sisa_anggaran(self):
        return self.total_anggaran - self.pengeluaran

    def saran_penghematan(self):
        if self.pengeluaran > self.total_anggaran:
            return f"Anda telah melebihi anggaran. Kurangi pengeluaran sebesar {self.pengeluaran - self.total_anggaran}."
        elif self.pengeluaran > 0.75 * self.total_anggaran:
            return f"Anda mendekati batas anggaran. Pertimbangkan untuk menghemat {self.total_anggaran - self.pengeluaran}."
        else:
            return "Pengeluaran Anda masih dalam batas anggaran."

class Pengguna:
    def __init__(self, nama):
        self.nama = nama
        self.transaksi = []
        self.anggaran = None

    def set_anggaran(self, anggaran):
        self.anggaran = anggaran

    def catat_transaksi(self, transaksi):
        self.transaksi.append(transaksi)
        if transaksi.tipe == 'pengeluaran' and self.anggaran:
            self.anggaran.tambah_pengeluaran(transaksi.jumlah)

    def laporan_bulanan(self, bulan, tahun):
        pemasukan = 0
        pengeluaran = 0
        for transaksi in self.transaksi:
            if transaksi.tanggal.month == bulan and transaksi.tanggal.year == tahun:
                if transaksi.tipe == 'pemasukan':
                    pemasukan += transaksi.jumlah
                elif transaksi.tipe == 'pengeluaran':
                    pengeluaran += transaksi.jumlah
        return pemasukan, pengeluaran

    def tampilkan_saran_penghematan(self):
        if self.anggaran:
            return self.anggaran.saran_penghematan()
        return "Anggaran belum diatur."

def main():
    pengguna = Pengguna("User")

    while True:
        print("1. Set Anggaran")
        print("2. Catat Pemasukan")
        print("3. Catat Pengeluaran")
        print("4. Laporan Bulanan")
        print("5. Saran Penghematan")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            total_anggaran = float(input("Masukkan total anggaran: "))
            anggaran = Anggaran(total_anggaran)
            pengguna.set_anggaran(anggaran)
            print("Anggaran berhasil diatur.")

        elif pilihan == "2":
            tanggal = datetime.strptime(input("Masukkan tanggal (YYYY-MM-DD): "), "%Y-%m-%d")
            jumlah = float(input("Masukkan jumlah pemasukan: "))
            keterangan = input("Masukkan keterangan: ")
            transaksi = Transaksi(tanggal, jumlah, keterangan, 'pemasukan')
            pengguna.catat_transaksi(transaksi)
            print("Pemasukan berhasil dicatat.")

        elif pilihan == "3":
            tanggal = datetime.strptime(input("Masukkan tanggal (YYYY-MM-DD): "), "%Y-%m-%d")
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            keterangan = input("Masukkan keterangan: ")
            transaksi = Transaksi(tanggal, jumlah, keterangan, 'pengeluaran')
            pengguna.catat_transaksi(transaksi)
            print("Pengeluaran berhasil dicatat.")

        elif pilihan == "4":
            bulan = int(input("Masukkan bulan (1-12): "))
            tahun = int(input("Masukkan tahun (YYYY): "))
            pemasukan, pengeluaran = pengguna.laporan_bulanan(bulan, tahun)
            print(f"Laporan Bulanan {bulan}/{tahun}:")
            print(f"Pemasukan: {pemasukan}")
            print(f"Pengeluaran: {pengeluaran}")

        elif pilihan == "5":
            saran = pengguna.tampilkan_saran_penghematan()
            print(saran)

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
