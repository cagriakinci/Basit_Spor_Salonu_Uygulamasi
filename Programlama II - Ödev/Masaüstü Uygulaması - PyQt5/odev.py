from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
import sys

class sporSalonu(QDialog):
    def __init__(self):
        super().__init__()
        grid=QGridLayout()
    
# Kayıt Ekleme Kısmı
        grid.addWidget(QLabel("Kayıt Ekle"),0,0) 
        grid.addWidget(QLabel("Adı:"),1,0)
        grid.addWidget(QLabel("Soyadı:"),2,0)
        grid.addWidget(QLabel("Cinsiyet:"),3,0)
        grid.addWidget(QLabel("Yaş:"),4,0)
        grid.addWidget(QLabel("Süre:"),5,0)
        grid.addWidget(QLabel("Fiyat:"),6,0)
        grid.addWidget(QLabel("Kayıt Tarihi:"),7,0)
        grid.addWidget(QLabel("Boy:"),8,0)
        grid.addWidget(QLabel("Kilo:"),9,0)

        
        self.ad=QLineEdit()
        self.soyad=QLineEdit()
        self.cinsiyet=QLineEdit()
        self.yas=QLineEdit()
        self.sure=QLineEdit()
        self.fiyat=QLineEdit()
        self.kayit_tarihi=QDateEdit(calendarPopup=True)
        self.boy=QLineEdit()
        self.kilo=QLineEdit()
        save=QPushButton("Kayıt Ekle")
        save.clicked.connect(self.save)
        save.setStyleSheet("background-color: white")

        
        grid.addWidget(self.ad,1,1)
        grid.addWidget(self.soyad,2,1)
        grid.addWidget(self.cinsiyet,3,1)
        grid.addWidget(self.yas,4,1)
        grid.addWidget(self.sure,5,1)
        grid.addWidget(self.fiyat,6,1)
        grid.addWidget(self.kayit_tarihi,7,1)
        grid.addWidget(self.boy,8,1)
        grid.addWidget(self.kilo,9,1)
        grid.addWidget(save,10,1)

# Vücut Kitle İndeksi Hesaplama Bölümü

        grid.addWidget(QLabel("Vücut Kitle İndeksi"),0,7)
        grid.addWidget(QLabel("Cinsiyet:"),1,7)
        grid.addWidget(QLabel("Kilo:"),2,7)
        grid.addWidget(QLabel("Boy:"),3,7)
        grid.addWidget(QLabel("Sonuç:"),4,7)


        self.cinsiyet1=QLineEdit()
        self.kilo1=QLineEdit()
        self.boy1=QLineEdit()
        self.sonuc=QLabel("")


        grid.addWidget(self.cinsiyet1,1,8)
        grid.addWidget(self.kilo1,2,8)
        grid.addWidget(self.boy1,3,8)
        grid.addWidget(self.sonuc,4,8)


# Kalori İhtiyacı Hesaplama Bölümü

        grid.addWidget(QLabel("Kalori İhtiyacı Hesaplama"),0,9)
        grid.addWidget(QLabel("Cinsiyet:"),1,9)
        grid.addWidget(QLabel("Günlük Aktivite:"),2,9)
        grid.addWidget(QLabel("Yaş:"),3,9)
        grid.addWidget(QLabel("Boy"),4,9)
        grid.addWidget(QLabel("Kilo"),5,9)
        grid.addWidget(QLabel("Sonuç:"),6,9)


        self.cinsiyet2=QLineEdit()
        self.cinsiyet2.setToolTip("Kadın yada Erkek yazarken baş harfini büyük yazınız.")
        self.calisma_bicimi = QComboBox(self)
        self.calisma_bicimi.addItem("Fazla hareket etmiyorum.")
        self.calisma_bicimi.addItem("Az hareket ediyorum.")
        self.calisma_bicimi.addItem("Orta derece hareket ediyorum.")
        self.calisma_bicimi.addItem("Çok aktif hareket ediyorum.")
        self.calisma_bicimi.addItem("Aşırı düzeyde hareket ediyorum.")
        grid.addWidget(self.calisma_bicimi,2,10)
        self.yas2=QLineEdit()
        self.boy2=QLineEdit()
        self.kilo2=QLineEdit()
        self.sonucKadin=QLabel("")
        self.sonucErkek=QLabel("")


        grid.addWidget(self.cinsiyet2,1,10)
        grid.addWidget(self.yas2,3,10)
        grid.addWidget(self.boy2,4,10)
        grid.addWidget(self.kilo2,5,10)
        grid.addWidget(self.sonucKadin,6,10)
        grid.addWidget(self.sonucErkek,7,10)


        # Vücut Kitle İndeksi Butonu
        kitleindeksibuton = QPushButton("Hesapla")
        kitleindeksibuton.setStyleSheet("background-color: white")
        kitleindeksibuton.clicked.connect(self.kitleindeksiHesapla)
        grid.addWidget(kitleindeksibuton,5,8)

        # Kalori İhtiyacı Hesaplama Butonu
        kaloributon = QPushButton("Hesapla")
        kaloributon.setStyleSheet("background-color: white")
        kaloributon.clicked.connect(self.kaloriHesaplama)
        grid.addWidget(kaloributon,8,10)

        self.setLayout(grid)
        self.setWindowTitle("Spor Salonu Yönetimi Yazılımı")
        

    def kitleindeksiHesapla(self):
        cinsiyet1 = self.cinsiyet1.text()
        boy1 = float(self.boy1.text())
        kilo1 = float(self.kilo1.text())
        sonuc = (boy1*boy1)*(kilo1)/10
        if sonuc>0 and sonuc<18.4:
            print(self.sonuc.setText('<font color="red">Zayıf -> %0.1f</font>'%sonuc))
        elif sonuc>18.5 and sonuc<24.9:
            print(self.sonuc.setText('<font color="red">Normal -> %0.1f</font>'%sonuc))
        elif sonuc>25 and sonuc<29.9:
            print(self.sonuc.setText('<font color="red">Kilolu -> %0.1f</font>'%sonuc))
        elif sonuc>30 and sonuc<34.9:
            print(self.sonuc.setText('<font color="red">Şişman -> %0.1f</font>'%sonuc))
        elif sonuc>35 and sonuc<44.9:
            print(self.sonuc.setText('<font color="red">Obez -> %0.1f</font>'%sonuc))
        
    def kaloriHesaplama(self):
        cinsiyet2 = self.cinsiyet2.text()
        yas2 = self.yas2.text()
        boy2 = float(self.boy2.text())
        kilo2 = float(self.kilo2.text())
        sonucKadin = 2.4*(65.5 + (9.6*float(kilo2)) + (1.8*float(boy2))- (4.7*int(yas2)))
        sonucErkek = 2*(66 + (13.7*float(kilo2)) + (5*float(boy2)) - (6.8*int(yas2)))
        if cinsiyet2 == "Kadın":
            print(self.sonucKadin.setText('<font color="red">%0.1f</font>'%sonucKadin))
        elif cinsiyet2 == "Erkek":
            print(self.sonucErkek.setText('<font color="blue">%0.1f</font>'%sonucErkek)) 


    def save(self):
        ad=self.ad.text()
        soyad=self.soyad.text()
        cinsiyet=self.cinsiyet.text()
        yas=self.yas.text()
        sure=self.sure.text()
        fiyat=self.fiyat.text()
        kayit_tarihi=self.kayit_tarihi.date()
        kayit_tarihi=kayit_tarihi.toPyDate()
        boy=self.boy.text()
        kilo=self.kilo.text()
        

        # Veritabanı Bağlantısı
        baglanti=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='spor_salonu')
        isaretci=baglanti.cursor()
        isaretci.execute('''INSERT INTO musteriler (ad,soyad,cinsiyet,yas,sure,fiyat,kayit_tarihi,boy,kilo) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s")'''%(ad,soyad,cinsiyet,yas,sure,fiyat,kayit_tarihi,boy,kilo))
        baglanti.commit()
        baglanti.close()

       
uyg=QApplication([])
pencere=sporSalonu()
pencere.setGeometry(500,350,1000,300)
pencere.setWindowIcon(QIcon("spor.png"))
pencere.setStyleSheet("background-color:AliceBlue")
pencere.show()
uyg.exec_()
