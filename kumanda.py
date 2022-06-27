#Televizyon Kumandası Uygulaması
#İşlemler: 1,2,3,4

from random import randint as r

class Kumanda:
    def __init__(self,tvDurum=False,tvSes=0,kanalListesi=["Trt"],kanal="Trt"):
        print("Kumanda Oluşturuluyor...")
        self.TvSesi = tvSes
        self.TvDurumu = tvDurum
        self.KanalListesi = kanalListesi
        self.Kanal = kanal
    def SesAzaltArttir(self):
        while True:
            if self.TvDurumu!=True:
                print("Lütfen Önce TV'yi Aç")
                break
            karakter = input("Sesi Azaltmak İçin '<', Sesi Arttırmak İçin '>', Çıkış İçin 'q' Tuşuna Bas")
            if karakter =='<' and self.TvSesi!=0:
                self.TvSesi -=1
            elif karakter=='>' and  self.TvSesi!=15:
                self.TvSesi+=1
            elif karakter =="q":
                print("Ses => {}.. Menüden Çıkılıyor...".format(self.TvSesi))
                break
            print("Ses => {}".format(self.TvSesi))
    def TvKapat(self):
        if self.TvDurumu ==True:
            print("Tv Kapatılıyor")
            self.TvDurumu =False
        else:
            print("TV Zaten Kapalı")
    def TvAc(self):
        if self.TvDurumu ==False:
            print("TV Açılıyor...")
            self.TvDurumu = True
        else :
            print("TV Zaten Açık")
    def RastgeleKanal(self):
        rastgele = r(0,len(self.KanalListesi)-1)
        self.Kanal = self.KanalListesi[rastgele]
        print("Şu anki Kanal => {}".format(self.Kanal))
    def KanalEkle(self,kanal):
        print("Kanal Eklendi, Eklenen Kanal => {}".format(kanal))
        self.KanalListesi.append(kanal)
    def KanalBilgileriniGoster(self):
         for x in self.KanalListesi:
             print(x)
    def __str__(self):
        return "TV Durumu: {}\n Ses: {}\n Kanallar: {}\n Şu Anki Kanal : {}\n".format(self.TvDurumu,self.TvSesi,self.KanalListesi,self.Kanal)