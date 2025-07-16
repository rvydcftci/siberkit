import subprocess
import platform

def trace_route(domain):
    print(f"\n[+] '{domain}' için traceroute başlatılıyor...\n")
    
    system_platform = platform.system().lower()
    
    if system_platform == "windows":
        # Windows'ta tracert komutu kullanılır
        command = ["tracert", domain]
    else:
        # Linux/macOS'ta traceroute komutu kullanılır
        command = ["traceroute", domain]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        print(result.stdout)
    except FileNotFoundError:
        print("[!] traceroute komutu sistemde yüklü değil. Lütfen yükleyin.")
    except subprocess.TimeoutExpired:
        print("[!] Traceroute zaman aşımına uğradı.")
    except Exception as e:
        print(f"[!] Hata oluştu: {e}")

def run():
    domain = input("Hedef domain girin (örnek: example.com): ").strip()
    if not domain:
        print("[!] Geçerli bir domain girmeniz gerekiyor.")
        return
    trace_route(domain)
