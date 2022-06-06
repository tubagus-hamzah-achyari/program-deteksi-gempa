"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCITION
"""
def ekstraksi_data():
    """
    Tanggal: 03 Juni 2022
    Waktu: 07:04:47 WIB
    MAgnitudo: 2.6
    Kedalaman: 10 km
    Lokasi: LS= 3.65 LS - BT= 128.16 BT
    Pusat gempa berada di darat 6 km Baratlaut Ambon
    Dirasakan (Skala MMI): II Paso
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '03 Juni 2022'
    hasil['waktu'] = '07:04:47 WIB'
    hasil['magnitudo'] = 2.6
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'LS': 3.65, 'BT': 128.16}
    hasil['pusat gempa'] = 'berada di darat 6 km Baratlaut Ambon'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Paso'


    return hasil


def tampilkan_data(hasil):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Pusat gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")



if __name__ == '__main__' :
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)