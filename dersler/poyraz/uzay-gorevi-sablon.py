#pgzero
# ==========================================================
#   ENERJİ FIRTINASI — GÖREV ŞABLONU
# ==========================================================
#   Nasıl çalışır?
#   - Kod 3 BÖLÜM'e ayrıldı. Her bölümün sonunda bir
#     KONTROL NOKTASI var: çalıştır, ekranda ne görmen
#     gerektiği yazıyor. Onu görmeden sonraki bölüme geçme!
#   - Görevlerin zorluk seviyesi yıldızla belli:
#       [*]    Yaz-geç: cevap yorumda saklı
#       [**]   Düşün: küçük bir karar vermen gerek
#       [***]  Meydan okuma: kendi fikrini kat
# ==========================================================

import random

WIDTH = 600
HEIGHT = 450
TITLE = "Enerji Fırtınası"


# ==========================================================
#   BÖLÜM 1 / 3  —  SAHNEYİ KUR
#   (Gemi, uzay, kristal ve enerji küreleri doğsun)
# ==========================================================

# Görev 1 [*]
# Oyuncu gemisi. Görsel: "ship", başlangıç: (300, 380)
ship = Actor("____", (____, ____))

# Görev 2 [*]
# Uzay arka planı. Görsel: "space"
space = Actor("____")

# Görev 3 [*]
# Toplanacak kristal. Görsel: "crystal", başlangıç: (300, 150)
crystal = Actor("____", (____, ____))

# Enerji kürelerini bu listede saklayacağız.
# SORU: Neden sözlük değil de liste? (Cevabını derste konuşacağız!)
orbs = []

# Skor sayı olarak tutulur ve 0'dan başlar.
score = ____

# Oyunun iki modu var: "game" (oynanıyor) ve "end" (bitti).
mode = "game"

# Oyuncuya kısa mesaj göstermek için.
message = ""


# Görev 4 [**]
# 4 enerji küresi üret. range() içine kaç yazmalısın?
for i in range(____):

    # x: 30 ile 570 arasında rastgele (ekranın içi)
    x = random.randint(____, ____)

    # y: -400 ile -50 arasında rastgele (ekranın YUKARISI —
    # küreler yukarıdan süzülerek gelsin diye eksi sayılar!)
    y = random.randint(____, ____)

    # Görev 5 [*]  Küreyi oluştur. Görsel: "orb"
    orb = Actor("____", (x, y))

    # Görev 6 [**]  Her küre farklı hızda insin: 2 ile 5 arası.
    orb.speed = random.randint(____, ____)

    # Görev 7 [*]  Küreyi listeye ekle.
    orbs.append(____)


# ----------------------------------------------------------
#   ÇİZİM — her karede ekranı baştan çizer
# ----------------------------------------------------------

def draw():
    space.draw()

    if mode == "game":
        ship.draw()
        crystal.draw()

        # Görev 8 [**]
        # Listedeki HER küreyi çiz.
        # İpucu: "orbs listesindeki her orb için" diye okunur.
        for orb in ____:
            orb.draw()

        screen.draw.text("Skor: " + str(score), (20, 20),
                         color="white", fontsize=28)
        screen.draw.text(message, center=(300, 420),
                         color="yellow", fontsize=24)

    elif mode == "end":
        screen.draw.text("OYUN BİTTİ!", center=(300, 200),
                         color="white", fontsize=40)
        screen.draw.text("Skor: " + str(score), center=(300, 250),
                         color="yellow", fontsize=30)


# ==========================================================
#   KONTROL NOKTASI 1
#   Çalıştır! Görmen gereken: uzay arka planı, gemi altta,
#   kristal ortada, 4 küre (belki henüz ekranın üstünde,
#   görünmüyor olabilirler — normal!). Skor: 0 yazmalı.
#   Gördün mü? Bölüm 2'ye geç.
# ==========================================================


# ==========================================================
#   BÖLÜM 2 / 3  —  HAREKET
#   (Gemi mouse'u izlesin, küreler aşağı yağsın)
# ==========================================================

def on_mouse_move(pos):
    # Görev 9 [**]
    # Gemi mouse'un olduğu yere gitsin.
    # İpucu: pos, mouse'un konumunu zaten taşıyor.
    ship.pos = ____


def move_orbs():
    for orb in orbs:

        # Küre hâlâ ekrandaysa aşağı insin.
        if orb.y < 500:
            # Görev 10 [**]
            # Kürenin y'sine KENDİ hızını ekle.
            # (Hızı Görev 6'da nereye kaydetmiştik?)
            orb.y = orb.y + ____

        # Küre ekranın altından çıktıysa:
        else:
            # Görev 11 [**]  GERİ DÖNÜŞÜM!
            # Küreyi silmek yok — ışınlıyoruz: yukarıda
            # rastgele bir yere geri gönder. Aynı küre
            # tekrar tekrar kullanılır. (-300, -50 arası y)
            orb.y = random.randint(____, ____)
            orb.x = random.randint(30, 570)

            # Görev 12 [***]
            # BONUS: Işınlanan küre yeni bir hız da kazansın
            # ki oyun tahmin edilemez olsun. Satırı sen yaz:
            # ____


# ==========================================================
#   KONTROL NOKTASI 2
#   Çalıştır! Görmen gereken: gemi mouse'u takip ediyor,
#   küreler yukarıdan yağıyor, ekrandan çıkan küre
#   yukarıdan tekrar geliyor (sonsuz yağmur!).
#   Gördün mü? Son bölüme geç.
# ==========================================================


# ==========================================================
#   BÖLÜM 3 / 3  —  ÇARPIŞMA VE KURALLAR
#   (Kristal = puan, küre = oyun sonu)
# ==========================================================

def move_crystal():
    # Görev 13 [*]
    # Kristal yeni bir yere zıplasın:
    # x: 40-560 arası, y: 40-330 arası.
    crystal.x = random.randint(____, ____)
    crystal.y = random.randint(____, ____)


def collisions():
    global score, mode, message

    # Görev 14 [**]
    # Gemi kristale değdi mi?
    # İpucu: colliderect() parantezine NEYE değdiğini yaz.
    if ship.colliderect(____):
        # Görev 15 [*]  Skor 1 artsın.
        score = score + ____
        message = "Kristal toplandı!"
        move_crystal()

    # Görev 16 [**]
    # Herhangi bir küreye değersek oyun biter.
    for orb in orbs:
        if ship.colliderect(____):
            mode = "____"


def update(dt):
    # Görev 17 [**]
    # Bu satır oyunun KALBİ: mode hangi kelimeye eşitse
    # sistemler çalışır?
    if mode == "____":
        move_orbs()
        collisions()


# ==========================================================
#   KONTROL NOKTASI 3 — FİNAL
#   Çalıştır! Kristal topladıkça skor artmalı, kristal
#   zıplamalı. Bir küreye değince "OYUN BİTTİ!" ekranı
#   gelmeli. Hepsi çalışıyorsa: OYUN TAMAM! 🚀
#
#   UZMAN GÖREVLERİ [***] (istersen):
#   A) Skor 10 olunca kürelerin hızı artsın (zorlaşan oyun)
#   B) "En yüksek skor" tutulup end ekranında gösterilsin
#   C) SPACE tuşuyla oyun baştan başlasın
# ==========================================================
