#komut tanımlama #İngilizce kodları da açmayı ve string split programı yeniden başlatma matrix hesap makinesi açma windows çalıştır + windows çalıştır recent komudu, return ne ona bakcaz
try:
    import pip
    import subprocess
    import time
except Exception as e:
    print('Pythonun içinde kurulu olan modüller bulunamadı. Pythonu silip tekrar yüklemeyi deneyin.')
    input()
time.sleep(0.06)
print("""                       _    __                     _""")
time.sleep(0.06)
print("""                      | |  / _|                   | |""")
time.sleep(0.06)
print("""   _ __ ___   ___ _ __| |_| |_ ___ _ __ ___   __ _| |""")
time.sleep(0.06)
print("""  | '_ ` _ \ / _ \ '__| __|  _/ __| '_ ` _ \ / _` | |""")
time.sleep(0.06)
print("""  | | | | | |  __/ |  | |_| | \__ \ | | | | | (_| | |""")
time.sleep(0.06)
print("""  |_| |_| |_|\___|_|   \__|_| |___/_| |_| |_|\__,_|_|""")
time.sleep(0.06)
print()
time.sleep(0.3)
print('Versiyon: 2.0.2')
time.sleep(0.3)
print('Github: github.com/mertfsmal')
time.sleep(0.3)
print('Bütün komutları görmek için "yardım" yazın.')
print()
time.sleep(0.3)

try:
    def stringDuzenle(duzenlenecekString):
        duzenlenecekString = duzenlenecekString.lower()
        yeniCmdKomut1 = duzenlenecekString.replace("ı", "i")
        yeniCmdKomut2 = yeniCmdKomut1.replace("ş", "s")
        yeniCmdKomut3 = yeniCmdKomut2.replace("ç", "c")
        yeniCmdKomut4 = yeniCmdKomut3.replace("ğ", "g")
        yeniCmdKomut5 = yeniCmdKomut4.replace("ö", "o")
        duzenlenecekString = yeniCmdKomut5.replace("ü", "u")
        return duzenlenecekString
except Exception as e:
    print('stringDuzenle hata', e)
    input()

try:
    while True:
        print('----------------------------')
        cmdKomutDuzenlenmemis=input('->  ')
        if len(cmdKomutDuzenlenmemis.split()) == 0:
            print('Çalıştırmak istediğiniz komudu girin.')
            while True:
                cmdKomutDuzenlenmemis=input('->  ')
                if len(cmdKomutDuzenlenmemis.split()) != 0:
                    break
        if len(cmdKomutDuzenlenmemis.split()) >= 3:
            #ikinciUzunKomut = False
            birinciKomut, ikinciKomut, ucuncuKomut = cmdKomutDuzenlenmemis.split(' ', 2)
            birinciKomut = stringDuzenle(birinciKomut)
        if len(cmdKomutDuzenlenmemis.split()) >= 2:
            #ikinciKomut, ucuncuKomut, = False
            birinciKomut, ikinciUzunKomut = cmdKomutDuzenlenmemis.split(' ', 1)
            birinciKomut = stringDuzenle(birinciKomut)
        if len(cmdKomutDuzenlenmemis.split()) == 1:
            #ikinciUzunKomut, ikinciKomut, ucuncuKomut, = False
            birinciKomut = stringDuzenle(cmdKomutDuzenlenmemis)

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
