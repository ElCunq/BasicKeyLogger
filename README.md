# Basit Python Keylogger

Bu proje, Python kullanılarak hazırlanmış **basit bir arayüzsüz keylogger** uygulamasıdır.  
Program, bilgisayar açıldığında otomatik olarak başlar ve her tuş vuruşunu bir `.txt` dosyasına kaydeder.

## Özellikler

- Sistem açıldığında otomatik başlama (Windows `Registry` autorun kaydı üzerinden)
- Arka planda sessiz çalışma (arayüz yok)
- Her tuş vuruşunu `Documents\logs.txt` dosyasına kaydetme
- 30 saniyede bir log dosyasını güncelleme
- Basit ve modüler yapı

## Gereksinimler

- Python 3.x
- `pynput` kütüphanesi

## Kurulum

1. Python 3 sürümünü yükleyin: https://www.python.org/downloads/
2. Gerekli kütüphaneyi yükleyin:

```bash
pip install pynput
```

3. `keylogger.py` dosyasını istediğiniz bir klasöre kaydedin.

## Kullanım

```bash
python keylogger.py
```

- Çalıştırıldığında:
    - `Documents` klasörünüzde `logs.txt` adlı bir dosya oluşturulur.
    - Her tuş vuruşu bu dosyada saklanır.
    - Program kendini **Windows açılışına** ekler ve her yeniden başlatmada otomatik başlar.

## Dosya Konumu

Log dosyası:

```
C:\Users\KULLANICI_ADI\Documents\logs.txt
```

Autorun kaydı:

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
Anahtar adı: SystemUpdater
```

## Uyarılar

- Bu yazılım **yetkili ve yasal test ortamları** için hazırlanmıştır.
- Kendi bilgisayarınızda veya yetkili olduğunuz sistemlerde kullanınız.
- Yasadışı kullanımlarda sorumluluk kabul edilmez.

## Bilinen Sınırlamalar

- Sadece **Windows** için otomatik başlatma desteği vardır. (Linux/Mac için ayrıca yapılandırma gerekir.)
- Log dosyası **şifrelenmemiş** olarak tutulur.

## Geliştirme Fikirleri

- Log dosyasını şifreleme
- C2 sunucusuna log gönderimi
- Anti-forensic önlemler
- Process hollowing veya DLL injection ile gizleme
- Çoklu persistence yöntemleri (Registry + Scheduled Task + WMI Event)

---

🛠️ Proje şu an temel seviyededir ve kolayca geliştirilebilir.

---
## Lisans

Bu proje açık kaynaklıdır ve [MIT Lisansı](https://opensource.org/licenses/MIT) altında sunulmaktadır.
