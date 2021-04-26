#komut tanımlama
import subprocess
print('cmd ama daha iyi mertfsmal')
while True:
    try:
        print('----------------------------')
        cmdKomut=input()
        print('----------------------------')
        if cmdKomut == 'dizin':
            subprocess.call('dir', shell=True)
        if cmdKomut == 'agac':
            subprocess.call('tree', shell=True)
        if cmdKomut == 'temizle':
            subprocess.call('cls', shell=True)
        if cmdKomut == 'ip bilgileri':
            subprocess.call('ipconfig', shell=True)
        if cmdKomut == 'wifi bilgileri':
            subprocess.call('netsh wlan show profiles', shell=True)
        if cmdKomut == 'wifi sifreleri':
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
    except Exception as e:
        print('Bu kod programa kayıtlı değildir. Lütfen tekrar deneyin.')
        pass
        #İngilizce kodları da açmayı ve
