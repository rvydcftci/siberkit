import dns.resolver
import socket

def get_dns_records(domain):
    """DNS kayıtlarını alır ve ekrana yazdırır."""
    # A Kaydı (IP adresi)
    try:
        print(f"\n[*] A Record (IP address) for {domain}:")
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(ipval.to_text())
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("DNS A Record bulunamadı.")

    # MX Kaydı (Mail Server)
    try:
        print(f"\n[*] MX Record (Mail Servers) for {domain}:")
        result = dns.resolver.resolve(domain, 'MX')
        for mxval in result:
            print(mxval.exchange.to_text())
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("DNS MX Record bulunamadı.")

    # NS Kaydı (Name Server)
    try:
        print(f"\n[*] NS Record (Name Servers) for {domain}:")
        result = dns.resolver.resolve(domain, 'NS')
        for nsval in result:
            print(nsval.to_text())
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("DNS NS Record bulunamadı.")

def run():
    """DNS Lookup aracını çalıştırır."""
    print("\n\033[1;32mDNS Lookup Aracı\033[0m")

    # Kullanıcıdan domain adı al
    domain = input("\033[1;37mLütfen DNS sorgulamak istediğiniz domain adını girin: \033[0m")

    # DNS kayıtlarını al ve yazdır
    get_dns_records(domain)

