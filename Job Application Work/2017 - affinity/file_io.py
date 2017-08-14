import csv


def read_from_file(file_path):
    with open(file_path, 'rb') as f:
        path_tokens = file_path.split('.')
        if path_tokens[-1] == 'tsv':
            rows = csv.reader(f, delimiter='\t', quotechar='"')
        elif path_tokens[-1] == 'csv':
            rows = csv.reader(f, delimiter=',', quotechar='"')
        else:
            raise RuntimeError('Incorrect file extension')
        return [row for row in rows]


def write_to_file(file_path, data_list):
    with open(file_path, 'wb') as f:
        path_tokens = file_path.split('.')
        if path_tokens[-1] == 'tsv':
            writer = csv.writer(f, delimiter='\t')
        elif path_tokens[-1] == 'csv':
            writer = csv.writer(f, delimiter=',')
        else:
            raise RuntimeError('Incorrect file extension')
        for data in data_list:
            writer.writerow(data)
