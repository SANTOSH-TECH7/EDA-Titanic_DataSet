# ---------------------------------------
# Step 0: Import Libraries and Load Data
# ---------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# Optional: Drop irrelevant columns
df.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# ---------------------------------------
# Step 1: Summary Statistics
# ---------------------------------------
print("----- Summary Statistics -----")
print(df.describe(include='all'))

print("\n----- Median of Numeric Columns -----")
print(df.median(numeric_only=True))

# ---------------------------------------
# Step 2: Histograms and Boxplots
# ---------------------------------------
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']

# Plot histograms
for col in numeric_cols:
    plt.figure(figsize=(6, 3))
    sns.histplot(df[col].dropna(), kde=True, bins=30)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Plot boxplots
for col in numeric_cols:
    plt.figure(figsize=(6, 3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()

# ---------------------------------------
# Step 3: Correlation Matrix and Pairplot
# ---------------------------------------
# Correlation matrix for numeric columns
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# Pairplot for key variables with 'Survived'
sns.pairplot(df[['Age', 'Fare', 'SibSp', 'Parch', 'Survived']], hue='Survived')
plt.suptitle("Pairplot of Features by Survival", y=1.02)
plt.tight_layout()
plt.show()

# ---------------------------------------
# Step 4: Identify Patterns and Trends
# ---------------------------------------

# Survival rate by Sex
plt.figure(figsize=(5, 3))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title("Survival Rate by Sex")
plt.tight_layout()
plt.show()

# Survival rate by Pclass
plt.figure(figsize=(5, 3))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title("Survival Rate by Passenger Class")
plt.tight_layout()
plt.show()

# Age distribution by survival
plt.figure(figsize=(6, 3))
sns.kdeplot(data=df, x='Age', hue='Survived', fill=True)
plt.title("Age Distribution by Survival")
plt.tight_layout()
plt.show()

# ---------------------------------------
# Step 5: Basic Feature-Level Inferences (printed)
# ---------------------------------------
print("\n===== Inferences =====")
print("1. Females had a higher survival rate than males.")
print("2. Passengers in 1st class survived more than those in 3rd class.")
print("3. Children (Age < 15) had higher survival chances.")
print("4. Higher fare passengers generally had better survival rates.")
print("5. Small families (1-2 siblings/parents) were more likely to survive.")
