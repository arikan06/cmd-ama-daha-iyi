#komut tanımlama #İngilizce kodları da açmayı ve string split programı yeniden başlatma matrix hesap makinesi açma windows çalıştır + windows çalıştır recent komudu, return ne ona bakcaz
try:
    import pip
    import subprocess
    import time
except Exception as e:
    print('Pythonun içinde kurulu olan modüller bulunamadı. Pythonu silip tekrar yüklemeyi deneyin.')
    input()

print("""                      _    __                     _
                     | |  / _|                   | |
  _ __ ___   ___ _ __| |_| |_ ___ _ __ ___   __ _| |
 | '_ ` _ \ / _ \ '__| __|  _/ __| '_ ` _ \ / _` | |
 | | | | | |  __/ |  | |_| | \__ \ | | | | | (_| | |
 |_| |_| |_|\___|_|   \__|_| |___/_| |_| |_|\__,_|_|

                                                    """)
time.sleep(0.2)
print('Versiyon: 2.0.0')
time.sleep(0.2)
print('Github: github.com/mertfsmal')
time.sleep(0.2)
print('Bütün komutları görmek için "yardım" yazın.')
print()
time.sleep(0.2)

try:
    while True:
        print('----------------------------')
        cmdKomutDuzenlenmemis=input('-> ')

        def stringDuzenle():
            print('string düzenle girildi')
            global cmdKomutDuzenlenmemis
            cmdKomutDuzenlenmemis = cmdKomutDuzenlenmemis.lower()
            yeniCmdKomut1 = cmdKomutDuzenlenmemis.replace("ı", "i")
            yeniCmdKomut2 = yeniCmdKomut1.replace("ş", "s")
            yeniCmdKomut3 = yeniCmdKomut2.replace("ç", "c")
            yeniCmdKomut4 = yeniCmdKomut3.replace("ğ", "g")
            yeniCmdKomut5 = yeniCmdKomut4.replace("ö", "o")
            cmdKomutDuzenlenmis = yeniCmdKomut5.replace("ü", "u")
            print('string düzenlendi')

        print('func çağırdık')
        stringDuzenle()
        print('Func bitir')

        if len(cmdKomutDuzenlenmis.split()) == 0:
            print('Girmek istediğiniz komudu girin.')
            while True:
                komutBekleniyor = input('-> ')
                if len(cmdKomutDuzenlenmemis.split()) >= 1:
                    stringDuzenle()
                    False

        elif len(cmdKomutDuzenlenmis.split()) >= 3:
            birinciKomut, ikinciKomut, ucuncuKomut = cmdKomutDuzenlenmis.split(' ', 2)
        elif len(cmdKomutDuzenlenmis.split()) == 2:
            birinciKomut, ikinciKomut = cmdKomutDuzenlenmis.split(' ', 1)
        else:
            birinciKomut = cmdKomutDuzenlenmis

        if birinciKomut == 'yardim':
            print("""# Programda bulunan komutlar (1.0):
* pip             = Python modüllerini indirmeyi sağlar.
* baslik          = Programın başlığını değiştirmenizi sağlar.
* renk            = Programın rengini değiştirmenizi sağlar.
* wifi sifreler   = Bilgisayarınızda kayıtlı olan wifi şifrelerini gösterir.
* wifi detayli    = Bilgisayarınızda kayıtlı olan wifi adreslerinin detaylı ayarlarını gösterir.
* wifi            = Bağlanabilecek wifi adreslerini gösterir.
* sil             = Dosya siler.
* standart        = Normal Cmd'ye geçiş.
* dizin           = Bulunduğunuzun dizini gösterir.
* dizin olustur   = Klasör oluşturur.
* baslat          = Cmd açar.
* ac              = dizin açar.
* gecmis          = yazdığınız komutların geçmişini gösterir.
* agac            = Dosyalarınızı gösterir.
* temizle         = Ekranı temizler.
* ip              = Ip bilgilerinizi gösterir.
* yardim          = Üstteki komutları programda görmenizi sağlar""")
except Exception as e:
    print(e)
    input()
