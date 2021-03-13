cv1={"isim" : "name1", "soyisim" : "surname1","yas" : "age1", "E-mail": "ornek1@hotmail.com", "yetenek": "Catia"}
cv2={"isim" : "name2", "soyisim" : "surname2","yas" : "age2", "E-mail": "ornek2@hotmail.com", "yetenek": "AutoCad"}
cv3={"isim" : "name3", "soyisim" : "surname3","yas" : "age3", "E-mail": "ornek3@hotmail.com", "yetenek": "Solidworks"}
cv4={"isim" : "name4", "soyisim" : "surname4","yas" : "age4", "E-mail": "ornek4@hotmail.com", "yetenek": "Matlab"}
cv5={"isim" : "name5", "soyisim" : "surname5","yas" : "age5", "E-mail": "ornek5@hotmail.com", "yetenek": "Python"}
for x in range(6):
  print("^"*20)
  if x == 0:
    print("isim:", cv1["isim"])
    print("soyisim:", cv1["soyisim"])
    print("yas:", cv1["yas"])
    print("E-mail:", cv1["E-mail"])
    print("Yetenek:", cv1["yetenek"])
  elif x == 1:
    print("isim:", cv2["isim"])
    print("soyisim:", cv2["soyisim"])
    print("yas:", cv2["yas"])
    print("E-mail:", cv2["E-mail"])
    print("Yetenek:", cv2["yetenek"])
  elif x == 2:
    print("isim:", cv3["isim"])
    print("soyisim:", cv3["soyisim"])
    print("yas:", cv3["yas"])
    print("E-mail:", cv3["E-mail"])
    print("Yetenek:", cv3["yetenek"])
  elif x == 3: 
    print("isim:", cv4["isim"])
    print("soyisim:", cv4["soyisim"])
    print("yas:", cv4["yas"])
    print("E-mail:", cv4["E-mail"])
    print("Yetenek:", cv4["yetenek"])
  elif x == 4:
    print("isim:", cv5["isim"])
    print("soyisim:", cv5["soyisim"])
    print("yas:", cv5["yas"])
    print("E-mail:", cv5["E-mail"])
    print("Yetenek:", cv5["yetenek"])
  else:
   print("Basvuran sayısı 5'dir!!")
