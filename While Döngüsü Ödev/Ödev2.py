#stokMiktar= Stok miktarı
#alim= Alınan ürün
#satim= Satılan ürün
stokMiktar=10000
alim=100
satim=500
hesapla=alim-satim
i=0
while (stokMiktar>0):
    stokMiktar=stokMiktar+hesapla
    i=i+1
print(i,".ayda stok sıfırlanır.")
