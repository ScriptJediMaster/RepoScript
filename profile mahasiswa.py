def tampilkan_profil_mahasiswa(Nama, NIM, Prodi, Hobi):
    print("[91mProfile Mahasiswa UNJAYA YOGYAKARTA")
    print("Mahasiswa Prodi {0}  UNJAYA YOGYAKARTA".format(Prodi))
    print("Dengan nama {0}".format(Nama))
    print("Mempunyai NIM {0}".format(NIM))
    print("Memiliki Hobi {0}".format(Hobi))

# Data Mahasiswa
data_mahasiswa = {
    'Nama': 'Restu Anggit Gumilar',
    'NIM': '232102009',
    'Prodi': 'Teknik Informatika',
    'Hobi': 'Memancing'
}

# Menampilkan profil mahasiswa
tampilkan_profil_mahasiswa(**data_mahasiswa)
