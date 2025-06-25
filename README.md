# Titanic Dataset - Exploratory Data Analysis (EDA)

This project performs a complete Exploratory Data Analysis (EDA) on the **Titanic dataset** from Kaggle. It includes statistical summaries, visualizations, and insights to understand the factors affecting passenger survival.

---

## 📦 Dataset

- **Source**: [Kaggle Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **File Used**: `titanic.csv`

---

## ✅ EDA Steps Performed

### 1. Import and Inspect
- Loaded the Titanic dataset using `pandas`
- Displayed data types, missing values, and sample rows

### 2. Summary Statistics
- Calculated **mean, median, standard deviation**, and more using `describe()` and `median()`

### 3. Visual Analysis
- **Histograms** and **Boxplots** for numerical features (`Age`, `Fare`, `SibSp`, `Parch`)
- **Correlation matrix** using heatmap
- **Pairplot** to visualize relationships between variables and survival
- **Barplots** for survival by `Sex` and `Pclass`
- **KDE plot** for Age distribution across survival classes

### 4. Pattern Discovery
- Observed trends like:
  - Females had higher survival rates
  - First-class passengers had better survival chances
  - Younger passengers (especially children) survived more
  - Smaller families survived more than larger ones

---

## 🛠️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/titanic-eda.git
cd titanic-eda
