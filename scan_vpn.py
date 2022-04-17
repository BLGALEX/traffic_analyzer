from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from nfstream import NFStreamer
import os
import pickle

DATA_PATH = 'datasets/'


def get_md_header():
    return '# Отчет по лабораторной работе № 3.2\n' \
           '## Выполнили: Лепёха Алексей, Ерилов Юрий, Саранцев Александр\n' \
           '# Результаты сканирования датасетов обученной моделью\n\n'


def scan_data_for_vpn_using(data_folder=DATA_PATH):
    tests = os.listdir(data_folder)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    res = ''

    for item in tests:
        if item.endswith(".pcap"):
            res += "### "+str(item)+":\n"
            df = NFStreamer(source=os.path.join(data_folder, item)).to_pandas()
            X = df[[
                "src_port",
                "dst_port",
                "bidirectional_packets",
                "bidirectional_bytes",
                "bidirectional_duration_ms",
                "src2dst_duration_ms",
                "src2dst_packets",
                "src2dst_bytes",
                "application_is_guessed",
            ]]
            X = preprocessing.normalize(X, axis=0)
            y_predicted = model.predict(X)
            if 1 in y_predicted:
                res += "#### VPN is used\n\n"
            else:
                res += "#### VPN is not used\n\n"
    return  res

if __name__ == '__main__':
    result = get_md_header()
    result += scan_data_for_vpn_using()
    with open("Scan_results.md", "w", encoding="utf-8") as f:
        f.write(result)

