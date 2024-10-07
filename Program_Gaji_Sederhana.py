# Mendefinisikan kamus untuk menyimpan upah per jam untuk setiap golongan 
upah_golongan = {
    'A' : 5000,
    'B' : 7000,
    'C' : 8000,
    "D" : 10000
}

# Mendefinisikan fungsi untuk menghitung upah lembur
def hitung_lembur (jam_kerja):
    if jam_kerja > 48:
        return (jam_kerja - 48) * 4000
    else :
        return 0
    
# Mendefinisikan fungsi untuk menghitung total gaji
def hitung_gaji(nama_karyawan, golongan, jam_kerja):
    upah_per_jam = upah_golongan[golongan]
    upah_lembur = hitung_lembur(jam_kerja)
    total_gaji = upah_per_jam * jam_kerja + upah_lembur
    return nama_karyawan, total_gaji

#Meminta input dari pengguna
nama_karyawan = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan karyawan (A, B, C, atau D): ")
jam_kerja = int(input("Masukkan jumlah jam kerja karyawan   :"))

# Validasi input golongan
if golongan not in upah_golongan:
    print("Golongan tidak valid. Harap masukkan A, B, C, atau D.")
else:
    # Validasi input jam kerja
    if jam_kerja < 0:
        print ("Jumlah jam kerja tidak valid. Jam kerja tidak bisa negatif.") 
    else:
        # Menghitung dan menampilkan total gaji 
        nama_karyawan, total_gaji = hitung_gaji(nama_karyawan, golongan, jam_kerja)
        print(f"Gaji {nama_karyawan} adalah Rp {total_gaji:,}")   