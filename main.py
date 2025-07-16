import os
import importlib
import time
import pyfiglet
import sys

def list_services():
    """service klasöründeki tüm Python dosyalarını listeler."""
    services = []
    service_dir = "service"
    
    for file in os.listdir(service_dir):
        if file.endswith(".py") and file != "__init__.py":
            services.append(file[:-3])  # .py uzantısını kaldır
    
    return services

def print_banner():
    """Görsel banner ve başlangıç mesajı."""
    # pyfiglet ile ASCII sanatı
    banner = pyfiglet.figlet_format("*SIBER KIT*", font="slant")  # "slant" fontu ile
    print("\033[1;36m" + banner + "\033[0m")  # Cyan renk ile banner
    print("\033[1;32mSiberKit Framework'e Hoşgeldiniz!\033[0m\n")
    time.sleep(1)

def animated_typing(text, delay=0.05):
    """Metni animasyonlu şekilde yazdırır."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print_banner()
    time.sleep(1)
    animated_typing("SiberKit Framework'ü başlatıyoruz...", 0.1)
    while True:
        print("\033[1;33m=== Araç Seçimi ===\033[0m")  # Sarı renk ile araç seçimi başlığı
        print("Lütfen bir araç seçin:\n")
        
        services = list_services()
        
        for index, service in enumerate(services, start=1):
            print(f"\033[1;34m[{index}]\033[0m {service}")  # Mavi renk ile araçlar
        print("\033[1;31m[0] Çıkış\033[0m")  # Kırmızı renk ile çıkış seçeneği
        
        try:
            choice = int(input("\033[1;37mSeçiminiz: \033[0m"))  # Beyaz renk ile seçim
            if choice == 0:
                print("\033[1;31mÇıkılıyor...\033[0m")  # Kırmızı renk ile çıkış mesajı
                break
            
            if 1 <= choice <= len(services):
                module_name = f"service.{services[choice - 1]}"
                module = importlib.import_module(module_name)
                
                if hasattr(module, "run"):
                    print(f"\n\033[1;32m{services[choice - 1]} aracı başlatılıyor...\033[0m\n")  # Yeşil renk ile araç başlatma
                    module.run()
                else:
                    print("\033[1;31mSeçilen araç 'run()' fonksiyonunu içermiyor!\033[0m")  # Kırmızı renk ile hata
            else:
                print("\033[1;31mGeçersiz seçim!\033[0m")  # Kırmızı renk ile geçersiz seçim
        except ValueError:
            print("\033[1;31mLütfen geçerli bir sayı girin!\033[0m")  # Kırmızı renk ile hatalı giriş

if __name__ == "__main__":
    main()

