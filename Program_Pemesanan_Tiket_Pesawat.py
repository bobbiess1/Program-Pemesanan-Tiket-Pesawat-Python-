print("===PROGRAM PEMESANAN TIKET PESAWAT===") 
print("KELOMPOK 19 - SHIFT 3") 
print("Anggota Kelompok:") 
print("1. Akbar Maulana (0076)") 
print("2. Muhammad Habib (0077)") 
print("3. Dafiq Mafaaza Mukti (0078)") 
print("4. Fadhil Dzaki Faiz (0079)") 
print("---------------------------------") 

budget = int(input("Masukkan budget Anda (Rp): ")) 

print("\nPilih kelas penerbangan:") 

print("1. Ekonomi") 

print("2. Bisnis") 

print("3. First Class") 

kelas = int(input("Masukkan pilihan kelas (1/2/3): ")) 

if kelas == 1: 

    if budget >= 1000000: 
        print("\nKelas Ekonomi tersedia") 
        print("Maskapai pilihan : Lion Air, Citilink") 
    else:
        print("\nUang tidak mencukupi untuk kelas Ekonomi.") 

 

elif kelas == 2: 

    if budget >= 5000000: 

        print("\nKelas Bisnis tersedia") 

        print("Maskapai pilihan : Garuda Indonesia, Batik Air") 

        if budget >= 10000000: 

            print("Bonus: Lounge Access") 

    else: 

        print("\nUang tidak mencukupi untuk kelas Bisnis.") 

 

elif kelas == 3: 

    if budget >= 8000000: 

        print("\nFirst Class tersedia") 

        print("Maskapai pilihan : Singapore Airlines, Emirates") 

        if budget >= 20000000: 

            print("Bonus: Lounge Access + Hotel Gratis") 

        elif budget >= 10000000: 

            print("Bonus: Lounge Access") 

    else: 

        print("\nUang tidak mencukupi untuk First Class.") 

 

else: 

    print("\nPilihan kelas tidak valid.") 