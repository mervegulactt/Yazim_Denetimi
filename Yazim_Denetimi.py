"""
@Author Merve Gülaçtı 1160505012
Derlem https://github.com/ncarkaci/TDKDictionaryCrawler/blob/master/Birle%C5%9Ftirilmi%C5%9F_S%C3%B6zl%C3%BCk_Kelime_Listesi.txt den çekilmiştir.
Yazim denetimi yapmak için SequenceMatcher algoritması kullanarak derlem ile sorgu karşılaştırılır.
Karşılaştırma sonucunda elde edilen satır kullanıcıya cevap olarak dendürülür.
"""

import heapq
import operator
from difflib import SequenceMatcher

# kullanıcıdan yazım denetimi yapılmak üzere veri alınır.
Yazim_Sorgu = input("Lütfen yazımını düzeltmek istediğiniz kelimeyi giriniz: ")
# alınan veri küçük harf olacak şekilde düzenlenir.
Yazim_Sorgu = Yazim_Sorgu.lower()

# Derlemin dosya yolu tanımlanır.
DosyaYolu = 'Birleştirilmiş_Sözlük_Kelime_Listesi.txt'
Oranlar = {}

# veriler önbelleğe alınır.
with open(DosyaYolu, encoding="UTF-8") as dosya:
    data = dosya.readlines()

with open(DosyaYolu, encoding="UTF-8") as dosya:
    Satir = dosya.readline()
    print("\nKarşılaştırma yapılıyor. Lütfen Bekleyiniz...")
    i = 0
    while Satir:
        i=i+1
        Oranlar[i] = 0
        # Derlem okunur.
        Satir = dosya.readline()
        d = SequenceMatcher(None, Satir, Yazim_Sorgu).ratio()
        Oranlar[i] = d

    # Kayıt edilen oranlar sıralanır en yüksek değer ve benzerlik oranı değişkene atanır.
    EnYuksekDeger = heapq.nlargest(1, Oranlar.items(), key=operator.itemgetter(1))
    print("\nEn yüksek değer: "+ data[EnYuksekDeger[0][0]])


