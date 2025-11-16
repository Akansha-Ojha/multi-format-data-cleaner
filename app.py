
import streamlit as st
import pandas as pd
from src.extractor import read_file, detect_file_type
from src.cleaner import convert_types, normalize_text, impute_numeric, remove_duplicates, winsorize, scale_numeric
from src.visualizer import plot_missing_counts, plot_distribution, plot_correlation
from src.exporter import export_df
from io import BytesIO

st.set_page_config(layout='wide', page_title='Multi-format Data Cleaner')
st.title('Multi-format Data Cleaning & Processing App')

st.sidebar.header('Upload & Options')
uploaded = st.sidebar.file_uploader('Upload file (CSV, XLSX, JSON, TSV, TXT)', type=['csv','xlsx','xls','json','tsv','txt'])
use_sample = st.sidebar.checkbox('Use sample dataset', value=True)
impute_strategy = st.sidebar.selectbox('Impute numeric with', ['median','mean'])
apply_winsor = st.sidebar.checkbox('Apply winsorization', value=True)
lower_q = st.sidebar.slider('Lower quantile', 0.0, 0.2, 0.01, 0.01)
upper_q = st.sidebar.slider('Upper quantile', 0.8, 1.0, 0.99, 0.01)
drop_duplicates_opt = st.sidebar.checkbox('Drop duplicates', value=True)
normalize_text_opt = st.sidebar.checkbox('Normalize text columns', value=True)
scale_opt = st.sidebar.checkbox('Add scaled numeric columns', value=False)

if use_sample and uploaded is None:
    df, ftype = read_file(open('data/raw/sample.csv','r', encoding='utf-8'), 'sample.csv')
elif uploaded is not None:
    df, ftype = read_file(uploaded, uploaded.name)
else:
    st.info('Upload a file or use the sample dataset.')
    st.stop()

st.subheader('Raw data preview')
st.dataframe(df.head())

with st.expander('Raw data info'):
    bio = BytesIO()
    df.info(buf=bio)
    st.text(bio.getvalue().decode())

st.subheader('Missing values per column')
st.bar_chart(df.isnull().sum())

# Cleaning controls
st.subheader('Cleaning Controls')
st.write('Detected columns and types:')
st.write(df.dtypes)

if st.button('Run Cleaning Pipeline'):
    df_clean = df.copy()
    df_clean = convert_types(df_clean)
    if normalize_text_opt:
        df_clean = normalize_text(df_clean)
    df_clean = impute_numeric(df_clean, strategy=impute_strategy)
    if apply_winsor:
        df_clean = winsorize(df_clean, lower_q=lower_q, upper_q=upper_q)
    if drop_duplicates_opt:
        df_clean = remove_duplicates(df_clean)
    if scale_opt:
        df_clean = scale_numeric(df_clean)

    st.success('Cleaning done. Preview:')
    st.dataframe(df_clean.head())

    # Visualizations
    st.subheader('Visualizations')
    miss_img = plot_missing_counts(df_clean)
    st.image(miss_img)
    num_cols = df_clean.select_dtypes(include=['number']).columns.tolist()
    if num_cols:
        sel = st.selectbox('Select numeric column to plot', num_cols)
        dist_img = plot_distribution(df_clean, sel)
        st.image(dist_img)
        corr_img = plot_correlation(df_clean)
        if corr_img is not None:
            st.image(corr_img)

    # Export
    bytes_data, outname = export_df(df_clean, ftype, uploaded.name if uploaded is not None else 'sample.csv')
    st.download_button('Download cleaned file', data=bytes_data, file_name=outname, mime='application/octet-stream')
