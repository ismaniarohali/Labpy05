daftarkontak = {"Nama": "Nomor Telepon"}
kontak = {'Syifa': '089662917109', 'Melati': '085897061641'}

print("="*30)
print("   Nama     |    Nomor Telepon   ")
print("="*30)
print(" # Syifa   |   ", kontak['Syifa'])
print(" # Melati  |   ", kontak['Melati'])
print("="*30)

# Menampilkan kontak Syifa
print("Menampilkan kontak Syifa")
print("="*30)
print(" # Syifa   |   ", kontak['Syifa'])
print("="*30)

# Menambahkan kontak dengan nama Dodi dan nomor 0865454434
print("Menambah kontak dengan nama Dodi dan nomor 0865454434 ")
kontak['Dodi'] = '0865454434'
print("="*30)
print("  Dodi   |   ", kontak['Dodi'])
print("="*30)

# Mengubah kontak Amel dengan nomor baru 089670700776
print("Mengubah kontak Amel dengan nomor baru 089670700776 ")
kontak['Amel'] = '089670700776'
print("="*30)
print(" # Amel  |   ", kontak['Amel'])
print("="*30)

# Menampilkan semua nama
print("Menampilkan semua nama")
print("="*30)
print(kontak.keys())
print("="*30)

# Menampilkan semua nomor
print("Menampilkan semua nomor")
print("="*30)
print(kontak.values())
print("="*30)

# Menampilkan semua daftar kontak beserta nama dan nomornya
print("Menampilkan daftar nama dan nomor")
print("="*30)
print(kontak.items())
print("="*30)

# Menghapus kontak Amel
print("Hapus kontak Amel")
kontak.pop('Amel')
print("="*30)
print(kontak.items())
print("="*30)
