fark=0
while True:
    print("Bir sayı girişi yapınız. Çıkmak için [0](sıfır)")
    girilen=int(input("sayı:"))
    if (girilen!=0):
        kalan=girilen%3
        fark=fark+kalan
        print("toplam:",fark)
    else:
        print("Çıkış yaptınız. Girdiğiniz sayıların farklarının toplamı:",fark)
        break
