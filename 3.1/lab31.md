
## Отчет по лаборатоной работе №3.1
### Подготовили Ерилов Ю., Лепёха А., Саранцев А.


### Wireguard

Для установки был найден подходящий гайд с скриптом, который автоматизирует создание конфигов. 
* [Скрипт](https://github.com/drew2a/wireguard)
* [Гайд](https://drew2a.medium.com/replace-your-vpn-provider-by-setting-up-wireguard-on-digitalocean-6954c9279b17)

Таким образом настройка выполняется всего за несколько команд:

```shell
wget https://raw.githubusercontent.com/drew2a/wireguard/master/wg-ubuntu-server-up.sh

chmod +x ./wg-ubuntu-server-up.sh
sudo ./wg-ubuntu-server-up.sh
   ```

После чего создается конфиг:

```shell
[Interface]
Address = 10.0.0.1/24
SaveConfig = true
ListenPort = 51820
PrivateKey = ☺☺☺☺☺☺☺☺☺☺☺☺☺
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT; iptables -t nat -A POSTROUTING -o et>PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT; iptables -t nat -D POSTROUTING -o >[Peer]
PublicKey = QjqKj8gefk6OZE2KnnEO5a5qOk+fBBBpsDntcnXjWVA=
AllowedIPs = 10.0.0.2/32
[Peer]
PublicKey = IkxGljTeFFDuMqqWiDTwouptQBhokr12VWs2z3G/o3c=
AllowedIPs = 10.0.0.3/32
[Peer]
PublicKey = AeM5u/hMwWjdn4TeR4sSiyYSKVS264/VAxhq40tlmVo=
AllowedIPs = 10.0.0.4/32
[Peer]
PublicKey = TsigEU/le+ZP4wwZQ0ZWbiYbNTmIDbzGMch/ru78Hy8=
AllowedIPs = 10.0.0.5/32
[Peer]
PublicKey = eBjNh5CQNAyqXDcgoLfkc8U68mfc8TYqCQArMH7Ihx0=
AllowedIPs = 10.0.0.6/32
[Peer]
PublicKey = CUgST2KheO3GwFJn6ofPUCB0MhqxfHj8fAuPqqzgbSM=
AllowedIPs = 10.0.0.7/32
[Peer]
PublicKey = j0jlsc0hHvkoha6UJKou7TteE8EmiazsK94QqTEFYS4=
AllowedIPs = 10.0.0.8/32
[Peer]
PublicKey = xXws6l+pkJ8t4wAVh3QbeRSvc8M6J+TNNHoHwLhQvkk=
AllowedIPs = 10.0.0.9/32
[Peer]
PublicKey = D8ZvqyHFr4WTdpzHZJxGL0bQYkfHyuk7Wl1w+q3CWAU=
AllowedIPs = 10.0.0.10/32
[Peer]
PublicKey = IMuFcV5qqfpvxJwMXbwXYQ5INxebzPpCj2Gmb4lM3QI=
AllowedIPs = 10.0.0.11/32
   ```

И вместе с ним 10 конфигов для клиентов, например:

```shell
[Interface]
PrivateKey = ☺☺☺☺☺☺☺☺☺☺☺☺☺
ListenPort = 51820
Address = 10.0.0.2/32
DNS = 10.0.0.1

[Peer]
PublicKey = ksIo5Kapd1rBxKNMDdtudzyD8RzLoHahqFJEISb5WUQ=
AllowedIPs = 0.0.0.0/0
Endpoint = 157.245.73.34:51820
PersistentKeepalive = 21
```

Копируем конфиг на клиент и запускаем подключение.
Появившийся адаптер в ipconfig:

```shell
Неизвестный адаптер win:

   DNS-суффикс подключения . . . . . :
   IPv4-адрес. . . . . . . . . . . . : 10.0.0.2
   Маска подсети . . . . . . . . . . : 255.255.255.255
   Основной шлюз. . . . . . . . . : 0.0.0.0
```

Весь лог:

```shell
Настройка протокола IP для Windows


Неизвестный адаптер win:

   DNS-суффикс подключения . . . . . :
   IPv4-адрес. . . . . . . . . . . . : 10.0.0.2
   Маска подсети . . . . . . . . . . : 255.255.255.255
   Основной шлюз. . . . . . . . . : 0.0.0.0

Адаптер Ethernet vEthernet (WSL):

   DNS-суффикс подключения . . . . . :
   Локальный IPv6-адрес канала . . . : fe80::150d:c64:5cd:6d80%97
   IPv4-адрес. . . . . . . . . . . . : 172.17.96.1
   Маска подсети . . . . . . . . . . : 255.255.240.0
   Основной шлюз. . . . . . . . . :

Адаптер Ethernet Npcap Loopback Adapter:

   DNS-суффикс подключения . . . . . :
   Локальный IPv6-адрес канала . . . : fe80::b87e:d284:bc8f:c116%23
   Автонастройка IPv4-адреса . . . . : 169.254.193.22
   Маска подсети . . . . . . . . . . : 255.255.0.0
   Основной шлюз. . . . . . . . . :

Адаптер Ethernet Ethernet 3:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер Ethernet Ethernet 4:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Неизвестный адаптер Подключение по локальной сети:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер беспроводной локальной сети Подключение по локальной сети* 9:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер беспроводной локальной сети Подключение по локальной сети* 10:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер беспроводной локальной сети Беспроводная сеть:

   DNS-суффикс подключения . . . . . :
   Локальный IPv6-адрес канала . . . : fe80::f9a0:f233:23b9:2fcd%14
   IPv4-адрес. . . . . . . . . . . . : 172.20.7.43
   Маска подсети . . . . . . . . . . : 255.255.240.0
   Основной шлюз. . . . . . . . . : 172.20.0.1

Адаптер Ethernet Сетевое подключение Bluetooth:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :
```

### IPSEC

Делал все по гайду из описания лабы:

* [Репозиторий с гайдом](https://github.com/hwdsl2/setup-ipsec-vpn)

Вывод консоли при запуске скрипта установки:

```shell
IPsec VPN server is now ready for use!

Connect to your new VPN with these details:

Server IP: 159.65.207.158
IPsec PSK: ☺☺☺☺☺☺☺☺☺☺☺☺☺
Username: vpnuser
Password: ☺☺☺☺☺☺☺☺☺☺☺☺☺

Write these down. You'll need them to connect!

Important notes:   https://git.io/vpnnotes
Setup VPN clients: https://git.io/vpnclients
IKEv2 guide:       https://git.io/ikev2

================================================

================================================

IKEv2 setup successful. Details for IKEv2 mode:

VPN server address: 159.65.207.158
VPN client name: vpnclient

Client configuration is available at:
/root/vpnclient.p12 (for Windows & Linux)
/root/vpnclient.sswan (for Android)
/root/vpnclient.mobileconfig (for iOS & macOS)

Next steps: Configure IKEv2 clients. See:
  https://git.io/ikev2clients
Feedback: bit.ly/vpn-feedback
```

Далее копируем файл .p12 и запускаем команды:
```shell
powershell -command "Add-VpnConnection -ServerAddress 159.65.207.158 -Name 'My IKEv2 VPN' -TunnelType IKEv2 -AuthenticationMethod MachineCertificate -EncryptionLevel Required -PassThru"

powershell -command "Set-VpnConnectionIPsecConfiguration -ConnectionName 'My IKEv2 VPN' -AuthenticationTransformConstants GCMAES128 -CipherTransformConstants GCMAES128 -EncryptionMethod AES256 -IntegrityCheckMethod SHA256 -PfsGroup None -DHGroup Group14 -PassThru -Force"
```

После включения VPN адаптер видно при вводе команды ipconfig:
```shell
Адаптер PPP IKEv2 VPN 159.65.207.158:

   DNS-суффикс подключения . . . . . :
   IPv4-адрес. . . . . . . . . . . . : 192.168.43.10
   Маска подсети . . . . . . . . . . : 255.255.255.255
   Основной шлюз. . . . . . . . . : 0.0.0.0
```

Весь лог:

```shell
Настройка протокола IP для Windows


Адаптер Ethernet vEthernet (WSL):

   DNS-суффикс подключения . . . . . :
   Локальный IPv6-адрес канала . . . : fe80::150d:c64:5cd:6d80%97
   IPv4-адрес. . . . . . . . . . . . : 172.17.96.1
   Маска подсети . . . . . . . . . . : 255.255.240.0
   Основной шлюз. . . . . . . . . :

Адаптер Ethernet Npcap Loopback Adapter:

   DNS-суффикс подключения . . . . . :
   Локальный IPv6-адрес канала . . . : fe80::b87e:d284:bc8f:c116%23
   Автонастройка IPv4-адреса . . . . : 169.254.193.22
   Маска подсети . . . . . . . . . . : 255.255.0.0
   Основной шлюз. . . . . . . . . :

Адаптер Ethernet Ethernet 3:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер Ethernet Ethernet 4:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Неизвестный адаптер Подключение по локальной сети:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер беспроводной локальной сети Подключение по локальной сети* 9:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер беспроводной локальной сети Подключение по локальной сети* 10:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :

Адаптер PPP IKEv2 VPN 159.65.207.158:

   DNS-суффикс подключения . . . . . :
   IPv4-адрес. . . . . . . . . . . . : 192.168.43.10
   Маска подсети . . . . . . . . . . : 255.255.255.255
   Основной шлюз. . . . . . . . . : 0.0.0.0

Адаптер беспроводной локальной сети Беспроводная сеть:

   DNS-суффикс подключения . . . . . :
   Локальный IPv6-адрес канала . . . : fe80::f9a0:f233:23b9:2fcd%14
   IPv4-адрес. . . . . . . . . . . . : 172.20.7.43
   Маска подсети . . . . . . . . . . : 255.255.240.0
   Основной шлюз. . . . . . . . . : 172.20.0.1

Адаптер Ethernet Сетевое подключение Bluetooth:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :
```