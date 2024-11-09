import pandas as pd
import numpy as np
from pingouin import cronbach_alpha
from itertools import combinations

# Load your dataset
data = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\KTEL\MAIN_DATASET\EXCEL\KTEL.xlsx')
data = data.drop(columns=['N_PARTICIPANT'])

# For demonstration, let's create a random dataset
np.random.seed(0)
data = pd.DataFrame(np.random.randn(96, 64))

# Define a function to calculate Cronbach's Alpha
def calculate_cronbach_alpha(df):
    if df.shape[1] < 2:
        return 0  # Return 0 for invalid clusters with fewer than 2 features
    alpha, _ = cronbach_alpha(df)
    return alpha

# Initial clusters: each feature as its own cluster
clusters = {i: [i] for i in range(data.shape[1])}

# Function to attempt merging all pairs of clusters
def try_merging_clusters(clusters):
    merged = False
    best_merge = None
    best_alpha = 0

    # Iterate over all pairs of clusters
    for (i, j) in combinations(clusters.keys(), 2):
        merged_features = clusters[i] + clusters[j]
        if len(merged_features) > 1:
            alpha = calculate_cronbach_alpha(data.iloc[:, merged_features])
            if alpha >= 0.6 and alpha > best_alpha:
                best_merge = (i, j)
                best_alpha = alpha

    if best_merge:
        i, j = best_merge
        clusters[i] = clusters[i] + clusters[j]
        del clusters[j]
        merged = True

    return merged

# Iteratively merge clusters
while True:
    if not try_merging_clusters(clusters):
        break

# Group the features based on the final clusters
final_clusters = {i: data.iloc[:, features] for i, features in clusters.items() if len(features) > 1}

# Print the resulting groups
for cluster_id, features in final_clusters.items():
    alpha_value = calculate_cronbach_alpha(features)
    print(f'Cluster {cluster_id} (Cronbach\'s Alpha = {alpha_value:.2f}):')
    print(features.columns.tolist())

# Check if no valid clusters were formed
if not final_clusters:
    print("No clusters with Cronbach's Alpha >= 0.6 were formed.")
