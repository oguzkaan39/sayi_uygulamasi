#!/usr/bin/env python3 
#-*- coding:utf-8-*-
#Klavyeden 0-99 arasında girilen sayiyi ekrana yazıyla yazdıran program
birler=["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar=["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
sayi=input("Sayi giriniz : ")
kalan=int(sayi)%10
bölüm=(int(sayi)/10) 
print("Sayının Yazıyla Yazılışı :%s"%(onlar[int(bölüm)]),"%s"%(birler[kalan]))