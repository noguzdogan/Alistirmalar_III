# If/else'lerin sırasında bocalamış olabilirim ama çalışıyor.
x = 0 # Bu değişkenimiz bize liste içindeki o anki pozisyonumuzu gösterecek
liste = [7,9,1,8,3] # Hocanın dersteki listesini örnek listem olarak belirledim.
while x < len(liste):
    if x == len(liste) - 1:
        x +=1 # While döngüsü bitsin diye yaptım yoksa bitmiyordu.
    elif liste[x] > liste[x+1]:
        temp = liste[x] # Yer değiştirme yapmak için geçici değişkene değeri atıyorum.
        liste[x] = liste[x+1]
        liste[x+1] = temp
        x = 0 # Stupid sort gereği her yer değiştirmeden sonra başa dönüyorum.
    else:
        x+=1 # öbür şartlar tutmuyorsa sıradaki pozisyona geçip tekrar kontrole gönderiyorum.
print("Listenizin düzenlenmiş hali: ",liste)
