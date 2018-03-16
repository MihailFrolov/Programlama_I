#kdc= Katma değer ciro
#tsm= Toplam satış miktarı
#hm= Hammadde maliyeti
#bom= Bakım onarım giderleri
#sg= Sevkiyat giderleri
#sahg= Satın alınan hizmet giderleri
def kdc(tsm,hm,bom,sg,sahg):
    global kdc
    kdc = tsm -(hm+bom+sg+sahg)
    return kdc
a = int(input("Toplam satış miktarını giriniz:"))
b = int(input("Hammadde maliyetini giriniz:"))
c = int(input("Bakım onarım giderlerini giriniz:"))
d = int(input("Sevkiyat giderlerini giriniz:"))
e = int(input("Satın alınan hizmet giderlerini giriniz:"))
f=kdc(a,b,c,d,e)
if(kdc>=1000):
    print("İşletme katma değer cirosu yüksektir. Katma değer cironuz:",kdc)
elif(kdc>=500 and kdc<=999):
    print("İşletme katma değer cirosu normaldir. Katma değer cironuz:",kdc)
else:
    print("İşletme katma değer cirosu düşüktür. Katma değer cironuz:",kdc)
