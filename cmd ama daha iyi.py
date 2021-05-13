#komut tanımlama #İngilizce kodları da açmayı ve string split programı yeniden başlatma matrix hesap makinesi açma windows çalıştır + windows çalıştır recent komudu, return ne ona bakcaz
# eğer title "title"
#reboot komudu
# _pip
try:
    import pip
    import subprocess
    import time
    import json
except Exception as e:
    print('Pythonun içinde kurulu olan modüller bulunamadı. Pythonu silip tekrar yüklemeyi deneyin.')
    input()

try:
    komutlarJson = json.load(open('komutlar.json'))
    komutlarJsonPrint = json.dumps(komutlarJson, indent=1)
except FileNotFoundError as e:
    print('Aşağıdaki linkten komutlar.json dosyasını indirin.')
    print('https://github.com/mertfsmal/cmd-ama-daha-iyi/blob/main/komutlar.json dosyasını indirin.')
    input()
except Exception as e:
    print('json hatası', e)
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
print('Versiyon: 3')
time.sleep(0.3)
print('Github: github.com/mertfsmal')
time.sleep(0.3)
print('Bütün komutları görmek için "_komutlar" yazın.')
print()
time.sleep(0.3)

baslikYardim = 'Yanlış kullanım. Doğru kullanım "başlık {başlığınız}"'
yardimYardim = 'asdasd'
try:
    def stringDuzenle(duzenlenecekString):
        if duzenlenecekString.startswith('"') and duzenlenecekString.endswith('"'):
            if len(duzenlenecekString) == 2:
                print('çift tırnağın içini doldurmalısınız.')
                duzenlenecekString = '[boş]'
                return duzenlenecekString
            if len(duzenlenecekString) >= 3:
                duzenlenecekString = duzenlenecekString.replace('"', '')
                return duzenlenecekString
        else:
            duzenlenecekStringTurkce = duzenlenecekString
            duzenlenecekString = duzenlenecekString.replace("İ", "i")
            duzenlenecekString = duzenlenecekString.lower()
            duzenlenecekString = duzenlenecekString.replace("ı", "i")
            duzenlenecekString = duzenlenecekString.replace("ş", "s")
            duzenlenecekString = duzenlenecekString.replace("ç", "c")
            duzenlenecekString = duzenlenecekString.replace("ğ", "g")
            duzenlenecekString = duzenlenecekString.replace("ö", "o")
            duzenlenecekString = duzenlenecekString.replace("ü", "u")
            duzenlenecekStringDegistiMi = duzenlenecekString
            duzenlenecekString = duzenlenecekString.replace("baslik", "title")
            duzenlenecekString = duzenlenecekString.replace("ip", "ipconfig")
            duzenlenecekString = duzenlenecekString.replace("renk", "color")
            duzenlenecekString = duzenlenecekString.replace("zaman", "date")
            duzenlenecekString = duzenlenecekString.replace("tarih", "date")
            duzenlenecekString = duzenlenecekString.replace("saat", "date")
            duzenlenecekString = duzenlenecekString.replace("bilgi", "cmd")
            duzenlenecekString = duzenlenecekString.replace("temizle", "cls")
            duzenlenecekString = duzenlenecekString.replace("agac", "tree")
            duzenlenecekString = duzenlenecekString.replace("yeni", "start")
            if duzenlenecekStringDegistiMi == duzenlenecekString:
                duzenlenecekString = duzenlenecekStringTurkce
                return duzenlenecekString
            else:
                return duzenlenecekString
except Exception as e:
    print('stringDuzenle hata', e)
    input()

try:
    def kontrol(kontrolEdilecek):
        if len(kontrolEdilecek.split()) >= komutlarJson['komutlar'][0][kontrolEdilecek][0]['gereksinim']:
            kontrolDegisken = True
            return kontrolDegisken
        else:
            kontrolDegisken = False
            return kontrolDegisken
except Exception as e:
    print('kontrol def hata', e)
    input()
    
try:
    def komut(komutDegisken):
        komutDegisken = str(komutDegisken)
        komutDegisken = komutDegisken.replace('_', '', 1)
        #kontrol(komutDegisken)
        if komutDegisken == 'komutlar':
            print(komutlarJsonPrint)
except Exception as e:
    print('komut bulunamadı bütün komutları görmek için _komutlar yazın.')
    input()
    pass

try:
    while True:
        cmdKomut=input('->  ')
        if len(cmdKomut.split()) == 0:
            print('Çalıştırmak istediğiniz komudu girin.')
            while True:
                cmdKomut=input('->  ')
                if len(cmdKomut.split()) != 0:
                    break
        if len(cmdKomut.split()) == 1:
            birinciKomut=cmdKomut
            birinciKomut=stringDuzenle(birinciKomut)
            calistirilacakKomut = birinciKomut
            if birinciKomut.startswith('_'):
                komut(calistirilacakKomut)
            else:
                subprocess.call(calistirilacakKomut, shell=True)
        if len(cmdKomut.split()) == 2:
            birinciKomut, ikinciKomut=cmdKomut.split()
            birinciKomut=stringDuzenle(birinciKomut)
            ikinciKomut=stringDuzenle(ikinciKomut)
            calistirilacakKomut = birinciKomut, ikinciKomut
            if birinciKomut.startswith('_'):
                komut(calistirilacakKomut)
            else:
                subprocess.call(calistirilacakKomut, shell=True)
        if len(cmdKomut.split()) == 3:
            birinciKomut, ikinciKomut, ucuncuKomut=cmdKomut.split()
            birinciKomut=stringDuzenle(birinciKomut)
            ikinciKomut=stringDuzenle(ikinciKomut)
            ucuncuKomut=stringDuzenle(ucuncuKomut)
            calistirilacakKomut = birinciKomut, ikinciKomut, ucuncuKomut
            if birinciKomut.startswith('_'):
                komut(calistirilacakKomut)
            else:
                subprocess.call(calistirilacakKomut, shell=True)
        if len(cmdKomut.split()) == 4:
            birinciKomut, ikinciKomut, ucuncuKomut, dorduncuKomut=cmdKomut.split()
            birinciKomut=stringDuzenle(birinciKomut)
            ikinciKomut=stringDuzenle(ikinciKomut)
            ucuncuKomut=stringDuzenle(ucuncuKomut)
            dorduncuKomut=stringDuzenle(dorduncuKomut)
            calistirilacakKomut = birinciKomut, ikinciKomut, ucuncuKomut, dorduncuKomut
            if birinciKomut.startswith('_'):
                komut(calistirilacakKomut)
            else:
                subprocess.call(calistirilacakKomut, shell=True)
        if len(cmdKomut.split()) >= 5:
            cmdKomut = stringDuzenle(cmdKomut)
            subprocess.call(cmdKomut, shell=True)
except Exception as e:
    print('main hata', e)
    input()
