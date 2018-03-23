#satis= Satış miktarı
#birimSatis= Birim satış fiyatı
satis=500
birimSatis=20
ciro=5000
i=0
while (ciro<=500000):
    ciro=ciro+(satis*birimSatis)
    satis=satis+200
    birimSatis=birimSatis+10
    i=i+1
    hesap=i/12
    sonuc=format(float(hesap),".1f")
print("500.000 kar limitine ulaşılmıştır.Kar limitine ",sonuc," yılda ulaşılmıştır.")
