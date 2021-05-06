#komut tanımlama #İngilizce kodları da açmayı ve string split programı yeniden başlatma matrix hesap makinesi açma windows çalıştır + windows çalıştır recent komudu, return ne ona bakcaz
# eğer title "title"
#reboot komudu
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
    print(e)
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
print('Bütün komutları görmek için "yardım" yazın.')
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
            duzenlenecekString = duzenlenecekString.replace("İ", "i")
            duzenlenecekString = duzenlenecekString.lower()
            duzenlenecekString = duzenlenecekString.replace("ı", "i")
            duzenlenecekString = duzenlenecekString.replace("ş", "s")
            duzenlenecekString = duzenlenecekString.replace("ç", "c")
            duzenlenecekString = duzenlenecekString.replace("ğ", "g")
            duzenlenecekString = duzenlenecekString.replace("ö", "o")
            duzenlenecekString = duzenlenecekString.replace("ü", "u")
            duzenlenecekString = duzenlenecekString.replace("baslik", "title")
            duzenlenecekString = duzenlenecekString.replace("ip", "ipconfig")
            duzenlenecekString = duzenlenecekString.replace("zaman", "date")
            duzenlenecekString = duzenlenecekString.replace("tarih", "date")
            duzenlenecekString = duzenlenecekString.replace("saat", "date")
            duzenlenecekString = duzenlenecekString.replace("bilgi", "cmd")
            duzenlenecekString = duzenlenecekString.replace("temizle", "cls")
            duzenlenecekString = duzenlenecekString.replace("agac", "tree")
            duzenlenecekString = duzenlenecekString.replace("yeni", "start")
            return duzenlenecekString
except Exception as e:
    print('stringDuzenle hata', e)
    input()

try:
    def ozellik():
        print('Buraya ekstra kodları eklicem')
except Exception as e:
    print(e)
    input()

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
            if birinciKomut.startswith('_'):
                ozellik()
            else:
                subprocess.call(birinciKomut, shell=True)
        if len(cmdKomut.split()) == 2:
            birinciKomut, ikinciKomut=cmdKomut.split()
            birinciKomut=stringDuzenle(birinciKomut)
            ikinciKomut=stringDuzenle(ikinciKomut)
            if birinciKomut.startswith('_'):
                ozellik()
            else:
                subprocess.call(f"{birinciKomut} {ikinciKomut}", shell=True)
        if len(cmdKomut.split()) == 3:
            birinciKomut, ikinciKomut, ucuncuKomut=cmdKomut.split()
            birinciKomut=stringDuzenle(birinciKomut)
            ikinciKomut=stringDuzenle(ikinciKomut)
            ucuncuKomut=stringDuzenle(ucuncuKomut)
            if birinciKomut.startswith('_'):
                ozellik()
            else:
                subprocess.call(f"{birinciKomut} {ikinciKomut} {ucuncuKomut}", shell=True)
        if len(cmdKomut.split()) == 4:
            birinciKomut, ikinciKomut, ucuncuKomut, dorduncuKomut=cmdKomut.split()
            birinciKomut=stringDuzenle(birinciKomut)
            ikinciKomut=stringDuzenle(ikinciKomut)
            ucuncuKomut=stringDuzenle(ucuncuKomut)
            dorduncuKomut=stringDuzenle(dorduncuKomut)
            if birinciKomut.startswith('_'):
                ozellik()
            else:
                subprocess.call(f"{birinciKomut} {ikinciKomut} {ucuncuKomut} {dorduncuKomut}", shell=True)
        if len(cmdKomut.split()) >= 5:
            print('En fazla 4 kelime yazabilirsiniz.')
except Exception as e:
    print(e)
    input()
