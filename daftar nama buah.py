def tampilkan_daftar_buah(nama_toko, *daftar_buah):
    print(nama_toko)
    print("Buah yang anda beli adalah:")
    for index, buah in enumerate(daftar_buah, start=1):
        print(f"{index}. {buah}")
    print("Terimakasih sudah beli disini dan sehat selalu")


tampilkan_daftar_buah("Toko Buah Unjaya Jaya Jaya Jos Yogyakarta", "Apel", "Semangka", "Jeruk", "Anggur")
