# önceki alıştırmada da benzerini yaptım o yüzden daha az açıklama yapıcam.
x = 0 # Pozisyonumuzu tayin ediyor.
liste = []
liste_len = input("Değerleri belirlemeden önce listenin uzunluğunu belirleyiniz: ")
while int(liste_len) != len(liste):
    eleman = input("Listeye eklemek istediğiniz değeri giriniz: ")
    liste.append(eleman)
print("Listenizin ilk hali: ",liste)
while x < len(liste):
    # Alt satırın başındaki dies'i atarsanız işlemleri tek tek görebilirsiniz. (bunun da yorumlaması manuel)
    #print(liste)
    if x == len(liste) - 1:
        x += 1 # Döngüyü bitirir
    elif liste[x+1] < liste[x]:
        temp = liste[x]
        liste[x] = liste[x+1]
        liste[x+1] = temp
        if x != 0: # Eğer pozisyonumuz 0. indeksten farklıysa seçilen bu elemanı en başa çekebilmek için pozisyonumuzu bir bir azaltmalıyız.
            x -= 1
    else:
        x += 1 # Eğer yukarıdakiler sağlanmıyorsa o pozisyon uygundur, yani sıradaki pozisyonu kontrol ederiz.
print("Listenizin düzenlenmiş hali: ",liste)
