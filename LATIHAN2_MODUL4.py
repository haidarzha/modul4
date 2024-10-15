def tahun_kabisat(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

def jumlah_hari(bulan, tahun):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return 31

print("-1 to stop the program")

while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    
    if bulan == -1:
        print("Program berhenti.")
        break
    
    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid. Masukkan bulan (1-12) atau -1 untuk berhenti.")
        continue
    
    tahun = int(input("Masukkan tahun (contoh: 2023): "))
    
    hari = jumlah_hari(bulan, tahun)
    print(f"Terdapat {hari} hari dalam bulan tersebut.")
