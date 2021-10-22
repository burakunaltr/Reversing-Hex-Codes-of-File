#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__      = "Burak Ünal"
__email__       = "burakunalofficial[H0RS3]gmail.com"

import binascii

print("Hex Kodlarını Ters Çevireceğiniz Dosyayı Giriniz..")
dosya = str(input("Dosya : "))
with open(dosya,'rb') as f: #Gösterilen dosya okunur.
    icerik = f.read()
hexDump = str(binascii.b2a_hex(icerik)) #Dosya içeriği hexkodlarına dönüştürülüp string olarak değişkene atanır.

liste = [hexDump[i:i+2] for i in range(0, len(hexDump), 2)] #String değişkeni 2 karakterli gruplar halinde liste değişkenine atanır.
reverseHex = ''.join(liste[::-1]) #Liste tersten başlayarak string değişkeninde birleştirilir.
reverseHex = reverseHex[1:-2] #Stringin başında ve sonundaki gereksiz karakterlerden kurtulunur.

print("Lütfen Çıktı için Uzantısıyla Birlikte Dosya Adı Giriniz..")
cikti = str(input("Çıktı : "))
with open(cikti,'wb') as fout: #Çıktı için dosya oluşturulur
    fout.write(binascii.a2b_hex(reverseHex)) #Ters çevrilmiş hex kodları dosyaya yazılır.

print("O iş Tamam ;)")
#test
#test2