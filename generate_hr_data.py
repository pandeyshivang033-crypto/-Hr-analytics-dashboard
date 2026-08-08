"""
generate_hr_data.py
Generates a synthetic HR dataset (employee attrition + workforce KPIs)
for the HR Analytics Dashboard project. Import the resulting CSV
directly into Tableau.
"""

import numpy as np
import pandas as pd

np.random.seed(7)

N = 1200

departments = ["Sales", "R&D", "HR", "Finance", "IT", "Operations"]
job_roles = {
    "Sales": ["Sales Executive", "Sales Manager"],
    "R&D": ["Research Scientist", "Lab Technician"],
    "HR": ["HR Executive", "HR Manager"],
    "Finance": ["Financial Analyst", "Accountant"],
    "IT": ["Software Engineer", "IT Support"],
    "Operations": ["Operations Executive", "Supervisor"],
}
genders = ["Male", "Female"]
marital_status = ["Single", "Married", "Divorced"]
education = ["High School", "Bachelor's", "Master's", "PhD"]

dept = np.random.choice(departments, N)
role = [np.random.choice(job_roles[d]) for d in dept]
age = np.random.randint(21, 58, N)
gender = np.random.choice(genders, N)
marital = np.random.choice(marital_status, N, p=[0.4, 0.5, 0.1])
edu = np.random.choice(education, N, p=[0.15, 0.55, 0.25, 0.05])
years_at_company = np.random.randint(0, 20, N)
distance_from_home = np.random.randint(1, 30, N)
monthly_income = np.round(np.random.normal(45000, 15000, N)).clip(15000, None)
job_satisfaction = np.random.randint(1, 5, N)      # 1-4 scale
work_life_balance = np.random.randint(1, 5, N)     # 1-4 scale
overtime = np.random.choice(["Yes", "No"], N, p=[0.3, 0.7])
performance_rating = np.random.randint(1, 5, N)    # 1-4 scale

# Attrition probability driven by realistic factors
attrition_score = (
    (overtime == "Yes") * 0.25
    + (job_satisfaction <= 2) * 0.20
    + (work_life_balance <= 2) * 0.15
    + (years_at_company < 2) * 0.15
    + (distance_from_home > 20) * 0.10
    + np.random.uniform(0, 0.3, N)
)
attrition = np.where(attrition_score > 0.65, "Yes", "No")

df = pd.DataFrame({
    "EmployeeID": range(1001, 1001 + N),
    "Age": age,
    "Department": dept,
    "JobRole": role,
    "Gender": gender,
    "MaritalStatus": marital,
    "Education": edu,
    "YearsAtCompany": years_at_company,
    "DistanceFromHome_km": distance_from_home,
    "MonthlyIncome": monthly_income.astype(int),
    "JobSatisfaction": job_satisfaction,
    "WorkLifeBalance": work_life_balance,
    "OverTime": overtime,
    "PerformanceRating": performance_rating,
    "Attrition": attrition,
})

df.to_csv("data/hr_data.csv", index=False)
print(f"Generated {len(df)} employee records -> data/hr_data.csv")
print(f"Attrition rate: {(df['Attrition']=='Yes').mean()*100:.1f}%")
