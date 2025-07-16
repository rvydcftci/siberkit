from pysnmp.hlapi import *

def snmp_walk(target, community):
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((target, 161)),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1')),
        lexicographicMode=False
    ):
        if errorIndication:
            print(f"[!] Hata: {errorIndication}")
            break
        elif errorStatus:
            print(f"[!] SNMP Hatası: {errorStatus.prettyPrint()} at {errorIndex}")
            break
        else:
            for varBind in varBinds:
                print(f"{varBind[0]} = {varBind[1]}")

def run():
    target = input("Hedef IP adresini girin (örnek: 192.168.1.1): ").strip()
    community = input("Community string girin (örnek: public): ").strip()

    if not target or not community:
        print("[!] Geçerli bir IP adresi ve community string giriniz.")
        return

    print(f"\n[+] '{target}' cihazı için SNMP Walk başlatılıyor...\n")
    snmp_walk(target, community)

if __name__ == "__main__":
    run()
