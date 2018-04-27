def aktifHesap():
    #Dönen varlıklar hesabının başı
    kasaHesap=int(input("100 Kasa hesabını giriniz:"))
    alinanCekler=int(input("101 Alınan çekler hesabını giriniz:"))
    bankalar=int(input("102 Bankalar hesabını giriniz:"))
    alinacakSenetler=int(input("121 Alınacak senetler hesabını giriniz:"))
    ticariMallar=int(input("153 Ticari mallar hesabını giriniz:"))
    donenV=kasaHesap+alinanCekler+bankalar+alinacakSenetler+ticariMallar
    print("YBS İşletmesinin dönen varlıklarının değeri",donenV,"TL'dir.")
    #Dönen varlıklar hesabının sonu
    
    #Duran varlıklar hesabının başı
    binalar=int(input("252 Binalar hesabını giriniz:"))
    tasitlar=int(input("254 Taşıtlar hesabını giriniz:"))
    demirbaslar=int(input("255 Demirbaşlar hesabını giriniz:"))
    duranV=binalar+tasitlar+demirbaslar
    print("YBS İşletmesinin duran varlıklarınının değeri",duranV,"TL'dir.")
    #Duran varlıklar hesabının sonu
    
    global aktif
    aktif=donenV+duranV
    print("YBS İşletmesinin aktif hesabının toplamı",aktif,"TL'dir.")

def pasifHesap():
    #Kısa vadeli yabancı kaynaklar hesabının başı
    bankaKredi=int(input("300 Banka kredileri hesabını giriniz:"))
    saticilar=int(input("320 Satıcılar hesabını giriniz:"))
    kvyk=bankaKredi+saticilar
    print("YBS İşletmesinin kısa vadeli yabancı kaynaklar hesabının değeri",kvyk,"TL'dir.")
    #Kısa vadeli yabancı kaynaklar hesabının sonu
    
    #Uzun vadeli yabancı kaynaklar hesabının başı
    bankaKredi2=int(input("400 Banka kredileri hesabını giriniz:"))
    borcSenetleri=int(input("421 Borç senetleri hesabını giriniz:"))
    uvyk=bankaKredi2+borcSenetleri
    print("YBS İşletmesinin uzun vadeli yabancı kaynaklar hesabının değeri",uvyk,"TL'dir.")
    #Uzun vadeli yabancı kaynaklar hesabının sonu
    
    #Öz kaynaklar hesabının başı
    sermaye=int(input("500 Sermaye hesabını giriniz:"))
    print("YBS İşletmesinin öz kaynaklar hesabının değeri",sermaye,"TL'dir.")
    #Öz kaynaklar hesabının sonu
    
    global pasif
    pasif=kvyk+uvyk+sermaye
    print("YBS İşletmesinin pasif hesabının toplamı",pasif,"TL'dir.")
    
aktifHesap()
pasifHesap()
if aktif==pasif:
    print("Kapanış bilançosu doğru hesaplanmıştır.")
else:
    print("Bilanço yanlış hesaplanmıştır.")
