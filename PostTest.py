Cnama = input("Nama : ")
Cnim = int(input("NIM : "))
Cpass = input("Password : ")

if Cnama == "Ana" and Cnim == 2399016102 and Cpass == "Cantik":
    print("Menetukan Volume Bangun Ruang")
    print("1.Bola")
    print("2.Tabung")
    print("3.Limas Segitiga")
    phi = 3.14
    Pilihan = int(input("Masukkan Pilihan Menu : "))
    if Pilihan == 1:
        jari = int(input("Nilai Jari : "))
        volume = 4/3*phi*(jari*jari*jari)
        print("Volume Bola : ",volume )
    elif Pilihan == 2:
        jari = int(input("Nilai Jari : "))
        tinggi = int(input("Nilai Tinggi : "))
        volume = phi*(jari*jari)*tinggi
        print("volume tabung : ",volume)
    elif Pilihan == 3:
        luasAlas = int(input("Nilai luas alas : "))
        tinggiLimas = int(input("Nilai tinggi limas : "))
        volume = 1/3*luasAlas*tinggiLimas
        print("volume limas segitiga : ",volume)
    else:
        print("tidak ada pilihan")