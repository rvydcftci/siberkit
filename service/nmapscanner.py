import subprocess
import os
import time

def run_nmap_scan(target):
    print(f"[*] Hedef taranıyor: {target}")
    try:
        # Nmap komutunu çalıştırıyoruz (tüm portlar ve işletim sistemi tespiti)
        command = ['nmap', '-sS', '-Pn', '-T4', '-p-', '-O', target]
        
        # Başlangıç zamanı
        start_time = time.time()
        
        # Nmap komutunu çalıştırıyoruz
        result = subprocess.run(command, capture_output=True, text=True, timeout=120)  # Zaman aşımını uzattık

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[+] Nmap çıktısı ({elapsed_time:.2f} saniye sürdü):")
        print(result.stdout)

        if result.stderr:
            print("[-] Hata mesajı:")
            print(result.stderr)

        # Nmap çıktısında açık portlar ve servisler hakkında bilgi almak
        if "open" in result.stdout:
            print("\n[+] Açık Portlar ve Servisler:")
            # Açık portları filtrelemek
            open_ports = [line for line in result.stdout.split('\n') if 'open' in line]
            for port in open_ports:
                print(f" - {port}")
        else:
            print("[-] Açık portlar tespit edilemedi.")
        
        # İşletim sistemi tespiti sonuçları
        if "OS details" in result.stdout:
            print("\n[+] İşletim Sistemi Tespiti:")
            os_details = [line for line in result.stdout.split('\n') if "OS details" in line]
            for detail in os_details:
                print(f" - {detail}")

    except subprocess.TimeoutExpired:
        print("[!] Nmap taraması zaman aşımına uğradı. Tarama süresi 120 saniye olarak belirlendi.")
    except FileNotFoundError:
        print("[!] Nmap yüklü değil. Lütfen 'nmap' aracını kur.")
    except Exception as e:
        print(f"[!] Beklenmedik bir hata oluştu: {e}")

def run():
    target = input("Taranacak IP veya domain gir: ").strip()
    if not target:
        print("[-] Geçerli bir hedef girmelisin.")
        return
    run_nmap_scan(target)

if __name__ == "__main__":
    run()

