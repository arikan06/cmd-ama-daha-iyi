# cmd ama daha iyi

## İçindekiler:
* [Tanıtım](#Tanıtım)
* [Prototip](#Prototip)
  * [Program nasıl çalışıyor? (1.0.0)](#Program-nasıl-çalışıyor?-(1.0.0))
  * [Programda bulunan komutlar (1.0.0):](#Programda-bulunan-komutlar-(1.0.0))
  * [1.0.0 Hataları](##1.0.0-Hataları)
* [Program nasıl çalışıyor? (2.0.0)](#Program-nasıl-çalışıyor?-(2.0.0))

# Tanıtım
buraları doldurcam

# Prototip
## Program nasıl çalışıyor? (1.0.0)
Program ilk önce Python içinde yüklü olan "subprocces" ve "pip" modüllerini programa ekliyor. Subprocces modülü programda cmd komutlarını çağırmamızı sağlıyor. Pip modülü programın özelliği olan modül indirmeyi sağlıyor. Programı açtıktan sonra sizden çalıştıracağınız komudu soruyor (üstte bulunan komutlardan) girdiğiniz karakterleri küçük harflere dönüştürüyor. Eğer Türkçe harf girdiyseniz program otomatik olarak Türkçe harfleri İngilizce harflere çeviriyor.

* ı => i
* ş => s
* ç => c
* ğ => g
* ö => o
* ü => u

Bunları gerçekleştirdikten sonra program sizin girdiğiniz veri eğer üç kelimeden fazlaysa veya üç kelimeyse sırasıyla birinciKomut, ikinciKomut, ucuncuKomut olarak değişkenlere ayırıyor. Veriniz iki kelimeye eşitse birinciKomut ve ikinciKomut olarak değişkenlere ayırıyor. Veriniz bir kelimeyse birinciKomut olarak değişkene ayırıyor.  

## Programda bulunan komutlar (1.0.0):
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
* yardim          = Üstteki komutları programda görmenizi sağlar

## 1.0.0 Hataları:
 * baslik komudunu çalıştırınca ucuncuKomut değişkenini eklemem ile artık başlığı 1 kelimeden fazla yapamıyoruz.
 * dizin olustur kullandıktan sonra dizin dersek ikinciKomut değişkeni değişmediği için dizin olustur komudunu tekrar çağırdığımızı sanıyor.

# Program nasıl çalışıyor? (2.0.0)
