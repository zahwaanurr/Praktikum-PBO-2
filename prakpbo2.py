def hitung_keliling(sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3
    return keliling

def hitung_luas(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def main():
    print("Program untuk menghitung keliling dan luas segitiga")
    print("1. Keliling")
    print("2. Luas")
    opsi = input("Masukkan pilihan: ")

    if opsi == '1':
        sisi1 = float(input("Masukkan sisi 1 : "))
        sisi2 = float(input("Masukkan sisi 2 : "))
        sisi3 = float(input("Masukkan sisi 3 : "))

        if (sisi1 + sisi2 > sisi3) and (sisi2 + sisi3 > sisi1) and (sisi1 + sisi3 > sisi2):
            keliling = hitung_keliling(sisi1, sisi2, sisi3)
            print("Keliling segitiga adalah:", keliling, "cm")
        else:
            print("\nSegitiga dengan panjang sisi yang dimasukkan tidak valid.")

    elif opsi == '2':
        alas = float(input("Masukkan alas : "))
        tinggi = float(input("Masukkan tinggi : "))
        luas = hitung_luas(alas, tinggi)
        print("Luas segitiga adalah:", luas, "cm^2")

    else:
        print("Opsi yang dimasukkan tidak valid.")

if __name__ == "__main__":
    main()

print("Terimakasih telah menggunakan program ini")
