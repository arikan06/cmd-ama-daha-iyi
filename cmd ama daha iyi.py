#komut tanımlama #İngilizce kodları da açmayı ve string split programı yeniden başlatma matrix hesap makinesi açma windows çalıştır + windows çalıştır recent komudu, return ne ona bakcaz
try:
    import pip
    import subprocess
    import time
    import json
except Exception as e:
    print('Pythonun içinde kurulu olan modüller bulunamadı. Pythonu silip tekrar yüklemeyi deneyin.')
    input()



try:
    with open("komutlar.json", encoding='utf-8', errors='ignore') as f:
        komutlarJson = json.load(f, strict=False)
        komutlarJsonPrint = json.dumps(komutlarJson, indent=1)

except FileNotFoundError as e:
    print('komutlar.json bulunamadı, komutlar.json yaratılıyor..')
    with open('komutlar.json','a+') as f:
        komutlarJsonYarat = {
         "Giris bilgileri": [

        ]}
        json.dump(komutlarJsonYarat, f, indent=1)
        print("komutlar.json yaratıldı")
        print('----------------------------------------------')
        pass
except Exception as e:
    print(f"hata: {e}")
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
print('Versiyon: 2.0.3')
time.sleep(0.3)
print('Github: github.com/mertfsmal')
time.sleep(0.3)
print('Bütün komutları görmek için "yardım" yazın.')
print()
time.sleep(0.3)

baslikYardim = 'Yanlış kullanım. Doğru kullanım "başlık {başlığınız}"'
yardimYardim = 'asdasd'
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
            #ikinciUzunKomut = None
            birinciKomut, ikinciKomut, ucuncuKomut = cmdKomutDuzenlenmemis.split(' ', 2)
            birinciKomut = stringDuzenle(birinciKomut)
        if len(cmdKomutDuzenlenmemis.split()) >= 2:
            #ikinciKomut, ucuncuKomut, = None
            birinciKomut, ikinciUzunKomut = cmdKomutDuzenlenmemis.split(' ', 1)
            birinciKomut = stringDuzenle(birinciKomut)
        if len(cmdKomutDuzenlenmemis.split()) == 1:
            #ikinciUzunKomut, ikinciKomut, ucuncuKomut, = None
            birinciKomut = stringDuzenle(cmdKomutDuzenlenmemis)


        if birinciKomut == 'baslik':
            try:
                subprocess.call(f'title {ikinciUzunKomut}', shell = True)
            except NameError:
                print(baslikYardim)
            except Exception as e:
                print(e)
                input()
        if birinciKomut == 'yardim':
            print(komutlarJsonPrint)
except Exception as e:
    print(e)
    input()
