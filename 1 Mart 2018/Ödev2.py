#------------ Fonksiyon kullanarak hesaplama -----------------
#pus=Planlanmış üretim süresi
#pd=Plansız duruş
def kullanılabilirlik():  
    pus=int(input("Planlanmış üretim süresini giriniz :"))
    pd=int(input("Plansız duruşu giriniz :"))
    kullanilabilirlik=(pus - pd) / pus
    return kullanilabilirlik

#scz=Standart çevrim zamanı
#um=Üretim miktarı
def performans():
    scz=int(input("Standart çevrim zamanını giriniz :"))
    um=int(input("Üretim miktarı giriniz :"))
    pus=int(input("Planlanmış üretim süresini giriniz :"))
    pd=int(input("Plansız duruşu giriniz :"))
    perf=(scz * um) / (pus - pd)
    return perf

#saum=Sağlam ürün miktarı
#tum=Toplam üretim mitarı
def kalite():
    saum=int(input("Sağlam ürün miktarını giriniz :"))
    tum=int(input("Toplam üretim mitarını giriniz :"))
    klt=saum / tum
    return klt

def oee():
    performans=int(input("Performansınızı giriniz :"))
    kalite=int(input("Kalitenizi giriniz :"))
    kullanılabilirlik=int(input("Kullanılabilirliği giriniz :"))
    oee=kullanılabilirlik * performans * kalite * 100,"%=invalid syntax hatası"
    return oee
