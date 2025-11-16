# 📊 Multi-Format Data Cleaning & Processing App  
### Upload → Clean → Visualize → Download

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
✔ Outlier handling with Winsorization  
✔ Duplicate removal  
✔ Optional numeric scaling  
✔ Interactive visualizations  
✔ Download cleaned data in the **same format**  
✔ Fully Python-based (pandas, numpy, sklearn, seaborn, matplotlib)  
✔ Streamlit frontend for clean UI  

---

## 📂 Project Structure
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
│ ├── visualizer.py # Graphs (EDA)
│ └── exporter.py # Saves cleaned data in the same input format
│
├── data/
│ ├── raw/ # Dirty sample datasets (CSV, Excel, JSON, TSV)
│ └── cleaned/ # Cleaned output files
│
└── notebooks/
└── demo.ipynb # Example Jupyter Notebook usage


---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/multi-format-data-cleaner
cd multi-format-data-cleaner
pip install -r requirements.txt
