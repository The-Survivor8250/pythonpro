import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file using pandas
data = pd.read_csv("C:\\Users\\RAHUL\\Desktop\\archive\\healthcare_dataset.csv")

# Extract the necessary columns using numpy
age = data['Age'].to_numpy()
room = data['Room Number'].to_numpy()
bill = data['Billing Amount'].to_numpy()
gender = data['Gender'].to_numpy()


# Plotting age distribution Histogram
plt.hist(age, bins=15, color='cyan', edgecolor='black')
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.show()


# Cleaning age data
print("Data Cleaning:-")
print("Number of NaN Values Before Cleaning:",np.isnan(age).sum())
age_cleaned = np.where(np.isnan(age), np.nanmean(age), age)
print("Number of NaN Values After Cleaning:",np.isnan(age_cleaned).sum())

# Older patients
print("\nFiltering:-")
older_patients = age_cleaned[age_cleaned > 50]
print(f"Number of patients older than 50: {older_patients.size}")

# Basic statistics
print("\nData Manipulation:-")
mean_age = np.mean(age_cleaned)
median_room = np.median(room)
std_bill = np.std(bill)

print(f"Mean Age: {mean_age}")
print(f"Median Room: {median_room}")
print(f"Standard Deviation of Bill: {std_bill}")


# Gender distribution
unique_genders, gender_counts = np.unique(gender, return_counts=True)

# Pie Chart for gender distribution
plt.pie(gender_counts, labels=unique_genders, autopct='%1.11f%%', startangle=140,colors=('pink','lightblue'))
plt.title('Gender Distribution')
plt.show()


# Scatter plot for Age vs. Bill
plt.scatter(age, bill, alpha=0.6, color='lightgreen', edgecolors='black')
plt.title('Age vs. Bill')
plt.xlabel('Age')
plt.ylabel('Bill')
plt.show()