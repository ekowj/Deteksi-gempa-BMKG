"""
Aplikasi Deteksi Gempa BMKG
Modularisasi dengan Function
Modularisasi dengan Package
"""
import gempaterkini

if __name__== '__main__':
    print('Aplikasi Utama')
    result = gempaterkini.ekstrasi_data()
    gempaterkini.tampilkan_data(result)
    