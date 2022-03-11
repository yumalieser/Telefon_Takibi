import phonenumbers
from phonenumbers import geocoder

print("""*******************************************************************************
Telefon Numarası Üzerinden Lokasyon ve Operatör Bulma Sistemine Hoşgeldiniz...
*******************************************************************************""")

number = input('Öğrenmek İstediğiniz Telefon Numarasını Başında (+) Alan Kodu Olacak Şekilde Girin : ')
number_p = phonenumbers.parse(number)
print(geocoder.description_for_number(number_p,'tr'))

from phonenumbers import carrier
print(carrier.name_for_number(number_p,'tr'))
