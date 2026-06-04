# Inventory & Sales Analytics

Exploratory data analysis of 10,692 retail/wholesale transactions to identify 
profitability drivers, vendor risk, and inventory inefficiencies.

**Tools:** Python · SQLite3 · Power BI  
**Dataset:** 10,692 records · 16 features

---

## Key Findings
- 198 brands have high profit margins but low sales → promotional opportunity
- Top 10 vendors account for 65.7% of total purchases → supply chain risk
- Bulk orders yield 72% lower unit cost ($10.78 vs $39.06 for small orders)
- $2.71M capital tied up in unsold inventory
- Low-performing vendors average 41.55% margin vs 31.17% for top vendors

## Dashboard Preview
![Dashboard](powerbi/screenshots/Dashboard.png)

## Project Structure
inventory-sales-analytics/
├── data/raw/               # Raw CSV dataset
├── notebooks/              # Jupyter EDA notebooks
├── src/                    # Python scripts
├── sql/                    # SQLite queries
├── powerbi/                # .pbix file + screenshots
├── reports/                # EDA PDF report
├── requirements.txt
└── README.md

## How to Run
pip install -r requirements.txt
jupyter notebook notebooks/Vendor Performance Analysis.ipynb

##Analysis By : 
Name : Rohan Singh
Institute : Indian Institute of Technology (Indian School of Mines) Dhanbad