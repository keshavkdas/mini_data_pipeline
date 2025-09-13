# 🚀 Mini Data Pipeline Dashboard

Visualize your sales data directly from MySQL using **Python + Streamlit**!  
Build interactive dashboards with charts, tables, and filters — no Power BI needed.

---

## 🛠 Setup

1. **Clone the repository**  
```bash
git clone https://github.com/<your_username>/mini_data_pipeline.git
cd my_data_pipeline
````

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure MySQL connection**

* Open `constants.py`
* Use environment variables to keep credentials safe:

```python
from dotenv import load_dotenv
import os
load_dotenv()

mysql_uri = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
```

* Create a `.env` file in the repo root:

```
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_DB=your_database
```

> ⚠️ **Do not commit `.env` to GitHub!** Ensure it is in `.gitignore`.

---

## ▶️ Run the Dashboard

```bash
streamlit run app.py
```

* The dashboard will open in your browser at `http://localhost:8501`
* Explore **interactive charts**, **tables**, and **filters**

---


### Main Dashboard

![Dashboard Screenshot](images/dashboard.png)


---

## ✅ Features

* 📥 **Extract** data directly from MySQL
* 🔄 **Transform** data and calculate metrics like `revenue`
* 📊 **Visualize** data with interactive Streamlit + Plotly charts
* 🔍 **Filter** by product, region, or other fields
* 🌐 Fully web-based dashboard without Power BI

---

## 💡 Tips

* Keep database credentials **secure using environment variables**
* Supports **local MySQL** or **cloud MySQL (RDS, etc.)**
* Extend the dashboard with more charts, KPIs, or tables
* Deploy online via **Streamlit Cloud, Heroku, or Railway**

---

## 📁 Project Structure

```
my_data_pipeline/
│
├── app.py                  # Main Streamlit dashboard
├── etl.py                  # Optional ETL scripts
├── constants.py            # MySQL connection (uses dotenv recommended)
├── requirements.txt        # Python dependencies
├── README.md               # Project instructions
└── images/                 # Screenshots for README
```

---

## 🛡 Security

* `.env` file is **ignored in Git**
* No secrets or passwords are pushed to GitHub
* Use your own credentials locally to run the dashboard

---

## ⚡ Future Enhancements

* Add **dynamic KPIs** for top-selling products or regions
* Include **date filters** and **time-series charts**
* Integrate with other databases or APIs for a larger pipeline
* Deploy the dashboard **online** for team access

```

This is **fully copy-paste ready** — just save it as `README.md` in your repo.
```
