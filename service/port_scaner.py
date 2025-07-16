import os
import socket  # socket modülünü import ettik

def get_local_ip():
    """Cihazın yerel ağdaki IP adresini alır."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))  # Yerel ağdaki herhangi bir IP'ye bağlanmaya çalışıyoruz
        local_ip = s.getsockname()[0]
    except:
        local_ip = '0.0.0.0'  # Eğer bağlantı sağlanamazsa
    finally:
        s.close()
    return local_ip

def run():
    print("Port Tarama Aracı")

    # Kendi IP adresini göster
    local_ip = get_local_ip()
    print(f"Sizin IP adresiniz: {local_ip}")

    # Kullanıcıdan IP adresini al
    ip = input("Lütfen taramak istediğiniz IP adresini girin: ")

    # Nmap komutunu çalıştır
    print(f"\n{ip} IP adresindeki port taraması başlatılıyor...")

    # Nmap komutunu çalıştırarak portları tarayalım
    os.system(f"nmap {ip}")
