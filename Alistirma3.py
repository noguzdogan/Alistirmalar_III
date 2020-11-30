x = 0 # Pozisyonumuzu tayin ediyor.
liste = [7,9,1,8,3]
while x < len(liste):
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
