#sm=Satış miktarı
#bsf=Plansız duruş
#tct=Toplam ciro text
def toplamCiro():
    sm=int(input("Satış miktarını giriniz :"))
    bsf=int(input("Birim satış fiyatını giriniz :"))
    tct="Toplam cironuz :"
    ciro=tct,sm * bsf
    return ciro

#tcs=Toplam çalışan sayısı
#ac=Adambaşı Ciro
#act=Adambaşı Ciro Text
def ac():
    ciro=int(input("Toplam cironuzu giriniz :"))
    tcs=25
    act="Adambaşı cironuz :"
    ac=act,ciro / tcs
    return ac
