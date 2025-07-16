import requests

def find_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; SubdomainFinder/1.0)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"[-] crt.sh isteği başarısız oldu. HTTP Kod: {response.status_code}")
            return []

        json_data = response.json()
        subdomains = set()

        for entry in json_data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split('\n'):
                sub = sub.strip()
                if sub.endswith(domain):
                    subdomains.add(sub)

        return sorted(subdomains)

    except requests.exceptions.RequestException as e:
        print(f"[!] HTTP isteği sırasında hata oluştu: {e}")
        return []
    except ValueError:
        print("[!] Geçersiz JSON yanıtı alındı.")
        return []
    except Exception as e:
        print(f"[!] Genel bir hata oluştu: {e}")
        return []

def run():
    domain = input("Hedef domain girin (örnek: example.com): ").strip()
    if not domain:
        print("[!] Geçerli bir domain girmelisiniz.")
        return

    print(f"\n[+] '{domain}' için subdomainler aranıyor...\n")
    results = find_subdomains(domain)

    if results:
        print(f"[+] {len(results)} subdomain bulundu:\n")
        for sub in results:
            print(f" - {sub}")
    else:
        print("[-] Hiçbir subdomain bulunamadı.")
