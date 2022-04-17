import argparse
from nfstream import NFStreamer
from datetime import datetime


class PCAPAnalyzer():

    def __init__(self, filename):
        self.filename = filename
        self.stream = NFStreamer(self.filename).to_pandas()

    def get_md_header(self):
        return '# Отчет по лабораторной работе № 3.2\n' \
               '## Выполнили: Лепёха Алексей, Ерилов Юрий, Саранцев Александр\n' \
               f'## Анализируемый файл: {self.filename}\n\n'

    def get_vpn_assertion(self):
        res = "### 1. Обнаружение VPN трафика\n"
        if "VPN" in self.stream['application_category_name'].unique():
            res += "VPN трафик обнаружен\n\n"
        else:
            res += "VPN трафик не обнаружен\n\n"
        return res

    def get_info_2(self):
        res = "### 2. Вывод информации о следующих данных: " \
                 "'src_ip','dst_ip','bidirectional_packets'," \
                 "'bidirectional_bytes','application_name','application_category_name' " \
                 "с возможностью вывода для уникальных значений " \
                 "'src_ip','dst_ip','application_name'\n"
        res += self.stream[[
            'src_ip',
            'dst_ip',
            'bidirectional_packets',
            'bidirectional_bytes',
            'application_name',
            'application_category_name'
        ]].to_markdown(index=False)
        res += '\n #### Уникальные\n'
        res += self.stream[[
            'src_ip',
            'dst_ip',
            'application_name'
        ]].drop_duplicates().to_markdown(index=False)
        res += "\n\n"
        return res

    def get_data_capture_start_end(self):
        res = "### 3. Диапазон времени захвата траффика\n"
        start = datetime.fromtimestamp(self.stream['bidirectional_first_seen_ms'].min() / 1000.0).strftime(
            '%Y-%m-%d %H:%M:%S')
        end = datetime.fromtimestamp(self.stream['bidirectional_last_seen_ms'].max() / 1000.0).strftime(
            '%Y-%m-%d %H:%M:%S')
        res += f'{start} – {end}\n\n'
        return res

    def get_trafic_summary(self):
        res = '### 4. Суммарный обьем траффика и сумма пакетов для каждого ip destination\n'

        res += self.stream[[
            'dst_ip',
            'bidirectional_packets',
            'bidirectional_bytes',
        ]].groupby(["dst_ip"]).sum().sort_values('bidirectional_bytes').to_markdown()
        res += "\n\n"
        return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for analyze .pcap file and generate .md file')
    parser.add_argument('filename', type=str, help='Absolute or relative .pcap file path, .md file will be saved '
                                                   'in the same folder with the same name')
    args = parser.parse_args()
    result = ""
    analyzer = PCAPAnalyzer(args.filename)
    result += analyzer.get_md_header()
    result += analyzer.get_vpn_assertion()
    result += analyzer.get_info_2()
    result += analyzer.get_data_capture_start_end()
    result += analyzer.get_trafic_summary()
    with open(f'{".".join(args.filename.split(".")[0:-1])}.md', "w", encoding="utf-8") as f:
        f.write(result)

