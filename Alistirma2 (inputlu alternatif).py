# If/else'lerin sırasında bocalamış olabilirim ama çalışıyor.
x = 0 # Bu değişkenimiz bize liste içindeki o anki pozisyonumuzu gösterecek
liste = []
liste_len = input("Değerleri atamadan önce girmek istediğiniz dizinin uzunluğunu sayıyla belirleyiniz: ")
# Yukarıdaki satırla kullanıcıdan dizi uzunluğu belirlemesini istedik.
while int(liste_len) != len(liste):
    eleman = input("Listeye eklemek istediğiniz değeri giriniz: ")
    liste.append(eleman)
print("Listenizin ilk hali: ",liste)    
while x < len(liste):
    # Alttaki satırın başındaki dies'i atarsınız işlemleri tek tek görebilirsiniz (ama yorumlaması manuel :D)
    #print(liste)
    if x == len(liste) - 1:
        x +=1 # While döngüsü bitsin diye yaptım yoksa bitmiyordu. (gereksiz bişi olabilir)
    elif liste[x] > liste[x+1]:
        temp = liste[x] # Yer değiştirme yapmak için geçici değişkene değeri atıyorum.
        liste[x] = liste[x+1]
        liste[x+1] = temp
        x = 0 # Stupid sort gereği her yer değiştirmeden sonra başa dönüyorum.
    else:
        x+=1 # öbür şartlar tutmuyorsa sıradaki pozisyona geçip tekrar kontrole gönderiyorum.
print("Listenizin düzenlenmiş hali: ",liste)
