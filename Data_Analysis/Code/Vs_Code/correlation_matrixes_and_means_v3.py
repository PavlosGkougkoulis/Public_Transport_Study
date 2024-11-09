# -*- coding: utf-8 -*-
"""Correlation_Matrixes_and_Means.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10uMapQJVMS2GPwZfY6Sb2KYAY0qyKj_8

# **1. Correlation Matrices and Means**

**1.1 KTEL - Correlation Matrix**
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np


# Read Excel file into DataFrame
df = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\KTEL\MAIN_DATASET\EXCEL\KTEL.xlsx')

# Drop 'N_PARTICIPANT' column
df = df.drop(columns=['N_PARTICIPANT'])

# Calculate correlation matrix
corr_matrix = df.corr()

# Set up the matplotlib figure
plt.figure(figsize=(20, 20))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_matrix, cmap=cmap, vmax=1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5},
            annot=False)

# Show plot
plt.title('Correlation Matrix - KTEL')
plt.show()

"""**1.2 KTEL - Means**"""

# Read Excel files into DataFrames
df_ktel = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\KTEL\MAIN_DATASET\EXCEL\KTEL.xlsx')

# Drop 'N_PARTICIPANT' column for the KTEL DataFrame
df_ktel = df_ktel.drop(columns=['N_PARTICIPANT'])

# Calculate means for each variable in KTEL DataFrame
means_ktel = df_ktel.mean().round(2)

# Convert means to a DataFrame
means_df_ktel = pd.DataFrame({'Variable': means_ktel.index, 'Mean': means_ktel.values})

# Plot the table
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')

# Create the table
table = ax.table(cellText=means_df_ktel.values,
                 colLabels=means_df_ktel.columns,
                 cellLoc='center',
                 loc='center')  # Set the table location to center

# Set table properties
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)  # Scale up the table for better readability

plt.savefig('means_ktel.jpg', bbox_inches='tight', pad_inches=0.5)
plt.show()

"""**2.1 OSE - Correlation Matrix**"""

# Read Excel file into DataFrame
df = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\OSE\MAIN_DATASET\EXCEL\OSE.xlsx')

# Drop 'N_PARTICIPANT' column
df = df.drop(columns=['N_PARTICIPANT'])

# Calculate correlation matrix
corr_matrix = df.corr()

# Set up the matplotlib figure
plt.figure(figsize=(20, 20))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_matrix, cmap=cmap, vmax=1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5},
            annot=False)

# Show plot
plt.title('Correlation Matrix - OSE')
plt.show()

"""**2.2 OSE - Means**"""

# Read Excel files into DataFrames
df_ose = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\OSE\MAIN_DATASET\EXCEL\OSE.xlsx')

# Drop 'N_PARTICIPANT' column for the OSE DataFrame
df_ose = df_ose.drop(columns=['N_PARTICIPANT'])

# Calculate means for each variable in OSE DataFrame
means_ose = df_ose.mean().round(2)

# Convert means to a DataFrame
means_df_ose = pd.DataFrame({'Variable': means_ose.index, 'Mean': means_ose.values})

# Plot the table
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')

# Create the table
table = ax.table(cellText=means_df_ose.values,
                 colLabels=means_df_ose.columns,
                 cellLoc='center',
                 loc='center')  # Set the table location to center

# Set table properties
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)  # Scale up the table for better readability

plt.savefig('means_ose.jpg', bbox_inches='tight', pad_inches=0.5)
plt.show()

"""**3.1 LIMANI - Correlation Matrix**"""

# Read Excel file into DataFrame
df = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\LIMANI\MAIN_DATASET\EXCEL\LIMANI.xlsx')

# Drop 'N_PARTICIPANT' column
df = df.drop(columns=['N_PARTICIPANT'])

# Calculate correlation matrix
corr_matrix = df.corr()

# Set up the matplotlib figure
plt.figure(figsize=(20, 20))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_matrix, cmap=cmap, vmax=1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5},
            annot=False)

# Show plot
plt.title('Correlation Matrix - LIMANI')
plt.show()

"""**3.2 LIMANI - Means**"""

# Read Excel files into DataFrames
df_limani = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\LIMANI\MAIN_DATASET\EXCEL\LIMANI.xlsx')

# Drop 'N_PARTICIPANT' column for the LIMANI DataFrame
df_limani = df_limani.drop(columns=['N_PARTICIPANT'])

# Calculate means for each variable in LIMANI DataFrame
means_limani = df_limani.mean().round(2)

# Convert means to a DataFrame
means_df_limani = pd.DataFrame({'Variable': means_limani.index, 'Mean': means_limani.values})

# Plot the table
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')

# Create the table
table = ax.table(cellText=means_df_limani.values,
                 colLabels=means_df_limani.columns,
                 cellLoc='center',
                 loc='center')  # Set the table location to center

# Set table properties
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)  # Scale up the table for better readability

plt.savefig('means_limani.jpg', bbox_inches='tight', pad_inches=0.5)
plt.show()

"""# **2. Cronbach Alpha values, tables and means**

## 1. KTEL
"""

# Load the dataset from the Excel file
data = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\KTEL\MAIN_DATASET\EXCEL\KTEL.xlsx')

# Remove the N_PARTICIPANT column
data = data.drop(columns=['N_PARTICIPANT'])

# Define the groups correctly
groups = {
    "TIME": ["TIME_WAITED", "ACCURACY", "BOARDING_TIME"],
    "PASSENGERS": ["AVAIL_SEATS", "PERSON_SPACE", "COPASS_BEHAVIOUR", "TRAVEL_PERSONS", "WHEELCHAIR", "BABY_STROLLER", "KIDS", "LUGGAGE", "AGED", "VISION_HELP", "BIKE_FOLD", "DOG", "OTHER", "DISABILITY"],
    "INFORMATION": ["INFO_OUT", "INFO_IN", "HELP_DRIVER", "PRODUCT_INFO", "INFO_TRIP"],
    "SAFETY": ["PERSON_SAFETY", "DRIVING_SAFETY", "PERSONNAL_SAFETY"],
    "STATION": ["CLEANLINESS_OUT", "ENTRANCE_OPT", "CLEANLINESS_INS", "TICKET_SELL", "BUILDING_MAINT", "STATION_CLEAN", "FACILITY_STATION", "STAFF_STATION", "STAFF_HELP", "PUBLIC_TRANSP_CONN", "PARKING_CARS", "PARKING_BIKES", "ENV_STATION", "ROOF_STATION", "SEATS_STATION", "CATER_FAC_STATION", "TICKET_PRICE_SATISFACTION"],
    "TRIP_TRANSPORT": ["AVAIL_SEATS", "SEAT_COMFORT", "TEMP_INS", "CONTRACTOR_DRIVER", "SEAT_RESERV", "TRANSPORT_CARD", "MULT_TRANS_OFFER", "TRANS_PURPOSE", "TRANSP_FREQ", "REASON_TRANSP_MEANS", "TRIP_SATISFACTION"],
    "CHARACTERISTICS": ["GENDER", "DRIVING_LIC", "PRIVATE_CAR_USE", "TWOWH_USE", "BIKE_USE", "NONE_ABOVE", "AGE", "EDUCATION_LVL", "JOB", "PPL_IN_HOUSE", "FAMILY_INCOME"]
}

# Ensure all relevant columns are numeric and handle missing values
for group, columns in groups.items():
    for col in columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert to numeric and coerce errors to NaN
        else:
            data[col] = np.nan  # Create columns with NaN if they don't exist in the data

# Function to calculate Cronbach's Alpha
def cronbach_alpha(df):
    df = df.dropna(axis=1, how='any')  # Drop columns with NaN values
    if df.shape[1] < 2:  # Need at least two items to calculate alpha
        return np.nan
    itemscores = df.values
    itemvars = itemscores.var(axis=0, ddof=1)
    tscores = itemscores.sum(axis=1)
    nitems = len(df.columns)
    return nitems / (nitems - 1) * (1 - itemvars.sum() / tscores.var(ddof=1))

# Calculate Cronbach's alpha for each group
cronbach_alphas = {group: cronbach_alpha(data[columns].dropna()) for group, columns in groups.items()}

# Calculate means for each group
group_means = {group: data[columns].mean(axis=1).mean() for group, columns in groups.items()}

# Printing and Visualization
# Grouping information and Cronbach's alpha
group_info = [{"Group": group, "Variables": ", ".join(columns), "Cronbach Alpha": alpha}
              for group, columns, alpha in zip(groups.keys(), groups.values(), cronbach_alphas.values())]

# Convert group_info to a DataFrame for better visualization
group_info_df = pd.DataFrame(group_info)

# Means of each group
means_info = [{"Group": group, "Mean": mean} for group, mean in group_means.items()]
means_info_df = pd.DataFrame(means_info)

# Plotting Cronbach's Alphas
plt.figure(figsize=(12, 6))
sns.barplot(x=list(cronbach_alphas.keys()), y=list(cronbach_alphas.values()))
plt.title("Cronbach's Alpha for Each Group - KTEL")
plt.xlabel('Group')
plt.ylabel("Cronbach's Alpha")
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
for index, value in enumerate(cronbach_alphas.values()):
    if np.isfinite(value):
        plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('cronbach_alphas.png')
plt.show()

# Convert group_means values to a list of floats
group_means_values = [value for value in group_means.values()]

# Plotting Group Means
plt.figure(figsize=(12, 6))
sns.barplot(x=list(group_means.keys()), y=group_means_values)
plt.title('Mean Values for Each Group - KTEL')
plt.xlabel('Group')
plt.ylabel('Mean Value')
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
for index, value in enumerate(group_means_values):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('group_means.png')
plt.show()

print("Grouping Information and Cronbach's Alpha:")
print(tabulate(group_info, headers="keys", tablefmt="fancy_grid"))

print("\nMeans of Each Group:")
print(tabulate(means_info, headers="keys", tablefmt="fancy_grid"))

print("\nCronbach Alphas:")
for group, alpha in cronbach_alphas.items():
    print(f"{group}: {alpha}")

print("\nGroup Means:")
for group, mean in group_means.items():
    print(f"{group}: {mean}")
correlation_matrices = {}
# Plot correlation matrices for each group
for group, correlation_matrix in correlation_matrices.items():
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"ha": 'center', "va": 'center'})
    plt.title(f'Correlation Matrix - {group} (KTEL)')
    plt.xlabel('Variables')
    plt.ylabel('Variables')
    plt.xticks(rotation=90)  # Rotate x-tick labels vertically
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f'correlation_matrix_{group}.png')
    plt.show()

# Function to calculate mean values for each group
def calculate_group_means(data, groups):
    group_means = {}
    for group, columns in groups.items():
        group_means[group] = data[columns].mean(axis=1)
    return group_means

# Calculate mean values for each group
group_means = calculate_group_means(data, groups)

# Convert group means into a DataFrame
group_means_df = pd.DataFrame(group_means)

# Calculate correlation matrix for group means
group_correlation_matrix = group_means_df.corr()

# Plot correlation matrix for groups
plt.figure(figsize=(10, 8))
sns.heatmap(group_correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix - Groups (KTEL)')
plt.xlabel('Groups')
plt.ylabel('Groups')
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('group_correlation_matrix.png')
plt.show()

"""## 2. OSE"""

# Load the dataset from the Excel file
data = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\OSE\MAIN_DATASET\EXCEL\OSE.xlsx')

# Remove the N_PARTICIPANT column
data = data.drop(columns=['N_PARTICIPANT'])

# Define the groups correctly
groups = {
    "TIME": ["TIME_WAITED", "ACCURACY", "BOARDING_TIME"],
    "PASSENGERS": ["AVAIL_SEATS", "PERSON_SPACE", "COPASS_BEHAVIOUR", "TRAVEL_PERSONS", "WHEELCHAIR", "BABY_STROLLER", "KIDS", "LUGGAGE", "AGED", "VISION_HELP", "BIKE_FOLD", "DOG", "OTHER", "DISABILITY"],
    "INFORMATION": ["INFO_OUT", "INFO_IN", "HELP_DRIVER", "PRODUCT_INFO", "INFO_TRIP"],
    "SAFETY": ["PERSON_SAFETY", "DRIVING_SAFETY", "PERSONNAL_SAFETY"],
    "STATION": ["CLEANLINESS_OUT", "ENTRANCE_OPT", "CLEANLINESS_INS", "TICKET_SELL", "BUILDING_MAINT", "STATION_CLEAN", "FACILITY_STATION", "STAFF_STATION", "STAFF_HELP", "PUBLIC_TRANSP_CONN", "PARKING_CARS", "PARKING_BIKES", "ENV_STATION", "ROOF_STATION", "SEATS_STATION", "CATER_FAC_STATION", "TICKET_PRICE_SATISFACTION"],
    "TRIP_TRANSPORT": ["AVAIL_SEATS", "SEAT_COMFORT", "TEMP_INS", "CONTRACTOR_DRIVER", "SEAT_RESERV", "TRANSPORT_CARD", "MULT_TRANS_OFFER", "TRANS_PURPOSE", "TRANSP_FREQ", "REASON_TRANSP_MEANS", "TRIP_SATISFACTION"],
    "CHARACTERISTICS": ["GENDER", "DRIVING_LIC", "PRIVATE_CAR_USE", "TWOWH_USE", "BIKE_USE", "NONE_ABOVE", "AGE", "EDUCATION_LVL", "JOB", "PPL_IN_HOUSE", "FAMILY_INCOME"]
}

# Ensure all relevant columns are numeric and handle missing values
for group, columns in groups.items():
    for col in columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert to numeric and coerce errors to NaN
        else:
            data[col] = np.nan  # Create columns with NaN if they don't exist in the data

# Function to calculate Cronbach's Alpha
def cronbach_alpha(df):
    df = df.dropna(axis=1, how='any')  # Drop columns with NaN values
    if df.shape[1] < 2:  # Need at least two items to calculate alpha
        return np.nan
    itemscores = df.values
    itemvars = itemscores.var(axis=0, ddof=1)
    tscores = itemscores.sum(axis=1)
    nitems = len(df.columns)
    return nitems / (nitems - 1) * (1 - itemvars.sum() / tscores.var(ddof=1))

# Calculate Cronbach's alpha for each group
cronbach_alphas = {group: cronbach_alpha(data[columns].dropna()) for group, columns in groups.items()}

# Calculate means for each group
group_means = {group: data[columns].mean(axis=1).mean() for group, columns in groups.items()}

# Printing and Visualization
# Grouping information and Cronbach's alpha
group_info = [{"Group": group, "Variables": ", ".join(columns), "Cronbach Alpha": alpha}
              for group, columns, alpha in zip(groups.keys(), groups.values(), cronbach_alphas.values())]

# Convert group_info to a DataFrame for better visualization
group_info_df = pd.DataFrame(group_info)

# Means of each group
means_info = [{"Group": group, "Mean": mean} for group, mean in group_means.items()]
means_info_df = pd.DataFrame(means_info)

# Plotting Cronbach's Alphas
plt.figure(figsize=(12, 6))
sns.barplot(x=list(cronbach_alphas.keys()), y=list(cronbach_alphas.values()))
plt.title("Cronbach's Alpha for Each Group - OSE")
plt.xlabel('Group')
plt.ylabel("Cronbach's Alpha")
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
for index, value in enumerate(cronbach_alphas.values()):
    if np.isfinite(value):
        plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('cronbach_alphas.png')
plt.show()

# Convert group_means values to a list of floats
group_means_values = [value for value in group_means.values()]

# Plotting Group Means
plt.figure(figsize=(12, 6))
sns.barplot(x=list(group_means.keys()), y=group_means_values)
plt.title('Mean Values for Each Group - OSE')
plt.xlabel('Group')
plt.ylabel('Mean Value')
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
for index, value in enumerate(group_means_values):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('group_means.png')
plt.show()

print("Grouping Information and Cronbach's Alpha:")
print(tabulate(group_info, headers="keys", tablefmt="fancy_grid"))

print("\nMeans of Each Group:")
print(tabulate(means_info, headers="keys", tablefmt="fancy_grid"))

print("\nCronbach Alphas:")
for group, alpha in cronbach_alphas.items():
    print(f"{group}: {alpha}")

print("\nGroup Means:")
for group, mean in group_means.items():
    print(f"{group}: {mean}")

# Plot correlation matrices for each group
for group, correlation_matrix in correlation_matrices.items():
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"ha": 'center', "va": 'center'})
    plt.title(f'Correlation Matrix - {group} (OSE)')
    plt.xlabel('Variables')
    plt.ylabel('Variables')
    plt.xticks(rotation=90)  # Rotate x-tick labels vertically
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f'correlation_matrix_{group}.png')
    plt.show()

# Function to calculate mean values for each group
def calculate_group_means(data, groups):
    group_means = {}
    for group, columns in groups.items():
        group_means[group] = data[columns].mean(axis=1)
    return group_means

# Calculate mean values for each group
group_means = calculate_group_means(data, groups)

# Convert group means into a DataFrame
group_means_df = pd.DataFrame(group_means)

# Calculate correlation matrix for group means
group_correlation_matrix = group_means_df.corr()

# Plot correlation matrix for groups
plt.figure(figsize=(10, 8))
sns.heatmap(group_correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix - Groups (OSE)')
plt.xlabel('Groups')
plt.ylabel('Groups')
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('group_correlation_matrix.png')
plt.show()

"""## 3. LIMANI"""

# Load the dataset from the Excel file
data = pd.read_excel(r'E:\University\8ο ΕΞΑΜΗΝΟ\ΣΧΕΔΙΑΣΜΟΣ ΚΑΙ ΑΞΙΟΛΟΓΗΣΗ ΣΥΣΤΗΜΑΤΩΝ ΜΕΤΑΦΟΡΩΝ\ERGASIA EKSAMHNOU\Data_Analysis\LIMANI\MAIN_DATASET\EXCEL\LIMANI.xlsx')

# Remove the N_PARTICIPANT column
data = data.drop(columns=['N_PARTICIPANT'])

# Define the groups correctly
groups = {
    "TIME": ["TIME_WAITED", "ACCURACY", "BOARDING_TIME"],
    "PASSENGERS": ["AVAIL_SEATS", "PERSON_SPACE", "COPASS_BEHAVIOUR", "TRAVEL_PERSONS", "WHEELCHAIR", "BABY_STROLLER", "KIDS", "LUGGAGE", "AGED", "VISION_HELP", "BIKE_FOLD", "DOG", "OTHER", "DISABILITY"],
    "INFORMATION": ["INFO_OUT", "INFO_IN", "HELP_DRIVER", "PRODUCT_INFO", "INFO_TRIP"],
    "SAFETY": ["PERSON_SAFETY", "DRIVING_SAFETY", "PERSONNAL_SAFETY"],
    "STATION": ["CLEANLINESS_OUT", "ENTRANCE_OPT", "CLEANLINESS_INS", "TICKET_SELL", "BUILDING_MAINT", "STATION_CLEAN", "FACILITY_STATION", "STAFF_STATION", "STAFF_HELP", "PUBLIC_TRANSP_CONN", "PARKING_CARS", "PARKING_BIKES", "ENV_STATION", "ROOF_STATION", "SEATS_STATION", "CATER_FAC_STATION", "TICKET_PRICE_SATISFACTION"],
    "TRIP_TRANSPORT": ["AVAIL_SEATS", "SEAT_COMFORT", "TEMP_INS", "CONTRACTOR_DRIVER", "SEAT_RESERV", "TRANSPORT_CARD", "MULT_TRANS_OFFER", "TRANS_PURPOSE", "TRANSP_FREQ", "REASON_TRANSP_MEANS", "TRIP_SATISFACTION"],
    "CHARACTERISTICS": ["GENDER", "DRIVING_LIC", "PRIVATE_CAR_USE", "TWOWH_USE", "BIKE_USE", "NONE_ABOVE", "AGE", "EDUCATION_LVL", "JOB", "PPL_IN_HOUSE", "FAMILY_INCOME"]
}

# Ensure all relevant columns are numeric and handle missing values
for group, columns in groups.items():
    for col in columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert to numeric and coerce errors to NaN
        else:
            data[col] = np.nan  # Create columns with NaN if they don't exist in the data

# Function to calculate Cronbach's Alpha
def cronbach_alpha(df):
    df = df.dropna(axis=1, how='any')  # Drop columns with NaN values
    if df.shape[1] < 2:  # Need at least two items to calculate alpha
        return np.nan
    itemscores = df.values
    itemvars = itemscores.var(axis=0, ddof=1)
    tscores = itemscores.sum(axis=1)
    nitems = len(df.columns)
    return nitems / (nitems - 1) * (1 - itemvars.sum() / tscores.var(ddof=1))

# Calculate Cronbach's alpha for each group
cronbach_alphas = {group: cronbach_alpha(data[columns].dropna()) for group, columns in groups.items()}

# Calculate means for each group
group_means = {group: data[columns].mean(axis=1).mean() for group, columns in groups.items()}

# Printing and Visualization
# Grouping information and Cronbach's alpha
group_info = [{"Group": group, "Variables": ", ".join(columns), "Cronbach Alpha": alpha}
              for group, columns, alpha in zip(groups.keys(), groups.values(), cronbach_alphas.values())]

# Convert group_info to a DataFrame for better visualization
group_info_df = pd.DataFrame(group_info)

# Means of each group
means_info = [{"Group": group, "Mean": mean} for group, mean in group_means.items()]
means_info_df = pd.DataFrame(means_info)

# Plotting Cronbach's Alphas
plt.figure(figsize=(12, 6))
sns.barplot(x=list(cronbach_alphas.keys()), y=list(cronbach_alphas.values()))
plt.title("Cronbach's Alpha for Each Group - LIMANI")
plt.xlabel('Group')
plt.ylabel("Cronbach's Alpha")
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
for index, value in enumerate(cronbach_alphas.values()):
    if np.isfinite(value):
        plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('cronbach_alphas.png')
plt.show()

# Convert group_means values to a list of floats
group_means_values = [value for value in group_means.values()]

# Plotting Group Means
plt.figure(figsize=(12, 6))
sns.barplot(x=list(group_means.keys()), y=group_means_values)
plt.title('Mean Values for Each Group - LIMANI')
plt.xlabel('Group')
plt.ylabel('Mean Value')
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
for index, value in enumerate(group_means_values):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('group_means.png')
plt.show()

print("Grouping Information and Cronbach's Alpha:")
print(tabulate(group_info, headers="keys", tablefmt="fancy_grid"))

print("\nMeans of Each Group:")
print(tabulate(means_info, headers="keys", tablefmt="fancy_grid"))

print("\nCronbach Alphas:")
for group, alpha in cronbach_alphas.items():
    print(f"{group}: {alpha}")

print("\nGroup Means:")
for group, mean in group_means.items():
    print(f"{group}: {mean}")

# Plot correlation matrices for each group
for group, correlation_matrix in correlation_matrices.items():
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"ha": 'center', "va": 'center'})
    plt.title(f'Correlation Matrix - {group} (LIMANI)')
    plt.xlabel('Variables')
    plt.ylabel('Variables')
    plt.xticks(rotation=90)  # Rotate x-tick labels vertically
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f'correlation_matrix_{group}.png')
    plt.show()

# Function to calculate mean values for each group
def calculate_group_means(data, groups):
    group_means = {}
    for group, columns in groups.items():
        group_means[group] = data[columns].mean(axis=1)
    return group_means

# Calculate mean values for each group
group_means = calculate_group_means(data, groups)

# Convert group means into a DataFrame
group_means_df = pd.DataFrame(group_means)

# Calculate correlation matrix for group means
group_correlation_matrix = group_means_df.corr()

# Plot correlation matrix for groups
plt.figure(figsize=(10, 8))
sns.heatmap(group_correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix - Groups (LIMANI)')
plt.xlabel('Groups')
plt.ylabel('Groups')
plt.xticks(rotation=90)  # Rotate x-axis labels vertically
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('group_correlation_matrix.png')
plt.show()

"""# **3. Overall Rating**"""
