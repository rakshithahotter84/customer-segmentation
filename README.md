# Customer Segmentation using K-Means Clustering

## Project Overview

Customer segmentation is the process of grouping customers into meaningful groups based on similar characteristics.

This project uses **K-Means Clustering** to segment customers using:

- Annual Income
- Spending Score

The goal is to identify groups of customers with similar purchasing behavior so that businesses can design more targeted marketing strategies.

## Machine Learning Approach

This is an **unsupervised learning** project.

### Algorithm

**K-Means Clustering**

K-Means divides customers into K groups by minimizing the distance between each customer and the center of its assigned cluster.

## Dataset

The project includes `data/Mall_Customers.csv`.

Columns:

| Column | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Gender | Customer gender |
| Age | Customer age |
| Annual Income (k$) | Annual income in thousands of dollars |
| Spending Score (1-100) | Spending score from 1 to 100 |

> Note: The included CSV is a self-contained representative dataset generated for this portfolio project. If you use an external dataset for a formal submission, cite its original source.

## Project Structure

```text
customer-segmentation/
│
├── data/
│   └── Mall_Customers.csv
│
├── notebooks/
│   └── customer_segmentation.ipynb
│
├── src/
│   └── customer_segmentation.py
│
├── outputs/
│   └── Generated charts and cluster results
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd customer-segmentation
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Python Project

From the project root:

```bash
python src/customer_segmentation.py
```

The script creates:

- `outputs/elbow_curve.png`
- `outputs/customer_segments.png`
- `outputs/cluster_profile.csv`
- `outputs/segmented_customers.csv`

## Run the Jupyter Notebook

```bash
jupyter notebook
```

Then open:

```text
notebooks/customer_segmentation.ipynb
```

## Understanding the Clusters

The exact meaning of each cluster depends on its average income and spending score.

Typical interpretations include:

- **High income + high spending:** High-value customers
- **High income + low spending:** Potential customers who may respond to targeted offers
- **Low income + high spending:** Price-sensitive but active shoppers
- **Low income + low spending:** Lower-engagement customers
- **Middle income + middle spending:** Average customers

These are descriptive interpretations, not fixed labels.

## Business Applications

Customer segmentation can help businesses:

1. Create targeted marketing campaigns
2. Personalize offers
3. Identify high-value customers
4. Improve customer retention
5. Design customer-specific promotions
6. Allocate marketing budgets more efficiently

## Skills Demonstrated

- Python
- Pandas
- NumPy
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Feature Scaling
- K-Means Clustering
- Elbow Method
- Git
- GitHub

## Author

Add your name here.

Example:

**Your Name**  
Data Science / Machine Learning Portfolio
