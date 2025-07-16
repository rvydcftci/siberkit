# mac_changer.py
import subprocess
import re
import random

def get_current_mac(interface):
    result = subprocess.run(["ip", "link", "show", interface], capture_output=True, text=True)
    match = re.search(r"link/ether (\S+)", result.stdout)
    return match.group(1) if match else None

def generate_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def validate_mac(mac):
    return re.match(r"^([0-9a-f]{2}:){5}[0-9a-f]{2}$", mac.lower())

def change_mac(interface, new_mac):
    subprocess.run(["sudo", "ip", "link", "set", interface, "down"])
    subprocess.run(["sudo", "ip", "link", "set", interface, "address", new_mac])
    subprocess.run(["sudo", "ip", "link", "set", interface, "up"])

def run():
    """MAC adresi değiştirici aracı"""
    print("\n\033[1;32mMAC Changer Aracı\033[0m")
    interface = input("\033[1;37mArayüz adı (örnek: wlan0): \033[0m")
    user_mac = input("Yeni MAC adresi girin (boş bırakırsan rastgele atanır): ").strip()

    new_mac = user_mac if user_mac else generate_random_mac()

    if not validate_mac(new_mac):
        print("Geçersiz MAC adresi formatı!")
        return

    old_mac = get_current_mac(interface)
    print(f"Mevcut MAC: {old_mac}")
    change_mac(interface, new_mac)
    updated_mac = get_current_mac(interface)

    if updated_mac.lower() == new_mac.lower():
        print(f" Başarıyla değiştirildi: {updated_mac}")
    else:
        print(f" MAC adresi değiştirilemedi!")