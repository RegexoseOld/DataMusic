import pandas as pd
import csv

txt_file_path = 'data/test_data01.txt'
csv_path = 'data/test_data.csv'

def convert_csv(t_path, c_path):
    read_file = pd.read_csv(t_path)
    read_file.to_csv(c_path)

def csv_convert():
    with open(txt_file_path, 'r') as in_file:
        stripped = (line.strip().replace("\\", "") for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(csv_path, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

csv_convert()

