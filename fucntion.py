def profil(nama, alamat, gender, umur, hoby):
    print("nama saya adalah", nama)
    print("alamat saya", alamat)
    print(gender)
    print("saya berrmur", umur)
    print("hoby saya adalah", hoby)
profil("Ima", "Jagakarsa", "laki-laki", "17 tahun", "Nonton Jkt48")


def tentukan_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

# Contoh penggunaan:
nilai = 70
print(tentukan_kelulusan(nilai))

def cetak_bilangan_ganjil(batas):
    for nilai in range(1, batas + 1, 2):
        print(nilai)

# Contoh penggunaan:
batas_tertinggi = 200
cetak_bilangan_ganjil(batas_tertinggi)