# Отчет по лабораторной работе № 3.2
## Выполнили: Лепёха Алексей, Ерилов Юрий, Саранцев Александр
## Анализируемый файл: openvpn.pcap

### 1. Обнаружение VPN трафика
VPN трафик обнаружен

### 2. Вывод информации о следующих данных: 'src_ip','dst_ip','bidirectional_packets','bidirectional_bytes','application_name','application_category_name' с возможностью вывода для уникальных значений 'src_ip','dst_ip','application_name'
                      src_ip           dst_ip  bidirectional_packets  bidirectional_bytes application_name application_category_name
0            192.168.123.189     77.74.181.38                     11                 1651              TLS                       Web
1             149.154.167.41  192.168.123.189                    128                42146     TLS.Telegram                      Chat
2  fe80::f9a0:f233:23b9:2fcd         ff02::fb                     19                 3926             MDNS                   Network
3            192.168.123.189  239.255.255.250                      1                  217             SSDP                    System
4            192.168.123.189  239.255.255.250                      4                  868             SSDP                    System
5            192.168.123.189      224.0.0.251                     19                 3546             MDNS                   Network
6            192.168.123.189    157.245.73.34                  64933             48523879          OpenVPN                       VPN