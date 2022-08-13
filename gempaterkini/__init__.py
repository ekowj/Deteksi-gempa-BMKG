def ekstrasi_data():
    """
        Tanggal: 12 Agustus 2022
        Wqktu: 12:25:02 WIB
        Magnitudo: 3.6
        Kedalaman: 4 km
        Lokasi: 3.74 LS - 119.54 BT
        Pusat gempa: Pusat Gempa berada di darat 10 km BaratDaya Pinrang
        Dirasakan: Dirasakan (Skala MMI): II-III Pinrang
        :return:
    """
    hasil = dict()
    hasil ['tanggal'] = '12 Agustus 2022'
    hasil ['waktu'] = '12:25:52 WIB'
    hasil ['magnitudo'] = 3.6
    hasil ['kedalaman'] = 4.0
    hasil ['lokasi'] ={'ls': 3.74, 'bt': 119.54}
    hasil ['pusat'] = 'Pusat Gempa berada di darat 10 km BaratDaya Pinrang'
    hasil ['dirasakan'] = 'Dirasakan (Skala MMI): II-III Pinrang'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print (f"Tanggal      : {result['tanggal']}")
    print (f"Waktu        : {result['waktu']}")
    print (f"Magnitudo    : {result['magnitudo']}")
    print (f"Kedalaman    : {result['kedalaman']}")
    print (f"Lokasi       : LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print (f"Pusat Gempa  : {result['pusat']}")
    print (f"Dirasakan    : {result['dirasakan']}")

