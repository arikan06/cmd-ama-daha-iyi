# cmd ama daha iyi
Bu program ile Cmd komutlarını Türkçe olarak kullanabilirsiniz. Programdaki komutları kullanmak için hem Türkçe hem İngilizce karakterler ve büyük harfler kullanabilirsiniz.

ı => i
ş => s
ç => c
ğ => g
ö => o
ü => u

Programda bulunan komutlar: 
* pip             = Python modüllerini indirmeyi sağlar.
* baslik          = Programın başlığını değiştirmenizi sağlar.
* renk            = Programın rengini değiştirmenizi sağlar.
* wifi sifreler   = Bilgisayarınızda kayıtlı olan wifi şifrelerini gösterir.
* wifi detayli    = Bilgisayarınızda kayıtlı olan wifi adreslerinin detaylı ayarlarını gösterir.
* wifi            = Bağlanabilecek wifi adreslerini gösterir.
* sil             = Dosya siler.
* standart        = Normal Cmd'ye geçiş.

# Program nasıl çalışıyor?
Program ilk önce Python içinde yüklü olan "subprocces" ve "pip" modüllerini programa ekliyor. Subprocces modülü programda cmd komutlarını çağırmamızı sağlıyor. Pip modülü programın özelliği olan modül indirmeyi sağlıyor. Programı açtıktan sonra sizden çalıştıracağınız komudu soruyor (üstte bulunan komutlardan) girdiğiniz karakterleri küçük harflere dönüştürüyor ve eğer Türkçe harf girdiyseniz (ı, ş, ç, ö, ü, ğ) bunları İngilizce karatkerlere dönüştürüyor. Bunları gerçekleştirdikten sonra program sizin girdiğiniz veri eğer üç kelimeden fazlaysa veya üç kelimeyse sırasıyla birinciKomut, ikinciKomut, ucuncuKomut olarak değişkenlere ayırıyor. Veriniz iki kelimeye eşitse birinciKomut ve ikinciKomut olarak değişkenlere ayırıyor. Veriniz bir kelimeyse birinciKomut olarak değişkene ayırıyor.  
