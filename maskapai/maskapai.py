class Penerbangan:
    def __init__(self, id_penerbangan, tujuan, kapasitas):
        self.id_penerbangan = id_penerbangan
        self.tujuan = tujuan
        self.kapasitas = kapasitas
        self.kursi_penumpang = []
    
    def PesanKursi(self, penumpang):
        if len(self.kursi_penumpang) < self.kapasitas:
            self.kursi_penumpang.append(penumpang)
            return True
        return False
    
    def BatasKursi(self, penumpang):
        if penumpang in self.kursi_penumpang:
            self.kursi_penumpang.remove(penumpang)
            return True
        return False
    
    def TampilkanPenumpang(self):
        for penumpang in self.kursi_penumpang:
            print(f"{penumpang.name} ID => {penumpang.id_paspor}")


class Penumpang:
    def __init__(self, name, id_paspor) -> None:
        self.name = name
        self.id_paspor = id_paspor

class Maskapai:
    def __init__(self):
        self.penerbangan = []
        self.penumpang = []
    
    def TambahPenerbangan(self, penerbangan):
        self.penerbangan.append(penerbangan)
    
    def TambahPenumpang(self, penumpang):
        self.penumpang.append(penumpang)
    
    def ListPenerbangan(self):
        for penerbangan in self.penerbangan:
            print(f"{penerbangan.id_penerbangan} tujuan ke {penerbangan.tujuan} = {penerbangan.kapasitas}")
    
        

def main():
    maskapai = Maskapai()
    while True:
        print("1. tambah penerbangan")
        print("2. tambah penumpang")
        print("3. list penerbangan")
        print("4. pesan tiket")
        print("5. batalkan tiket")
        print("6. tampilkan penumpang")
        pilihan = input("masukkan menu pilihan : ")

        if pilihan == "1":
            id_penerbangan = int(input("masukkan id penerbangan : "))
            tujuan = input("masukkan tujuan penerbangan : ")
            kapasitas = int(input("masukkan kapasitas : "))
            penerbangan = Penerbangan(id_penerbangan, tujuan, kapasitas)
            maskapai.TambahPenerbangan(penerbangan)
            print("========Penerbangan Berhasil Dibuat========")
        
        elif pilihan == "2":
            name = input("masukkan nama : ")
            id_paspor = int(input("masukkan id paspor : "))
            penumpang = Penumpang(name, id_paspor)
            maskapai.TambahPenumpang(penumpang)
            print("========Penumpang Berhasil Terdaftar========")

        elif pilihan == "3":
            print("\n========Daftar Penerbangan========")
            maskapai.ListPenerbangan()
            print("")

        elif pilihan == "4":
            print("========Pesan Tiket========")
            id_penerbangan = int(input("masukkan id penerbangan : "))
            id_paspor = int(input("masukkan id pasport : "))
            penerbangan = next((p for p in maskapai.penerbangan if p.id_penerbangan == id_penerbangan), None)
            paspor = next((p for p in maskapai.penumpang if p.id_paspor == id_paspor), None)
            if penerbangan and paspor:
                if penerbangan.PesanKursi(paspor):
                    print("tiket berhasil di pesan")
                else:
                    print("kapasista sudah penuh")
            else:
                print("penerbangan atau penumpang tidak terdaftar")

        elif pilihan == "5":
            id_penerbangan = int(input("masukkan id penerbangan : "))
            id_paspor = int(input("masukkan id paspor : "))
            penerbangan = next((p for p  in maskapai.penerbangan if p.id_penerbangan == id_penerbangan), None)
            paspor = next((p for p in maskapai.penumpang if p.id_paspor == id_paspor), None)
            if penerbangan and paspor:
                if penerbangan.BatasKursi(paspor):
                    print("tiket berhasil dibatalkan")
                else:
                    print("sistem error silahkan hubungi 1123")
            else:
                print("penerbangan atau penumpang tidak terdaftar")
            
        elif pilihan == "6":
            id_penerbangan = int(input("masukkan id penerbangan : "))
            penerbangan = next((p for p in maskapai.penerbangan if p.id_penerbangan == id_penerbangan), None)
            if penerbangan:
                print("========Daftar Penumpang=========")
                print(f"tujuan penerbangan ke {penerbangan.tujuan}")
                penerbangan.TampilkanPenumpang()
                print("")
            else:
                print("penerbagan tidak ti temukan")

main()