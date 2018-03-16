#donem_basi= Dönem başı stoğu
#koltuk= Koltuk sayısı
#yatak= Yatak sayısı
#dolap= Dolap sayısı
#donem_sonu= Dönem sonu stoğu
#ort= Ortalama stok
def donem_basi(koltuk,yatak,dolap):
    global donem_basi
    donem_basi= koltuk+yatak+dolap
    return donem_basi
a = int(input("Koltuk sayısını giriniz:"))
b = int(input("Yatak sayısını giriniz:"))
c = int(input("Dolap sayısını giriniz:"))
d=donem_basi(a,b,c)
print("Dönem başı stoğunuz:",donem_basi)
def donem_sonu(koltuk,yatak,dolap):
    global donem_sonu
    donem_sonu= koltuk+yatak+dolap
    return donem_sonu
x = int(input("Koltuk sayısını giriniz:"))
y = int(input("Yatak sayısını giriniz:"))
z = int(input("Dolap sayısını giriniz:"))
v=donem_sonu(x,y,z)
print("Dönem sonu stoğunuz:",donem_sonu)
hesapla=(donem_basi + donem_sonu) / 2
ort=format(float(hesapla),".0f")
print("Ortalama stoğunuz:",ort)
