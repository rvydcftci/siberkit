import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import os

class DirScanner:
    def __init__(self, target_url, wordlist=None, max_threads=10):
        self.target_url = target_url if target_url.startswith(('http://', 'https://')) else f'http://{target_url}'
        self.wordlist = self.load_wordlist(wordlist) if wordlist else self.default_wordlist()
        self.max_threads = max_threads
        self.found_dirs = []

    @staticmethod
    def default_wordlist():
        return [
            'admin', 'login', 'wp-admin', 'images', 'css', 'js',
            'assets', 'uploads', 'backup', 'phpmyadmin', 'test'
        ]

    @staticmethod
    def load_wordlist(wordlist_path):
        try:
            with open(wordlist_path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"[!] Wordlist dosyası bulunamadı: {wordlist_path}")
            return []
        except Exception as e:
            print(f"[!] Wordlist yüklenirken hata: {e}")
            return []

    def scan_dir(self, dir_path):
        url = urljoin(self.target_url + '/', dir_path)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                self.found_dirs.append(url)
                print(f"[+] Bulundu: {url}")
        except requests.RequestException:
            pass

    def scan(self):
        if not self.wordlist:
            print("[!] Wordlist boş, tarama yapılamıyor.")
            return

        print(f"\n[+] {self.target_url} dizinleri taranıyor...")
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            executor.map(self.scan_dir, self.wordlist)

        print("\n[-] Tarama tamamlandı. Bulunan dizinler:")
        for url in self.found_dirs:
            print(f" - {url}")

def run():
    target = input("Hedef domain girin (örnek: turkcell.com): ").strip()
    wordlist_path = input("Wordlist dosyasının yolu: ").strip()

    if not os.path.exists(wordlist_path):
        print(f"[!] Hata: Wordlist dosyası bulunamadı: {wordlist_path}")
        return

    scanner = DirScanner(target, wordlist_path)
    scanner.scan()

# Bu blok sadece bu dosya doğrudan çalıştırıldığında devreye girer
if __name__ == "__main__":
    run()

