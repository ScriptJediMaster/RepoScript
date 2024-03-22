def main():
    daftar_nama = []
    input_nama = input("Masukkan Nama?\nya/tidak : ")
    index = 1
    while input_nama.lower() == 'ya':
        nama = input("Nama : ")
        daftar_nama.append(nama)
        input_nama = input("Masukkan Nama?\nya/tidak : ")
        index += 1

    print("Beberapa nama yang telah dimasukkan:")
    for i, nama in enumerate(daftar_nama, start=1):
        print(f"Nama {i} adalah {nama}")

if __name__ == "__main__":
    main()
