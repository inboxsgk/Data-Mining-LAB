import pandas as pd
import matplotlib.pyplot as plt

print("-"*25,"Gowtham Karthikeyan S\n21BBS0157\n","-"*25)

df = pd.read_csv(r'..\Dataset.csv')
print("Dimensions: ", df.shape)

print("\nStructure: ")
print(df.info())

print("\nAttribut names: ")
for i in df.columns.tolist():
    print(i)

print("\nAttribute Values: ")
print(df.Name)

print('-'*25,"\nSection subquestion 2\n", '-'*25)

print('\nFirst 5 records:')
print(df.head(5))

print("\nLast 5 Records:")
print(df.tail(5))

print("\nName, Designation, Salary of First 10 records:")
print(df[['Name','Designation','Salary']].head(10))

print("\nName on the records: ")
print(df['Name'])

print("\nAll records: ")
print(df)

print('-'*25,"\nSection subquestion 3\n", '-'*25)

print('\nMean, Median, Mode of \n(i) Salary:')
print("Mean: ", df['Salary'].mean())
print("Median: ", df['Salary'].median())
print("Mode: ", df['Salary'].mode())
print('\n(ii) Experience:')
print("Mean: ", df['Experience'].mean())
print("Median: ", df['Experience'].median())
print("Mode: ", df['Experience'].mode())

print("\nFinding variance and covariance: ")
print("The varaince of Salary is:", df.Salary.var())
print("The varaince of Experience is:", df.Experience.var())
print("\nThe covariance of Salary and Experience is:", df.Salary.cov(df.Experience))

print("\nThe correlation between Salary and Experience: ")
print(df.Salary.corr(df.Experience))

print('-'*25,"\nSection subquestion 4\n", '-'*25)

print('\nPie chart: Designation')
designation_counts = df['Designation'].value_counts()
plt.figure(figsize=(6, 3))
plt.pie(designation_counts, labels=designation_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Designation Distribution')
plt.legend(designation_counts.index, title="Designations", loc="lower left", bbox_to_anchor=(1, 0.5))
plt.show()

print("\nHistogram : Salary")
plt.figure(figsize=(6, 3))
plt.hist(df['Salary'], bins=5, color='red', edgecolor='black', alpha=0.7)
plt.title('Salary Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Salary', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding grid lines for the y-axis
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

print("\nScatter plot : salary to experience")
plt.figure(figsize=(6, 4))
plt.scatter(df['Experience'], df['Salary'], color='red', s=100, edgecolor='black', alpha=0.8)
plt.title('Salary vs. Experience', fontsize=16, fontweight='bold')
plt.xlabel('Experience (Years)', fontsize=14)
plt.ylabel('Salary (In Rupees)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()