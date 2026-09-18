"""
Customer Segmentation using K-Means Clustering
------------------------------------------------
Run:
    python src/customer_segmentation.py

The script:
1. Loads customer data
2. Explores and cleans the data
3. Uses the Elbow Method to choose K
4. Applies K-Means clustering
5. Saves visualizations and segmented customer data
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "Mall_Customers.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    df = pd.read_csv(DATA_PATH)

    print("First 5 rows:")
    print(df.head())
    print("\nShape:", df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())

    # Features used for segmentation
    features = ["Annual Income (k$)", "Spending Score (1-100)"]
    X = df[features].copy()

    # Elbow method
    inertias = []
    k_values = range(2, 11)

    for k in k_values:
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        model.fit(X)
        inertias.append(model.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(list(k_values), inertias, marker="o")
    plt.title("Elbow Method for Optimal Number of Clusters")
    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Inertia")
    plt.xticks(list(k_values))
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "elbow_curve.png", dpi=150)
    plt.close()

    # Scale features before clustering
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # K=5 is used for this project
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # Cluster visualization
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Cluster",
        palette="deep",
        s=80
    )
    plt.title("Customer Segments")
    plt.legend(title="Cluster")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "customer_segments.png", dpi=150)
    plt.close()

    # Cluster profile
    profile = df.groupby("Cluster")[features].mean().round(2)
    counts = df["Cluster"].value_counts().sort_index().rename("Customer Count")
    profile = profile.join(counts)

    profile.to_csv(OUTPUT_DIR / "cluster_profile.csv")

    # Save segmented data
    df.to_csv(OUTPUT_DIR / "segmented_customers.csv", index=False)

    print("\nCluster profile:")
    print(profile)

    print("\nFiles saved in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
