#komut tanımlama #İngilizce kodları da açmayı ve string split programı yeniden başlatma matrix hesap makinesi açma windows çalıştır + windows çalıştır recent komudu, return ne ona bakcaz
import pip
import subprocess
print('cmd ama daha iyi mertfsmal')
while True:
    try:
        print('----------------------------')
        cmdKomut=input()
        cmdKomut = cmdKomut.lower()
        yeniCmdKomut1 = cmdKomut.replace("ı", "i")
        yeniCmdKomut2 = yeniCmdKomut1.replace("ş", "s")
        yeniCmdKomut3 = yeniCmdKomut2.replace("ç", "c")
        yeniCmdKomut4 = yeniCmdKomut3.replace("ğ", "g")
        yeniCmdKomut5 = yeniCmdKomut4.replace("ö", "o")
        yeniCmdKomut = yeniCmdKomut5.replace("ü", "u")

        if len(yeniCmdKomut.split()) >= 3:
            birinciKomut, ikinciKomut, ucuncuKomut = yeniCmdKomut.split(' ', 2)
        elif len(yeniCmdKomut.split()) == 2:
            birinciKomut, ikinciKomut = yeniCmdKomut.split(' ', 1)
        else:
            birinciKomut = yeniCmdKomut

        if birinciKomut == "sil":
            try:
                subprocess.call(f"del {ikinciKomut}", shell= True)
            except NameError:
                print('Yanlış kullanım. Doğru kullanım: "sil {silmek istediğiniz dosya}"')
        if birinciKomut == 'pip':
            try:
                if ikinciKomut == 'indir':
                    pip.main(['install', ucuncuKomut])
            except Exception as e:
                print('Yanlış kullanım. Doğru kullanım: "pip indir {indirmek istediğiniz dosya}"')
                pass
        if birinciKomut == 'ac':
            try:
                subprocess.call(f'cd {ikinciKomut}', shell = True)
            except Exception as e:
                print('Yanlış kullanım. Doğru kullanım: "ac {açmak istediğiniz dizin}"')
                pass
        if birinciKomut == 'baslik':
            try:
                subprocess.call(f'title {ikinciKomut}', shell = True)
            except Exception as e:
                print('Yanlış kullanım. Doğru kullanım: "Başlık {başlığınız}"')
                pass
        if birinciKomut == 'renk':
            try:
                subprocess.call(f'color {ikinciKomut}', shell = True)
            except Exception as e:
                print('Yanlış kullanım. Doğru kullanım: "renk {dilediğiniz renk}"')
                pass
        if birinciKomut == 'standart':
            while True:
                try:
                    normalCmd = input()
                    if normalCmd == 'cikis':
                        break
                    if normalCmd != 'cikis':
                        subprocess.call(normalCmd, shell=True)
                except Exception as e:
                    print(e)
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
        if birinciKomut == 'baslat':
            subprocess.call('start', shell=True)
        if birinciKomut == 'gecmis':
            subprocess.call('doskey /history', shell=True)
        if birinciKomut == 'dizin':
            try:
                if ikinciKomut == 'olustur':
                    subprocess.call(f'mkdir {ucuncuKomut}', shell = True)
            except NameError:
                subprocess.call('dir', shell=True)
        if birinciKomut == 'agac':
            subprocess.call('tree', shell=True)
        if birinciKomut == 'temizle':
            subprocess.call('cls', shell=True)
        if birinciKomut == 'ip':
            subprocess.call('ipconfig', shell=True)
        if birinciKomut == 'wifi':
            try:
                if ikinciKomut == 'detayli':
                    try:
                        subprocess.call(f"netsh wlan show profiles {ucuncuKomut} key=clear")
                    except NameError:
                        print('Yanlış kullanım. Doğru kullanım: "wifi detayli {wifi adı}"')
                if ikinciKomut == 'sifreler':
                    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
                    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                    for i in profiles:
                        try:
                            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                            try:
                                print ("{:<30}|  {:<}".format(i, results[0]))
                            except IndexError:
                                print ("{:<30}|  {:<}".format(i, ""))
                        except subprocess.CalledProcessError:
                            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
            except NameError as e:
                subprocess.call(f'netsh wlan show profiles', shell=True)
    except Exception as e:
        print('Bu kod programa kayıtlı değildir. Lütfen tekrar deneyin.', e)
        pass
        #İngilizce kodları da açmayı ve string split
