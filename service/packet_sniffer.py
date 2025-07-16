# packet_sniffer.py
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] Yeni Paket: {ip_layer.src} -> {ip_layer.dst}")
        if TCP in packet:
            print("  Protokol: TCP")
        elif UDP in packet:
            print("  Protokol: UDP")
        elif ICMP in packet:
            print("  Protokol: ICMP")
        else:
            print("  Protokol: Diğer")

def run():
    """Paket dinleyiciyi başlatır."""
    print("\n\033[1;32mPacket Sniffer Aracı\033[0m")
    iface = input("\033[1;37mLütfen dinlenecek arayüzü girin (örnek: eth0, wlan0): \033[0m")
    print(f"{iface} arayüzü üzerinde dinleniyor...\nDurmak için Ctrl+C'ye basın.\n")
    sniff(iface=iface, prn=packet_callback, store=False)