# Insurance Risk Analytics

## Project Overview

This project analyzes insurance portfolio data to identify key risk drivers, profitability patterns, and claim behavior. The analysis supports data-driven underwriting decisions and establishes a foundation for statistical testing and predictive modeling.

The project follows software engineering best practices, including version control, continuous integration, reusable code modules, and reproducible data workflows.

---

## Objectives

The primary objectives of this project are:

- Perform exploratory data analysis (EDA) on insurance data.
- Assess data quality and completeness.
- Investigate profitability using loss ratio analysis.
- Identify geographic, demographic, and vehicle-related risk factors.
- Analyze claim frequency and claim severity trends.
- Establish a reproducible data science workflow using Git, GitHub, and DVC.

---

## Repository Structure

```text
insurance-risk-analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   └── raw/
│       └── insurance_data.csv
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── reports/
│   └── final_report.md
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   └── eda_utils.py
│
├── tests/
│   └── test_data_loader.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd insurance-risk-analytics
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/01_eda.ipynb
```

and run all cells sequentially.

---

## Task 1: Exploratory Data Analysis

The EDA investigates:

- Data structure and quality
- Missing value assessment
- Distribution of key financial variables
- Loss ratio analysis
- Geographic risk patterns
- Vehicle make and model risk
- Claim severity analysis
- Temporal claim and premium trends
- Correlation analysis

---

## Key Findings

- The portfolio exhibits an average loss ratio of approximately 53%.
- Claims are highly right-skewed, with most policyholders generating no claims.
- Luxury vehicles show the highest loss ratios among vehicle categories.
- Geographic differences in profitability exist across provinces.
- Toyota generates the highest total claim volume due to exposure.
- Mercedes-Benz E-Class, BMW 5 Series, and Toyota Land Cruiser exhibit the highest average claim severity.
- Premiums display a bimodal distribution, indicating multiple customer risk segments.

---

## Data Version Control (DVC)

This project uses DVC (Data Version Control) to track datasets separately from Git.

### Setup

Install DVC:

```bash
pip install dvc
```

Initialize DVC:

```bash
dvc init
```

Configure the local remote storage:

```bash
mkdir ../dvc-storage
dvc remote add -d localstorage ../dvc-storage
```

### Retrieve Data

Pull tracked datasets:

```bash
dvc pull
```

### Tracked Versions

- Raw dataset: `data/raw/insurance_data.csv`
- Cleaned dataset: `data/processed/insurance_data_clean.csv`

Both datasets are versioned through DVC and stored in the configured local remote.

## CI/CD Pipeline

GitHub Actions is configured to:

- Run flake8 linting checks.
- Execute pytest unit tests.
- Validate code quality on every push and pull request.

---

## Testing

Run linting:

```bash
flake8 src/
```

Run unit tests:

```bash
pytest
```

---

## Author

Tsion Habtesilassei
