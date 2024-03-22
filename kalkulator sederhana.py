def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a / b if b != 0 else "Tidak bisa melakukan pembagian dengan nol"

def penambahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def main():
    while True:
        print("Menu Kalkulator:")
        print("1. Perkalian")
        print("2. Pembagian")
        print("3. Penambahan")
        print("4. Pengurangan")
        print("5. Stop")

        pilihan = input("Masukkan pilihan Anda (1/2/3/4/5): ")

        if pilihan == '5':
            print("Program dihentikan.")
            break

        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print("Hasil perkalian:", perkalian(angka1, angka2))
        elif pilihan == '2':
            print("Hasil pembagian:", pembagian(angka1, angka2))
        elif pilihan == '3':
            print("Hasil penambahan:", penambahan(angka1, angka2))
        elif pilihan == '4':
            print("Hasil pengurangan:", pengurangan(angka1, angka2))
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()