import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("company_employee_dataset.csv")

# Prepare counts
gender_counts = df["Gender"].value_counts()
city_counts = df["City"].value_counts()
dept_salary = df.groupby("Department")["Salary"].mean()

# Create subplots in 1 figure (3 rows, 1 column)
plt.figure(figsize=(12, 14))

# -------- 1️⃣ Gender Distribution --------
plt.subplot(3, 1, 1)
plt.bar(gender_counts.index, gender_counts.values)
plt.title("Gender Distribution", fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.grid(axis="y", alpha=0.3)

# -------- 2️⃣ City-wise Employee Count --------
plt.subplot(3, 1, 2)
plt.bar(city_counts.index, city_counts.values)
plt.title("City-wise Employee Count", fontsize=14)
plt.xlabel("City")
plt.ylabel("Employees")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

# -------- 3️⃣ Average Salary per Department --------
plt.subplot(3, 1, 3)
plt.bar(dept_salary.index, dept_salary.values)
plt.title("Average Salary by Department", fontsize=14)
plt.xlabel("Department")
plt.ylabel("Avg Salary")
plt.xticks(rotation=30)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
