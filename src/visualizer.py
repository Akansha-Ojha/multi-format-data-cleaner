
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

sns.set()

def plot_missing_counts(df: pd.DataFrame):
    missing = df.isnull().sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8,4))
    missing.plot.bar(ax=ax)
    ax.set_title('Missing values per column')
    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf

def plot_distribution(df: pd.DataFrame, col: str):
    fig, ax = plt.subplots(1,2,figsize=(10,4))
    sns.histplot(df[col].dropna(), kde=True, ax=ax[0])
    sns.boxplot(x=df[col], ax=ax[1])
    fig.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf

def plot_correlation(df: pd.DataFrame):
    num = df.select_dtypes(include=['number'])
    if num.shape[1] < 2:
        return None
    corr = num.corr()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf
