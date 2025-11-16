
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    # Try converting numeric-like columns
    for col in df.columns:
        if df[col].dtype == object:
            # try numeric
            try:
                df[col] = pd.to_numeric(df[col].str.replace(',', '').str.strip(), errors='coerce')
            except Exception:
                pass
    return df

def normalize_text(df: pd.DataFrame, text_cols=None) -> pd.DataFrame:
    if text_cols is None:
        text_cols = df.select_dtypes(include=['object']).columns.tolist()
    for c in text_cols:
        df[c] = df[c].astype(str).str.strip().str.title().replace({'Nan':'Unknown','None':'Unknown','': 'Unknown'})
    return df

def impute_numeric(df: pd.DataFrame, strategy='median') -> pd.DataFrame:
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if num_cols:
        imputer = SimpleImputer(strategy=strategy)
        df[num_cols] = imputer.fit_transform(df[num_cols])
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)

def winsorize(df: pd.DataFrame, lower_q=0.01, upper_q=0.99) -> pd.DataFrame:
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for c in num_cols:
        low = df[c].quantile(lower_q)
        high = df[c].quantile(upper_q)
        df[c] = df[c].clip(lower=low, upper=high)
    return df

def scale_numeric(df: pd.DataFrame) -> pd.DataFrame:
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if num_cols:
        scaler = StandardScaler()
        df[[c+'_scaled' for c in num_cols]] = scaler.fit_transform(df[num_cols])
    return df
