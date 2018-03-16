#mcs2016= 2016 yılını müşterilerle çalışma süresi
#mcs2017= 2017 yılını müşterilerle çalışma süresi
#cs2016= 2016 yılı çalışma süresi
#tms2016= 2016 yılı toplam müşteri sayısı
#cs2017= 2017 yılı çalışma süresi
#tms2017= 2017 yılı toplam müşteri sayısı
cs2016=170
tms2016=50
cs2017=cs2016 + 50
tms2017=tms2016 + 20
def mcs2016(cs2016,tms2016):
    mcs2016 = cs2016 / tms2016
    return mcs2016
def mcs2017(cs2017,tms2017):
    mcs2017 = cs2017 / tms2017
    return mcs2017
hesapla=mcs2016(cs2016,tms2016)-mcs2017(cs2017,tms2017)
sonuc=format(float(hesapla),".2f")
print("2016-2017 yılları arasındaki müşterilerle çalışma sayısı farkı:",sonuc)

