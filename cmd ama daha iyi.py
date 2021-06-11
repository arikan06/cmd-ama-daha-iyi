#komut tanımlama #İngilizce kodları da açmayı ve string split programı yeniden başlatma matrix hesap makinesi açma windows çalıştır + windows çalıştır recent komudu, return ne ona bakcaz
# eğer title "title"
#reboot komudu
# _pip
try:
    #import pip
    import subprocess
    import time
    import json
except Exception as e:
    print('Pythonun içinde kurulu olan modüller bulunamadı. Pythonu silip tekrar yüklemeyi deneyin.')
    input()
subprocess.call('title cmd ama daha iyi', shell=True)
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
def mertfsmal():
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
mertfsmal()
time.sleep(0.3)
print('Versiyon: 3')
time.sleep(0.3)
print('Github: github.com/mertfsmal')
time.sleep(0.3)
print('Bütün komutları görmek için ".komutlar" yazın.')
print()
time.sleep(0.3)

def ingilizce(ingilizcelestir):
    ingilizcelestir = ingilizcelestir.replace("İ", "i")
    ingilizcelestir = ingilizcelestir.lower()
    ingilizcelestir = ingilizcelestir.replace("ı", "i")
    ingilizcelestir = ingilizcelestir.replace("ş", "s")
    ingilizcelestir = ingilizcelestir.replace("ç", "c")
    ingilizcelestir = ingilizcelestir.replace("ğ", "g")
    ingilizcelestir = ingilizcelestir.replace("ö", "o")
    ingilizcelestir = ingilizcelestir.replace("ü", "u")
    return ingilizcelestir

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
        duzenlenecekString=ingilizce(duzenlenecekString)
        duzenlenecekStringDegistiMi = duzenlenecekString
        if duzenlenecekString in komutlarJson["butun komutlar"].split(','):
            duzenlenecekString = duzenlenecekString.replace(duzenlenecekString, komutlarJson['komutlar'][0][duzenlenecekString][0]['ceviri'])
        if duzenlenecekStringDegistiMi == duzenlenecekString:
            duzenlenecekString = duzenlenecekStringTurkce
            return duzenlenecekString
        else:
            return duzenlenecekString

def komut(komutDegisken):
    komutDegisken = komutDegisken.replace('.', '', 1)
    #komutDegisken = komutDegisken.replace(' ', '', 1)
    komutDegisken=ingilizce(komutDegisken)
    if len(komutDegisken.split()) == 1:
        komut1 = komutDegisken.split()
        if komutDegisken == 'mertfsmal':
            mertfsmal()
        if komutDegisken == 'komutlar':
            print(komutlarJson["butun komutlar"].split(','))
    if len(komutDegisken.split()) == 2:
        komut1, komut2 = komutDegisken.split()

        if komutDegisken == 'wifi detayli':
            subprocess.call('netsh wlan show profiles', shell=True)
            k=input('Bilgisayarda kayıtlı wifi adresleri yukarıdadır. Detaylı bilgi öğrenmek istediklerinizin adresini girin. ')
            subprocess.call(f'netsh wlan show profiles {k} key=clear', shell=True)

        if komutDegisken == 'wifi sifreler':
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    print ("{:<30}|  {:<}".format(i, results[0]))

        if komut1 == 'komutlar':
            print(komutlarJson["komutlar"][0][komut2])
    if len(komutDegisken.split()) == 3:
        komut1, komut2, komut3 = komutDegisken.split()
        if komut1 == 'komutlar':
            if komut3 == 'gereksinim' or 'kullanim' or 'aciklama':
                print(komutlarJson["komutlar"][0][komut2][0][komut3])
            else:
                print('Komut bulunamadı.')
    if len(komutDegisken.split()) >= 4:
        print('komut bulunamadı. Bütün komutlar için ".komutlar" yazın')

def uygulama():
    while True:
        cmdKomut=input('->  ')
        if len(cmdKomut) == 0:
            print('Çalıştırmak istediğiniz komudu girin.')
            while True:
                cmdKomut=input('->  ')
                if len(cmdKomut.split()) != 0:
                    break
        if len(cmdKomut.split()) >= 1:
            calistirilacakKomut = ''
            #print(calistirilacakKomut.startswith())
            if cmdKomut.startswith('.'):
                komut(cmdKomut)
            else:
                if  str(len(cmdKomut.split())) >= komutlarJson['komutlar'][0][ingilizce(cmdKomut.split()[0])][0]['gereksinim']:
                    for kelime in cmdKomut.split():
                        kelime = stringDuzenle(kelime)
                        if kelime == cmdKomut.split()[len(cmdKomut.split())-1]:
                            calistirilacakKomut += f'{kelime}'
                        else:
                            calistirilacakKomut += f'{kelime} '
                    subprocess.call(calistirilacakKomut, shell=True)
                else:
                    print('Yanlış kullanım. Doğru kullanım: ', komutlarJson['komutlar'][0][ingilizce(cmdKomut.split()[0])][0]['kullanim'])
if __name__ == '__main__':
    while True:
        try:
            uygulama()
        except Exception as e:
            print('Hata! Hatayı görüntülemek için "e" yazın')
            ek=input()
            if ek == 'e':
                print(e)
                input()
                uygulama()
            else:
                uygulama()
