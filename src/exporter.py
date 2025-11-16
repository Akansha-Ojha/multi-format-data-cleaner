from typing import Tuple
import pandas as pd
import io

def export_df(df: pd.DataFrame, file_type: str, original_filename: str) -> Tuple[bytes, str]:
    '''
    Returns (bytes_data, download_filename)
    '''
    lower = original_filename.lower()
    if file_type == 'csv' or lower.endswith('.csv'):
        return df.to_csv(index=False).encode('utf-8'), original_filename.replace('.csv','_cleaned.csv')
    if file_type == 'tsv' or lower.endswith('.tsv') or lower.endswith('.txt'):
        # preserve tab separated
        return df.to_csv(index=False, sep='\t').encode('utf-8'), original_filename.rsplit('.',1)[0] + '_cleaned.tsv'
    if file_type == 'excel' or lower.endswith('.xlsx') or lower.endswith('.xls'):
        buf = io.BytesIO()
        df.to_excel(buf, index=False, engine='openpyxl')
        return buf.getvalue(), original_filename.rsplit('.',1)[0] + '_cleaned.xlsx'
    if file_type == 'json' or lower.endswith('.json'):
        return df.to_json(orient='records', lines=False).encode('utf-8'), original_filename.rsplit('.',1)[0] + '_cleaned.json'
    # fallback to csv
    return df.to_csv(index=False).encode('utf-8'), original_filename + '_cleaned.csv'
