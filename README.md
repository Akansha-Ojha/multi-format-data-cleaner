# 📊 Multi-Format Data Cleaning & Processing App  
### Upload → Clean → Visualize → Download

[![Open In Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ewpqdxfwy5kyxthk7tjihs.streamlit.app/)


![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Cleaning-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An interactive **Streamlit application** that accepts multiple file formats (CSV, Excel, JSON, TXT, TSV), automatically cleans the data, visualizes it, and allows you to **download the cleaned dataset in the same format** as the uploaded file.

---

## 🚀 Features

✔ Upload CSV, Excel, JSON, TXT, TSV  
✔ Automatic data cleaning pipeline  
✔ Missing value imputation (mean/median)  
✔ Type conversion (object → numeric)  
✔ Whitespace & text normalization  
✔ Outlier handling (Winsorization)  
✔ Duplicate removal  
✔ Optional numeric scaling  
✔ Interactive visualizations  
✔ Download cleaned data in the **same format**  
✔ 100% Python-based (pandas, numpy, sklearn, seaborn, matplotlib)  
✔ Clean Streamlit UI  

---

## 📂 Project Structure
```
multi_format_cleaner_project/
│── app.py
│── requirements.txt
│── README.md
│── LICENSE
│── project_description.md
│
├── src/
│ ├── extractor.py # Detects file type & loads datasets
│ ├── cleaner.py # Cleaning pipeline
│ ├── visualizer.py # EDA plots
│ └── exporter.py # Saves cleaned data in same format
│
├── data/
│ ├── raw/ # Dirty sample datasets (CSV, Excel, JSON, TSV)
│ └── cleaned/ # Cleaned output files
│
└── notebooks/
└── demo.ipynb # Example Jupyter Notebook usage

```

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/multi-format-data-cleaner
cd multi-format-data-cleaner
pip install -r requirements.txt
streamlit run app.py
```


## 🧼 Cleaning Pipeline Includes

- Type conversion (numeric parsing)
- Text normalization (strip + title case)
- Missing-value handling (mean/median)
- Duplicate removal
- Outlier capping (Winsorization)
- Optional numerical scaling
- Produces ML/analytics-ready dataset

## 📊 Visualizations Generated

- Missing values bar chart  
- Histogram + KDE plot  
- Boxplot  
- Correlation heatmap  

## 📤 Download Cleaned Data

| Input Format | Output Format |
|--------------|---------------|
| `.csv`       | `.csv`        |
| `.xlsx`      | `.xlsx`       |
| `.json`      | `.json`       |
| `.txt`       | `.txt/.tsv`   |
| `.tsv`       | `.tsv`        |


## 🌐 Deployment (Streamlit Cloud)

1. Push this project to GitHub  
2. Visit: https://share.streamlit.io  
3. Select your GitHub repository  
4. Choose `app.py` as the main file  
5. Deploy! 🚀  

## 📝 License
This project is licensed under the MIT License.

## 👤 Author
Akansha Ojha
