def DevidenYeild(hargaDeviden, HargaBeli):
    return hargaDeviden/HargaBeli * 100

def Keuntungan(hargajual, hargabeli):
    if hargajual > hargabeli:
        return (hargajual - hargabeli) / hargabeli * 100
    else:
        return (hargabeli - hargajual) / hargabeli * 100

while True:
    print("1. hitung pendapatan")
    print("2. hitung deviden")
    pilihan = input("masukkan nomor menu : ")
    if pilihan == "1":
        hargabeli = float(input("masukkan harga beli : "))
        hargajual = float(input("masukkan harga jual : "))
        hasil = Keuntungan(hargajual, hargabeli)
        print(f"keuntungan = {hasil:.2f}")     
    elif pilihan == "2":
        deviden = float(input("masukkan harga deviden : "))
        harga = float(input("masukkan avarege anda : "))
        hasil = DevidenYeild(deviden, harga)
        print(f"keuntungan deviden = {hasil:.2f}")



