#gunlukUretim= Günlük yapılan üretim
#gunlukDefUrun= Günlük defolu ürün miktarı
#toplamDefUrun= Toplam defolu ürün miktarı
gunlukUretim=200
gunlukDefUrun=0
toplamDefUrun=0
i=0
while (gunlukDefUrun<=gunlukUretim*0.20):
    gunlukDefUrun=int(input("Günlük defolu ürün sayısını giriniz:"))
    toplamDefUrun=toplamDefUrun+gunlukDefUrun
    hesap=(gunlukDefUrun/200)*100
    sonuc=format(float(hesap),".1f")
    kalan=hesap-20
    sonuc2=format(float(kalan),".1f")
    i=i+1
    if (gunlukDefUrun>gunlukUretim*0.20):
        print("Defolu ürün sayısı limiti aşıldı. Defolu ürün oranınız yüzde",sonuc,"dir. Defolu ürün sayısı limitinin yüzde",kalan,"üzerdesiniz. Bunu yüzde 20'nin altına çekmelisiniz")
    else:
        print(i,"Günlük","Defolu ürün sayınız:",toplamDefUrun,"'dir. Defolu ürün sayı oranınız yüzde",sonuc,"'dir. Bu, olması gerekenden yüzde",sonuc2,"daha azdır.")
