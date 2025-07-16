import requests

def check_vpn(ip):
    token = 'c635016bc650e5'  # ipinfo.io token (kendi tokeninle değiştirmen önerilir)
    url = f"https://ipinfo.io/{ip}/json?token={token}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"[!] API isteği başarısız oldu. Kod: {response.status_code}"

        data = response.json()

        # 'privacy' alanı her zaman olmayabilir, önlem al
        privacy_info = data.get("privacy", {})
        if privacy_info.get("vpn"):
            return f"[+] VPN tespit edildi: {ip}"
        else:
            return f"[-] VPN tespit edilmedi: {ip}"
    
    except Exception as e:
        return f"[!] Hata oluştu: {e}"

def get_ip_input():
    ip = input("VPN kontrolü yapmak için IP adresini girin: ").strip()
    return ip

def run():
    ip = get_ip_input()
    if not ip:
        print("[!] Geçerli bir IP adresi girilmedi.")
        return
    
    result = check_vpn(ip)
    print(result)

if __name__ == "__main__":
    run()

