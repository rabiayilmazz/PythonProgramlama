###########   Hesap Makinesi    ###########

print(" Toplama işlemi - 1 \n Çıkarma işlemi - 2 \n Bölme işlemi - 3 \n Çarpma işlemi - 4")

sayi1 = int(input("Sayi1 :"))
sayi2 = int(input("Sayi2 :"))

secim = input("Secim yap :")

if secim == "1":
    print("Toplam :",sayi1+sayi2)

elif secim == "2":
    print("Çıkarma :",sayi2-sayi1)

elif secim == "3":
    print("Carpma :",sayi2*sayi1)

elif secim == "4":
    print("Bölme :",sayi2/sayi1)
else:
    print("Yanlış tuşlama yaptınız...")
