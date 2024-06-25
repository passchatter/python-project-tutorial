class Nasabah:
    def __init__(self, name, saldo, id_nasabah, pin):
        self.name = name
        self.saldo = saldo
        self.id_nasabah = id_nasabah
        self.pin = pin
        self.transaksi = []
    
    def TambahSaldo(self, jumlah):
        self.saldo += jumlah
    
    def KurangSaldo(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            return True
        return False 

    def CatatTransaksi(self, detail):
        self.transaksi.append(detail)

class Bank:
    def __init__(self):
        self.DaftarNasabah = []
        
    
    def TambahNasabah(self, nasabah):
        self.DaftarNasabah.append(nasabah)
        print(f"Debug: Nasabah {nasabah.name} dengan ID {nasabah.id_nasabah} berhasil ditambahkan.")  # Debugging print statement

    def ListNasabah(self):
        if not self.DaftarNasabah:
            print("Belum ada nasabah yang terdaftar.")
        else:
            for nasabah in self.DaftarNasabah:
                print(f"{nasabah.name} => {nasabah.id_nasabah}")
        print(f"\nDebug: Total Nasabah: {len(self.DaftarNasabah)}")  # Debugging print statement
    
    def Carinasabah(self, name):
        hasil = []
        for nasabah in self.DaftarNasabah:
            if name and name.lower() in nasabah.name.lower():
                hasil.append(nasabah)
        return hasil

    def TopUpSaldo(self, id_nasabah, pin, jumlah):
        for nasabah in self.DaftarNasabah:
            if nasabah.id_nasabah == id_nasabah and nasabah.pin == pin:
                nasabah.TambahSaldo(jumlah)
                nasabah.CatatTransaksi(f"top up saldo sebesar {jumlah}")
                return
        print("nasabah tidak di temukan")
    
    def Witdrow(self, id_nasabah, pin, jumlah):
        for nasabah in self.DaftarNasabah:
            if nasabah.id_nasabah == id_nasabah and nasabah.pin == pin:
                nasabah.KurangSaldo(jumlah)
                nasabah.CatatTransaksi(f"withdraw saldo sebesar {jumlah}")
                return True
            return False
        print("nasabah tidakdi temukan")


    def InfoNasabah(self, id_nasabah, pin):
        for nasabah in self.DaftarNasabah:
            if nasabah.id_nasabah == id_nasabah and nasabah.pin == pin:
                print("\n")
                print(f"nama : {nasabah.name}")
                print(f"saldo : {nasabah.saldo}")
                for transaksi in nasabah.transaksi:
                    print(f"-{transaksi}")
                print("\n")
                return
        print("nasama atau pin salah")
    
    def InfoNasabahTransaksi(self, id_penerima):
        for nasabah in self.DaftarNasabah:
            if nasabah.id_nasabah == id_penerima:
                print(f"name : {nasabah.name}")
                return
        return False
    
    def Transfer(self, id_nasabah, pin, jumlah, id_penerima):
        pengirim_valid = False
        penerima_valid = False 
        nasabah_pengirim = None
        nasabah_penerima = None

        for nasabah in self.DaftarNasabah:
            if nasabah.id_nasabah == id_nasabah and nasabah.pin == pin:
                pengirim_valid = True
                nasabah_pengirim = nasabah
                
                if not nasabah.KurangSaldo(jumlah):
                    print("saldo tidak cukup")
                    return

            if nasabah.id_nasabah == id_penerima:
                penerima_valid = True
                nasabah_penerima = nasabah

            if pengirim_valid and penerima_valid:
                break
        
        if not nasabah_pengirim:
            print("transaksi gagal pin atau id_nasabah salah")
            return
        
        if not nasabah_penerima:
            print("id_penerima salah tidak ditemukan")
            nasabah_pengirim.TambahSaldo(jumlah)
            return
        
        print(f"apakah anda yakin transfer {jumlah} ke {nasabah_penerima.name} ID({id_penerima})")
        konfirmasi = input("pilih y/n : ")
        if konfirmasi != "y":
            print("tranber dibatalkan")
            nasabah_pengirim.TambahSaldo(jumlah)
            return
        
        nasabah_penerima.TambahSaldo(jumlah)
        nasabah_penerima.CatatTransaksi(f"menerima transer sebesar {jumlah} dari {nasabah_pengirim.name} ID : {id_nasabah}")
        nasabah_pengirim.CatatTransaksi(f"transfer sebesar {jumlah} ke {nasabah_penerima.name} ID : {id_penerima}")
        print("Transfer berhasil.")
        print("")


def main():
    bank = Bank()
    while True:
        print("1. Tambah Nasabah")
        print("2. List Nasabah")
        print("3. Cari Nasabah")
        print("4. Infor Nasabah")
        print("5. tambah saldo")
        print("6. Withdraw")
        print("7. Transfer")
        pilihan = input("masukkan pilihan : ")

        if pilihan == "1":
            name = input("masukkan nama anda : ")
            saldo = int(input("minimal saldo = 200000 : "))
            while saldo < 200000:
                print("Saldo kurang dari 200000. Silakan masukkan saldo yang benar.")
                saldo = int(input("minimal saldo = 200000 : "))
            id_nasabah = int(input("masukkan id nasabah : "))
            pin = int(input("masukkan pin : "))
            nasabah = Nasabah(name, saldo, id_nasabah, pin)
            bank.TambahNasabah(nasabah)
            print("Nasabah berhasil terdaftar")
        
        elif pilihan == "2":
            print("\n======== Daftar Nasabah ======== ")
            bank.ListNasabah()
            print("")
        
        elif pilihan == "3":
            print("======Cari Nasabah======")
            name = input("masukkan nama nasabah : ")
            hasil = bank.Carinasabah(name)
            if hasil:
                print("\n========nasabah yang ditemukan========")
                for nasabah in hasil:
                    print(f"{nasabah.name} => {nasabah.id_nasabah}")
                print("")
            else:
                print("nasabah tidak ditemukan")
            
        elif pilihan == "4":
            print("========Info Nasabah========")
            id_nasabah = int(input("masukkan id nasabah : "))
            pin = int(input("masukkan pin : "))
            bank.InfoNasabah(id_nasabah, pin)
        
        elif pilihan == "5":
            print("========Tambah Saldo========")
            id_nasabah = int(input("masukkan id nasabah : "))
            pin = int(input("masukkan pin nasabah : "))
            jumlah = int(input("masukkan nominal : "))
            bank.TopUpSaldo(id_nasabah, pin, jumlah)
            print("saldo berhasil di tambahkan")
        
        elif pilihan == "6":
            print("======Withdrow Saldo======")
            id_nasabah = int(input("masukkan id nasabah : "))
            pin = int(input("masukkan pin : "))
            jumlah = int(input("masukkan jumlah : "))
            if bank.Witdrow(id_nasabah, pin, jumlah):
                print("saldo berhasil di tarik")
            else:
                print("maaf saldo tidak cukup")
        
        elif pilihan == "7":
            print("========Transfer========")
            id_nasabah = int(input("id nasabah : "))
            pin = int(input("masukkan pin : "))
            id_penerima = int(input("id penerima : "))
            jumlah = int(input("jumlah : "))
            bank.Transfer(id_nasabah, pin, jumlah, id_penerima)

        

if __name__ == "__main__":
    main()
