#Menampilkan Data Mahasiswa
putri_nama = "putri"
putri_umur = 18
putri_program_studi = "Sistem Informasi"
putri_jenis_kelamin = "Laki-laki"
putri_tinggi = 170
putri_kelas = "SI-3B"
putri_lulus = False

putri_nama = "putri"
putri_umur = 22
putri_tinggi = 175
putri_kelas = "SI-3C"
putri_lulus = True

print ("Nama:", putri_nama)
print ("Umur:", putri_umur, "tahun")
print ("Tinggi Badan:", putri_tinggi, "cm")
print ("Program Studi:", putri_program_studi)
print ("Kelas:", putri_kelas)
print ("Jenis Kelamin:", putri_jenis_kelamin)

if putri_lulus:
   print ("Status: Alumni")
else:
   print ("Status: Mahasiswa aktif")    