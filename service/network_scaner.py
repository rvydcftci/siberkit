from scapy.all import ARP, Ether, srp

def run():
    print("Ağ Tarama Aracı - Scapy")

    # Kullanıcıdan IP aralığını al
    ip_range = input("Lütfen taramak istediğiniz IP aralığını girin (örnek: 192.168.1.0/24): ")

    # Kullanıcıdan ağ cihazı arayüzünü al
    interface = input("Lütfen ağ cihazı arayüzünü girin (örnek: eth0, wlan0): ")

    # ARP istekleri göndererek ağdaki cihazları tespit et
    print(f"{ip_range} aralığında tarama başlatılıyor...")
    
    # ARP isteği (IP - MAC adresi eşleştirmesi)
    arp_request = ARP(pdst=ip_range)
    ether_request = Ether(dst="ff:ff:ff:ff:ff:ff")  # Yayın MAC adresi
    packet = ether_request/arp_request

    # Paketleri gönder ve cevapları al
    print("Cevaplar bekleniyor...")
    result = srp(packet, timeout=3, iface=interface, verbose=False)[0]

    # Sonuçları yazdır
    devices = []
    for sent, received in result:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})

    # Eğer cihaz varsa, listele
    if devices:
        print("\nBulunan cihazlar:")
        for device in devices:
            print(f"IP: {device['ip']}   MAC: {device['mac']}")
    else:
        print("Ağda cihaz bulunamadı.")


