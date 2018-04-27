def etkilesim():
    global hesapla
    begeni=int(input("Beğeni sayısını giriniz:"))
    yorum=int(input("Yorum sayısını giriniz:"))
    paylasim=int(input("Paylaşım sayısını giriniz:"))
    icerik=int(input("İçerik sayısını giriniz:"))
    takipci=int(input("Takipçi sayısını giriniz:"))
    hesapla=((begeni+yorum+paylasim)/icerik)/takipci
    print("Etkileşim oranınız:",hesapla)

etkilesim()
if hesapla<0.2:
    print("Başarısız")
else:
    print("Başarılı")
