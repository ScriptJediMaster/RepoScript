def tampilkan_profil_mahasiswa(Nama, NIM, Prodi, Hobi):
    print("Profile Mahasiswa UNIV UNJAYA YOGYAKARTA")
    print("Mahasiswa Prodi {0} UNIV UNJAYA YOGYAKARTA".format(Prodi))
    print("Dengan nama {0}".format(Nama))
    print("Mempunyai NIM {0}".format(NIM))
    print("Memiliki Hobi {0}".format(Hobi))


data_mahasiswa = {
    'Nama': 'RESTU ANGGIT GUMILAR',
    'NIM': '232102009',
    'Prodi': 'S1 INFORMATIKA',
    'Hobi': 'REBAHAN SANTUY'
}

tampilkan_profil_mahasiswa(**data_mahasiswa)
