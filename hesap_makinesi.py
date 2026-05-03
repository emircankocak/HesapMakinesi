def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def böl(a,b):
    return a/b


sonuçlar = []

while True:
    
    try:
       sayi1 = int(input("1. Sayıyı girin:"))
       sayi2 = int(input("2. Sayıyı girin:"))  

    except ValueError:
       print("Hata! lütfen sayısal bir değer giriniz...")
       continue
    
    print("""
          1 - Toplama
          2 - Çıkarma
          3 - Çarpma
          4 - Bölme
    """ )
    secenek = input("1-4 arası bir işlem seçiniz:")

    if secenek == "q":
        print("İşlem sonlandırılıyor...")
        break
    
    elif secenek == "1":
        print(f"Toplama Sonucu: {topla(sayi1,sayi2)}")
        sonuçlar.append(topla(sayi1,sayi2))
        
    elif secenek =="2":
        print(f"Çıkarma Sonucu: {cikar(sayi1,sayi2)}")
        sonuçlar.append(cikar(sayi1,sayi2))
        
    elif secenek == "3":
        print(f"Çarpma Sonucu: {carp(sayi1,sayi2)}")
        sonuçlar.append(carp(sayi1,sayi2))

    elif secenek == "4":
        print(f"Bölme Sonucu: {böl(sayi1,sayi2)}")
        sonuçlar.append(böl(sayi1,sayi2))

    elif secenek == "5":
        print(f"Sonuçlar (geçmiş): {sonuçlar}")

    else:
        print("Lütfen 1-4 arası bir işlem deneyin!")
        continue










