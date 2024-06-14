'''
Mytxtim = open("MyFile.txt")
# bu şu anlama geliyor bu dosyayı açıyor ve benim değişkenime kayıt ediyor.oldukça mantıklı bir hareket aslında burası.

print(type(Mytxtim))

print(Mytxtim.read())     # ben burada "Mytxtim" adında olan değişkenimin içerisni okuyabiliyorum ama bır sorun var ben eğer
# tekrar oku yaparsam içerisini boş göstericektir.çünkü en baştam başlıyor sonuna kadar taratıyor ve sonunda kalıyor.

print(Mytxtim.read())

# şimdi ben dosyanın tekrardan en başına gitmem gerekecek bunu da
Mytxtim.seek(0)  # yaparak manuel bir şekilde gerçekleştiriyorum kardeşş. ama bu hiç mantıklı değil zaten az sonra ben bunun
# otamatik nasıl yapılır onu göreceöm.

print(Mytxtim.read())
Mytxtim.seek(0)
# gördüğünüz gibi burası oldukça maneul bir şekilde devam ediyor ben böyle sevmem bok gibi bide bunlarda yetmiyormuş gibi
# şeyde var.sen en sonda bide açmış olduğun dosyayı kapatman gerekecek.

Mytxtim.close()
 # bütün bu manuellerden kullanmanın bir yolu var : with
# ----------------------------------------------------------------------------------------------------------------------

          # dosyamın adı   # bu kısmada değişkenim adı ne olsun istiyorsam.
with open("MyFile.txt") as Mytxtim:
    mycontent = Mytxtim.read()
print("-----------")
print(mycontent)                #  dosyayı artık kapatmama gerek yok seek(0) yapmama gerek yok oh misss.

# benim ben dosyamı açtıktan sonra yazma okuma gibi eylemler yapabiliyorum.

                                    # ben aynı veya farklı bir değişkene atayabiliyorum bu as'den sonraki kısım benim değişken ismim
                                    # istediğimi koyabiliyorum.
                                    # buradaki "w" ise writedan gelir.
with open("MyFile.txt",mode="w") as MyFile2:     # mode="w" yapınca içinde ne varsa siler o anki ne yazıyorsan onu içeriye aktarır.
    MyFile2.write("bunu daha yeni yazdım")       # az sonra üstüne nasıl ekleneceğini göstereceğiz.

with open("MyFile.txt",mode="r") as MyContent:  # buradaki "r" ise read'den gelir.
   MyContent.read()

# eğer ben hepsini silmek yerine sadece eklemek istersem o zaman appenddin "a" sını kullanıcam.

with open("MyFile.txt",mode="a") as MyFile2:
    MyFile2.write("test4545")

with open("MyFile.txt",mode="r") as MyFile2:
    MyContent2 = MyFile2.read()

# burada mantığı anlamak çok önemli neden with kullanmaya ihityaç var.neden mod kullanıyoruz bunun ikisini öğrendikten sonra
# gerisini unuttuktan sorna bakılarak hatırlanaanbilir .


messagebox ne işe yarar ?

messagebox, Tkinter kütüphanesinde bulunan bir modül veya sınıftır ve kullanıcıya bilgi vermek, ondan bir giriş almak veya bir
onay almak için kullanılır. Tkinter'de bulunan messagebox modülü, çeşitli standart iletişim kutuları sağlar.
kullanıcıya bilgi mesajları, uyarılar, hatalar veya onay iletileri göstermek için kullanılır.
Ayrıca, kullanıcıdan giriş almak için bir giriş kutusu veya onay almak için bir onay kutusu oluşturabilirsiniz.

messagebox modülü, Tkinter GUI uygulamalarında kullanıcının etkileşimli geri dönüş almak için oldukça kullanışlıdır.
aşağıda kullanım şekilllerini görelim.
'''


#from tkinter import messagebox
#messagebox.showinfo("Bilgi mesajı", "Bu bir bilgi mesajıdır.")


#from tkinter import messagebox
#messagebox.showwarning("Uyarı", "Bu bir uyarı mesajıdır.")

#from tkinter import messagebox
#messagebox.showerror("Hata", "Bu bir hata mesajıdır.")


#from tkinter import messagebox
#response = messagebox.askquestion("Onay", "Devam etmek istiyor musunuz?")
#if response == 'yes':
 #   print("Evet'e tıklandı.")
#else:
 #   print("Hayır'a tıklandı.")


#from tkinter import messagebox
#response = messagebox.askokcancel("Onay", "Devam etmek istiyor musunuz?")
#if response:
 #   print("Tamam'a tıklandı.")
#else:
 #   print("İptal'e tıklandı.")














