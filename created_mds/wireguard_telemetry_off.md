# Отчет по лабораторной работе № 3.2
## Выполнили: Лепёха Алексей, Ерилов Юрий, Саранцев Александр
## Анализируемый файл: datasets/wireguard_telemetry_off.pcap

### 1. Обнаружение VPN трафика
VPN трафик обнаружен

### 2. Вывод информации о следующих данных: 'src_ip','dst_ip','bidirectional_packets','bidirectional_bytes','application_name','application_category_name' с возможностью вывода для уникальных значений 'src_ip','dst_ip','application_name'
| src_ip          | dst_ip          |   bidirectional_packets |   bidirectional_bytes | application_name   | application_category_name   |
|:----------------|:----------------|------------------------:|----------------------:|:-------------------|:----------------------------|
| 13.107.21.200   | 192.168.123.189 |                       1 |                    54 | TLS.Azure          | Cloud                       |
| 192.168.123.189 | 10.0.0.1        |                       4 |                   264 | DNS                | Network                     |
| 77.74.181.38    | 192.168.123.189 |                      10 |                   771 | TLS                | Web                         |
| 13.107.6.158    | 192.168.123.189 |                       1 |                    54 | TLS.Azure          | Cloud                       |
| 52.113.196.254  | 192.168.123.189 |                       1 |                    54 | TLS.Skype_Teams    | VoIP                        |
| 13.107.246.46   | 192.168.123.189 |                       1 |                    54 | TLS.Azure          | Cloud                       |
| 149.154.167.50  | 192.168.123.189 |                       2 |                   108 | TLS.Telegram       | Chat                        |
| 157.245.73.34   | 192.168.123.189 |                   37395 |              30678362 | WireGuard          | VPN                         |
| 204.79.197.222  | 192.168.123.189 |                       1 |                    54 | TLS.Azure          | Cloud                       |
 #### Уникальные
| src_ip          | dst_ip          | application_name   |
|:----------------|:----------------|:-------------------|
| 13.107.21.200   | 192.168.123.189 | TLS.Azure          |
| 192.168.123.189 | 10.0.0.1        | DNS                |
| 77.74.181.38    | 192.168.123.189 | TLS                |
| 13.107.6.158    | 192.168.123.189 | TLS.Azure          |
| 52.113.196.254  | 192.168.123.189 | TLS.Skype_Teams    |
| 13.107.246.46   | 192.168.123.189 | TLS.Azure          |
| 149.154.167.50  | 192.168.123.189 | TLS.Telegram       |
| 157.245.73.34   | 192.168.123.189 | WireGuard          |
| 204.79.197.222  | 192.168.123.189 | TLS.Azure          |

### 3. Диапазон времени захвата траффика
2022-04-17 20:19:29 – 2022-04-17 20:21:15

### 4. Суммарный обьем траффика и сумма пакетов для каждого ip destination
| dst_ip          |   bidirectional_packets |   bidirectional_bytes |
|:----------------|------------------------:|----------------------:|
| 10.0.0.1        |                       4 |         264           |
| 192.168.123.189 |                   37412 |           3.06795e+07 |

