
import pandas as pd
import json
from typing import Tuple, Optional
import io

def detect_file_type(filename: str) -> str:
    lower = filename.lower()
    if lower.endswith('.csv'):
        return 'csv'
    if lower.endswith('.xlsx') or lower.endswith('.xls'):
        return 'excel'
    if lower.endswith('.json'):
        return 'json'
    if lower.endswith('.tsv'):
        return 'tsv'
    if lower.endswith('.txt'):
        return 'txt'
    return 'unknown'

def read_file(file, filename: str) -> Tuple[pd.DataFrame, str]:
    '''Read uploaded file (file is a file-like object) and return DataFrame and detected type'''
    ftype = detect_file_type(filename)
    if ftype == 'csv':
        df = pd.read_csv(file)
    elif ftype == 'excel':
        df = pd.read_excel(file)
    elif ftype == 'json':
        # try to load as list of records or dict of lists
        try:
            data = json.load(file)
            df = pd.json_normalize(data)
        except Exception:
            # try read as lines
            file.seek(0)
            df = pd.read_json(file, lines=True)
    elif ftype == 'tsv' or ftype == 'txt':
        # attempt delimiter sniffing for txt
        file.seek(0)
        sample = file.read(4096)
        file.seek(0)
        import csv as _csv
        sniffer = _csv.Sniffer()
        try:
            dialect = sniffer.sniff(sample)
            sep = dialect.delimiter
        except Exception:
            sep = ','
        df = pd.read_csv(file, sep=sep)
    else:
        raise ValueError(f'Unsupported file type: {filename}')
    return df, ftype
