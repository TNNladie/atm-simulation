# 1. Giriş ekranı → kullanıcı adı / şifre kontrolü
# 2. Ana menü → bakiye görüntüle / para çek / para yatır / çıkış
# 3. Tüm işlemler fonksiyonlara bölünmüş olacak

bakiye = 10000 # başlangıç bakiyesi
kullanici_adi = "tuanna" # kullanıcı adı
dogru_sifre = "2004" # doğru şifre
islem_gecmisi = []

def giris():
    print("ATM Sistemine Hoş Geldiniz!")
    hak = 3  # giriş hakkı
    while hak > 0:
        sifre = input("Lütfen şifrenizi giriniz: ")
        if sifre == dogru_sifre:
            print("Giriş başarılı!\n")
            return True
        else:
            hak -= 1
            if hak > 0:
                print(f"Hatalı şifre! Kalan giriş hakkınız: {hak}\n")   
            else:
                print("3 kez hatalı şifre girdiniz. Program sonlandırılıyor...\n")
    return False

def menu():
    print("Ana Menü:")
    print("1. Bakiye Görüntüle")
    print("2. Para Yatır")
    print("3. Para Çek")
    print("4. İşlem Geçmişi")
    print("5. Çıkış")

def para_yatir(bakiye):
    miktar = float(input("Yatırılacak miktarı giriniz: "))
    if miktar > 0:
        bakiye += miktar
        islem_gecmisi.append(f"{miktar} TL yatırıldı.")
        print(f"{miktar} TL bakiyenize eklendi. Güncel bakiyeniz: {bakiye} TL\n")
    else:
        print("Geçersiz miktar!\n")
    return bakiye

def islem_yap(bakiye):
    while True:
        menu()
        secim = input("Lütfen bir işlem seçiniz (1-4): ")
       
        if secim == "1":
          print(f"Güncel bakiyeniz: {bakiye} TL\n")
        
        elif secim == "2":
          miktar= float(input("Yatırılacak miktarı giriniz: "))
          bakiye += miktar
          islem_gecmisi.append(f"{miktar} TL yatırıldı.")
          print(f"{miktar} TL bakiyenize eklendi. Güncel bakiyeniz: {bakiye} TL\n")
        
        
        elif secim == "3":
          miktar= float(input("Çekilecek miktarı giriniz: "))
          if miktar > bakiye:
            print("Yetersiz bakiye! İşlem gerçekleştirilemiyor.\n")
          else:
            bakiye -= miktar
            islem_gecmisi.append(f"{miktar} TL çekildi.")
            print(f"{miktar} TL bakiyenizden çekildi. Güncel bakiyeniz: {bakiye} TL\n")

        elif secim == "4":
            if islem_gecmisi:
                print("İşlem Geçmişi:")
                for islem in islem_gecmisi:
                    print(islem)
            else:
                print("İşlem geçmişi bulunmamaktadır.\n")

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-4 arasında bir seçim yapınız.\n")

if giris():
    islem_yap(bakiye)

            