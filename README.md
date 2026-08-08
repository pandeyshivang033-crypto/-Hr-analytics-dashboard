# 📊 HR Analytics Dashboard

An interactive Tableau dashboard analyzing employee attrition trends and
monitoring workforce KPIs — built to help HR teams identify patterns
behind employee turnover and support retention planning.

## 📁 Project Structure

```
hr-analytics-dashboard/
├── data/
│   └── hr_data.csv           # employee dataset (1,200 records)
├── generate_hr_data.py       # script that generated the dataset
├── HR_Analytics_Dashboard.twbx  # (add after building in Tableau)
└── README.md
```

## 📈 Dataset Overview

1,200 employee records with the following fields:

| Column | Description |
|---|---|
| EmployeeID | Unique employee identifier |
| Age, Gender, MaritalStatus, Education | Demographics |
| Department, JobRole | Org structure |
| YearsAtCompany, DistanceFromHome_km | Tenure & commute |
| MonthlyIncome | Compensation |
| JobSatisfaction, WorkLifeBalance (1–4 scale) | Engagement metrics |
| OverTime | Yes/No |
| PerformanceRating (1–4 scale) | Performance |
| **Attrition** | Yes/No — target metric |

## 🛠️ How to Build the Dashboard in Tableau

1. **Open Tableau Desktop** → Connect → Text File → select `data/hr_data.csv`.
2. Go to a new **Sheet** and build these views:
   - **KPI cards**: Total Employees, Attrition Rate (%), Average Monthly Income — use `Number of Records` and calculated fields (e.g. `SUM(IF Attrition='Yes' THEN 1 ELSE 0 END) / COUNT(EmployeeID)`).
   - **Attrition by Department**: Bar chart — `Department` on Columns, `Attrition Rate` on Rows, color by Attrition.
   - **Attrition by Job Satisfaction / Work-Life Balance**: Bar or heatmap — shows how disengagement drives attrition.
   - **Attrition vs OverTime**: Stacked bar — a classic driver of turnover.
   - **Age & Tenure distribution**: Histogram of `Age` and `YearsAtCompany`, colored by Attrition.
   - **Income by Department**: Box plot of `MonthlyIncome` per `Department`.
3. Combine the sheets into a **Dashboard** (New Dashboard → drag sheets onto canvas). Add filters for `Department` and `Gender` so viewers can slice the data.
4. Add a title, clean up colors (red/gray for Attrition Yes/No is a common convention), and arrange into a 2x3 or 3x2 grid.
5. **File → Save As** → save as `HR_Analytics_Dashboard.twbx` (packaged workbook — this bundles the data so it works on GitHub without a live connection).
6. Add the `.twbx` file to this project folder.

## 🔍 Key Insights to Highlight

- Departments/roles with the highest attrition rate
- The relationship between overtime and attrition
- How job satisfaction and work-life balance scores correlate with turnover
- Income bands most affected by attrition

## ▶️ Regenerating the Data

```bash
pip install pandas numpy
python generate_hr_data.py
```

## ✍️ Author

**Shivang Pandey** – Data Analyst
[LinkedIn](https://www.linkedin.com/in/shivang-pandey-2a489a418/)
