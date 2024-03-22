def Mobil(nama, **biodata):
    """Fungsi untuk mencetak informasi tentang mobil"""
    print("Nama Mobil:", nama)
    print("Versi:", biodata['versi'])
    print("Tahun:", biodata['tahun'])
    print("Rakitan:", biodata['rakitan'])


corolla = {'tahun': 1999, 'versi': "Cross", 'rakitan': "Thailand"}
Mobil("Corolla", **corolla)
