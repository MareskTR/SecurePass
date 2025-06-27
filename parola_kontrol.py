# Final Projesi: Parola Güvenliği Aracı
# Hazırlayan: [Ad Soyadını Buraya Yaz]
# Ders: [Dersin Adı] | Öğretim Görevlisi: [Hocanın Adı]
# Amaç: Kullanıcının girdiği parolanın güvenliğini kontrol etmek ve sık kullanılan parolaları tespit etmek

import re  # Regex modülü ile karakter kontrolü yapılacak

# En sık kullanılan bazı zayıf parolalar listesi
sik_parolalar = [
    '123456', 'password', '123456789', 'qwerty', '12345678',
    '111111', '123123', 'abc123', '1234567', 'password1'
]

def parola_gucu_kontrol(parola):
    """
    Girilen parolanın güçlü olup olmadığını kontrol eder.
    Her kriter 1 puan getirir. Toplamda 5 üzerinden puan verilir.
    """
    puan = 0

    if len(parola) >= 8:
        puan += 1  # Uzunluk yeterli

    if re.search(r'[A-Z]', parola):
        puan += 1  # Büyük harf içeriyor

    if re.search(r'[a-z]', parola):
        puan += 1  # Küçük harf içeriyor

    if re.search(r'[0-9]', parola):
        puan += 1  # Rakam içeriyor

    if re.search(r'[^A-Za-z0-9]', parola):
        puan += 1  # Sembol içeriyor

    return puan

def sik_kullanilan_mi(parola):
    """
    Parola sık kullanılanlar listesinde mi kontrol eder.
    """
    return parola in sik_parolalar

if __name__ == "__main__":
    print("🔐 Parola Güvenliği Kontrol Aracı")
    parola = input("Lütfen parolanızı girin: ")

    # İlk olarak parola sık kullanılanlardan mı?
    if sik_kullanilan_mi(parola):
        print("⚠️ Bu parola çok sık kullanılan zayıf bir paroladır! Lütfen daha güvenli bir parola seçin.")
    else:
        # Güç puanını hesapla
        guc = parola_gucu_kontrol(parola)
        print(f"🔎 Parola Güç Skoru: {guc}/5")

        # Kullanıcıyı bilgilendir
        if guc == 5:
            print("✅ Harika! Parolanız oldukça güçlü.")
        elif guc >= 3:
            print("🟡 Orta seviye bir parola. Daha güçlü hale getirmek için sembol veya büyük harf ekleyebilirsiniz.")
        else:
            print("🔴 Zayıf parola. Lütfen daha uzun ve karmaşık bir parola belirleyin.")
