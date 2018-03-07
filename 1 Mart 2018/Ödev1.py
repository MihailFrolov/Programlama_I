#Şirketin gelirleri ve giderleri ayrı ayrı hesaplanarak şirketin kar edip etmediğini belirt.
finansmanGelir=int(input("Finansman gelirini giriniz :"))
pazarGelir=int(input("Pazar gelirini giriniz :"))
kiraGelir=int(input("Kira gelirini giriniz :"))
gelir=finansmanGelir + pazarGelir + kiraGelir
print("Toplam geliriniz",gelir,"TL'dir.")


ucret=int(input("Ücret giderini giriniz :"))
finansmanGider=int(input("Finansman giderini giriniz :"))
pazarGider=int(input("Pazar giderini giriniz :"))
kiraGider=int(input("Kira giderini giriniz :"))
muhasebeGider=int(input("Muhasebe giderini giriniz :"))
gider=ucret + finansmanGider + pazarGider + kiraGider + muhasebeGider
print("Toplam gideriniz",gider,"TL'dir.")

kar=gelir-gider
if(kar>=1000):
    print("İşletmeniz kar limitine ulaşmıştır. Elde ettiğiniz miktar, kar liminin",kar - 1000,"TL üstündedir.")
elif(kar<1000):
    print("İşletmeniz kar limitine ulaşamamıştır. Elde ettiğiniz miktar, kar limitinin ",kar - 1000,"TL altındadır.")
else:
    print("İşletmeniz başabaş noktasındadır.")
