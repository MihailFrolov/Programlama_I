#calisan= Çalışan sayısı
#yevmiye= Günlük yevmiye
#haftalikMaas= Haftalık maaş
#haftalikMesai=Haftalık mesai
#aylikMesai=Aylık mesai
#aylikMaas= Aylık maaş
calisan=50
yevmiye=90
haftalikMaas=630
aylikMaas=0
while aylikMaas<=22:
    haftalikMesai=int(input("Haftalık mesaiyi giriniz:"))
    aylikMesai=haftalikMesai*4
    haftalikMaas=haftalikMaas+(haftalikMesai*yevmiye*0.10)
    aylikMaas=aylikMaas+haftalikMaas*4
    sonuc=format(float(aylikMaas),".0f")
    if(aylikMesai>22):
        print("Aylık mesai 22 saatten fazla olamaz.")
    else:
        print("Aylık personele ödenen toplam maaş",sonuc,"TL'dir.")
 
