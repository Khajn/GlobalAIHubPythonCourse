soru=["Cumhurbaşkanı kaç yılda bir seçilir?",
      "Pusulada ( N ) harfi hangi yönü ifade eder ?",
      "Çocuk hakları günü hangi tarihte kutlanmaktadır ?",
      "Türkçe hangi dil grubuna girmektedir ?",
      "2007 yılında Avrupa Birliğine giren ülkeler hangileridir ?",
      "Müzik ezgileri yazılırken sesleri gösteren işaretlere ne ad verilir ?",
      "Dinamiti icat eden ve her yıl adına çeşitli dallarda ödüller verilen ünlü bilim adamı kimdir?",
      "Nobel ödülleri hangi ülkede verilmektedir?",
      "Tarihte Türk adıyla kurulan ilk devlet hangisidir?",
      "Altın Palmiye Ödülleri hangi şehrimizde verilmektedir?"]
cevap=["5","Kuzey","20 Kasım","Ural – Altay","Bulgaristan – Romanya","Nota","Alfred Nobel","İsveç","Göktürk","Antalya"]
dogrucevapsayisi=0
print(" — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —  ")
print("|                      Merhaba, bilgi yarışmasına hoşgeldiniz.                    |")
print("| Testten geçebilmek için 10 sorudan 5 tanesini doğru cevaplamanız gerekmektedir. |")
print("|                                İyi şanslar..!                                   |")
print(" — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — ")
for i in range(len(soru)):
    print("")
    print("Yarışmamızın {}. Sorusu".format(i+1))
    print("-"*23)
    print(soru[i])
    cevapp=input("{}. Soru İçin Cevap: ".format(i+1))
    if (cevapp.lower()==cevap[i].lower()):
        print("Cevabınız Doğru")        
        dogrucevapsayisi +=1        
    else:
        print("Cevabınız Yanlış. Doğru cevap: {}".format(cevap[i].capitalize()))
    print("Şuan {} doğru cevabınız var.".format(dogrucevapsayisi))
if (dogrucevapsayisi>=5):
    print("")
    print("Tebrikler, bilgi yarışmasını başarıyla tamamladınız. {} Tane soruyu doğru bildiniz".format(dogrucevapsayisi))
else:
    print("")
    print("Üzgünüz, bilgi yarışmasını başarıyla tamamlayamadınız. {} Tane soruyu doğru bildiniz".format(dogrucevapsayisi))
