from tkinter import *                               # ben tkinter kütüphanesinin bütün özeliklerini import ettim anlamına
# geliyor burası.
from tkinter import messagebox
import base64

#apply cryptography with vigenere ciphher
#https://stackoverflow.com/a/38223403

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#save notes
def save_and_encrypt_notes():
    title = title_entry.get()                       # kullanıcının girmiş olduğu başlığı başlık kısmına text kısmına ve ayrıca
    message = input_text.get("1.0",END)     # şifre kismında olan verileri ben bu şekilde aldım.burada textin nasıl alındığı
    master_secret = master_secret_input.get()       # bizim için önemli bir nokta.

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:       # bunlardan herhangi bir tanesi boş olursa benim programım
                                                                              # zaten çalışmaz.
            messagebox.showwarning(title="Error!", message="Please enter all information.")
    else:
        message_encrypted = encode(master_secret, message)

        try:
            with open("mysecret.txt", "a") as data_file:                # zaten benim dosyayı açmamın 3 tane modu vardı.r w a
                data_file.write(f'\n{title}\n{message_encrypted}')      # oluşturmuş olduğum dosyanın içeriği burada söz konusu.
                # her oluşturduğum yeni bir şifrelemede mysecret dosyamın içine ekleme yapıyorum burada.

        except FileNotFoundError:                           # dosyamın ilk defa açılma durumuna karşın ben böyle bir önlem getirdim
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        finally:
            title_entry.delete(0, END)                 # silmenın usulude zaten budur.
            master_secret_input.delete(0, END)
            input_text.delete("1.0",END)              # farkettiyseniz .get() fonksiyonunuda çalıştırırken ben "1.0" şeklinde
            # yazdım burada. ve sonuna END koydum.

#decrypt notes

def decrypt_notes():
    message_encrypted = input_text.get("1.0", END)
    master_secret = master_secret_input.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")






#UI(tasarım kısmım benim burası ben aklınıza hangi tasarım geliyor ise bunun altında gerçekleştiricem artık)

window = Tk()                          # ilk aşama zaten bir pencere oluşturmaktır burada.
window.title("Secret Notes")
window.config(padx=5, pady=5)         # config burada değiştirebileceğim özelikleri gösterir.
# padx ve pady Tkinter'daki widget'ların (araçların) çerçevesi içindeki içerik ile çerçeve arasındaki
# yatay ve dikey boşlukları belirtmek için kullanılan parametrelerdir.padding'den gelir kenar boşluğu anlamına gelir.


# şimdi burası da bir resim ekleme bölümü
mycanvas = Canvas(height=100, width=100)       # fotoğrafımıma ayrılacak yerin boyutunu ben burada belirledim.
                                               # bunu yaparkende Canvas kullandım
logo = PhotoImage(file="resim (1).png")           # fotoğrafımı tanıtma işini ben burda gerçekleştirdim.
mycanvas.create_image(50,50,image=logo)       # fotoğrafımın boyutu ise burada belirleniyor.
mycanvas.pack()                                   # tabikide ben her widget de olduğu gibi burada da pack yapmak zorunadyım.

title_info_label = Label(text="Enter your title",font=("Verdena",20,"normal"))
title_info_label.pack()

title_entry = Entry(width=30)
title_entry.pack()

input_info_label = Label(text="Enter your secret",font=("Verdena",20,"normal"))
input_info_label.pack()

input_text = Text(width=30, height=15)
input_text.pack()

master_secret_label = Label(text="Enter master key",font=("Verdena",20,"normal"))
master_secret_label.pack()

master_secret_input = Entry(width=30)
master_secret_input.pack()

save_button = Button(text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack()

decrypt_button = Button(text="Decrypt",command=decrypt_notes)
decrypt_button.pack()



# Pencereyi belirtilen boyut ve konumda aç ve ayrıca benim geometry fonksiyonu kullanma şeklimede dikkatlice bak.
window.geometry(f'{600}x{750}+{450}+{5}')
window.resizable(height=False , width=False) # ben burada da kullanıcının boyutları değiştirmesini istemiyorum.

window.mainloop()     # burası benim için elzem bir nokta eğer bu olmassa benim işim sakat çünkü bu ;
# Tkinter uygulamalarında GUI'nin ana döngüsünü başlatan ve kullanıcının etkileşimde bulunabileceği bir döngüyü başlatan bir metoddur.
# Tkinter ile bir pencere oluşturduktan sonra, mainloop() metodu çağrıldığında, uygulama etkileşimli hale gelir ve
# kullanıcı olaylara (event) tepki verebilir.