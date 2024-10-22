#Menghitung IPS
def hitung_ips(mutu, sks):
    #Menghitung total bobot
    total_mutu_sks = ((mutu{0} * 2)) + (mutu{1} * 2) + (mutu{3} * 3) + (mutu{4} * 4) + (mutu{5} * 3) +(mutu{6} * 4)
    ips = total_mutu_sks / 20 #Total SKS  tetap 20 seperti di rumus return ips
    
    #Fungsi untuk menentukan status kelulusan
    def status_kelulusan(ips):
        if ips >=2.75:
            return "Tetap"
        elif 2.00 > ips > 2.75:
            